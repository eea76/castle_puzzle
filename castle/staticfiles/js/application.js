$(document).ready(function() {

    // function for making the ajax call
    function ajaxCall(message, address, url) {
        $.ajax({
            type: 'post',
            data: JSON.stringify(message),
            url: url,
            success: function(response) {
                location.href = address;
            },

            processData: false,
            contentType: false,
            async: true
        });

        return true;
    }

    // resizes the imagemaps so the coordinates
    // stay in the same location regardless of zoom level
    $('map').imageMapResize();

    // call the view_painting view with id of clicked image
    $('area').on('click', function(e) {
        e.preventDefault();
        var address = $(this).attr('href');
        var painting = $(this).attr('href').split('/');
        var paintingName = painting.pop();
        var message = {};

        message.paintingName = paintingName;

        ajaxCall(message, address, '/view_painting');

    })

    // if guessed title < 3 words, allow for more guesses
    // if === 3, hide title list and ask if user is ready to submit
    var guesses = 0;
    var timestamps = [];
    $('.viewed-painting').on('click', function() {

        if (guesses < 3) {

            var paintingName = $(this).text();

            var currentTime = new Date();
            timestamps.push(currentTime);

            $('.unnamed-painting-title').append('<span class="viewed-painting-name" style="display:inline-block;padding:0 10px;">' + paintingName + ' ' + '</span>');

            guesses += 1;
        }

        if (guesses === 3) {
            console.log(timestamps);
            var guessedTitle = $('.unnamed-painting-title').text();
            $('.viewed-paintings').hide();
            $('.submit-title').fadeIn(1000);
            $('#submitted-title').text(guessedTitle);
        }
    });

    // clear the viewed paintings
    // (this makes a call to django and deletes all
    // viewed paintings associated with the logged-in user)
    $('.start-over').on('click', function() {
        window.location = '/unnamed';
    })

    // submits chosen title
    // alert if incorrect, show success modal if correct
    $('.submit').on('click', function() {
        var guessedTitle = $('.unnamed-painting-title').text();
        var message = {};

        message.guess = guessedTitle;
        message.timestamps = timestamps;

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
                    var guessCount = response.attempts_count;
                    $('.title-text h1').text(english);
                    $('.title-text h5').text(latin);
                    $('.title-text p #guess-count').text(guessCount);
                    $('.results-modal .image-container').find('img').attr('src', imageAddress);
                    $('.painting-container').fadeOut(2000);
                    $('.titles-container').fadeOut(2000);
                    $('.results-modal').fadeIn(4000);
                } else if (response.tried_to_hack) {
                    alert(response.tried_to_hack);
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


    //get page load info
    var user = detect.parse(navigator.userAgent);

    var data_message = {};
    data_message.browser = user.browser.name;
    data_message.os = user.os.name;
    data_message.url = window.location.href;
    console.log(data_message.os);

    $.ajax({
        type: 'post',
        data: JSON.stringify(data_message),
        url: '/detect_browser/',
        success: function(response) {

        },
        processData: false,
        contentType: false,
        async: true
    });
});
