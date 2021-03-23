// Import libraries
import React, { Component } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import './App.css';

// Import local files
import SearchView from './components/views/SearchView/SearchView';
import TrialView from './components/views/TrialView/TrialView';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <main>
          <Switch>
            <Route path="/" component={SearchView} exact />
            <Route path="/trials" component={TrialView} exact />
          </Switch>
        </main>
      </BrowserRouter>
    );
  }
}

export default App;
