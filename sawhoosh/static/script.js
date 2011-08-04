$(document).ready(function () {
   $('#search').submit(function () {
      return false; 
   });
   
   $('#search_button').click(function () {
      $.ajax({
          url: '/search',
          type: 'GET',
          context: document.body,
          dataType: 'json',
          data: $('#search').serialize(),
          success: function(data) {
              $('#search_results').html(data['search_results_html']);
          }
      });
   });
});