from sqlalchemy.orm.exc import NoResultFound

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
            
class AuthorContainer(ModelContainer):
    __name__ = 'author'
    
class DocumentContainer(ModelContainer):
    __name__ = 'document'
    
def root_factory(request):
    return Root(request)

def container_factory(cls, request):
    if cls == Author:
        c = AuthorContainer(cls)
    elif cls == Document:
        c = DocumentContainer(cls)
    c.__parent__ = root_factory(request)
    return c
        
from sawhoosh.model import DBSession

__all__ = ['root_factory', 'container_factory']