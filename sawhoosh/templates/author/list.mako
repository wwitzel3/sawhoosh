<%inherit file="../base.mako"/>
<ul>
%for a in authors:
    <li><a href="${request.route_url('author_instance', id=a.id)}">${a}</a></li>
%endfor
