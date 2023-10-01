import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    todos: []
  };
  componentDidMount() {
    this.getTodo();
  }
  getTodo() {
    axios
        .get('http://127.0.0.1:8001/api/')
        .then(res => {
          this.setState({todos: res.data});
        })
        .catch(err => {
          console.log(err);
        });
  }
  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.body}</span>
            </div>
        ))}
      </div>
    );
  }
}
export default App;
