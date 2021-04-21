import React from 'react';
import { Button } from 'antd';
import './TopLevelSearchLogo.css';
import logo from './logo.png';

function TopLevelSearchLogo() {
  return (
    <Button type="link" href="/">
      <div className="ctf-logo-wrapper">
        <img src={logo} className="ctf-logo" alt="logo" />
        <span className="ctf-logo" />
      </div>
    </Button>
  );
}

export default TopLevelSearchLogo;
