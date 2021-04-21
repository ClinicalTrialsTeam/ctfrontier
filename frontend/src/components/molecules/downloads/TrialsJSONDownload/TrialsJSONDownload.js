import React from 'react';
import { Typography, Button } from 'antd';
import PropTypes from 'prop-types';
import image from './4.png';

const TrialsJSONDownload = ({ data }) => {
  const { Text } = Typography;

  return (
    <>
      <Text strong>Save Search Results (JSON)</Text>
      <p>{data}</p>
      <img src={image} alt="icon" height="200" />
      <Button type="primary">Save</Button>
    </>
  );
};

TrialsJSONDownload.propTypes = {
  data: PropTypes.array.isRequired,
};

export default TrialsJSONDownload;
