import React from 'react';
import './Tasks.css';

// Redux Related Imports
import { connect } from 'react-redux';
import * as actions from '../../actions/listAction';

// Configuration
import config from '../../config/dev';

class TasksComponent extends React.Component {
  constructor(props) {
    super(props)
    this.loadTasks = this.loadTasks.bind(this);
  }

  async loadTasks() {
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

  async createList() { }

  render() {
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
                  <td>Set as Done</td>
                  <td>Delete</td>
                </tr>
              )
            })}
          </tbody>
        </table>
        <button>Add List</button>
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
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TasksComponent);
