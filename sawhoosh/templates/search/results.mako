%if results:
<ul id="search_results">
% for r in results:
    <li><a href="${request.route_url(r.route_name(), id=r.id)}">${r}</a></li>
%endfor
</ul>
%else:
<p>No results found</p>
%endif