import React from 'react';
import { Typography, Button } from 'antd';
import PropTypes from 'prop-types';
import image from './1.png';

const TrialsCSVDownload = ({ data }) => {
  const { Text } = Typography;

  return (
    <>
      <Text strong>Save Search Results (CSV)</Text>
      <p>{data}</p>
      <img src={image} alt="icon" height="200" />
      <Button type="primary">Save</Button>
    </>
  );
};

TrialsCSVDownload.propTypes = {
  data: PropTypes.array.isRequired,
};

export default TrialsCSVDownload;
