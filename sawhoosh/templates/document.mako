<%inherit file="base.mako"/>

<p>Title: ${document.title}</p>
<p>Author: <a href="/${document.author.uri()}">${document.author.name}</a></p>
<hr/>
<p>Content</p>
${document.content}