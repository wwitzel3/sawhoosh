import transaction

from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from pyramid.url import route_url
from pyramid.view import view_config

import sawhoosh.model as M

@view_config(route_name='author_new', renderer='author/new.mako')
def author_new(request):
    return dict()

@view_config(route_name='author_edit', renderer='author/edit.mako')
def author_edit(request):
    author = request.db.query(M.Author).get(request.matchdict.get('id'))
    if not author:
        raise HTTPNotFound
    return dict(author=author)

@view_config(route_name='author_instance', renderer='author/view.mako')
def author_view(request):
    author = request.db.query(M.Author).get(request.matchdict.get('id'))
    if not author:
        raise HTTPNotFound
    return dict(author=author)

@view_config(route_name='author', renderer='author/list.mako')
def author_list(request):
    authors = request.db.query(M.Author).all()
    return dict(authors=authors)
           
@view_config(route_name='author_instance', request_method='PUT')
def author_update(request):
    author = request.db.query(M.Author).get(request.matchdict.get('id'))
    if not author:
        raise HTTPNotFound
    author.name = request.params.get('name')
    return HTTPFound(location = route_url('author_instance', request, id=author.id))

@view_config(route_name='author_instance', request_method='DELETE')
def author_delete(request):
    author = request.db.query(M.Author).get(request.matchdict.get('id'))
    if not author:
        raise HTTPNotFound
    request.db.delete(author)
    request.db.flush()
    return HTTPFound(location = route_url('author', request))
           
@view_config(route_name='author', request_method='POST')
def author_create(request):
    name = request.params.get('name')
    a = M.Author(name=name)
    request.db.add(a)
    request.db.flush()
    return HTTPFound(location = route_url('author_instance', request, id=a.id))
