import React, { Component } from 'react';
import {
  Collapse, Typography, Row, Col,
} from 'antd';

class SingleTrialDisplay extends Component {
  render() {
    const { Panel } = Collapse;
    const { Title } = Typography;

    return (
      <>
        <Title level={4}>
          Does Timeliness of DTaP-IPV-Hib Vaccination
          Affect Development of Atopic Dermatitis Before 1 Year of Age?
        </Title>
        <Row key="row-summary" gutter={[8, 8]}>
          <Col key="col-sum-1" span={12}>
            <p />
          </Col>
          <Col key="col-sum-2" span={2}>
            <p id="or-p">OR</p>
          </Col>
        </Row>
        <Collapse defaultActiveKey={['1']}>
          <Panel
            key="panel-tracking"
            header="Tracking information"
          >
            <p />
          </Panel>
          <Panel
            key="2"
            header="Descriptive information"
          >
            <p />
          </Panel>
          <Panel
            key="3"
            header="Recruitment information"
          >
            <p />
          </Panel>
          <Panel
            key="4"
            header="Administrative information"
          >
            <p />
          </Panel>
        </Collapse>
      </>
    );
  }
}

export default SingleTrialDisplay;
