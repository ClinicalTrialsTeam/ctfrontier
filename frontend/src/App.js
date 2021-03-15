import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import project from './apis/project';

const App = () => {
  const [exampleInfo, setExampleInfo] = useState([]);

  const fetchExample = async () => {
    try {
      const response = await project.get('brief_summaries');
      setExampleInfo(response.data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    fetchExample();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit
          {' '}
          <code>src/App.js</code>
          {' '}
          and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <div>
        <h1>Example API Response</h1>
        <h2>{exampleInfo.length}</h2>
        {console.log(exampleInfo)}
      </div>
    </div>
  );
};

export default App;
