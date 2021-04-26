import React from 'react';
import { Button } from 'antd';
import image from './icon-json-endpoints.png';

const StatReportDownload = () => {
  return (
    <>
      <img className="download-icon" src={image} alt="icon" />
      <Button className="download-button" type="primary">Save Endpoint Report</Button>
    </>
  );
};

export default StatReportDownload;
