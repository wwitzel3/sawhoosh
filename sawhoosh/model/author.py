import uuid

from sqlalchemy import Integer
from sqlalchemy import CHAR
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from sqlalchemy.orm import relation

from sawhoosh.model import Base, new_uuid
from sawhoosh.model.document import Document

class Author(Base):
    __tablename__ = 'author'
    __whoosh_value__ = 'id,name'
    
    id = Column(CHAR(32), primary_key=True, default=new_uuid)
    name = Column(String, nullable=False)
    
    documents = relation(Document, backref='author', cascade='all')
        
    def __str__(self):
        return u'Author: {0}'.format(self.name)

    def route_name(self):
        return 'author_instance'
        
