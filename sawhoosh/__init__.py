from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from sawhoosh.model import initialize_sql

from sawhoosh.resources import root_factory
from sawhoosh.security import RequestWithDBAttribute

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    
    config = Configurator(
        settings=settings,
        root_factory=root_factory,
        request_factory=RequestWithDBAttribute,
    )

    config.begin()
        
    config.scan('sawhoosh.model')    
    initialize_sql(engine)
    
    config.add_static_view('static', 'sawhoosh:static')
    config.scan('sawhoosh.views')
    
    config.end()
    return config.make_wsgi_app()


