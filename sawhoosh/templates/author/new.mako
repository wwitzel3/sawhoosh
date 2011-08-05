<%inherit file="../base.mako"/>

<form id="author" name="create" action="${request.route_url('author')}" method="POST">
<label for="name">Name</label>
<input type="text" name="name" />
<input type="submit" />
</form>
