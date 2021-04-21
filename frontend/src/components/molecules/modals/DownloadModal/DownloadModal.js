import React, { Component } from 'react';
import { Modal, Row, Col } from 'antd';
import PropTypes from 'prop-types';
import SearchConfigDownload from '../../downloads/SearchConfigDownload/SearchConfigDownload';
import TrialsCSVDownload from '../../downloads/TrialsCSVDownload/TrialsCSVDownload';
import TrialsJSONDownload from '../../downloads/TrialsJSONDownload/TrialsJSONDownload';
import StatReportDownload from '../../downloads/StatReportDownload/StatReportDownload';

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
        style={{ top: 50 }}
        title="Downloads"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        width={700}
      >
        <p>{data}</p>
        <Row key="row-downloads" gutter={[16, 8]}>
          <Col key="col-downloads-1" span={12}>
            <TrialsCSVDownload />
            <SearchConfigDownload />
          </Col>
          <Col key="col-downloads-2" span={12}>
            <TrialsJSONDownload />
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
