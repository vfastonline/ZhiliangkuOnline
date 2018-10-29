import axios from 'axios';


// let host = 'http://www.zhiliangku.com';
// let host = 'http://localhost:8080';
let host = '/api';

// 登录接口
export const logins = parmas => {
  return axios.post(`${host}/login/`,parmas)
};
//班级列表数据
export const class_list = parmas => {
  return axios.get(`${host}/get_team/`)
};

//发送班级详细数据
export const class_details = params => {
  return axios.get(`${host}/user_score_item_avg/?`, params)
};


