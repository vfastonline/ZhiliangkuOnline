import axios from 'axios';


let host = 'http://www.zhiliangku.com';
// let host = 'http://localhost:8080';

//发验证码短信
export const smsCode = parmas => {
  return axios.post(`${host}/sms_code/`, parmas)
};


