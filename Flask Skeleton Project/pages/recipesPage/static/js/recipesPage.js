// recipes

$(document).ready(function () {
    $(".more.btn").on('click', function () {
        $(this).parent().parent().find(".more-text").toggleClass("active");
    });
});