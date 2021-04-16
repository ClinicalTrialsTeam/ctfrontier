import React, { Component } from 'react';
import {
  Checkbox, Collapse, Form, Typography,
  Space, DatePicker, Input, Row, Col, Select,
} from 'antd';
import PropTypes from 'prop-types';
import NumberInputField from '../../atoms/NumberInputField/NumberInputField';
import SelectField from '../../atoms/SelectField/SelectField';

import './FacetedSearchGroup.css';

const { RangePicker } = DatePicker;

class FacetedSearchGroup extends Component {
  render() {
    const {
      recruitment, phases, roa, ageGroup,
      // results, types, sex, ethnicities, distance, states,
    } = this.props;
    const { Panel } = Collapse;
    const { Text } = Typography;
    const { Option } = Select;

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

    const ageGroupList = [];

    const selectArrays = [
      [ageGroup, ageGroupList],
    ];

    selectArrays.forEach((element) => {
      Array.from(element[0].entries()).forEach(([index, value]) => {
        element[1].push(
          <Option key={index} value={value}>{value}</Option>
        );
      });
    });

    return (
      <>
        <Form
          layout="vertical"
        >
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
              <Row key="form_row_age" gutter={[8, 8]}>
                <Col key="col-age-num" span={16}>
                  <NumberInputField
                    className="age-num"
                    min={0}
                    max={100}
                    size="small"
                    key="field-age"
                    label="Age"
                    title="A type of eligibility criteria that indicates the age a person must be to participate in a clinical study. This may be indicated by a specific age or the following age groups:
                    Child (birth-17);
                    Adult (18-64);
                    Older Adult (65+)."
                    name="age"
                    handleInputChange={this.handleInputChange}
                  />
                </Col>
                <Col key="col-or" span={8}>
                  <p id="or-p">OR</p>
                </Col>
              </Row>
              <Row key="form-row-age-group" gutter={[16, 8]}>
                <Col key="col-age-group" span={24}>
                  <SelectField
                    mode="multiple"
                    size="small"
                    key="field-age-group"
                    name="age_group"
                    label="Age Group"
                    title="A type of eligibility criteria that indicates the age a person must be to participate in a clinical study. This may be indicated by a specific age or the following age groups:
                      Child (birth-17);
                      Adult (18-64);
                      Older Adult (65+)."
                    placeholder="Select the age group"
                    options={ageGroupList}
                    handleInputChange={this.handleAgeGroupChange}
                  />
                </Col>
              </Row>
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
              <RangePicker size="small" />
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
  ageGroup: PropTypes.array.isRequired,
};

export default FacetedSearchGroup;
