<%inherit file="../base.mako"/>
<p>
<h3>Author: ${author.name}</h3>
<h3>Publications</h3>
<ul>
%for d in author.documents:
<li><a href="${request.route_url(d.route_name(), id=d.id)}">${d.title}</a></li>
%endfor
</ul>

<a href="${request.route_url('author_edit', id=author.id)}">Edit</a>

<form id="delete" name="delete" action="${request.route_url('author_instance', id=author.id)}" method="POST">
<input type="submit" value="DELETE!" />
<input type="hidden" name="_method" value="DELETE" />
</form>

</p>
