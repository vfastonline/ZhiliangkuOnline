import axios from 'axios';
let host = 'https://www.zhiliangku.com';
// let host = 'http://localhost:8080';
// let host = '/api'

// 登录接口
export const login = parmas => {
  return axios.post(`${host}/login/`,parmas)
};
//班级接口
export const sendClass = parmas => {
  return axios.get(`${host}/get_team/`)
};
// 提交接口
export const userClass = parmas => {
// 
  // return axios.patch(`${host}/set_user_class/5bb1c6071c6233406b01b3fe/`, parmas)
  return axios.patch(`${host}/set_user_class/5bb1c6071c6233406b01b3fe/`, parmas)
};
// 评价页面老师与学生详细信息接口
export const information = parmas => {
  return axios.get(`${host}/user_score/`)
};
// 提交老师评价数据
export const submit_data = parmas => {
  return axios.post(`${host}/user_score/`, parmas)
};
// 提交学生
export const class_data = parmas => {
  return axios.post(`${host}/user_score/`, parmas)
};

