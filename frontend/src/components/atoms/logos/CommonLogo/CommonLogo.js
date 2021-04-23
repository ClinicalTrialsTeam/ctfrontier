import React from 'react';
import { Button } from 'antd';
import './CommonLogo.css';
import logo from './logo.png';

function CommonLogo() {
  return (
    <Button type="link" href="/">
      <img src={logo} className="ctf-common-logo" alt="logo" />
    </Button>
  );
}

export default CommonLogo;
