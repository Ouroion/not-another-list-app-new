import * as constants from '../constants/index';

export function setLists(lists) {
  return {
    type: constants.SET_LISTS,
    payload: lists
  };
}

export function loginFailed() {

}
