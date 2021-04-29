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
        <p>
          Some trials do not have a start or a completion date.
          In this case, a start date is equated to the earliest start date in the selection;
          the completion date is equated to the latest completion date in the selection.
        </p>
        <TimelineChart data={data} />
      </Modal>
    );
  }
}

TimelineModal.propTypes = {
  isModalVisible: PropTypes.bool.isRequired,
  handleOk: PropTypes.func.isRequired,
  handleCancel: PropTypes.func.isRequired,
  data: PropTypes.object.isRequired,
};

export default TimelineModal;
