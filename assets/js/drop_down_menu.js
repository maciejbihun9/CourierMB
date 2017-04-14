
function hideMenuItems(elementId) {
    var x = document.getElementById(elementId);
    x.style.display = 'none';
}

function showMenuItems(elementId) {
    var x = document.getElementById(elementId);
    x.style.display = 'block';
}

function displaySendButton(){
  var item = ".send_btn";
  $(item).on("mouseover", function(){
    showMenuItems("send_dropdown");
  });
  $(item).on("mouseleave", function(){
    hideMenuItems("send_dropdown");
  });
}

function displayTrackButton(){
  var item = ".track_btn";
  $(item).on("mouseover", function(){
    showMenuItems("track_dropdown");
  });
  $(item).on("mouseleave", function(){
    hideMenuItems("track_dropdown");
  });
}

$(function() {
  $('nav li ul').hide().removeClass('fallback');
  $('nav li').hover(
    function () {
      $('ul', this).stop().slideDown(100);
    },
    function () {
      $('ul', this).stop().slideUp(100);
    }
  );


  displaySendButton();
  displayTrackButton();
});




// Close the dropdown menu if the user clicks outside of it
/*
window.onclick = function(event) {
  console.log("click on window");
  var dropdown = document.getElementById("track_dropdown");
  if (!event.target.matches('track_dropdown')){
     if (dropdown.style.display == 'block') {
        console.log("Element is still visible");
        dropdown.style.display = 'none';
      }
  }
};*/
