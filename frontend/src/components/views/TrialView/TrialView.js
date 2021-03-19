import React, { Component } from 'react';
import { Layout, Tabs } from 'antd';
import ListViewTable from '../../organisms/ListViewTable/ListViewTable';
import CommonLogo from '../../atoms/logos/CommonLogo/CommonLogo';

import 'antd/dist/antd.css';

const { Footer, Content } = Layout;
const { TabPane } = Tabs;

class TrialView extends Component {
  render() {
    return (
      <Layout className="layout" style={{ backgroundColor: 'white' }}>
        <CommonLogo />
        <Content id="content-bg">
          <Tabs defaultActiveKey="1">
            <TabPane tab="List View" key="1">
              <ListViewTable />
            </TabPane>
            <TabPane tab="Map View" key="2">
              Content of Tab Pane 2
            </TabPane>
          </Tabs>
        </Content>
        <Footer style={{ textAlign: 'center', backgroundColor: 'white' }}>Clinical Trials Frontier ©2021</Footer>
      </Layout>
    );
  }
}

export default TrialView;
