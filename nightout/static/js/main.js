$(document).ready(function(){

    $( ".clickme" ).click(function() {
    $( ".searchbox" ).animate({
    width: "toggle"
    }, 500, function() {
    });
    });

});
