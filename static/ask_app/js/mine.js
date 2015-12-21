$('.js-rating').on('click', function() {
    var new_this = $(this);
    $.post('/question/' + $(this).data('question-id') + '/change/rating/',
        { rating: new_this.data('type') },
        function(){
            $( '.js-change-rating' ).load( '/ .js-change-rating' );
        }
    );
});

$('.js-press-flag').on('click', function() {
    var new_this = $(this);
    $.post('/answer/' + $(this).data('answer-id') + '/change/flag/',
        { flag: new_this.data('flag') },
        function(){
            $( "body" ).load( '/question/' + $('.js-rating').data('question-id') + '/' );
        }
    );
});
