import uuid

from sqlalchemy import Integer
from sqlalchemy import CHAR
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from sqlalchemy.orm import relation

from sawhoosh.model import Base
from sawhoosh.model.document import Document

class Author(Base):
    __tablename__ = 'author'
    __whoosh_value__ = 'id,name'
    
    id = Column(CHAR(32), primary_key=True, default=uuid.uuid4().hex)
    name = Column(String, nullable=False)
    
    documents = relation(Document, backref='author')
        
    def __str__(self):
        return u'Author: {0}'.format(self.name)
        
