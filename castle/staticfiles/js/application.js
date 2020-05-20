$(document).ready(function() {


    $('.viewed-painting').on('click', function() {
        var paintingName = $(this).text()
        $('.unnamed-painting-title').text(paintingName);
    })








});
