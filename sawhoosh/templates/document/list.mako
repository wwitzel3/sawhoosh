<%inherit file="../base.mako"/>
<ul>
%for d in documents:
    <li><a href="${request.route_url(d.route_name(), id=d.id)}">${d}</a></li>
%endfor


<br/><br/>