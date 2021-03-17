import React, { Component } from 'react';
import { Layout } from 'antd';
import ParallaxStarsBackground from '../../components/atoms/backgrounds/ParallaxStars/ParallaxStars';
import TopLevelSearchContainer from '../../components/organisms/TopLevelSearchContainer/TopLevelSearchContainer';
import TopLevelSearchLogo from '../../components/atoms/logos/TopLevelSearchLogo/TopLevelSearchLogo';

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
          <TopLevelSearchContainer />
        </div>
        <Footer style={{ textAlign: 'center' }}>Clinical Trials Frontier ©2021</Footer>
      </Layout>
    );
  }
}

export default TopLevelSearchView;
