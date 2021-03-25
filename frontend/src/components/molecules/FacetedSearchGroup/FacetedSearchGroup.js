import React, { Component } from 'react';
import {
  Checkbox, Collapse, Form, Typography, Space,
} from 'antd';
import PropTypes from 'prop-types';

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
          <Collapse>
            <Panel key="1" header="Status">
              <Title level={5}>Recruitment Status</Title>
              <Space direction="vertical">
                {recruitmentCheckboxes}
                <Title level={5}>Expanded Access</Title>
              </Space>
              {accessCheckboxes}
            </Panel>
            <Panel key="2" header="Phase">
              {phasesCheckboxes}
            </Panel>
            <Panel key="3" header="Administration">
              <p>{text}</p>
            </Panel>
            <Panel key="4" header="Target">
              <p>Data</p>
            </Panel>
            <Panel key="5" header="Modality">
              <p>Data</p>
            </Panel>
            <Panel key="6" header="No. of patients">
              <p>Data</p>
            </Panel>
            <Panel key="7" header="Sponsor">
              <p>Data</p>
            </Panel>
            <Panel key="8" header="Sponsor Type">
              <p>Data</p>
            </Panel>
            <Panel key="9" header="Dates" style={{ marginBottom: 24 }}>
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
