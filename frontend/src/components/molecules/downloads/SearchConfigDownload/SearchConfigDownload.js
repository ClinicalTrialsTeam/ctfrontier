import React from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import image from './3.png';

const SearchConfigDownload = ({ data }) => {
  return (
    <>
      <p>{data}</p>
      <img className="download-icon" src={image} alt="icon" />
      <Button className="download-button" type="primary">Save Search Configuration (TXT)</Button>
    </>
  );
};

SearchConfigDownload.propTypes = {
  data: PropTypes.array.isRequired,
};

export default SearchConfigDownload;
