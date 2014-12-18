$(document).ready(function() {
    $('.vote-btn').click(function(){
	var vote_button = $(this);
	var entry_pk = vote_button.attr("entry-pk");
	$.post(vote_url, 
	       {csrfmiddlewaretoken : csrf_token, 
		entry_pk: entry_pk}, 
	       function(data, status) {
		   $('#num-votes-'+entry_pk).html(data);
		   vote_button.hide();
	});
    });
});

