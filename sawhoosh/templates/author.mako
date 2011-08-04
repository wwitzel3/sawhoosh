<%inherit file="base.mako"/>

<h3>Author: ${author.name}</h3>
<h3>Publications</h3>
<ul>
%for d in author.documents:
<li><a href="/${d.uri()}">${d.title}</a></li>
%endfor
</ul>