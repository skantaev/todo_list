const site_url = 'http://127.0.0.1:8000/';
let markDone;
let deleteElement;

$(document).ready(function () {
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    markDone = function (id) {
        $.ajax({
            url: site_url + 'update/',
            method: "POST",
            data: {
                'id': id,
            },
            success: function () {
                $("#list").load(" #list");
            }
        })
    };

    deleteElement = function (id) {
        $.ajax({
            url: site_url + 'delete/',
            method: "POST",
            data: {
                'id': id,
                'delete': 'yes',
            },
            success: function () {
                $("#list").load(" #list");
            }
        })
    }
});