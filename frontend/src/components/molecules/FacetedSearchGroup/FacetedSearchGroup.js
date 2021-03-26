import React, { Component } from 'react';
import {
  Checkbox, Collapse, Form, Typography, Space, DatePicker,
} from 'antd';
import PropTypes from 'prop-types';

import './FacetedSearchGroup.css';

const { RangePicker } = DatePicker;

class FacetedSearchGroup extends Component {
  render() {
    const {
      access, recruitment, phases, roa,
    } = this.props;
    const { Panel } = Collapse;
    const { Text } = Typography;

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

    const roaCheckboxes = [];

    Array.from(roa.entries()).forEach(([index, value]) => {
      roaCheckboxes.push(
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
              <Space key="recr-status-checkboxes" direction="vertical">
                <Text key="txt-1" strong>Recruitment Status</Text>
                {recruitmentCheckboxes}
                <Text key="txt-2" strong>Expanded Access</Text>
                {accessCheckboxes}
              </Space>
            </Panel>
            <Panel
              key="2"
              header="Phase"
              className="fs-group-panel"
            >
              <Space direction="vertical">
                {phasesCheckboxes}
              </Space>
            </Panel>
            <Panel
              key="3"
              header="Administration"
              className="fs-group-panel"
            >
              <Space direction="vertical">
                {roaCheckboxes}
              </Space>
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
              id="rangepicker-panel"
              header="Dates"
              className="fs-group-panel"
            >
              <RangePicker picker="month" size="small" />
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
  roa: PropTypes.array.isRequired,
};

export default FacetedSearchGroup;
