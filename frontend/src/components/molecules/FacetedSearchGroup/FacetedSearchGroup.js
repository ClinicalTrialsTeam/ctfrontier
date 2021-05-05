import React, { Component } from 'react';
import {
  Checkbox, Collapse, Form,
  Row, Col, Select,
} from 'antd';
import PropTypes from 'prop-types';
import { InfoCircleOutlined } from '@ant-design/icons';
import NumberInputField from '../../atoms/NumberInputField/NumberInputField';
import SelectField from '../../atoms/SelectField/SelectField';
import CheckBoxGroup from '../CheckBoxGroup/CheckBoxGroup';
import TextInputField from '../../atoms/TextInputField/TextInputField';
import RangePickerField from '../../atoms/RangePickerField/RangePickerField';

import './FacetedSearchGroup.css';

class FacetedSearchGroup extends Component {
  render() {
    const {
      status, phases, roa, ageGroup, ethnicities,
      funder, documents, submission, results, types, sex, handleInputChange,
      handleStatusChange,
    } = this.props;
    const { Panel } = Collapse;
    const { Option } = Select;

    // Checkbox groups
    const statusCheckboxes = [];
    const phasesCheckboxes = [];
    const roaCheckboxes = [];
    const ageGroupCheckboxes = [];

    const checkboxArrays = [
      [status, statusCheckboxes],
      [phases, phasesCheckboxes],
      [roa, roaCheckboxes],
      [ageGroup, ageGroupCheckboxes],
    ];

    checkboxArrays.forEach((element) => {
      Array.from(element[0].entries()).forEach(([index, value]) => {
        element[1].push(
          <Checkbox key={index}
                    value={value}
                    style={{ lineHeight: '24px' }}
                    onChange={handleStatusChange}
                    name={value}
          >
            {value}
          </Checkbox>
        );
      });
    });

    // Lists
    const funderList = [];
    const typeList = [];
    const resultsList = [];
    const documentsList = [];
    const submissionList = [];
    const ethnicitiesList = [];
    const sexList = [];

    const selectArrays = [
      [funder, funderList],
      [types, typeList],
      [results, resultsList],
      [documents, documentsList],
      [submission, submissionList],
      [ethnicities, ethnicitiesList],
      [sex, sexList],
    ];

    selectArrays.forEach((element) => {
      Array.from(element[0].entries()).forEach(([index, value]) => {
        element[1].push(
          <Option key={index} value={value}>{value}</Option>
        );
      });
    });

    // Date Rangepickers
    const studyStartTitle = "The actual date on which the first participant was enrolled in a clinical study. The 'estimated' study start date is the date that the researchers think will be the study start date.";
    const primaryCompletionTitle = "The date on which the last participant in a clinical study was examined or received an intervention to collect final data for the primary outcome measure. Whether the clinical study ended according to the protocol or was terminated does not affect this date. For clinical studies with more than one primary outcome measure with different completion dates, this term refers to the date on which data collection is completed for all the primary outcome measures. The 'estimated' primary completion date is the date that the researchers think will be the primary completion date for the study.";

    const rangePickerData = [
      ['range-study-start', 'First patient in', studyStartTitle],
      ['range-primary-completion', 'Last patient out', primaryCompletionTitle],
    ];
    const rangePickers = [];

    Array.from(rangePickerData.entries()).forEach(([, element]) => {
      rangePickers.push(
        <RangePickerField
          size="small"
          key={element[0]}
          label={element[1]}
          title={element[2]}
          name={element[0]}
          handleInputChange={handleInputChange}
        />
      );
    });

    return (
      <>
        <Form
          layout="vertical"
        >
          <Collapse defaultActiveKey={['1', 'facet-eligibility']} className="fs-group-collapse">
            <Panel
              key="1"
              header="Status"
              className="fs-group-panel"
            >
              <CheckBoxGroup
                key="checkboxes-status"
                name="status"
                label="Recruitment Status"
                title="Indicates the current recruitment status"
                checkboxes={statusCheckboxes}
                handleInputChange={handleInputChange}
              />
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
                    name="eligibility_age"
                    handleInputChange={this.handleInputChange}
                  />
                </Col>
                <Col key="col-or" span={8}>
                  <p id="or-p">OR</p>
                </Col>
              </Row>
              <Row key="form-row-age-group" gutter={[16, 8]}>
                <Col key="col-age-group" span={24}>
                  <CheckBoxGroup
                    key="checkboxes-age-group"
                    name="eligibility_age_group"
                    label="Age Group"
                    title="A type of eligibility criteria that indicates the age a person must be to participate in a clinical study. This may be indicated by a specific age or the following age groups:
                        Child (birth-17);
                        Adult (18-64);
                        Older Adult (65+)."
                    checkboxes={ageGroupCheckboxes}
                  />
                </Col>
              </Row>
              <Row key="form-row-ethnicity" gutter={[16, 8]}>
                <Col key="col-ethinicity" span={24}>
                  <SelectField
                    size="small"
                    key="field-ethnicity"
                    name="ethnicity"
                    label="Race / Ethnicity"
                    title="American Indian or Alaska Native: A person having origins in any of the original peoples of North and South America (including Central America) and who maintains tribal affiliation or community attachment.
                      Asian: A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam.
                      Black or African American: A person having origins in any of the Black racial groups of Africa.
                      Native Hawaiian or Other Pacific Islander: A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands.
                      White: A person having origins in any of the original peoples of Europe, the Middle East, or North Africa. Hispanic or Latino: A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race."
                    placeholder="Select the ethnicity"
                    options={ethnicitiesList}
                    handleInputChange={this.handleEthnicityChange}
                  />
                </Col>
              </Row>
              <Row key="form-row-sex" gutter={[16, 8]}>
                <Col key="col-ethinicity" span={24}>
                  <SelectField
                    size="small"
                    key="field-sex"
                    name="sex"
                    label="Sex"
                    title="A type of eligibility criteria that indicates the sex of people who may participate in a clinical study (all, female, male). Sex is a person's classification as female or male based on biological distinctions. Sex is distinct from gender-based eligibility."
                    placeholder="Select the participant's sex"
                    options={sexList}
                    handleInputChange={this.handleSexChange}
                  />
                </Col>
              </Row>
              <Row key="form-row-is-healty" gutter={[16, 8]}>
                <Col key="col-is-healthy" span={24}>
                  <Form.Item
                    key="checkbox-healthy"
                    label="Healthy"
                    tooltip={{
                      title: 'A type of eligibility criteria that indicates whether people who do not have the condition/disease being studied can participate in that clinical study.',
                      icon: <InfoCircleOutlined />,
                    }}
                  >
                    <Checkbox>Is healthy?</Checkbox>
                  </Form.Item>
                </Col>
              </Row>
            </Panel>
            <Panel
              key="2"
              header="Phase"
              className="fs-group-panel"
            >
              <CheckBoxGroup
                key="checkboxes-phase"
                name="phase"
                label="Study phase"
                title="The stage of a clinical trial studying a drug or biological product, based on definitions developed by the U.S. Food and Drug Administration (FDA). The phase is based on the study's objective, the number of participants, and other characteristics. There are five phases: Early Phase 1 (formerly listed as Phase 0), Phase 1, Phase 2, Phase 3, and Phase 4. Not Applicable is used to describe trials without FDA-defined phases, including trials of devices or behavioral interventions."
                checkboxes={phasesCheckboxes}
              />
            </Panel>
            <Panel
              key="3"
              header="Administration"
              className="fs-group-panel"
            >
              <CheckBoxGroup
                key="checkboxes-roa"
                name="phase"
                label="Route of Administration"
                title="A route of administration in pharmacology is the path by which a drug is taken into the body. Common examples include oral and intravenous administration."
                checkboxes={roaCheckboxes}
              />
            </Panel>
            <Panel
              key="4"
              header="Target"
              className="fs-group-panel"
            >
              <TextInputField
                key="field-target"
                size="small"
                label="MOA / Target"
                title="Mechanism of Action (MOA) is a biochemical interaction that a drug disrupts usually involving a specific protein (target), such as an enzyme or receptor."
                name="target"
                handleInputChange={handleInputChange}
              />
            </Panel>
            <Panel
              key="5"
              header="Modality"
              className="fs-group-panel"
            >
              <TextInputField
                key="field-modality"
                size="small"
                label="Modality"
                title="A therapeutic approach for drugs, such as small molecules, antibodies, RNAi, CAR T cell, or peptide."
                name="modality"
                handleInputChange={handleInputChange}
              />
            </Panel>
            <Panel
              key="6"
              header="Number of Subjects"
              className="fs-group-panel"
            >
              <NumberInputField
                min={1}
                size="small"
                key="field-participants-min"
                label="Minimum subjects"
                title="The minimum number of subjects participating in the clinical study (inclusive)."
                name="participants_min"
                handleInputChange={handleInputChange}
              />
              <NumberInputField
                min={1}
                size="small"
                key="field-participants-max"
                label="Maximum subjects"
                title="The maximum number of subjects participating in the clinical study (exclusive)."
                name="participants_max"
                handleInputChange={handleInputChange}
              />
            </Panel>
            <Panel
              key="7"
              header="Sponsor"
              className="fs-group-panel"
            >
              <TextInputField
                key="field-sponsor"
                size="small"
                label="Sponsor / Collaborators"
                title="Sponsor is the organization or person who initiates the study and who has authority and control over the study. Collaborator is an organization other than the sponsor that provides support for a clinical study. This support may include activities related to funding, design, implementation, data analysis, or reporting."
                name="target"
                handleInputChange={handleInputChange}
              />
            </Panel>
            <Panel
              key="8"
              header="Sponsor Type"
              className="fs-group-panel"
            >
              <SelectField
                key="field-funder"
                size="small"
                name="study_funder_type"
                label="Sponsor Type"
                title="Describes the organization that provides funding or support for a clinical study. This support may include activities related to funding, design, implementation, data analysis, or reporting. Organizations listed as sponsors and collaborators for a study are considered the funders of the study. ClinicalTrials.gov refers to four types of funders: U.S. National Institutes of Health; Other U.S. Federal agencies (for example, Food and Drug Administration, Centers for Disease Control and Prevention, or U.S. Department of Veterans Affairs); Industry (for example: pharmaceutical and device companies); All others (including individuals, universities, and community-based organizations)."
                placeholder="Select the sponsor type"
                options={funderList}
                handleInputChange={this.handleFunderChange}
              />
            </Panel>
            <Panel
              key="9"
              id="facet-dates"
              header="Study dates"
              className="fs-group-panel"
            >
              {rangePickers}
            </Panel>
            <Panel
              key="facet-type"
              header="Study Type"
              className="fs-group-panel"
            >
              <SelectField
                key="field-types"
                size="small"
                name="types"
                label="Study Type"
                title="Describes the nature of a clinical study. Study types include interventional studies (also called clinical trials), observational studies (including patient registries), and expanded access."
                placeholder="Select the type"
                options={typeList}
                handleInputChange={this.handleTypeChange}
              />
            </Panel>
            <Panel
              key="facet-results"
              header="Study Results"
              className="fs-group-panel"
            >
              <SelectField
                key="field-results"
                size="small"
                name="results"
                label="Study Results"
                title="A study record that includes the summary results posted in the ClinicalTrials.gov results database. Summary results information includes participant flow, baseline characteristics, outcome measures, and adverse events (including serious adverse events)."
                placeholder="Select the results"
                options={resultsList}
                handleInputChange={this.handleResultsChange}
              />
            </Panel>
            <Panel
              key="facet-documents"
              header="Study Documents"
              className="fs-group-panel"
            >
              <SelectField
                key="field-documents"
                size="small"
                name="study_document_type"
                label="Study Documents"
                title="Refers to the type of documents that the study sponsor or principal investigator may add to their study record. These include a study protocol, statistical analysis plan, and informed consent form."
                placeholder="Select the type of documents"
                options={documentsList}
                handleInputChange={this.handleDocumentsChange}
              />
            </Panel>
          </Collapse>
        </Form>
      </>
    );
  }
}

FacetedSearchGroup.propTypes = {
  funder: PropTypes.array.isRequired,
  handleInputChange: PropTypes.func,
  handleStatusChange: PropTypes.func,
  types: PropTypes.array.isRequired,
  results: PropTypes.array.isRequired,
  documents: PropTypes.array.isRequired,
  submission: PropTypes.array.isRequired,
  status: PropTypes.array.isRequired,
  phases: PropTypes.array.isRequired,
  roa: PropTypes.array.isRequired,
  ageGroup: PropTypes.array.isRequired,
  ethnicities: PropTypes.array.isRequired,
  sex: PropTypes.array.isRequired,
};

export default FacetedSearchGroup;
