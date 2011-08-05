from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from pyramid.url import route_url
from pyramid.view import view_config

import sawhoosh.model as M
@view_config(route_name='document_new', renderer='document/new.mako')
def document_new(request):
    authors = request.db.query(M.Author).all()
    return dict(authors=authors)

@view_config(route_name='document_edit', renderer='document/edit.mako')
def author_edit(request):
    document = request.db.query(M.Document).get(request.matchdict.get('id'))
    if not document:
        raise HTTPNotFound
    return dict(document=document)
            
@view_config(route_name='document_instance', renderer='document/view.mako')
def document_view(request):
    document = request.db.query(M.Document).get(request.matchdict.get('id'))
    if not document:
        raise HTTPNotFound
    return dict(document=document)
    
@view_config(route_name='document', request_method='GET', renderer='document/list.mako')
def document_list(request):
    documents = request.db.query(M.Document).all()
    return dict(documents=documents)

@view_config(route_name='document_instance', request_method='DELETE')
def document_delete(request):
    document = request.db.query(M.Document).get(request.matchdict.get('id'))
    if not document:
        raise HTTPNotFound
    request.db.delete(document)
    request.db.flush()
    return HTTPFound(location = route_url('document', request))
        
@view_config(route_name='document', request_method='POST')
def document_create(request):
    author = request.db.query(M.Author).get(request.params.get('author'))
    
    title = request.params.get('title')
    content = request.params.get('content')
    
    d = M.Document(title=title, content=content)
    author.documents.append(d)
    request.db.flush()
    
    return HTTPFound(location = route_url('document_instance', request, id=d.id))
    
@view_config(route_name='document_instance', request_method='PUT')
def document_update(request):
    document = request.db.query(M.Document).get(request.matchdict.get('id'))
    if not document:
        raise HTTPNotFound
    document.title = request.params.get('title')
    document.content = request.params.get('content')
    return HTTPFound(location = route_url('document_instance', request, id=document.id))