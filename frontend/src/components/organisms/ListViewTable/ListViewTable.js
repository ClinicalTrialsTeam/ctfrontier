import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import {
  Table, Space, Button, Row, Col, Card, Tooltip, Typography, Pagination,
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

const parsedResults = (data) => {
  return data.search_results.map((result) => {
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
};

class ListViewTable extends Component {
  constructor(props) {
    super(props);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.setDashboardModalVisible = this.setDashboardModalVisible.bind(this);
    this.setTimelineModalVisible = this.setTimelineModalVisible.bind(this);
    this.setDownloadModalVisible = this.setDownloadModalVisible.bind(this);
    this.handleSearch = this.handleSearch.bind(this);
    this.handleClear = this.handleClear.bind(this);
    this.formRef = React.createRef();
    this.facetsRef = React.createRef();
    this.state = {
      currentPage: 1,
      intervention: '',
      condition: '',
      target: '',
      otherTerms: '',
      isDashboardModalVisible: false,
      isTimelineModalVisible: false,
      isDownloadModalVisible: false,
      isDashboardDisabled: true,
      isTimelineDisabled: true,
      isDownloadDisabled: true,
      payload: this.props.history.location.state.payload,
      // searchData: this.props.history.location.state.data,
      dashboardData: {},
      exportData: {},
      timelineData: {},
      resultsByPage: {},
      studyCount: '...',
    };

    const { data } = this.props.history.location.state;
    this.state.resultsByPage = { 1: parsedResults(data) };
  }

  async componentDidMount() {
    const { payload } = this.state;
    payload.metadata_required = true;
    // Getting metadata (total results count)
    try {
      const response = await ctgov.post('search_studies', payload);
      const studyCount = response.data.metadata[0].results_count;
      this.setState({
        studyCount,
      });
    } catch (err) {
      log.error(err);
      this.setState({
        studyCount: '0',
      });
    }
    // Getting dashboard and timeline data
    try {
      const dashboardResponse = await ctgov.post('trials_dashboard', payload);
      this.setState({
        dashboardData: dashboardResponse.data,
        isDashboardDisabled: false,
      });
      const timelinePayload = {
        nct_ids: dashboardResponse.data.nct_ids,
      };
      const timelineResponse = await ctgov.post('trial_timelines', timelinePayload);
      this.setState({
        timelineData: timelineResponse.data,
        isTimelineDisabled: false,
      });
    } catch (err) {
      log.error(err);
    }
    // Getting export data
    try {
      const exportResponse = await ctgov.post('search_results_export', payload);
      console.log(exportResponse.data);
      this.setState({
        exportData: exportResponse.data,
        isDownloadDisabled: false,
      });
    } catch (err) {
      log.error(err);
    }
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
    const value = target.inputType === 'checkbox' ? target.checked : target.value;
    const { name } = target;

    this.setState({
      [name]: value,
    });
  }

  async handlePagination(page, pageSize) {
    if (page in this.state.resultsByPage) {
      this.setState({
        currentPage: page,
      });
    } else {
      try {
        const newPayload = this.state.payload;
        newPayload.last = (page * pageSize);
        newPayload.first = newPayload.last - pageSize + 1;
        newPayload.metadata_required = false;
        const response = await ctgov.post('search_studies', newPayload);
        log.info(response.data);
        this.setState((prevState) => {
          return ({
            currentPage: page,
            payload: newPayload,
            resultsByPage: {
              ...prevState.resultsByPage,
              [page]: parsedResults(response.data),
            },
          });
        });
      } catch (err) {
        log.error(err);
      }
    }
  }

  async handleSearch() {
    const payload = {
      status: '',
      condition: this.state.condition,
      other_terms: this.state.otherTerms,
      intervention: this.state.intervention,
      target: this.state.target,
      nct_id: this.state.nct_id,
      eligibility_criteria: '',
      first: '',
      last: '',
    };
    try {
      const response = await ctgov.post('search_studies', payload);
      log.info(response.data);
    } catch (err) {
      log.error(err);
    }
  }

  async setDashboardModalVisible(isDashboardModalVisible) {
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
              href={'./' + nctId}
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
    const dataCount = parseInt(this.state.studyCount);

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
                <Button
                  type="primary"
                  key="fs-button-submit"
                  className="facet-button"
                >
                  Apply
                </Button>
                <Button key="fs-button-clear" className="facet-button">
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
                />
              </div>
            </Col>
            <Col key="trails_table-col" className="gutter-row" span={20}>
              <Row key="trials-table-extras">
                <Col key="trials-stat-col" span={8}>
                  <Row id="trials-stat-row" justify="start" align="middle">
                    Total number of trials:
                    {' '}
                    {this.state.studyCount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')}
                  </Row>
                </Col>
                <Col key="trials-modal-btn-col" span={16}>
                  <Row id="trials-modal-btn-row" justify="end">
                    <Space align="end">
                      <Tooltip title="View dashboard">
                        <Button
                          disabled={this.state.isDashboardDisabled}
                          loading={this.state.isDashboardDisabled}
                          key="btn_dashboard"
                          onClick={() => {
                            return this.setDashboardModalVisible(true);
                          }}
                          icon={<BarChartOutlined />}
                        />
                      </Tooltip>
                      <Tooltip title="View timeline">
                        <Button
                          disabled={this.state.isTimelineDisabled}
                          loading={this.state.isTimelineDisabled}
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
                        count={this.state.studyCount}
                        handleOk={() => {
                          return this.setDashboardModalVisible(false, '');
                        }}
                        handleCancel={() => {
                          return this.setDashboardModalVisible(false, '');
                        }}
                      />
                      <TimelineModal
                        isModalVisible={this.state.isTimelineModalVisible}
                        data={this.state.timelineData}
                        handleOk={() => {
                          return this.setTimelineModalVisible(false, '');
                        }}
                        handleCancel={() => {
                          return this.setTimelineModalVisible(false, '');
                        }}
                      />
                      <DownloadModal
                        isModalVisible={this.state.isDownloadModalVisible}
                        isDownloading={this.state.isDownloadDisabled}
                        data={this.state.exportData}
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
                pagination={false}
                scroll={{ x: '1000', y: 1100 }}
                className="trials-table"
                key="trials-table"
                rowSelection={{
                  type: 'checkbox',
                }}
                columns={columns}
                dataSource={this.state.resultsByPage[this.state.currentPage]}
                size="small"
              />
              <Pagination
                className="trials-pagination"
                onChange={(page, pageSize) => {
                  return this.handlePagination(page, pageSize);
                }}
                current={this.state.currentPage}
                pageSize={20}
                total={dataCount}
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
