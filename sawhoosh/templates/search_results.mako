<ul id="search_results">
% for r in results:
    <li><a href="/${r.uri()}">${r}</a></li>
%endfor
</ul>