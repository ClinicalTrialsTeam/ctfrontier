/* eslint-disable react/no-unused-state */
import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import {
  Collapse, Typography, Row, Col, Descriptions, Divider,
} from 'antd';
import PropTypes from 'prop-types';
import ctgov from '../../../apis/ctgov';

class SingleTrialDisplay extends Component {
  constructor(props) {
    super(props);
    this.state = {
      acronym: { title: 'Acronym', value: '...' },
      brief_title: { title: 'Brief Title', value: '...' },
      condition_name: { title: 'Condition', value: '...' },
      country_name: { title: 'Country', value: '...' },
      document_types: { title: 'Document Types', value: '...' },
      eligibility_criteria: { title: 'Eligibility Criteria', value: '...' },
      eligibility_gender: { title: 'Gender', value: '...' },
      eligibility_max_age: { title: 'Maximum Age', value: '...' },
      eligibility_min_age: { title: 'Minimum Age', value: '...' },
      funder_type: { title: 'Funder Type', value: '...' },
      healthy_volunteers: { title: 'Accepts Healty Volunteers', value: '...' },
      intervention_name: { title: 'Intervention', value: '...' },
      is_unapproved_device: { title: 'Is Unapproved Device', value: '...' },
      last_update_posted_date: { title: 'Last Update Posted', value: '...' },
      location_name: { title: 'Location', value: '...' },
      nct_id: { title: 'NCT Number', value: '...' },
      official_title: { title: 'Official Title', value: '...' },
      primary_completion_date: { title: 'Primary Completion Date', value: '...' },
      primary_outcome_measures: { title: 'Primary Outcome Measures', value: '...' },
      results_first_posted_date: { title: 'Results First Posted', value: '...' },
      results_submitted_qc_done: { title: 'Results Submitted QC Done', value: '...' },
      results_submitted_qc_not_done: { title: 'Results Submitted QC Not Done', value: '...' },
      secondary_outcome_measures: { title: 'Secondary Outcome Measures', value: '...' },
      sponsor_name: { title: 'Sponsor', value: '...' },
      state_name: { title: 'State', value: '...' },
      status: { title: 'Recruitment Status', value: '...' },
      study_brief_desc: { title: 'Brief Description', value: '...' },
      study_detailed_desc: { title: 'Detailed Description', value: '...' },
      study_first_posted_date: { title: 'First Posted', value: '...' },
      study_ids: { title: 'Study IDs', value: '...' },
      study_phase: { title: 'Phase', value: '...' },
      study_start_date: { title: 'Start Date', value: '...' },
      study_type: { title: 'Study Type', value: '...' },
    };
  }

  async componentDidMount() {
    const nctId = this.props.location.pathname.split('/').slice(-1)[0];
    try {
      const nct = { nct_id: nctId };
      const response = await ctgov.post('study_detail', nct);
      Object.entries(response.data[0]).forEach(
        ([key, value]) => {
          const { title } = this.state[key];
          this.setState({ [key]: { title, value } });
        }
      );
    } catch (err) {
      // City name is ignored and generates an inconsequential error
      console.log(err);
    }
  }

  render() {
    const { Panel } = Collapse;
    const { Title } = Typography;

    const rightSummaryDescriptions = [];
    const trackingInformation = [];
    const descriptiveInformation = [];
    const recruitmentInformation = [];
    const administrativeInformation = [];

    const rightSummaryKeys = ['sponsor_name', 'status', 'study_first_posted_date', 'last_update_posted_date'];
    const trackingInformationKeys = [
      'results_first_posted_date',
      'last_update_posted_date',
      'study_start_date',
      'primary_completion_date',
      'primary_outcome_measures',
      'secondary_outcome_measures',
    ];
    const descriptiveInformationKeys = [
      'official_title',
      'brief_title',
      'study_brief_desc',
      'study_detailed_desc',
      'study_type',
      'condition_name',
      'intervention_name',
    ];
    const recruitmentInformationKeys = [
      'eligibility_min_age',
      'eligibility_max_age',
      'eligibility_gender',
      'healthy_volunteers',
      'eligibility_criteria',
      'study_phase',
    ];
    const administrativeInformationKeys = [
      'study_ids',
      'funder_type',
      'document_types',
    ];

    const descriptionsArrays = [
      [rightSummaryKeys, rightSummaryDescriptions],
      [trackingInformationKeys, trackingInformation],
      [descriptiveInformationKeys, descriptiveInformation],
      [recruitmentInformationKeys, recruitmentInformation],
      [administrativeInformationKeys, administrativeInformation],
    ];

    descriptionsArrays.forEach((element) => {
      Array.from(element[0].entries()).forEach(([, value]) => {
        const { title } = this.state[value];
        let content = this.state[value].value;
        if (!content) {
          content = 'Not Available';
        }
        element[1].push(
          <Descriptions.Item
            key={value}
            span={4}
            label={title}
          >
            {content}
          </Descriptions.Item>
        );
      });
    });

    return (
      <>
        <Title level={4}>
          {this.state.brief_title.value}
        </Title>
        <Divider orientation="left">
          ClinicalTrials.gov Identifier:
          {' '}
          {this.state.nct_id.value}
        </Divider>
        <Row key="row-summary" gutter={[16, 8]}>
          <Col key="col-sum-2" span={24}>
            <Descriptions bordered size="small">
              {rightSummaryDescriptions}
            </Descriptions>
          </Col>
        </Row>
        <br />
        <Collapse defaultActiveKey={['panel-tracking']}>
          <Panel
            key="panel-tracking"
            header="Tracking information"
          >
            <Descriptions bordered size="small">
              {trackingInformation}
            </Descriptions>
          </Panel>
          <Panel
            key="panel-descriptive"
            header="Descriptive information"
          >
            <Descriptions bordered size="small">
              {descriptiveInformation}
            </Descriptions>
          </Panel>
          <Panel
            key="panel-recruitment"
            header="Recruitment information"
          >
            <Descriptions bordered size="small">
              {recruitmentInformation}
            </Descriptions>
          </Panel>
          <Panel
            key="panel-administrative"
            header="Administrative information"
          >
            <Descriptions bordered size="small">
              {administrativeInformation}
            </Descriptions>
          </Panel>
        </Collapse>
      </>
    );
  }
}

SingleTrialDisplay.propTypes = {
  location: PropTypes.object.isRequired,
};

export default withRouter(SingleTrialDisplay);
