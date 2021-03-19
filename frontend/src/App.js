// Import libraries
import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import './App.css';

// Import local files
import AltTopLevelSearchView from './components/views/AltTopLevelSearchView/AltTopLevelSearchView';
import TrialView from './components/views/TrialView/TrialView';

class App extends Component {
  render() {
    return (
      <main>
        <Switch>
          <Route path="/" component={AltTopLevelSearchView} exact />
          <Route path="/trials" component={TrialView} exact />
        </Switch>
      </main>
    );
  }
}

export default App;
