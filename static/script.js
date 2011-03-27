$(document).ready(function() {
	$('dd').hide();
	/*$("dd:not(:first)").hide();*/
	$("dt a").click(function(){
		
		$("dd:visible").slideUp("slow");
		$(this).parent().next().slideDown("slow");
		return false;
	});
});

$(document).ready(function() {
	$("#more").hide();
	$("#expand").click(function(){
	$(this).hide();
	$("#more").slideDown("fast");
	
	});

});

/*$(document).ready(function() {*/