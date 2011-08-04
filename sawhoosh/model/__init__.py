import transaction

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
    
    def index(self):
        writer = WIX.writer()
        
        id = u'{0}'.format(self.id)
        writer.delete_by_term('id', self.id)
        
        cls = u'{0}'.format(pickle.dumps(self.__class__))
        value = u' '.join([getattr(self, attr) for attr in self.__whoosh_value__.split(',')])
        writer.add_document(id=id, cls=cls, value=value)
        writer.commit()

    def deindex(self):
        writer = WIX.writer()
        writer.delete_by_term('id', self.id)
        writer.commit()
        
Base = declarative_base(cls=SawhooshBase)

def reindex(session, flush_context):
    for i in session.new:
        i.index()
    for i in session.dirty:
        i.index()
    for i in session.deleted:
        i.deindex()        
event.listen(DBSession, 'after_flush', reindex)

def populate():
    session = DBSession()
    import time
    timestr = u'BLAH {0}'.format(time.time())
    a = Author(name=timestr)
    a.documents.append(Document(title=timestr, content='SQLalchemy Pyramid Traversal Whoosh'))
    session.add(a)
    session.flush()
    transaction.commit()

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    populate()
    transaction.abort()
    return DBSession
    
from sawhoosh.search import WIX
from sawhoosh.model.author import Author
from sawhoosh.model.document import Document

__all__ = ['DBSession', 'Base', 'initialize_sql']