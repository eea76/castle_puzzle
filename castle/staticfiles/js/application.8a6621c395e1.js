$(document).ready(function() {

    $('map').imageMapResize();

    $('area').on('click', function(e) {
        e.preventDefault();
        var address = $(this).attr('href');
        var painting = $(this).attr('href').split('/');
        var paintingId = painting.pop();

        console.log(address);
        var message = {};

        message.paintingId = paintingId;


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
            $('.viewed-paintings-list').slideUp(1000);
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
                if (response === 'correct') {
                    // $('.painting-container').animate({opacity: 0}, 2000);
                    $('.painting-container').fadeOut(2000);
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
