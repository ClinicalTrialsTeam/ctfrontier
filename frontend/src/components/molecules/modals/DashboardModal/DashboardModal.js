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
      count,
    } = this.props;

    let totalTop = 0;

    if (data.sponsors) {
      data.sponsors.forEach((element) => {
        totalTop += element.trials_count;
      });
    }

    const percent = Math.round((totalTop / parseInt(count)) * 100);

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
        <Tabs defaultActiveKey="1">
          <TabPane tab="Sponsors" key="tab-sponsors">
            <p>
              The top 10 study sponsors initiated
              {' '}
              {percent}
              % of selected trials.
            </p>
            <DashboardSponsorsChart data={data.sponsors} />
          </TabPane>
          <TabPane tab="Phases" key="tab-phases">
            <DashboardPhasesChart data={data.phases} />
          </TabPane>
          <TabPane tab="Interventions" key="tab-interventions">
            <p>
              Since some trials use multiple interventions methods,
              the sum of trials per intervention type may exceed
              the total of trials.
            </p>
            <DashboardInterventionsChart data={data.interventions} />
          </TabPane>
          <TabPane tab="Status" key="tab-recr-status">
            <DashboardStatusChart data={data.status} />
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
  data: PropTypes.object.isRequired,
  count: PropTypes.string.isRequired,
};

export default DashboardModal;
