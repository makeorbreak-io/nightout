$(document).ready(function(){

    $( ".clickme" ).click(function() {
    $( ".searchbox" ).animate({
    width: "toggle"
    }, 500, function() {
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
