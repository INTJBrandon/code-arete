// shows overlay & stops user from scrolling
$("img.hamburger").click(function(){
    $("div.overlay").fadeIn();
    $("html, body").css({
        overflow: 'hidden',
        height: '100%'
    });
});

// hides overlay & allows user to scroll again
$("img.close").click(function(){
    $("div.overlay").fadeOut();
    $("html, body").css({
        overflow: 'auto',
        height: 'auto'
    });
});

var postNumber = document.getElementsByClassName('post');
if (postNumber.length > 4) {
    alert("There's more than 4");
}