import React, { Component } from 'react';
import { Modal, Tabs } from 'antd';
import PropTypes from 'prop-types';
import DashboardSponsorsChart from '../../charts/DashboardSponsorsChart/DashboardSponsorChart';
import DashboardInterventionsChart from '../../charts/DashboardInterventionsChart/DashboardInterventionsChart';
import DashboardPhasesChart from '../../charts/DashboardPhasesChart/DashboardPhasesChart';
import DashboardStatusChart from '../../charts/DasboardStatusChart/DashboardStatusChart';

import './DashboardModal.css';

class DashboardModal extends Component {
  render() {
    const { TabPane } = Tabs;
    const {
      isModalVisible,
      handleOk,
      handleCancel,
      data,
    } = this.props;

    return (
      <Modal
        className="dashboard-modal"
        style={{ top: 50 }}
        title="Trials Dashboard"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        width={700}
      >
        {/* <p>{data}</p> */}
        <Tabs defaultActiveKey="1">
          <TabPane tab="Sponsors" key="tab-sponsors">
            <p>
              Top 10 study sponsors initiated 15% of selected trials.
              {data}
            </p>
            <DashboardSponsorsChart />
          </TabPane>
          <TabPane tab="Phases" key="tab-phases">
            <DashboardPhasesChart />
          </TabPane>
          <TabPane tab="Interventions" key="tab-interventions">
            <p>
              Since some trials use multiple interventions methods,
              the sum of trials perintervention type will exceed
              the total of trials.
              {data}
            </p>
            <DashboardInterventionsChart />
          </TabPane>
          <TabPane tab="Status" key="tab-recr-status">
            <DashboardStatusChart />
          </TabPane>
          <TabPane tab="Targets" key="tab-targets">
            Content unavailable
          </TabPane>
        </Tabs>
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
