import React, { Component } from 'react';
import {
  Modal, Row, Col, Divider,
} from 'antd';
import PropTypes from 'prop-types';
import SearchConfigDownload from '../../downloads/SearchConfigDownload/SearchConfigDownload';
import TrialsCSVDownload from '../../downloads/TrialsCSVDownload/TrialsCSVDownload';
import TrialsJSONDownload from '../../downloads/TrialsJSONDownload/TrialsJSONDownload';
import EndpointsReportDownload from '../../downloads/EndpointsReportDownload/EndpointsReportDownload';

import './DownloadModal.css';

class DownloadModal extends Component {
  render() {
    const {
      isDownloading,
      isModalVisible,
      handleOk,
      handleCancel,
      data,
      payload,
    } = this.props;

    return (
      <Modal
        className="download-modal"
        style={{ top: 50 }}
        title="Downloads"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        width={700}
      >
        <Divider plain orientation="left">Search Results Download Options</Divider>
        <Row key="row-downloads-standard" justify="space-around">
          <Col key="col-downloads-1" span={12}>
            <TrialsCSVDownload data={data} isDownloading={isDownloading} />
          </Col>
          <Col key="col-downloads-2" span={12}>
            <TrialsJSONDownload data={data} isDownloading={isDownloading} />
          </Col>
        </Row>
        <br />
        <Divider plain orientation="left">Expanded Download Options</Divider>
        <Row key="row-downloads-expanded" justify="space-around">
          <Col key="col-downloads-3" span={12}>
            <SearchConfigDownload payload={payload} />
          </Col>
          <Col key="col-downloads-4" span={12}>
            <EndpointsReportDownload />
          </Col>
        </Row>
      </Modal>
    );
  }
}

DownloadModal.propTypes = {
  isDownloading: PropTypes.bool.isRequired,
  isModalVisible: PropTypes.bool.isRequired,
  handleOk: PropTypes.func.isRequired,
  handleCancel: PropTypes.func.isRequired,
  data: PropTypes.object.isRequired,
  payload: PropTypes.object.isRequired,
};

export default DownloadModal;
