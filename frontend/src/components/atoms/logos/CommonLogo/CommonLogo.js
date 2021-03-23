import React from 'react';
import './CommonLogo.css';
import logo from './logo.png';

function CommonLogo() {
  return (
    <img src={logo} className="ctf-common-logo" alt="logo" />
  );
}

export default CommonLogo;
