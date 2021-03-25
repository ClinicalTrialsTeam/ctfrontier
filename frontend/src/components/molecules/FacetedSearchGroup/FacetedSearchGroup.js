import React, { Component } from 'react';
import {
  Checkbox, Collapse, Form, Typography, Space,
} from 'antd';
import PropTypes from 'prop-types';
import { v4 as uuidv4 } from 'uuid';

class FacetedSearchGroup extends Component {
  render() {
    const { access, recruitment, phases } = this.props;
    const { Panel } = Collapse;
    const { Title } = Typography;

    const text = 'Data';

    const recruitmentCheckboxes = [];

    Array.from(recruitment.entries()).forEach(([, value]) => {
      recruitmentCheckboxes.push(
        <Checkbox key={uuidv4()} value={value} style={{ lineHeight: '24px' }}>
          {value}
        </Checkbox>
      );
    });

    const accessCheckboxes = [];

    Array.from(access.entries()).forEach(([, value]) => {
      accessCheckboxes.push(
        <Checkbox key={uuidv4()} value={value} style={{ lineHeight: '24px' }}>
          {value}
        </Checkbox>
      );
    });

    const phasesCheckboxes = [];

    Array.from(phases.entries()).forEach(([, value]) => {
      phasesCheckboxes.push(
        <Checkbox key={uuidv4()} value={value} style={{ lineHeight: '24px' }}>
          {value}
        </Checkbox>
      );
    });

    return (
      <>
        <Form>
          <Collapse>
            <Panel key={uuidv4()} header="Status">
              <Title level={5}>Recruitment Status</Title>
              <Space direction="vertical">
                {recruitmentCheckboxes}
                <Title level={5}>Expanded Access</Title>
              </Space>
              {accessCheckboxes}
            </Panel>
            <Panel key={uuidv4()} header="Phase">
              {phasesCheckboxes}
            </Panel>
            <Panel key={uuidv4()} header="Administration">
              <p>{text}</p>
            </Panel>
            <Panel key={uuidv4()} header="Target">
              <p>Data</p>
            </Panel>
            <Panel key={uuidv4()} header="Modality">
              <p>Data</p>
            </Panel>
            <Panel key={uuidv4()} header="No. of patients">
              <p>Data</p>
            </Panel>
            <Panel key={uuidv4()} header="Sponsor">
              <p>Data</p>
            </Panel>
            <Panel key={uuidv4()} header="Sponsor Type">
              <p>Data</p>
            </Panel>
            <Panel key={uuidv4()} header="Dates" style={{ marginBottom: 24 }}>
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
