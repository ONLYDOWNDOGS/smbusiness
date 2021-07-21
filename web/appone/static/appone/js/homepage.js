// Put jQuery here, not javascript you dumb-dumb
$(window).scroll(function() {
    $(".top").css("opacity", 2.5 - $(window).scrollTop() / 250);
});


//  $(window).scroll(function() {
//      $(".middle").css("opacity", 2.5 - $(window).scrollTop() / 250);
//  });

$(window).scroll(function() {
    $(".bottom").css("opacity", 7 - $(window).scrollTop() / 250);
});