import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import {
  Table, Space, Button, Row, Col, Card, Tooltip, Typography,
} from 'antd';
import PropTypes from 'prop-types';
import {
  AlignLeftOutlined, BarChartOutlined, DownloadOutlined,
} from '@ant-design/icons';
import log from 'loglevel';
import ctgov from '../../../apis/ctgov';

import FacetedSearchGroup from '../../molecules/FacetedSearchGroup/FacetedSearchGroup';
import DashboardModal from '../../molecules/modals/DashboardModal/DashboardModal';
import TimelineModal from '../../molecules/modals/TimelineModal/TimelineModal';
import DownloadModal from '../../molecules/modals/DownloadModal/DownloadModal';

import {
  status, access, phases, roa, results,
  types, sex, ageGroup, ethnicities, distance, states,
  funder, documents, submission,
} from '../../../variables/SelectOptionsData';

import './ListViewTable.css';
import CTFButton from '../../atoms/buttons/Button/Button';

class ListViewTable extends Component {
  constructor(props) {
    super(props);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleStatusChange = this.handleStatusChange.bind(this);
    this.setDashboardModalVisible = this.setDashboardModalVisible.bind(this);
    this.setTimelineModalVisible = this.setTimelineModalVisible.bind(this);
    this.setDownloadModalVisible = this.setDownloadModalVisible.bind(this);
    this.handleSearch = this.handleSearch.bind(this);
    this.handleClear = this.handleClear.bind(this);
    this.formRef = React.createRef();
    this.facetsRef = React.createRef();
    this.state = {
      intervention: '',
      condition: '',
      target: '',
      otherTerms: '',
      isDashboardModalVisible: false,
      isTimelineModalVisible: false,
      isDownloadModalVisible: false,
      searchData: this.props.history.location.state.data,
      payload: this.props.history.location.state.payload,
      searchParameters: this.props.history.location.state.searchParameters,
      dashboardData: {},
      applyFilters: false,
    };
  }

  handleClear() {
    this.setState({
      intervention: '',
      condition: '',
      target: '',
      nct_id: '',
    });
    this.formRef.current.resetFields();
  }

  handleInputChange(e) {
    const { target } = e;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const { name } = target;

    let {searchParameters} = this.state;
    searchParameters[name] = value;

    this.setState({
      searchParameters,
    });
  }

  handleStatusChange(e) {
    const { target } = e;
    const value = target.name;

    let {searchParameters} = this.state;
    searchParameters.status = value;

    this.setState({
      searchParameters,
    });
  }

  async handleSearch() {
    const payload = {
      status: this.state.searchParameters.status,
      condition: this.state.searchParameters.condition,
      other_terms: this.state.searchParameters.otherTerms,
      country: this.state.searchParameters.country,
      intervention: this.state.searchParameters.intervention,
      target: this.state.searchParameters.target,
      nct_id: this.state.searchParameters.nct_id,
      eligibility_criteria: '',
      modality: this.state.searchParameters.modality,
      sponsor: this.state.searchParameters.sponsor,
      phase: this.state.searchParameters.phase,
      start_date_from: this.state.searchParameters.startDateFrom,
      start_date_to: this.state.searchParameters.startDateTo,
      primary_completion_date_from: this.state.searchParameters.primaryCompletionDateFrom,
      primary_completion_date_to: this.state.searchParameters.primaryCompletionDateTo,
      first_posted_date_from: this.state.searchParameters.firstPostedDateFrom,
      first_posted_date_to: this.state.searchParameters.firstPostedDateTo,
      results_first_posted_date_from: this.state.searchParameters.resultsFirstPostedDateFrom,
      results_first_posted_date_to: this.state.searchParameters.resultsFirstPostedDateTo,
      last_update_posted_date_from: this.state.searchParameters.lastUpdatePostedDateFrom,
      last_update_posted_date_to: this.state.searchParameters.lastUpdatePostedDateTo,
      study_results: this.state.searchParameters.results,
      study_type: this.state.searchParameters.type,
      eligibility_age: this.state.searchParameters.age,
      eligibility_min_age: this.state.searchParameters.minAge,
      eligibility_max_age: this.state.searchParameters.maxAge,
      eligibility_gender: this.state.searchParameters.sex,
      eligibility_ethnicity: this.state.searchParameters.ethnicity,
      eligibility_condition: '',
      eligibility_healthy_volunteer: this.state.searchParameters.healthy === true ? 'Accepts Healthy Volunteers' : '',
      study_title_acronym: this.state.searchParameters.title,
      study_outcome_measure: this.state.searchParameters.studyOutcomeMeasure,
      study_collaborator: this.state.searchParameters.studyCollaborator,
      study_ids: this.state.searchParameters.studyIds,
      study_location_terms: this.state.searchParameters.locationTerms,
      study_funder_type: this.state.searchParameters.studyFunderType,
      study_document_type: this.state.searchParameters.studyDocumentType,
      study_results_submitted: this.state.searchParameters.studyResultsSubmitted,
      study_roa: this.state.searchParameters.roa,
      state: this.state.searchParameters.state,
      city: this.state.searchParameters.city,
      distance: this.state.searchParameters.distance,
      subcondition: this.state.searchParameters.subcondition,
      first: 0,
      last: 100,
      metadata_required: true,
    };
    try {
      const response = await ctgov.post('search_studies', payload);
      this.setState({
        searchData: response.data,
        payload,
        applyFilters: true,
      });
      log.info(response.data);
    } catch (err) {
      console.log(err);
    }
  }

  async setDashboardModalVisible(isDashboardModalVisible) {
    const { payload } = this.state;
    if (isDashboardModalVisible) {
      try {
        const response = await ctgov.post('trials_dashboard', payload);
        this.setState({
          dashboardData: response.data,
        });
      } catch (err) {
        console.log(err);
      }
    }
    this.setState({
      isDashboardModalVisible,
    });
  }

  setTimelineModalVisible(isTimelineModalVisible) {
    this.setState({
      isTimelineModalVisible,
    });
  }

  setDownloadModalVisible(isDownloadModalVisible) {
    this.setState({
      isDownloadModalVisible,
    });
  }

  render() {
    const { Link } = Typography;
    const columns = [
      {
        title: 'NCT ID',
        dataIndex: 'nct_id',
        key: 'nct_id',
        fixed: 'left',
        width: 120,
        sortDirections: ['descend', 'ascend'],
        sorter: (a, b) => { return a.nct_id.localeCompare(b.nct_id); },
        render: (nctId) => {
          return (
            <Link
              type="link"
              size="small"
              href={'./trials/' + nctId}
            >
              {nctId}
            </Link>
          );
        },
      },
      {
        title: 'Brief Title',
        dataIndex: 'brief_title',
        key: 'brief_title',
        width: 250,
      },
      {
        title: 'Condition',
        dataIndex: 'condition_name',
        key: 'condition_name',
        width: 150,
        sortDirections: ['descend', 'ascend'],
        sorter: (a, b) => {
          return a.condition_name.localeCompare(b.condition_name);
        },
      },
      {
        title: 'Intervention',
        dataIndex: 'intervention_name',
        key: 'intervention_name',
        sorter: true,
        width: 200,
      },
      {
        title: 'Sponsor',
        dataIndex: 'sponsor_name',
        key: 'sponsor_name',
        sortDirections: ['descend', 'ascend'],
        sorter: (a, b) => { return a.sponsor_name.localeCompare(b.sponsor_name); },
        width: 150,
      },
      {
        title: 'Phase',
        dataIndex: 'study_phase',
        key: 'study_phase',
        sortDirections: ['descend', 'ascend'],
        sorter: (a, b) => { return a.study_phase.localeCompare(b.study_phase); },
        width: 100,
      },
      {
        title: 'Status',
        dataIndex: 'status',
        key: 'status',
        sortDirections: ['descend', 'ascend'],
        sorter: (a, b) => { return a.status.localeCompare(b.status); },
        width: 100,
      },
    ];
    const { data } = this.props.history.location.state;
    const dataCount = parseInt(data.metadata[0].results_count);
    const parsedResults = data.search_results.map((result) => {
      return {
        key: result.nct_id,
        nct_id: result.nct_id,
        brief_title: result.brief_title,
        condition_name: result.condition_name !== null ? result.condition_name.split('|').join(', ') : '',
        sponsor_name: result.sponsor_name !== null ? result.sponsor_name.split('|').join(', ') : '',
        study_phase: result.study_phase !== null ? result.study_phase.split('/').join(', ') : '',
        intervention_name: result.intervention_name !== null ? result.intervention_name.split('|').join(', ') : '',
        status: result.status,
      };
    });

    return (
      <div>
        <Card id="trial-card">
          <Row
            key="list_view_items"
            gutter={{
              xs: 8,
              sm: 12,
              md: 12,
              lg: 12,
            }}
          >
            <Col key="fs-group-col" id="fs-group-col" className="gutter-row" span={4}>
              <Space key="fs-buttons">
                <CTFButton
                  loading={this.state.isLoading}
                  key="btn_search"
                  inputType="primary"
                  text="Apply"
                  clickHandler={this.handleSearch}
                />
                <Button key="fs-button-clear" className="facet-button" clickHandler={this.handleClear}>
                  Clear
                </Button>
              </Space>
              <div ref={this.facetsRef}>
                <FacetedSearchGroup
                  key="fs-group"
                  access={access}
                  status={status}
                  phases={phases}
                  roa={roa}
                  results={results}
                  types={types}
                  sex={sex}
                  ageGroup={ageGroup}
                  ethnicities={ethnicities}
                  states={states}
                  distance={distance}
                  funder={funder}
                  documents={documents}
                  submission={submission}
                  handleInputChange={this.handleInputChange}
                  handleStatusChange={this.handleStatusChange}
                />
              </div>
            </Col>
            <Col key="trails_table-col" className="gutter-row" span={20}>
              <Row key="trials-table-extras">
                <Col key="trials-stat-col" span={8}>
                  <Row id="trials-stat-row" justify="start" align="middle">
                    Total number of trials:
                    {' '}
                    {dataCount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')}
                  </Row>
                </Col>
                <Col key="trials-modal-btn-col" span={16}>
                  <Row id="trials-modal-btn-row" justify="end">
                    <Space align="end">
                      <Tooltip title="View dashboard">
                        <Button
                          key="btn_dashboard"
                          onClick={() => {
                            return this.setDashboardModalVisible(true);
                          }}
                          icon={<BarChartOutlined />}
                        />
                      </Tooltip>
                      <Tooltip title="View timeline">
                        <Button
                          key="btn_timeline"
                          onClick={() => {
                            return this.setTimelineModalVisible(true);
                          }}
                          icon={<AlignLeftOutlined />}
                        />
                      </Tooltip>
                      <Tooltip title="Download options">
                        <Button
                          key="btn_download"
                          onClick={() => {
                            return this.setDownloadModalVisible(true);
                          }}
                          icon={<DownloadOutlined />}
                        />
                      </Tooltip>
                      <DashboardModal
                        isModalVisible={this.state.isDashboardModalVisible}
                        data={this.state.dashboardData}
                        count={this.state.searchData.metadata[0].results_count}
                        handleOk={() => {
                          return this.setDashboardModalVisible(false, '');
                        }}
                        handleCancel={() => {
                          return this.setDashboardModalVisible(false, '');
                        }}
                      />
                      <TimelineModal
                        isModalVisible={this.state.isTimelineModalVisible}
                        data={this.state.searchData}
                        handleOk={() => {
                          return this.setTimelineModalVisible(false, '');
                        }}
                        handleCancel={() => {
                          return this.setTimelineModalVisible(false, '');
                        }}
                      />
                      <DownloadModal
                        isModalVisible={this.state.isDownloadModalVisible}
                        data={this.state.searchData}
                        payload={this.state.payload}
                        handleOk={() => {
                          return this.setDownloadModalVisible(false, '');
                        }}
                        handleCancel={() => {
                          return this.setDownloadModalVisible(false, '');
                        }}
                      />
                    </Space>
                  </Row>
                </Col>
              </Row>
              <Table
                pagination={{ total: dataCount, pageSize: 20 }}
                scroll={{ x: '1000', y: 1100 }}
                className="trials-table"
                key="trials-table"
                rowSelection={{
                  type: 'checkbox',
                }}
                columns={columns}
                dataSource={parsedResults}
                size="small"
              />
            </Col>
          </Row>
        </Card>
      </div>
    );
  }
}

ListViewTable.propTypes = {
  history: PropTypes.object.isRequired,
};

export default withRouter(ListViewTable);
