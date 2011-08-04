from pyramid.view import view_config
from pyramid.renderers import render

try:
    import cPickle as pickle
except ImportError, e:
    import pickle
    
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

from sawhoosh.search import SawhooshSchema
from sawhoosh.search import INDEX_NAME
from sawhoosh.search import results_to_instances

@view_config(renderer='index.mako')
def index(request):
    return dict()
    
@view_config(name='search', renderer='json', xhr=True)
def search_ajax(request):
    query = request.params.get('keywords')
    parser = QueryParser('value', request.ix.schema)
    with request.ix.searcher() as searcher:
        query = parser.parse(query)
        results = searcher.search(query)
        search_results_html=render('sawhoosh:templates/search_results.mako',
                              dict(results=results_to_instances(request.db, results)),
                              request=request)
    return dict(search_results_html=search_results_html)
    
@view_config(name='search', renderer='search.mako')
def search_mako(request):
    return dict()
