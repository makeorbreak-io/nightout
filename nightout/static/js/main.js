$(document).ready(function(){

    $( ".clickme" ).click(function() {
    $( ".searchbox" ).animate({
    width: "toggle"
    }, 500, function() {
    });
    });
    //var availableTags = JSON.parse(availableTags)

$(function() {
  function split( val ) {
    return val.split( /,\s*/ );
  }
  function extractLast( term ) {
    return split( term ).pop();
  }

$( "#userSearch" )
  // don't navigate away from the field on tab when selecting an item
  .bind( "keydown", function( event ) {
    if ( event.keyCode === $.ui.keyCode.TAB &&
        $( this ).data( "ui-widget" ).menu.active ) {
      event.preventDefault();
    }
  })
  .autocomplete({
    source:availableTags,
    search: function() {
      // custom minLength
      var term = extractLast( this.value );
      if ( term.length < 1 ) {
        return false;
      }
    },
    focus: function() {
      // prevent value inserted on focus
      return false;
    },
    select: function( event, ui ) {
      var terms = split( this.value );
      // remove the current input
      terms.pop();
      // add the selected item
      terms.push( ui.item.value );
      // add placeholder to get the comma-and-space at the end
      terms.push( "" );
      this.value = terms.join( ", " );
      return false;
    }
  });
  $( "#userEventa" )
    // don't navigate away from the field on tab when selecting an item
    .bind( "keydown", function( event ) {
      if ( event.keyCode === $.ui.keyCode.TAB &&
          $( this ).data( "ui-widget" ).menu.active ) {
        event.preventDefault();
      }
    })
    .autocomplete({
      source:availableTagsEv,
      search: function() {
        // custom minLength
        var term = extractLast( this.value );
        if ( term.length < 1 ) {
          return false;
        }
      },
      focus: function() {
        // prevent value inserted on focus
        return false;
      },
      select: function( event, ui ) {
        var terms = split( this.value );
        // remove the current input
        terms.pop();
        // add the selected item
        terms.push( ui.item.value );
        // add placeholder to get the comma-and-space at the end
        terms.push( "" );
        this.value = terms.join( ", " );
        return false;
      }
    });

});
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function changeEventStatus(id){
  var e = document.getElementById("status_"+id);
  var val = e.options[e.selectedIndex].value;

  $.ajaxSetup({
      headers: { "X-CSRFToken": getCookie("csrftoken") }
  });
  $.ajax({
    url:"/ajax/changeEventStatus",
    type: "POST",
    data: {EventId: id, value:val },
    success:function(response){},
    complete:function(){},
    error:function (xhr, textStatus, thrownError){
        alert("error doing something");
    }
});
}

function search(){
  var el = document.getElementById('searchBox');
  var list = document.getElementById('searchResults')
  var searchstr=el.value;
  $.ajaxSetup({
      headers: { "X-CSRFToken": getCookie("csrftoken") }
  });
  $.ajax({
    url:"/ajax/search",
    type: "POST",
    data: {search: searchstr},
    success:function(response){
      $(list).empty();
      obj = JSON.parse(response)
      console.log(obj.length);
      for (var user in obj) {
        console.log(obj[user].fields.first_name);
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href="/user/"+obj[user].pk;
        a.appendChild(document.createTextNode(obj[user].fields.first_name+" "+obj[user].fields.last_name));
        li.appendChild(a);
        li.className="list-group-item";
        list.appendChild(li);
      }

    },
    complete:function(){},
    error:function (xhr, textStatus, thrownError){
        alert("error doing something");
    }
});
}
