import React, { Component } from 'react';
import { Card, Result, Button } from 'antd';

class PageNotFoundView extends Component {
  render() {
    return (
      <Card id="404-card">
        <Result
          status="404"
          title="404"
          subTitle="Sorry, the page you visited does not exist."
          extra={<Button href="/" type="primary">Back Home</Button>}
        />
      </Card>
    );
  }
}

export default PageNotFoundView;
