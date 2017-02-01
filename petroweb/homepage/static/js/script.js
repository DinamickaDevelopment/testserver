$(function () {
    var videoResize = function () {
        $('.reqTrial').css({ "height": $(window).height() + "px"});
    }
    videoResize();
    $(window).resize(function () {
        videoResize();
    });   
})



