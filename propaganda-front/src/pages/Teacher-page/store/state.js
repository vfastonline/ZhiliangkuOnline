import cookie from "../statics/js/cookie";

const userInfo = {
  name: cookie.getCookie('name') || '',
  token: cookie.getCookie('token') || ''
};

const state = {
  userInfo,
  loginDialogOpen: false
};

export default state
