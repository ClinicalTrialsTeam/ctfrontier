import React from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import image from './1.png';

const TrialsCSVDownload = ({ data }) => {
  return (
    <>
      <p>{data}</p>
      <img className="download-icon" src={image} alt="icon" />
      <Button className="download-button" type="primary">Save Search Results (CSV)</Button>
    </>
  );
};

TrialsCSVDownload.propTypes = {
  data: PropTypes.array.isRequired,
};

export default TrialsCSVDownload;
