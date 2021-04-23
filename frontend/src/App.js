// Import libraries
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import PropTypes from 'prop-types';
import './App.css';

// Import local files
import TrialsLayout from './components/organisms/Layout/Layout';
import SearchView from './components/views/SearchView/SearchView';
import TrialListView from './components/views/TrialListView/TrialListView';
import SingleTrialView from './components/views/SingleTrialView/SingleTrialView';
import PageNotFoundView from './components/views/PageNotFoundView/PageNotFoundView';

function App() {
  return (
    <BrowserRouter>
      <main>
        <Switch>
          <RouteWrapper path="/" component={SearchView} layout={TrialsLayout} exact />
          <RouteWrapper path="/trials" component={TrialListView} layout={TrialsLayout} exact />
          <RouteWrapper path="/trials/:nctId" component={SingleTrialView} layout={TrialsLayout} />
          <RouteWrapper path="/" component={PageNotFoundView} layout={TrialsLayout} />
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
