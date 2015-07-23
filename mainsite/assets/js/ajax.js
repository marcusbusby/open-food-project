$(function(){
	$('#search').keyup(function() {
		$.ajax({
			type: "GET",
			url: "/search/",
			data: {
				'search_text' : $('#search').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: 'html'
		});
	});

	$('.sort a').click(function(evt) {
		evt.preventDefault();
		$.ajax({
			type: "GET",
			url: "/sort/",
			data: {
				'sort_value' : $('.sort').attr('id'),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: sortSuccess,
			dataType: 'html'
		});
	});
});

function sortSuccess(data, textStatus, jqXHR)
{
	$('#sort-results').html(data);
}

function searchSuccess(data, textStatus, jqXHR)
{
	$('#search-results').html(data);
}