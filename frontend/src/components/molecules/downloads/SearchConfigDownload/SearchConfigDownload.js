import React from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import image from './icon-json-search.png';

const SearchConfigDownload = ({ data }) => {
  return (
    <>
      <p>{data}</p>
      <img className="download-icon" src={image} alt="icon" />
      <Button className="download-button" type="primary">Save Search Configuration</Button>
    </>
  );
};

SearchConfigDownload.propTypes = {
  data: PropTypes.array.isRequired,
};

export default SearchConfigDownload;
