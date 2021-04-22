import React from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import image from './icon-json-endpoints.png';

const StatReportDownload = ({ data }) => {
  return (
    <>
      <p>{data}</p>
      <img className="download-icon" src={image} alt="icon" />
      <Button className="download-button" type="primary">Save Endpoint Report</Button>
    </>
  );
};

StatReportDownload.propTypes = {
  data: PropTypes.array.isRequired,
};

export default StatReportDownload;
