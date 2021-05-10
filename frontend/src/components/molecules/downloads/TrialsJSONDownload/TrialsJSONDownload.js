import React, { Component } from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import FileDownload from 'js-file-download';
import image from './icon-json-trials.png';

class TrialsJSONDownload extends Component {
  static downloadSearchConfig(data) {
    FileDownload(JSON.stringify(data), 'trials.json');
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
          onClick={() => { return TrialsJSONDownload.downloadSearchConfig(data); }}
          type="primary"
        >
          Save Search Results
        </Button>
      </>
    );
  }
}

TrialsJSONDownload.propTypes = {
  isDownloading: PropTypes.bool.isRequired,
  data: PropTypes.object.isRequired,
};

export default TrialsJSONDownload;
