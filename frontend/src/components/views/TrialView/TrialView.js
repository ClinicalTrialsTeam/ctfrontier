import React, { Component } from 'react';
import { Tabs } from 'antd';
import ListViewTable from '../../organisms/ListViewTable/ListViewTable';

import 'antd/dist/antd.css';

const { TabPane } = Tabs;

class TrialView extends Component {
  render() {
    return (
      <Tabs defaultActiveKey="1">
        <TabPane tab="List View" key="1">
          <ListViewTable />
        </TabPane>
        <TabPane tab="Map View" key="2">
          <ListViewTable />
        </TabPane>
      </Tabs>
    );
  }
}

export default TrialView;
