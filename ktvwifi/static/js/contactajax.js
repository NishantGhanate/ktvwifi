$(document).ready(function () {
    $("#contactform").submit(function (event) {
      $.ajax({
        type: "POST",
        url: "/contact",
        data: {
          'video': $('#test').val() // from form
        },
        success: function () {
          $('#message').html("<h2>Contact Form Submitted!</h2>")
        }
      });
      return false; //<---- move it here
    });
  });