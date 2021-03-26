// Import libraries
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import PropTypes from 'prop-types';
import './App.css';

// Import local files
import TrialsLayout from './components/organisms/Layout/Layout';
import SearchView from './components/views/SearchView/SearchView';
import TrialView from './components/views/TrialView/TrialView';

function App() {
  return (
    <BrowserRouter>
      <main>
        <Switch>
          <RouteWrapper path="/" component={SearchView} layout={TrialsLayout} exact />
          <RouteWrapper path="/trials" component={TrialView} layout={TrialsLayout} exact />
        </Switch>
      </main>
    </BrowserRouter>
  );
}

function RouteWrapper({
  component: Component,
  layout: Layout,
}) {
  return (
    <Route
      render={() => {
        return (
          <Layout>
            <Component />
          </Layout>
        );
      }}
    />
  );
}

RouteWrapper.propTypes = {
  component: PropTypes.func.isRequired,
  layout: PropTypes.func.isRequired,
};

export default App;
