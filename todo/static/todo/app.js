const site_url = 'http://127.0.0.1:8000/';
let markDone;
let deleteElement;

$(document).ready(function () {
    markDone = function (id) {
        $.ajax({
            url: site_url + 'update/',
            cache: false,
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
            cache: false,
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