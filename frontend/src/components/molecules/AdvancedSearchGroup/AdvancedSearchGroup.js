import React, { Component } from 'react';
import {
  Select, Col, Form, Row, Typography,
} from 'antd';
import PropTypes from 'prop-types';

import TextInputField from '../../atoms/TextInputField/TextInputField';
import SelectField from '../../atoms/SelectField/SelectField';
import RangePickerField from '../../atoms/RangePickerField/RangePickerField';

import {
  funder, documents, submission,
} from '../../../variables/TopLevelSearchData';

class AdvancedSearchGroup extends Component {
  render() {
    const {
      handleInputChange,
      handleDatePickers,
      handleSelectChange,
    } = this.props;
    const { Text } = Typography;
    const { Option } = Select;

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

    const studyStartTitle = "The actual date on which the first participant was enrolled in a clinical study. The 'estimated' study start date is the date that the researchers think will be the study start date.";
    const primaryCompletionTitle = "The date on which the last participant in a clinical study was examined or received an intervention to collect final data for the primary outcome measure. Whether the clinical study ended according to the protocol or was terminated does not affect this date. For clinical studies with more than one primary outcome measure with different completion dates, this term refers to the date on which data collection is completed for all the primary outcome measures. The 'estimated' primary completion date is the date that the researchers think will be the primary completion date for the study.";
    const firstPostedTitle = 'The date on which the study record was first available on ClinicalTrials.gov. There is typically a delay of a few days between the date the study sponsor or investigator submitted the study record and the first posted date.';
    const resultsFirstPostedTitle = 'The date on which summary results information was first available on ClinicalTrials.gov. There is typically a delay between the date the study sponsor or investigator first submits summary results information (the results first submitted date) and the results first posted date.';
    const lastUpdatePostedTitle = "The most recent date on which changes to a study record were made available on ClinicalTrials.gov. There may be a delay between when the changes were submitted to ClinicalTrials.gov by the study's sponsor or investigator (the last update submitted date) and the last update posted date.";

    const rangePickerData = [
      ['range-study-start', 'Study start', studyStartTitle],
      ['range-primary-completion', 'Primary completion', primaryCompletionTitle],
      ['range-first-posted', 'Last update posted', firstPostedTitle],
      ['range-results-first-posted', 'First posted', resultsFirstPostedTitle],
      ['range-last-update-posted', 'Results first posted', lastUpdatePostedTitle],
    ];
    const rangePickers = [];

    Array.from(rangePickerData.entries()).forEach(([, element]) => {
      rangePickers.push(
        <RangePickerField
          key={element[0]}
          label={element[1]}
          title={element[2]}
          name={element[0]}
          handleInputChange={handleDatePickers[element[0]]}
        />
      );
    });

    const rangePickersLeft = Array.from(rangePickers).slice(0, 3);
    const rangePickersRight = Array.from(rangePickers).slice(3, 5);

    return (
      <>
        <Row key="row-expanded-options" gutter={[32, 16]} style={{ marginBottom: '18px' }}>
          <Col key="col-study-dates" span={8}>
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
          <Col key="col-targeted-search" span={8}>
            <Text className="section-text" strong key="t_2">Targeted Search</Text>
            <TextInputField
              key="field-collaborator"
              label="Collaborator"
              title="An organization other than the sponsor that provides support for a clinical study. This support may include activities related to funding, design, implementation, data analysis, or reporting."
              name="studyCollaborator"
              handleInputChange={handleInputChange}
            />
            <TextInputField
              key="field-outcome"
              label="Outcome measure"
              title="For clinical trials, a planned measurement described in the protocol that is used to determine the effect of an intervention/treatment on participants. For observational studies, a measurement or observation that is used to describe patterns of diseases or traits, or associations with exposures, risk factors, or treatment. Types of outcome measures include primary outcome measure and secondary outcome measure."
              name="studyOutcomeMeasure"
              handleInputChange={handleInputChange}
            />
            <TextInputField
              key="field-study-ids"
              label="Study IDs"
              title="Identifiers that are assigned to a clinical study by the study's sponsor, funders, or others. They include unique identifiers from other trial study registries and National Institutes of Health grant numbers. Note: ClinicalTrials.gov assigns a unique identification code to each clinical study registered on ClinicalTrials.gov. Also called the NCT number, the format is 'NCT' followed by an 8-digit number (for example, NCT00000419)."
              name="studyIds"
              handleInputChange={handleInputChange}
            />
          </Col>
          <Col key="col-additional-criteria" span={8}>
            <Text className="section-text" strong key="t_3">Additional Criteria</Text>
            <SelectField
              key="field-funder"
              name="studyFunderType"
              label="Funder Type"
              title="Describes the organization that provides funding or support for a clinical study. This support may include activities related to funding, design, implementation, data analysis, or reporting. Organizations listed as sponsors and collaborators for a study are considered the funders of the study. ClinicalTrials.gov refers to four types of funders: U.S. National Institutes of Health; Other U.S. Federal agencies (for example, Food and Drug Administration, Centers for Disease Control and Prevention, or U.S. Department of Veterans Affairs); Industry (for example: pharmaceutical and device companies); All others (including individuals, universities, and community-based organizations)."
              placeholder="Select the funder type"
              options={funderList}
              handleInputChange={handleSelectChange.handleFunderChange}
            />
            <SelectField
              key="field-documents"
              name="studyDocumentType"
              label="Study Documents"
              title="Refers to the type of documents that the study sponsor or principal investigator may add to their study record. These include a study protocol, statistical analysis plan, and informed consent form."
              placeholder="Select the type of documents"
              options={documentsList}
              handleInputChange={handleSelectChange.handleDocumentsChange}
            />
            <SelectField
              key="field-submission"
              name="studyResultsSubmitted"
              label="Results Submitted"
              title="Indicates that the study sponsor or investigator has submitted summary results information for a clinical study to ClinicalTrials.gov but the quality control (QC) review process has not concluded."
              placeholder="Select the type of submission"
              options={submissionList}
              handleInputChange={handleSelectChange.handleSubmissionChange}
            />
          </Col>
        </Row>
      </>
    );
  }
}

AdvancedSearchGroup.propTypes = {
  handleInputChange: PropTypes.func.isRequired,
  handleDatePickers: PropTypes.object.isRequired,
  handleSelectChange: PropTypes.object.isRequired,
};

export default AdvancedSearchGroup;
