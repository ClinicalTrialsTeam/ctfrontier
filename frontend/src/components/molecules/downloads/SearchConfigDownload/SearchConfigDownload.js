import React from 'react';
import { Typography, Button } from 'antd';
import PropTypes from 'prop-types';
import image from './3.png';

const SearchConfigDownload = ({ data }) => {
  const { Text } = Typography;

  return (
    <>
      <Text strong>Save Search Configuration (TXT)</Text>
      <p>{data}</p>
      <img src={image} alt="icon" height="200" />
      <Button type="primary">Save</Button>
    </>
  );
};

SearchConfigDownload.propTypes = {
  data: PropTypes.array.isRequired,
};

export default SearchConfigDownload;
