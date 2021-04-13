import React, { Component } from 'react';
import {
  Select, Checkbox, Col, Form, Row, DatePicker, Typography,
} from 'antd';
import PropTypes from 'prop-types';
import { v4 as uuidv4 } from 'uuid';

import TextInputField from '../../atoms/TextInputField/TextInputField';
import SelectField from '../../atoms/SelectField/SelectField';

import {
  funder, documents, submission,
} from '../../../variables/TopLevelSearchData';

class AdvancedSearchGroup extends Component {
  render() {
    const { access, recruitment, handleInputChange } = this.props;
    const { Text } = Typography;
    const { Option } = Select;

    const recruitmentCheckboxes = [];
    const { RangePicker } = DatePicker;

    const funderList = [];
    const documentsList = [];
    const submissionList = [];

    const selectArrays = [
      [funder, funderList],
      [documents, documentsList],
      [submission, submissionList],
    ];

    selectArrays.forEach((element) => {
      Array.from(element[0].entries()).forEach(([index, value]) => {
        element[1].push(
          <Option key={index} value={value}>{value}</Option>
        );
      });
    });

    const rangePickerData = [
      ['range_1', 'Study start'],
      ['range_2', 'Primary completion'],
      ['range_3', 'Last update posted'],
      ['range_4', 'First posted'],
      ['range_5', 'Results first posted'],
    ];
    const rangePickers = [];

    rangePickerData.forEach((element) => {
      rangePickers.push(
        <Form.Item
          key={element[0]}
          label={element[1]}
        >
          <RangePicker />
        </Form.Item>
      );
    });

    const rangePickersLeft = Array.from(rangePickers).slice(0, 3);
    const rangePickersRight = Array.from(rangePickers).slice(3, 5);

    Array.from(recruitment.entries()).forEach(([, value]) => {
      recruitmentCheckboxes.push(
        <Col key={uuidv4()} span={12}>
          <Checkbox key={uuidv4()} value={value} style={{ lineHeight: '32px' }}>
            {value}
          </Checkbox>
        </Col>
      );
    });

    const accessCheckboxes = [];

    Array.from(access.entries()).forEach(([, value]) => {
      accessCheckboxes.push(
        <Col key={uuidv4()} span={12}>
          <Checkbox key={uuidv4()} value={value} style={{ lineHeight: '32px' }}>
            {value}
          </Checkbox>
        </Col>
      );
    });

    return (
      <>
        <Row key={uuidv4()} gutter={[32, 16]} style={{ marginBottom: '18px' }}>
          <Col key={uuidv4()} span={8}>
            <Text className="section-text" strong key="t_1">Study Dates</Text>
            <Form.Item
              name="ranges"
            >
              <Row className="gutter-row" gutter={16}>
                <Col key="dates-left" span={12}>
                  {rangePickersLeft}
                </Col>
                <Col key="dates-right" span={12}>
                  {rangePickersRight}
                </Col>
              </Row>
            </Form.Item>
          </Col>
          <Col key={uuidv4()} span={8}>
            <Text className="section-text" strong key="t_2">Targeted Search</Text>
            <TextInputField
              key="field-collaborator"
              label="Collaborator"
              title="An organization other than the sponsor that provides support for a clinical study. This support may include activities related to funding, design, implementation, data analysis, or reporting."
              name="study_collaborator"
              handleInputChange={handleInputChange}
            />
            <TextInputField
              key="field-outcome"
              label="Outcome measure"
              title="For clinical trials, a planned measurement described in the protocol that is used to determine the effect of an intervention/treatment on participants. For observational studies, a measurement or observation that is used to describe patterns of diseases or traits, or associations with exposures, risk factors, or treatment. Types of outcome measures include primary outcome measure and secondary outcome measure."
              name="study_outcome_measure"
              handleInputChange={handleInputChange}
            />
            <TextInputField
              key="field-study-ids"
              label="Study IDs"
              title="Identifiers that are assigned to a clinical study by the study's sponsor, funders, or others. They include unique identifiers from other trial study registries and National Institutes of Health grant numbers. Note: ClinicalTrials.gov assigns a unique identification code to each clinical study registered on ClinicalTrials.gov. Also called the NCT number, the format is 'NCT' followed by an 8-digit number (for example, NCT00000419)."
              name="study_ids"
              handleInputChange={handleInputChange}
            />
          </Col>
          <Col key={uuidv4()} span={8}>
            <Text className="section-text" strong key="t_3">Additional Criteria</Text>
            <SelectField
              key="field-funder"
              name="study_funder_type"
              label="Funder Type"
              title="Describes the organization that provides funding or support for a clinical study. This support may include activities related to funding, design, implementation, data analysis, or reporting. Organizations listed as sponsors and collaborators for a study are considered the funders of the study. ClinicalTrials.gov refers to four types of funders: U.S. National Institutes of Health; Other U.S. Federal agencies (for example, Food and Drug Administration, Centers for Disease Control and Prevention, or U.S. Department of Veterans Affairs); Industry (for example: pharmaceutical and device companies); All others (including individuals, universities, and community-based organizations)."
              placeholder="Select the funder type"
              options={funderList}
              handleInputChange={this.handleFunderChange}
            />
            <SelectField
              key="field-documents"
              name="study_document_type"
              label="Study Documents"
              title="Refers to the type of documents that the study sponsor or principal investigator may add to their study record. These include a study protocol, statistical analysis plan, and informed consent form."
              placeholder="Select the type of documents"
              options={documentsList}
              handleInputChange={this.handleDocumentsChange}
            />
            <SelectField
              key="field-submission"
              name="study_results_submitted"
              label="Results Submitted"
              title="Indicates that the study sponsor or investigator has submitted summary results information for a clinical study to ClinicalTrials.gov but the quality control (QC) review process has not concluded."
              placeholder="Select the type of submission"
              options={submissionList}
              handleInputChange={this.handleSubmissionChange}
            />
          </Col>
        </Row>
      </>
    );
  }
}

AdvancedSearchGroup.propTypes = {
  access: PropTypes.array.isRequired,
  recruitment: PropTypes.array.isRequired,
  handleInputChange: PropTypes.func.isRequired,
};

export default AdvancedSearchGroup;
