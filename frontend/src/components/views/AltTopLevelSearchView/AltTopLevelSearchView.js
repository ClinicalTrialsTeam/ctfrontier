import React, { Component } from 'react';
import { Layout } from 'antd';
import AltTopLevelSearchForm from '../../components/organisms/NewForm/NewForm';
import CommonLogo from '../../components/atoms/logos/CommonLogo/CommonLogo';

import './AltTopLevelSearchView.css';
import 'antd/dist/antd.css';

const { Footer, Content } = Layout;

class AltTopLevelSearchView extends Component {
  render() {
    return (
      <Layout className="layout" style={{ backgroundColor: 'white' }}>
        <CommonLogo />
        <Content id="content-bg">
          <AltTopLevelSearchForm />
        </Content>
        <Footer style={{ textAlign: 'center', backgroundColor: 'white' }}>Clinical Trials Frontier ©2021</Footer>
      </Layout>
    );
  }
}

export default AltTopLevelSearchView;
