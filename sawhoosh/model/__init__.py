import transaction
import uuid

try:
    import cPickle as pickle
except ImportError, e:
    import pickle

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))        

class SawhooshBase(object):
    # The fields of the class you want to index (make searchable)
    __whoosh_value__ = 'attribue,attribute,...'
    
    def index(self, writer):
        id = u'{0}'.format(self.id)
        cls = u'{0}'.format(pickle.dumps(self.__class__))
        value = u' '.join([getattr(self, attr) for attr in self.__whoosh_value__.split(',')])
        writer.add_document(id=id, cls=cls, value=value)

    def reindex(self, writer):
        id = u'{0}'.format(self.id)
        writer.delete_by_term('id', self.id)
        self.index(writer)
        
    def deindex(self, writer):
        id = u'{0}'.format(self.id)
        writer.delete_by_term('id', self.id)
        
    def route_name(self):
        """Override this in the model itself if your route name(s)
           do not match your table names
          """
        return self.__tablename__
        
Base = declarative_base(cls=SawhooshBase)

def update_indexes(session, flush_context):
    writer = WIX.writer()
    print "WOOOOOO"
    for i in session.new:
        print i, "NEW"
        i.index(writer)
    for i in session.dirty:
        print i, "DIRTY"
        i.reindex(writer)
    for i in session.deleted:
        print i, "DELETED"
        i.deindex(writer)        
    writer.commit()
    
event.listen(DBSession, 'after_flush', update_indexes)

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return DBSession
    
def new_uuid():
    return uuid.uuid4().hex

from sawhoosh.search import WIX
from sawhoosh.model.author import Author
from sawhoosh.model.document import Document

__all__ = ['DBSession', 'Base', 'initialize_sql']