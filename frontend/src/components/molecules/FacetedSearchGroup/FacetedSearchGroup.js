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

    Array.from(recruitment.entries()).forEach(([, value]) => {
      recruitmentCheckboxes.push(
        <Checkbox value={value} style={{ lineHeight: '24px' }}>
          {value}
        </Checkbox>
      );
    });

    const accessCheckboxes = [];

    Array.from(access.entries()).forEach(([, value]) => {
      accessCheckboxes.push(
        <Checkbox value={value} style={{ lineHeight: '24px' }}>
          {value}
        </Checkbox>
      );
    });

    const phasesCheckboxes = [];

    Array.from(phases.entries()).forEach(([, value]) => {
      phasesCheckboxes.push(
        <Checkbox value={value} style={{ lineHeight: '24px' }}>
          {value}
        </Checkbox>
      );
    });

    return (
      <>
        <Form>
          <Collapse>
            <Panel header="Status" key="1">
              <Title level={5}>Recruitment Status</Title>
              <Space direction="vertical">
                {recruitmentCheckboxes}
                <Title level={5}>Expanded Access</Title>
              </Space>
              {accessCheckboxes}
            </Panel>
            <Panel header="Phase" key="2">
              {phasesCheckboxes}
            </Panel>
            <Panel header="Administration" key="3">
              <p>{text}</p>
            </Panel>
            <Panel header="Target" key="4">
              <p>Data</p>
            </Panel>
            <Panel header="Modality" key="5">
              <p>Data</p>
            </Panel>
            <Panel header="No. of patients" key="6">
              <p>Data</p>
            </Panel>
            <Panel header="Sponsor" key="7">
              <p>Data</p>
            </Panel>
            <Panel header="Sponsor Type" key="8">
              <p>Data</p>
            </Panel>
            <Panel header="Dates" key="8" style={{ marginBottom: 24 }}>
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
