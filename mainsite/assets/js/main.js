$(function(){

	$('.myModal').on("show.bs.modal", function(evt) {
		var linkobj = $(evt.relatedTarget);
		$(this).find('.modal-body').load(linkobj.attr('href'))
	});

	$('.post-form').on('submit', function(event){
		event.preventDefault();
		console.log("form submitted!")
	})
});