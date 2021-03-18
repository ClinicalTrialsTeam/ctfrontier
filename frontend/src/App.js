// Import libraries
import React, { Component } from 'react';
import './App.css';

// Import local files
import TopLevelSearchView from './components/views/TopLevelSearchView/TopLevelSearchView';

class App extends Component {
  render() {
    return (
      <div className="App">
        <TopLevelSearchView />
      </div>
    );
  }
}

export default App;
