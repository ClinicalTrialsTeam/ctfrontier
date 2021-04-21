import React from 'react';
import { Layout } from 'antd';
import PropTypes from 'prop-types';
import CommonLogo from '../../atoms/logos/CommonLogo/CommonLogo';

import './Layout.css';
import 'antd/dist/antd.css';

const { Footer, Content } = Layout;

const TrialsLayout = ({ children }) => {
  return (
    <Layout className="layout" style={{ backgroundColor: 'white' }}>
      <CommonLogo className="logo" />
      <Content id="content-bg">
        {children}
      </Content>
      <Footer style={{ textAlign: 'center', backgroundColor: 'white' }}>Clinical Trials Frontier ©2021</Footer>
    </Layout>
  );
};

TrialsLayout.propTypes = {
  children: PropTypes.object.isRequired,
};

export default TrialsLayout;
