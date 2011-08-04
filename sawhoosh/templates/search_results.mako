<ul id="search_results">
% for r in results:
    <li><a href="${request.resource_url(r)}">${r}</a></li>
%endfor
</ul>