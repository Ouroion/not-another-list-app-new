import * as constants from '../constants/index';

export function setLists(lists) {
  return {
    type: constants.SET_LISTS,
    payload: lists
  };
}

export function switchShowAddListForm(currentVal) {
  return {
    type: constants.SWITCH_SHOW_ADD_LIST_FORM,
    payload: !currentVal
  };
}

export function setCreateListName(name) {
  return {
    type: constants.SET_CREATE_LIST_NAME,
    payload: name
  };
}

export function setCreateListDescription(description) {
  return {
    type: constants.SET_CREATE_LIST_DESCRIPTION,
    payload: description
  };
}
