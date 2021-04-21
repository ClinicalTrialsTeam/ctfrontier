import React from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import image from './4.png';

const TrialsJSONDownload = ({ data }) => {
  return (
    <>
      <p>{data}</p>
      <img className="download-icon" src={image} alt="icon" />
      <Button className="download-button" type="primary">Save Search Results (JSON)</Button>
    </>
  );
};

TrialsJSONDownload.propTypes = {
  data: PropTypes.array.isRequired,
};

export default TrialsJSONDownload;
