(function ($) {
    $(document).ready(function ($) {
        var qrcode = window.location.protocol + "//" + window.location.host + '/qrcode/';
        var redirect = window.location.protocol + "//" + window.location.host + "/login/weixinapp/?next=/score/report";
        var viewsitelink = '<li>' +
            '<a class="viewsitelink" href="' + qrcode + redirect + '" role="button" target="_blank">' +
            '浏览 班主任评分汇总' +
            '</a>' +
            '</li>';
        $(".object-tools").append(viewsitelink);
    })
})(django.jQuery);