import React, { Component } from 'react';
import { Modal } from 'antd';
import PropTypes from 'prop-types';
import TimelineChart from '../../charts/TimelineChart/TimelineChart';

import './TimelineModal.css';

class TimelineModal extends Component {
  render() {
    const {
      isModalVisible,
      handleOk,
      handleCancel,
      data,
    } = this.props;

    return (
      <Modal
        className="timeline-modal"
        style={{ top: 50 }}
        title="Trials Timeline"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        width={700}
      >
        <p>{data}</p>
        <TimelineChart />
      </Modal>
    );
  }
}

TimelineModal.propTypes = {
  isModalVisible: PropTypes.bool.isRequired,
  handleOk: PropTypes.func.isRequired,
  handleCancel: PropTypes.func.isRequired,
  data: PropTypes.array.isRequired,
};

export default TimelineModal;
