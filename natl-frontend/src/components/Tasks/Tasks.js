import React from 'react';
import './Tasks.css';

// Redux Related Imports
import { connect } from 'react-redux';
import * as listActions from '../../actions/listAction';
import * as actions from '../../actions/taskAction';

// Configuration
import config from '../../config/dev';

class TasksComponent extends React.Component {
  constructor(props) {
    super(props)
    this.createTask= this.createTask.bind(this);
    this.loadTasks = this.loadTasks.bind(this);
    this.deleteTask = this.deleteTask.bind(this);
    this.switchTaskIsDone = this.switchTaskIsDone.bind(this);
  }

  async createTask() {
    const resp = await fetch(`${config.baseUrl}/task/create`, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        access_id: this.props.login.accessId,
        name: this.props.tasks.name,
        description: this.props.tasks.description,
        list_id: this.props.tasks.taskListId,
        is_done: false
      })
    });
    const body = await resp.json();
    if (body !== undefined) {
      console.log(body)
    }
    await this.loadTasks(this.props.tasks.taskListId)
    this.props.switchShowAddTaskForm(this.props.tasks.showAddTaskForm)
   }

   async deleteTask(id){
    const resp = await fetch(`${config.baseUrl}/task/delete`, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        access_id: this.props.login.accessId,
        id: id,
      })
    });
    const body = await resp.json();
    if (body !== undefined) {
      console.log(body)
    }
    await this.loadTasks(this.props.tasks.taskListId)
   }

   async loadTasks(id) {
    const resp = await fetch(`${config.baseUrl}/task/list`, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        access_id: this.props.login.accessId,
        list_id: id,
      })
    });
    const body = await resp.json();
    if (body !== undefined) {
      console.log(body)
    }
    this.props.setTasks(body)
   }

   async switchTaskIsDone(id, is_done) {
    const resp = await fetch(`${config.baseUrl}/task/isdone`, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        access_id: this.props.login.accessId,
        id: id,
        is_done: is_done
      })
    });
    const body = await resp.json();
    if (body !== undefined) {
      console.log(body)
    }
    this.loadTasks(this.props.tasks.taskListId)
   }

  render() {
    if (this.props.tasks.showAddTaskForm){
      return (
        <div className="list-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Description</th>
              <th>Done?</th>
            </tr>
          </thead>
          <tbody>
            {this.props.tasks.tasks.map((data, key) => {
              return (
                <tr key={key}>
                  <td>{data.id}</td>
                  <td>{data.name}</td>
                  <td>{data.description}</td>
                  <td>{data.is_done.toString()}</td>
                  <td> <button type="submit" onClick={() => this.switchTaskIsDone(data.id, !data.is_done)}>Switch Is Done</button></td>
                  <td> <button type="submit" onClick={() => this.deleteTask(data.id)}>Delete Task</button></td>
                </tr>
              )
            })}
          </tbody>
        </table>
        <button onClick={() => this.props.switchShowAddTaskForm(this.props.tasks.showAddTaskForm)}>Add Task</button>
        <div className="login-wrapper">
                <h1>Please Log In</h1>
                <div>
                    <label>
                        <p>Task Name</p>
                        <input type="text" onChange={(name) => this.props.setCreateTaskName(name.target.value)} />
                    </label>
                    <label>
                        <p>Task Description</p>
                        <input type="text" onChange={(description) => this.props.setCreateTaskDescription(description.target.value)} />
                    </label>
                    <div>
                        <button type="submit" onClick={() => this.createTask()}>Create List</button>
                    </div>
                </div>
            </div>
      </div>
      )
    }
    return (
      <div className="list-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Description</th>
              <th>Done?</th>
            </tr>
          </thead>
          <tbody>
            {this.props.tasks.tasks.map((data, key) => {
              return (
                <tr key={key}>
                  <td>{data.id}</td>
                  <td>{data.name}</td>
                  <td>{data.description}</td>
                  <td>{data.is_done.toString()}</td>
                  <td> <button type="submit" onClick={() => this.switchTaskIsDone(data.id, !data.is_done)}>Switch Is Done</button></td>
                  <td> <button type="submit" onClick={() => this.deleteTask(data.id)}>Delete Task</button></td>
                </tr>
              )
            })}
          </tbody>
        </table>
        <button onClick={() => this.props.switchShowAddTaskForm(this.props.tasks.showAddTaskForm)}>Add Task</button>
      </div>
    )
  }
}
const mapStateToProps = (state) => {
  return { ...state };
};

const mapDispatchToProps = (dispatch) => {
  return {
    switchShowAddTaskForm: (currentVal) => dispatch(actions.switchShowAddTaskForm(currentVal)),
    setCreateTaskName: (name) => dispatch(actions.setCreateTaskName(name)),
    setCreateTaskDescription: (description) => dispatch(actions.setCreateTaskDescription(description)),
    setTasks: (tasks) => dispatch(actions.setTasks(tasks)),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TasksComponent);
