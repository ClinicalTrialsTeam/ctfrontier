import React, { Component } from 'react';
import { Modal } from 'antd';
import PropTypes from 'prop-types';

class DashboardModal extends Component {
  render() {
    const {
      isModalVisible,
      handleOk,
      handleCancel,
      data,
    } = this.props;
    return (
      <Modal
        title="Dashboard"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <p>{data}</p>
        <p>Bla bla</p>
      </Modal>
    );
  }
}

DashboardModal.propTypes = {
  isModalVisible: PropTypes.bool.isRequired,
  handleOk: PropTypes.func.isRequired,
  handleCancel: PropTypes.func.isRequired,
  data: PropTypes.array.isRequired,
};

export default DashboardModal;
