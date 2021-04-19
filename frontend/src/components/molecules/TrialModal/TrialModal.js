import React, { Component } from 'react';
import { Modal } from 'antd';
import PropTypes from 'prop-types';
import SampleChart from '../charts/SampleChart/SampleChart';
// import TimelineChart from '../charts/TimelineChart/TimelineChart';

class TrialVizModal extends Component {
  render() {
    const {
      type,
      isModalVisible,
      handleOk,
      handleCancel,
      data,
    } = this.props;

    return (
      <Modal
        title={type}
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <p>{data}</p>
        {/* <TimelineChart
          data={data}
        /> */}
        <SampleChart />
      </Modal>
    );
  }
}

TrialVizModal.propTypes = {
  isModalVisible: PropTypes.bool.isRequired,
  handleOk: PropTypes.func.isRequired,
  handleCancel: PropTypes.func.isRequired,
  data: PropTypes.array.isRequired,
  type: PropTypes.string.isRequired,
};

export default TrialVizModal;
