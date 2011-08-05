<%inherit file="../base.mako"/>

<form id="author" name="edit" action="${request.route_url('document_instance', id=document.id)}" method="POST">
<label for="title">Title</label>
<input type="text" name="title" value="${document.title}" />
<label for="content">Content</label>
<textarea name="content">
${document.content}
</textarea>
<input type="hidden" name="_method" value="PUT" />
<input type="submit" />
</form>
