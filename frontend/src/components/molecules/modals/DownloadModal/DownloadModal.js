import React, { Component } from 'react';
import {
  Modal, Row, Col, Divider,
} from 'antd';
import PropTypes from 'prop-types';
import SearchConfigDownload from '../../downloads/SearchConfigDownload/SearchConfigDownload';
import TrialsCSVDownload from '../../downloads/TrialsCSVDownload/TrialsCSVDownload';
import TrialsJSONDownload from '../../downloads/TrialsJSONDownload/TrialsJSONDownload';
import StatReportDownload from '../../downloads/StatReportDownload/StatReportDownload';

import './DownloadModal.css';

class DownloadModal extends Component {
  render() {
    const {
      isModalVisible,
      handleOk,
      handleCancel,
      data,
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
        <p>{data}</p>
        <Divider plain orientation="left">Search Results Download Options</Divider>
        <Row key="row-downloads-standard" justify="space-around">
          <Col key="col-downloads-1" span={12}>
            <TrialsCSVDownload />
          </Col>
          <Col key="col-downloads-2" span={12}>
            <TrialsJSONDownload />
          </Col>
        </Row>
        <br />
        <Divider plain orientation="left">Expanded Download Options</Divider>
        <Row key="row-downloads-expanded" justify="space-around">
          <Col key="col-downloads-3" span={12}>
            <SearchConfigDownload />
          </Col>
          <Col key="col-downloads-4" span={12}>
            <StatReportDownload />
          </Col>
        </Row>
      </Modal>
    );
  }
}

DownloadModal.propTypes = {
  isModalVisible: PropTypes.bool.isRequired,
  handleOk: PropTypes.func.isRequired,
  handleCancel: PropTypes.func.isRequired,
  data: PropTypes.array.isRequired,
};

export default DownloadModal;
