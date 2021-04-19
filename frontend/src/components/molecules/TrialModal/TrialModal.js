import React, { Component } from 'react';
import { Modal } from 'antd';
import PropTypes from 'prop-types';

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
        {/* <p>Bla bla</p> */}
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
