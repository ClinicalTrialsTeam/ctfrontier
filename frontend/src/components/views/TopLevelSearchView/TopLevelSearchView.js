import React, { Component } from 'react';
import { Layout } from 'antd';
import ParallaxStarsBackground from '../../atoms/backgrounds/ParallaxStars/ParallaxStars';
import TopLevelSearchForm from '../../organisms/TopLevelSearchForm/TopLevelSearchForm';
import TopLevelSearchLogo from '../../atoms/logos/TopLevelSearchLogo/TopLevelSearchLogo';

import './TopLevelSearchView.css';
import 'antd/dist/antd.css';

const { Footer } = Layout;

class TopLevelSearchView extends Component {
  render() {
    return (
      <Layout className="layout">
        <ParallaxStarsBackground />
        <div id="wrapper">
          <TopLevelSearchLogo />
          <TopLevelSearchForm />
        </div>
        <Footer style={{ textAlign: 'center' }}>Clinical Trials Frontier ©2021</Footer>
      </Layout>
    );
  }
}

export default TopLevelSearchView;
