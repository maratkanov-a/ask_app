$(document).ready(function () {
//стандартный код инициализации запросов в ajax
    $.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
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
//-----------------------------------------------------------------------------------------------------
// скрываем элементы, которые потом вызовем
    $('.js-user-question').hide();
    $('.js-user-ans').hide();
    $('.js-new-ans').hide();
    var answer = $('.js-answer');
//---------------------------------------------------------------------------------------------------
// показываем поле ответа по нажатию
    answer.hide();
    $('.js-question').on('click', function(){
        $(this).next().toggle('slow');
    });
//---------------------------------------------------------------------------------------------------
//после набора текста в скрытом поле, по нажтию на кнопку ответить, отправляем POST запрос на сервер
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
            }

        });
        answer.hide('slow');
        return false;
    });
//---------------------------------------------------------------------------------------------------
//по нажатию на кнопки + или - отправляем запрос и меняем рейтинг на HTML странице
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
//---------------------------------------------------------------------------------------------------
//чистим всю страницу и вставляем туда задание вопроса
    $('.js-create-question').on('click', function(){
        $('.js-all-page').html('');
        $('.paginator').html('');
        $('.for-test').load('/create/');
    });
//---------------------------------------------------------------------------------------------------
//на странице пользователя по нажтию на кнопку показываем все его вопросы
    $('.userpage-question').on('click', function(){
        $('.js-user-question').toggle('slow');
        return false;
    });
//---------------------------------------------------------------------------------------------------
//на странице пользователя по нажтию на кнопку показываем все его ответы
    $('.userpage-ans').on('click', function(){
        $('.js-user-ans').toggle('slow');
        return false;
    });
//---------------------------------------------------------------------------------------------------
//чистим всю страницу и туда вставляем ответы, удовлетворяющие поиску
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
                $('.for-test').html(data);
            }
        });
    });
//---------------------------------------------------------------------------------------------------
});
