import React from 'react';
import './Lists.css';

// Redux Related Imports
import { connect } from 'react-redux';
import * as actions from '../../actions/listAction';
import * as tasksActions from '../../actions/taskAction';

// Configuration
import config from '../../config/dev';

class ListsComponent extends React.Component {
  constructor(props) {
    super(props)
    this.loadLists = this.loadLists.bind(this);
    this.createList = this.createList.bind(this);
    this.loadTasks = this.loadTasks.bind(this);
    this.deleteList = this.deleteList.bind(this);
    this.loadLists()
  }

  async loadLists() {
    const resp = await fetch(`${config.baseUrl}/list/list`, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        access_id: this.props.login.accessId,
      })
    });
    const body = await resp.json();
    if (body !== undefined) {
      console.log(body)
      this.props.setLists(body);
    }
  }

  async createList() {
    const resp = await fetch(`${config.baseUrl}/list/create`, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        access_id: this.props.login.accessId,
        name: this.props.lists.name,
        description: this.props.lists.description,
        is_done: false
      })
    });
    const body = await resp.json();
    if (body !== undefined) {
      console.log(body)
    }
    await this.loadLists()
    this.props.switchShowAddList(this.props.lists.showAddList)
   }

   async deleteList(id){
    const resp = await fetch(`${config.baseUrl}/list/delete`, {
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
    await this.loadLists()
    this.loadLists();
   }

   async loadTasks(listName, id) {
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
    this.props.setTaskListName(listName)
    this.props.setTaskListId(id)
   }

  render() {
    if (this.props.lists.showAddList){
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
            {this.props.lists.list.map((data, key) => {
              return (
                <tr key={key}>
                  <td>{data.id}</td>
                  <td>{data.name}</td>
                  <td>{data.description}</td>
                  <td>{data.is_done.toString()}</td>
                  <td> <button type="submit" onClick={() => this.loadTasks(data.name, data.id)}>View Tasks</button></td>
                  <td> <button type="submit" onClick={() => this.deleteList(data.id)}>Delete List</button></td>
                </tr>
              )
            })}
          </tbody>
        </table>
        <button onClick={() => this.props.switchShowAddList(this.props.lists.showAddList)}>Add List</button>
        <div className="login-wrapper">
                <h1>Please Log In</h1>
                <div>
                    <label>
                        <p>List Name</p>
                        <input type="text" onChange={(name) => this.props.setCreateListName(name.target.value)} />
                    </label>
                    <label>
                        <p>List Description</p>
                        <input type="text" onChange={(description) => this.props.setCreateListDescription(description.target.value)} />
                    </label>
                    <div>
                        <button type="submit" onClick={() => this.createList()}>Create List</button>
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
            {this.props.lists.list.map((data, key) => {
              return (
                <tr key={key}>
                  <td>{data.id}</td>
                  <td>{data.name}</td>
                  <td>{data.description}</td>
                  <td>{data.is_done.toString()}</td>
                  <td> <button type="submit" onClick={() => this.loadTasks(data.name, data.id)}>View Tasks</button></td>
                  <td> <button type="submit" onClick={() => this.deleteList(data.id)}>Delete List</button></td>
                </tr>
              )
            })}
          </tbody>
        </table>
        <button onClick={() => this.props.switchShowAddList(this.props.lists.showAddList)}>Add List</button>
      </div>
    )
  }
}
const mapStateToProps = (state) => {
  return { ...state };
};

const mapDispatchToProps = (dispatch) => {
  return {
    setLists: (lists) => dispatch(actions.setLists(lists)),
    switchShowAddList: (currentVal) => dispatch(actions.switchShowAddListForm(currentVal)),
    setCreateListName: (name) => dispatch(actions.setCreateListName(name)),
    setCreateListDescription: (description) => dispatch(actions.setCreateListDescription(description)),
    setTasks: (tasks) => dispatch(tasksActions.setTasks(tasks)),
    setTaskListName: (listName) => dispatch(tasksActions.setTaskListName(listName)),
    setTaskListId: (listId) => dispatch(tasksActions.setTaskListId(listId))

  };
};

export default connect(mapStateToProps, mapDispatchToProps)(ListsComponent);
