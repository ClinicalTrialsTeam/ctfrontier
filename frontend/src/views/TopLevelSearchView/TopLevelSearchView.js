import React, { Component } from 'react';
import { Layout, Card } from 'antd';
import ParallaxStarsBackground from '../../components/atoms/backgrounds/ParallaxStars/ParallaxStars';
// import FrostedCard from '../../components/molecules/cards/Frosted/Frosted';
import TopLevelSearchForm from '../../components/organisms/TopLevelSearchForm/TopLevelSearchForm';
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
          {/* <FrostedCard> */}
          <Card id="frostedcard">
            <TopLevelSearchForm />
          </Card>
          {/* </FrostedCard> */}
        </div>
        <Footer style={{ textAlign: 'center' }}>Clinical Trials Frontier ©2021</Footer>
      </Layout>
    );
  }
}

export default TopLevelSearchView;
