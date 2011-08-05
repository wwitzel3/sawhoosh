<%inherit file="../base.mako"/>

<form action="/search" method="GET" name="search" id="search">
<input type="text" name="keywords" />
<button id="search_button">Search...</button>
</form>

<div id="search_results"></div>