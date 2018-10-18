import cookie from "../static/js/cookie";

const userInfo = {
  name: cookie.getCookie('name') || '',
  token: cookie.getCookie('token') || ''
};

const state = {
  userInfo,
  loginDialogOpen: false
};

export default state
