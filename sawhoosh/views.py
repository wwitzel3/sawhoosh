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

import sawhoosh.model as M

@view_config(route_name='index', renderer='index.mako')
def index(request):
    return dict()
    
@view_config(route_name='search', renderer='json', xhr=True)
def search_ajax(request):
    query = request.params.get('keywords')
    parser = QueryParser('value', request.ix.schema)
    with request.ix.searcher() as searcher:
        query = parser.parse(query)
        results = searcher.search(query)
        search_results_html=render('sawhoosh:templates/search_results.mako',
                              dict(results=results_to_instances(request, results)),
                              request=request)
    return dict(search_results_html=search_results_html)
    
@view_config(route_name='search', renderer='search.mako')
def search_mako(request):
    return dict()
    
@view_config(route_name='author', renderer='author.mako')
def author_view(request):
    author = request.db.query(M.Author).get(request.matchdict.get('id'))
    if not author:
        raise HTTPNotFound
    return dict(author=author)

@view_config(route_name='document', renderer='document.mako')
def document_view(request):
    document = request.db.query(M.Document).get(request.matchdict.get('id'))
    if not document:
        raise HTTPNotFound
    return dict(document=document)