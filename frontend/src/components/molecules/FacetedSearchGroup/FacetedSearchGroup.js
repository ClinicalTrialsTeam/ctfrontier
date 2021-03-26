import React, { Component } from 'react';
import {
  Checkbox, Collapse, Form, Typography, Space,
} from 'antd';
import PropTypes from 'prop-types';

import './FacetedSearchGroup.css';

class FacetedSearchGroup extends Component {
  render() {
    const { access, recruitment, phases } = this.props;
    const { Panel } = Collapse;
    const { Title } = Typography;

    const text = 'Data';

    const recruitmentCheckboxes = [];

    Array.from(recruitment.entries()).forEach(([index, value]) => {
      recruitmentCheckboxes.push(
        <Checkbox key={index} value={value} style={{ lineHeight: '24px' }}>
          {value}
        </Checkbox>
      );
    });

    const accessCheckboxes = [];

    Array.from(access.entries()).forEach(([index, value]) => {
      accessCheckboxes.push(
        <Checkbox key={index} value={value} style={{ lineHeight: '24px' }}>
          {value}
        </Checkbox>
      );
    });

    const phasesCheckboxes = [];

    Array.from(phases.entries()).forEach(([index, value]) => {
      phasesCheckboxes.push(
        <Checkbox key={index} value={value} style={{ lineHeight: '24px' }}>
          {value}
        </Checkbox>
      );
    });

    return (
      <>
        <Form>
          <Collapse className="fs-group-collapse">
            <Panel
              key="1"
              header="Status"
              className="fs-group-panel"
            >
              <Title level={5}>Recruitment Status</Title>
              <Space direction="vertical">
                {recruitmentCheckboxes}
                <Title level={5}>Expanded Access</Title>
              </Space>
              {accessCheckboxes}
            </Panel>
            <Panel
              key="2"
              header="Phase"
              className="fs-group-panel"
            >
              {phasesCheckboxes}
            </Panel>
            <Panel
              key="3"
              header="Administration"
              className="fs-group-panel"
            >
              <p>{text}</p>
            </Panel>
            <Panel
              key="4"
              header="Target"
              className="fs-group-panel"
            >
              <p>Data</p>
            </Panel>
            <Panel
              key="5"
              header="Modality"
              className="fs-group-panel"
            >
              <p>Data</p>
            </Panel>
            <Panel
              key="6"
              header="No. of patients"
              className="fs-group-panel"
            >
              <p>Data</p>
            </Panel>
            <Panel
              key="7"
              header="Sponsor"
              className="fs-group-panel"
            >
              <p>Data</p>
            </Panel>
            <Panel
              key="8"
              header="Sponsor Type"
              className="fs-group-panel"
            >
              <p>Data</p>
            </Panel>
            <Panel
              key="9"
              header="Dates"
              className="fs-group-panel"
            >
              <p>Data</p>
            </Panel>
          </Collapse>
        </Form>
      </>
    );
  }
}

FacetedSearchGroup.propTypes = {
  access: PropTypes.array.isRequired,
  recruitment: PropTypes.array.isRequired,
  phases: PropTypes.array.isRequired,
};

export default FacetedSearchGroup;
