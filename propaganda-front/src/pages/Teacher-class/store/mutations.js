import * as types from './mutation-types';
import cookie from '../statics/js/cookie';
import Vue from 'vue';
import Axios from 'axios';

Vue.prototype.$http = Axios;


export default {
  [types.SET_INFO](state) {
    state.userInfo = {
      name: cookie.getCookie('name'),
      token: cookie.getCookie('token')
    };
  },

  [types.SET_LOGINDIALOGOPEN](state, data) {
    state.loginDialogOpen = data;
  }
}
