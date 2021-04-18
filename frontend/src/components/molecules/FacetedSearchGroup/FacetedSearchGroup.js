import React, { Component } from 'react';
import {
  Checkbox, Collapse, Form, Typography, Space, DatePicker, Input,
} from 'antd';
import PropTypes from 'prop-types';

import './FacetedSearchGroup.css';

const { RangePicker } = DatePicker;

class FacetedSearchGroup extends Component {
  render() {
    const {
      recruitment, phases, roa,
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
              </Space>
            </Panel>
            <Panel
              key="facet-eligibility"
              header="Eligibility criteria"
              className="fs-group-panel"
            >
              <p>Data</p>
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
              <Input size="small" placeholder="Enter MOA or target" />
            </Panel>
            <Panel
              key="5"
              header="Modality"
              className="fs-group-panel"
            >
              <Input size="small" placeholder="Enter modality" />
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
              id="facet-dates"
              header="Dates"
              className="fs-group-panel"
            >
              <RangePicker picker="month" size="small" />
            </Panel>
            <Panel
              key="facet-type"
              header="Study Type"
              className="fs-group-panel"
            >
              <p>Data</p>
            </Panel>
            <Panel
              key="facet-results"
              header="Study Results"
              className="fs-group-panel"
            >
              <p>Data</p>
            </Panel>
            <Panel
              key="facet-documents"
              header="Study Documents"
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
  recruitment: PropTypes.array.isRequired,
  phases: PropTypes.array.isRequired,
  roa: PropTypes.array.isRequired,
};

export default FacetedSearchGroup;
