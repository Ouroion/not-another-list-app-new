import { createStore, combineReducers, applyMiddleware } from 'redux';

// API Reducers
import thunk from 'redux-thunk';
import listReducer from '../reducers/listReducer';
import loginReducer from '../reducers/loginReducer';
import taskReducer from '../reducers/taskReducer';

// Page Reduces

// Component Reducers

// 3rd Parter

const rootReducer = combineReducers(
  {
    login: loginReducer,
    lists: listReducer,
    tasks: taskReducer
  }
);
const configureStore = () => {
  return createStore(rootReducer, applyMiddleware(thunk));
};

export default configureStore;
