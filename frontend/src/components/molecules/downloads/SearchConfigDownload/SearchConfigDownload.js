import React, { Component } from 'react';
import { Button } from 'antd';
import PropTypes from 'prop-types';
import FileDownload from 'js-file-download';
import image from './icon-json-search.png';

class SearchConfigDownload extends Component {
  static downloadSearchConfig(payload) {
    FileDownload(JSON.stringify(payload), 'search-config.json');
    console.log(payload);
  }

  // constructor(props) {
  //   super(props);
  //   this.downloadSearchConfig = this.downloadSearchConfig.bind(this);
  // }

  render() {
    const {
      payload,
    } = this.props;

    return (
      <>
        <img className="download-icon" src={image} alt="icon" />
        <Button
          className="download-button"
          onClick={() => { return SearchConfigDownload.downloadSearchConfig(payload); }}
          type="primary"
        >
          Save Search Configuration
        </Button>
      </>
    );
  }
}

SearchConfigDownload.propTypes = {
  payload: PropTypes.object.isRequired,
};

export default SearchConfigDownload;
