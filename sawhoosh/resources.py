from sqlalchemy.orm.exc import NoResultFound

from sawhoosh.model import DBSession
from sawhoosh.model.document import Document
from sawhoosh.model.author import Author

class Root(dict):
    __name__ = None
    __parent__ = None
          
    def __init__(self, request):
        dict.__init__(self)
        
        self.request = request
        self['author'] = AuthorContainer(Author, self)
        self['document'] = DocumentContainer(Document, self)
        
class ModelContainer(object):
    def __init__(self, cls, parent=None):
        self.cls = cls
        self.db = DBSession
        self.parent = parent if parent else self
    def __getitem__(self, k):
        try:
            item = self.db.query(self.cls).filter_by(id=k).one()
            item.__name__ = str(k)
            item.__parent__ = self.parent
            return item
        except NoResultFound, e:
            raise KeyError
    def __len__(self):
        return self.db.query(self.cls).count()    
    def __iter__(self):
        return self.db.query(self.cls)
            
class AuthorContainer(ModelContainer): pass
class DocumentContainer(ModelContainer): pass

def root_factory(request):
    return Root(request)
