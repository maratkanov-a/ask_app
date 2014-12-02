/**
 * Created by sashok on 03.11.14.
 */
$(document).ready(function () {

    $.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});

    $('.js-user-question').hide();
    $('.js-user-ans').hide();
    $('.js-new-ans').hide();
    var answer = $('.js-answer');
    answer.hide();
    $('.js-question').on('click', function(){
        $(this).next().toggle('slow');
    });

    answer.on('submit', function(){
        var elem = $(this);
        $.ajax('/home/',{
            type: 'POST',
            data: $(this).parent().find('.form-ans').serialize(),
            success: function(result){
                var el = elem.parent().next();
                var text = elem.parent().find('.js-text-in-area').val();
                el.children('.js-for-text').html(text);
                el.show('slow')
            },
            error: function(){
                $('.for-test').html('BAD');
            }

        });
        answer.hide('slow');
        return false;
    });

    $('.rating').on('submit', function(){return false;});
    $('.js-minus, .js-plus').on('click', function(e){

        var element = $(this);
        var ratingEl = element.parent().find('.update-me');
        var ratingVal = +ratingEl.text();

        e.preventDefault();
        $.ajax('/home/rate/', {
            type: 'POST',
            async: false,
            dataType: "text",
//            data: $('.rating').serialize(),
            data:  {rate: element.val(), ans_id: element.data('id')},
            success:function(){

                ratingEl.html(element.hasClass('js-minus') ? --ratingVal : ++ratingVal);
                element.parent().find('.update_me').html(ratingEl);
            },
            error: function(){
                $('.for-test').html('BAD');
            },
            complete: function(){
                element.addClass('disabled');

            }
        });
    });

    $('.js-create-question').on('click', function(){
        $('.js-all-page').html('');
        $('.paginator').html('');
        $('.for-test').load('/create/');
    });

//    $('.js-create-question').on('submit', function(e){
//        var elem = $(this);
//        e.preventDefault();
//        $.ajax('/create/',{
//            type: 'POST',
//            dataType: 'text',
//            data: elem.serialize(),
////            data: {question_label: elem.find(), question_text: elem.find('.form-control').val()},
//            success: function(){
//                $('.for-test-create').html('GOOD');
//            },
//            error: function(){
//                $('.for-test-create').html('BAD');
//            }
//        });
//    return false;
//    });

    $('.userpage-question').on('click', function(){
        $('.js-user-question').toggle('slow');
        return false;
    });
    $('.userpage-ans').on('click', function(){
        $('.js-user-ans').toggle('slow');
        return false;
    });

    $('.js-search').on('keyup', function(e){
        e.preventDefault();
        $('.js-all-page').html('');
        $('.paginator').html('');
        var elem = $('.js-search-text');
        $.ajax('/forsearch/',{
            type: 'GET',
            dataType:'text',
            data: {text: elem.val()},
            success: function(data){
//                var el = elem.val();
//                var page = xmlhttp.open("GET",'/forsearch/'+'?text='+el ,true);
                $('.for-test').html(data);
            }
        });
    });


});
