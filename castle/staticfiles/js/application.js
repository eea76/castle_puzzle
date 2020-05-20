$(document).ready(function() {

    var guesses = 0;
    $('.viewed-painting').on('click', function() {

        if (guesses < 3) {
            var paintingName = $(this).text();
            $('.unnamed-painting-title').append('<span class="viewed-painting-name" style="display:inline-block;padding:0 10px;">' + paintingName + ' ' + '</span>');

            guesses += 1;
        }

        if (guesses === 3) {
            var guessedTitle = $('.unnamed-painting-title').text();
            $('.viewed-paintings-list').slideUp(2000);
            $('.submit-title').fadeIn(3000);
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
                    alert('sorry try again or don\'t');
                }
            },

            processData: false,
            contentType: false,
            async: true
        });

        return true;

    })









});
