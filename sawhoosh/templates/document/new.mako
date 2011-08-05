<%inherit file="../base.mako"/>

<form id="document" name="create" action="${request.route_url('document')}" method="POST">
<label for="author">Author</label>
<select name="author">
%for a in authors:
<option value="${a.id}">${a.name}</option>
%endfor
</select>
<label for="name">Title</label>
<input type="text" name="title" />
<textarea name="content">
</textarea>
<input type="submit" />
</form>

<br/><br/>