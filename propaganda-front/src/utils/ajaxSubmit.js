var ajaxSubmit = {};
var dateStram = (new Date()).getTime();
ajaxSubmit.allUrl = {
  // 职场素质接口eq,
  "login_eq": "eq/",
  // 逻辑能力接口
  "login_iq": "iq/",
  // 登录接口
  "login": "quick-login/",
  // 短信验证码
  "message": "sms_code/",
  // 咨询师接口
  "consultation": "consultant/"


}
ajaxSubmit.ajax = function(option) {
  //默认data传值
  option.data = option.data ? option.data : {};
  //url, data, success, cache, alone, async, type, dataType, error
  var url = option.url;
  var data = option.data;
  var type = option.type || 'post'; //请求类型
  var dataType = option.dataType || 'json'; //接收数据类型
  var async = option.async || true; //异步请求
  var cache = option.cache || false; //浏览器历史缓存
  var contentType = option.contentType || 'application/x-www-form-urlencoded; charset=UTF-8';
  var success = function(data) {
    option.success ? option.success(data) : "";
  };
  var error = function(jqXHR, textStatus, errorThrown) {
    option.error ? option.error() : "";
  };
  $.ajax({
    url: url,
    data: data,
    type: type,
    contentType: contentType,
    dataType: dataType,
    async: async,
    timeout: 50000,
    success: success,
    error: error,
    beforeSend: function(XMLHttpRequest) { 
         
        },
  });
}

export default ajaxSubmit;
