<%inherit file="../base.mako"/>

<p>Title: ${document.title}</p>
<p>Author: <a href="${request.route_url(document.author.route_name(), id=document.author.id)}">${document.author.name}</a></p>
<hr/>
<p>Content</p>
${document.content}


<a href="${request.route_url('document_edit', id=document.id)}">Edit</a>

<form id="delete" name="delete" action="${request.route_url('document_instance', id=document.id)}" method="POST">
<input type="submit" value="DELETE!" />
<input type="hidden" name="_method" value="DELETE" />
</form>

<br/><br/>