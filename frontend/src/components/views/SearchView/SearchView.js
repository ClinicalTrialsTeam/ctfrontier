import React, { Component } from 'react';
import { Layout } from 'antd';
import SearchForm from '../../organisms/SearchForm/SearchForm';
import CommonLogo from '../../atoms/logos/CommonLogo/CommonLogo';

import './SearchView.css';
import 'antd/dist/antd.css';

const { Footer, Content } = Layout;

class SearchView extends Component {
  render() {
    return (
      <Layout className="layout" style={{ backgroundColor: 'white' }}>
        <CommonLogo />
        <Content id="content-bg">
          <SearchForm />
        </Content>
        <Footer style={{ textAlign: 'center', backgroundColor: 'white' }}>Clinical Trials Frontier ©2021</Footer>
      </Layout>
    );
  }
}

export default SearchView;
