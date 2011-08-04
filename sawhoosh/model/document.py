import uuid

from sqlalchemy import Integer
from sqlalchemy import CHAR
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Text

from sqlalchemy import event
from sawhoosh.model import Base

class Document(Base):
    __tablename__ = 'documents'
    __whoosh_value__ = 'id,title,content,author_id'
    
    id = Column(CHAR(32), primary_key=True, default=uuid.uuid4().hex)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    
    author_id = Column(Integer, ForeignKey('authors.id'), index=True)
