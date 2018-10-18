import Vue from 'vue'
import Vuex from 'vuex';

import mutations from './mutations';
import state from './state';
import * as actions from './actions';
import * as getters from './getters';

Vue.use(Vuex);

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});
