from pyramid.decorator import reify
from pyramid.request import Request

from sawhoosh.search import WIX
from sawhoosh.model import DBSession

class RequestWithDBAttribute(Request):
    @reify
    def db(self):
        return DBSession()
        
    @reify
    def ix(self):
        return WIX
