<%inherit file="../base.mako"/>

<form id="author" name="edit" action="${request.route_url('author_instance', id=author.id)}" method="POST">
<label for="name">Name</label>
<input type="text" name="name" value="${author.name}" />
<input type="hidden" name="_method" value="PUT" />
<input type="submit" />
</form>
