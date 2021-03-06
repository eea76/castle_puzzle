$(document).ready(function() {

    function ajaxCall(message, address, url) {
        $.ajax({
            type: 'post',
            data: JSON.stringify(message),
            url: 'view_painting',
            success: function(response) {
                location.href = address;
            },

            processData: false,
            contentType: false,
            async: true
        });

        return true;
    }

    $('map').imageMapResize();

    $('area').on('click', function(e) {
        e.preventDefault();
        var address = $(this).attr('href');
        var painting = $(this).attr('href').split('/');
        var paintingId = painting.pop();

        console.log(address);
        var message = {};

        message.paintingId = paintingId;

        ajaxCall(message, address, 'view_painting');

    })

    var guesses = 0;
    $('.viewed-painting').on('click', function() {

        if (guesses < 3) {
            var paintingName = $(this).text();
            $('.unnamed-painting-title').append('<span class="viewed-painting-name" style="display:inline-block;padding:0 10px;">' + paintingName + ' ' + '</span>');

            guesses += 1;
        }

        if (guesses === 3) {
            var guessedTitle = $('.unnamed-painting-title').text();
            $('.viewed-paintings').hide();
            $('.submit-title').fadeIn(1000);
            $('#submitted-title').text(guessedTitle);
        }
    });

    $('.start-over').on('click', function() {
        window.location = '/unnamed';
    })


    $('.submit').on('click', function() {
        var guessedTitle = $('.unnamed-painting-title').text();
        var message = {};

        message.guess = guessedTitle;

        $.ajax({
            type: 'post',
            data: JSON.stringify(message),
            url: 'painting_guess',
            success: function(response) {
                response = JSON.parse(response)
                if (response.correct) {

                    var english = response.english;
                    var latin = response.latin;
                    var imageAddress = response.image;
                    $('.title-text h1').text(english);
                    $('.title-text h5').text(latin);
                    $('.results-modal .image-container').find('img').attr('src', imageAddress);
                    $('.painting-container').fadeOut(2000);
                    $('.titles-container').fadeOut(2000);
                    $('.results-modal').fadeIn(4000);
                } else {
                    alert('sorry that is incorrect');
                }
            },

            processData: false,
            contentType: false,
            async: true
        });

        return true;

    })









});
