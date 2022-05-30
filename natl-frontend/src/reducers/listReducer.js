import * as constants from '../constants/index';

const initialState = {
  list: []
};
const listReducer = (state = initialState, action) => {
  switch (action.type) {
    case constants.SET_LISTS:
      return {
        ...state,
        list: action.payload
      };
    default:
      return state;
  }
};
export default listReducer;
