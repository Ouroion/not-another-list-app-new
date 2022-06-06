import * as constants from '../constants/index';

export function setTasks(tasks) {
  return {
    type: constants.SET_TASKS,
    payload: tasks
  };
}

export function setTaskListName(name) {
  return {
    type: constants.SET_TASKS_LIST_NAME,
    payload: name
  };
}

export function setTaskListId(name) {
  return {
    type: constants.SET_TASKS_LIST_ID,
    payload: name
  };
}

export function switchShowAddTaskForm(currentVal) {
  return {
    type: constants.SWITCH_SHOW_ADD_TASK_FORM,
    payload: !currentVal
  };
}

export function setCreateTaskName(name) {
  return {
    type: constants.SET_CREATE_TASK_NAME,
    payload: name
  };
}

export function setCreateTaskDescription(description) {
  return {
    type: constants.SET_CREATE_TASK_DESCRIPTION,
    payload: description
  };
}

export function switchSetTaskIsDone(currentVal) {
  return {
    type: constants.SWITCH_SET_TASK_IS_DONE,
    payload: !currentVal
  };
}
