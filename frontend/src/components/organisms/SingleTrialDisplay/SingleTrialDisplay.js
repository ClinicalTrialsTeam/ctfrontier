import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import {
  Collapse, Typography, Row, Col, Descriptions, Divider,
} from 'antd';
import PropTypes from 'prop-types';
import { fields } from './SingleTrialDisplayConfig';
import ctgov from '../../../apis/ctgov';

class SingleTrialDisplay extends Component {
  async componentDidMount() {
    const nctId = this.props.location.pathname.split('/').slice(-1)[0];
    console.log(nctId);
    try {
      const nct = { nct_id: nctId };
      const response = await ctgov.post('study_detail', nct);
      // this.setState({
      //   nctData: response.data,
      //   nctId,
      // });
      console.log(response);
    } catch (err) {
      console.log(err);
    }
  }

  render() {
    const { Panel } = Collapse;
    const { Title } = Typography;

    const leftSummaryDescriptions = [];
    const rightSummaryDescriptions = [];
    const trackingInformation = [];
    const descriptiveInformation = [];
    const recruitmentInformation = [];
    const administrativeInformation = [];

    const leftSummaryKeys = ['sponsor', 'studyCollaborator', 'responsibleParty'];
    const rightSummaryKeys = ['status', 'resultsFirstPostedDate', 'lastUpdatePostedDate'];
    const trackingInformationKeys = [
      'firstSubmittedDate',
      'resultsFirstPostedDate',
      'lastUpdatePostedDate',
      'studyStartDate',
      'primaryCompletionDate',
      'studyOutcomeMeasuresCurrentPrimary',
      'studyOutcomeMeasuresOriginalPrimary',
      'studyOutcomeMeasuresCurrentSecondary',
      'studyOutcomeMeasuresOriginalSecondary',
    ];
    const descriptiveInformationKeys = [
      'title',
      'briefTitle',
      'summary',
      'detailedDescription',
      'type',
      'design',
      'sampling',
      'population',
      'condition',
      'subcondition',
      'intervention',
    ];
    const recruitmentInformationKeys = [
      'age',
      'sex',
      'ethnicity',
      'healthy',
    ];
    const administrativeInformationKeys = [
      'studyIds',
      'studyFunderType',
      'studyDocumentType',
    ];

    const descriptionsArrays = [
      [leftSummaryKeys, leftSummaryDescriptions],
      [rightSummaryKeys, rightSummaryDescriptions],
      [trackingInformationKeys, trackingInformation],
      [descriptiveInformationKeys, descriptiveInformation],
      [recruitmentInformationKeys, recruitmentInformation],
      [administrativeInformationKeys, administrativeInformation],
    ];

    descriptionsArrays.forEach((element) => {
      Array.from(element[0].entries()).forEach(([, value]) => {
        const title = fields[value];
        element[1].push(
          <Descriptions.Item
            key={value}
            span={4}
            label={title}
          >
            Placeholder text placeholder text placeholder text
          </Descriptions.Item>
        );
      });
    });

    return (
      <>
        <Title level={4}>
          Does Timeliness of DTaP-IPV-Hib Vaccination
          Affect Development of Atopic Dermatitis Before 1 Year of Age?
        </Title>
        <Divider orientation="left">ClinicalTrials.gov Identifier: </Divider>
        <Row key="row-summary" gutter={[16, 8]}>
          <Col key="col-sum-1" span={12}>
            <Descriptions bordered size="small" width="100px">
              {leftSummaryDescriptions}
            </Descriptions>
          </Col>
          <Col key="col-sum-2" span={12}>
            <Descriptions bordered size="small">
              {rightSummaryDescriptions}
            </Descriptions>
          </Col>
        </Row>
        <br />
        <Collapse defaultActiveKey={['1']}>
          <Panel
            key="panel-tracking"
            header="Tracking information"
          >
            <Descriptions bordered size="small">
              {trackingInformation}
            </Descriptions>
          </Panel>
          <Panel
            key="2"
            header="Descriptive information"
          >
            <Descriptions bordered size="small">
              {descriptiveInformation}
            </Descriptions>
          </Panel>
          <Panel
            key="3"
            header="Recruitment information"
          >
            <Descriptions bordered size="small">
              {recruitmentInformation}
            </Descriptions>
          </Panel>
          <Panel
            key="4"
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
