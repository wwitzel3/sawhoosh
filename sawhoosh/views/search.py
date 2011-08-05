from pyramid.view import view_config
from pyramid.renderers import render

from whoosh.qparser import QueryParser
from sawhoosh.search import results_to_instances

@view_config(route_name='search', renderer='json', xhr=True)
def search_ajax(request):
    query = request.params.get('keywords')
    parser = QueryParser('value', request.ix.schema)
    with request.ix.searcher() as searcher:
        query = parser.parse(query)
        results = searcher.search(query)
        search_results_html=render('sawhoosh:templates/search/results.mako',
                              dict(results=results_to_instances(request, results)),
                              request=request)
    return dict(search_results_html=search_results_html)
    
@view_config(route_name='search', renderer='search/view.mako')
def search_mako(request):
    return dict()