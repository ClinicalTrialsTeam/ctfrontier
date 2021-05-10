import React, { Component } from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import FileDownload from 'js-file-download';
import image from './icon-csv.png';

class TrialsCSVDownload extends Component {
  static downloadSearchConfig(data) {
    const replacer = (key, value) => { return (value === null ? '' : value); }; // specifying handling null values here
    const header = Object.keys(data[0]); // defining header row
    const csv = [
      header.join(','), // header row first
      ...data.map((row) => { return header.map((fieldName) => { return JSON.stringify(row[fieldName], replacer); }).join(','); }),
    ].join('\r\n');

    FileDownload(csv, 'trials.csv');
  }

  render() {
    const {
      isDownloading,
      data,
    } = this.props;

    return (
      <>
        <img className="download-icon" src={image} alt="icon" />
        <Button
          disabled={isDownloading}
          loading={isDownloading}
          className="download-button"
          onClick={() => { return TrialsCSVDownload.downloadSearchConfig(data); }}
          type="primary"
        >
          Save Search Results
        </Button>
      </>
    );
  }
}

TrialsCSVDownload.propTypes = {
  isDownloading: PropTypes.bool.isRequired,
  data: PropTypes.object.isRequired,
};

export default TrialsCSVDownload;
