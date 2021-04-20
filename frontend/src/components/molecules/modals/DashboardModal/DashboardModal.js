import React, { Component } from 'react';
import { Modal } from 'antd';
import PropTypes from 'prop-types';
import DashboardChart from '../../charts/DashboardChart/DashboardChart';

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
        title="Trials Dashboard"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        width={700}
      >
        <p>{data}</p>
        <DashboardChart />
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
