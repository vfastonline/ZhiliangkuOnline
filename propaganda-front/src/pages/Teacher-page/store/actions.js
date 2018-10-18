import * as types from './mutation-types';
// 提交mutation
function makeAction (type) {
  return ({ commit }, ...args) => commit(type, ...args);
}

export const setInfo = makeAction(types.SET_INFO);
export const setNav = makeAction(types.SET_NAV);

// export const getPermit = makeAction(types.GET_PERMIT);
// export const getNavInfo = makeAction(types.GET_NAV);

export const setLoginDialogStatus = makeAction(types.SET_LOGINDIALOGOPEN);
