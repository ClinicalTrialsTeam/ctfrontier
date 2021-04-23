import React, { Component } from 'react';
import { Collapse, Row, Col } from 'antd';

class SingleTrialDisplay extends Component {
  render() {
    const { Panel } = Collapse;

    return (
      <>
        <Collapse defaultActiveKey={['1']} className="fs-group-collapse">
          <Panel
            key="1"
            header="Status"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="facet-eligibility"
            header="Eligibility criteria"
            className="fs-group-panel"
          >
            <Row key="form_row_age" gutter={[8, 8]}>
              <Col key="col-age-num" span={16}>
                <p />
              </Col>
              <Col key="col-or" span={8}>
                <p id="or-p">OR</p>
              </Col>
            </Row>
            <Row key="form-row-age-group" gutter={[16, 8]}>
              <Col key="col-age-group" span={24}>
                <p />
              </Col>
            </Row>
            <Row key="form-row-ethnicity" gutter={[16, 8]}>
              <Col key="col-ethinicity" span={24}>
                <p />
              </Col>
            </Row>
            <Row key="form-row-sex" gutter={[16, 8]}>
              <Col key="col-ethinicity" span={24}>
                <p />
              </Col>
            </Row>
            <Row key="form-row-is-healty" gutter={[16, 8]}>
              <Col key="col-is-healthy" span={24}>
                <p />
              </Col>
            </Row>
          </Panel>
          <Panel
            key="2"
            header="Phase"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="3"
            header="Administration"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="4"
            header="Target"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="5"
            header="Modality"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="6"
            header="Number of Subjects"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="7"
            header="Sponsor"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="8"
            header="Sponsor Type"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="9"
            id="facet-dates"
            header="Study dates"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="facet-type"
            header="Study Type"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="facet-results"
            header="Study Results"
            className="fs-group-panel"
          >
            <p />
          </Panel>
          <Panel
            key="facet-documents"
            header="Study Documents"
            className="fs-group-panel"
          >
            <p />
          </Panel>
        </Collapse>
      </>
    );
  }
}

export default SingleTrialDisplay;
