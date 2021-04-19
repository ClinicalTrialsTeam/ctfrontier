import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import {
  Table, Space, Button, Row, Col, Card, Tooltip,
} from 'antd';
import PropTypes from 'prop-types';
import {
  AlignLeftOutlined, BarChartOutlined, DownloadOutlined,
} from '@ant-design/icons';
import ctgov from '../../../apis/ctgov';

import FacetedSearchGroup from '../../molecules/FacetedSearchGroup/FacetedSearchGroup';
import TrialModal from '../../molecules/TrialModal/TrialModal';

import {
  recruitment, access, phases, roa, results,
  types, sex, ageGroup, ethnicities, distance, states,
  funder, documents, submission,
} from '../../../variables/SelectOptionsData';

import { columns } from './ListViewTableConfig';
import './ListViewTable.css';

class ListViewTable extends Component {
  constructor(props) {
    super(props);
    this.handleInputChange = this.handleInputChange.bind(this);
    // this.setDashboardModalVisible = this.setDashboardModalVisible.bind(this);
    // this.setTimelineModalVisible = this.setTimelineModalVisible.bind(this);
    this.setModalVisible = this.setModalVisible.bind(this);
    this.handleSearch = this.handleSearch.bind(this);
    this.handleClear = this.handleClear.bind(this);
    this.formRef = React.createRef();
    this.state = {
      intervention: '',
      condition: '',
      target: '',
      otherTerms: '',
      // isDashboardModalVisible: false,
      // isTimelineModalVisible: false,
      isModalVisible: false,
      modalType: '',
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
    const value = target.inputType === 'checkbox' ? target.checked : target.value;
    const { name } = target;

    this.setState({
      [name]: value,
    });
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
      console.log(response.data);
    } catch (err) {
      console.log(err);
    }
  }

  // setDashboardModalVisible(isDashboardModalVisible) {
  //   this.setState({ isDashboardModalVisible });
  // }

  // setTimelineModalVisible(isTimelineModalVisible) {
  //   this.setState({ isTimelineModalVisible });
  // }

  setModalVisible(isModalVisible, type) {
    this.setState({
      isModalVisible,
      modalType: type,
    });
  }

  render() {
    const { data } = this.props.history.location.state;
    console.log(data);
    const parsedResults = data.search_results.map((result) => {
      return {
        key: result.nct_id,
        nct_id: result.nct_id,
        brief_title: result.brief_title,
        condition_name: result.condition_name
    !== null ? result.condition_name.split('|').join(', ') : '',
        intervention_name: result.intervention_name
    !== null ? result.intervention_name.split('|').join(', ') : '',
        status: result.status,
      };
    });
    const dataPlaceholder = [];

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
              <FacetedSearchGroup
                key="fs-group"
                access={access}
                recruitment={recruitment}
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
            </Col>
            <Col key="trails_table-col" className="gutter-row" span={20}>
              <Row key="trials-table-extras">
                <Col key="trials-stat-col" span={8}>
                  <Row id="trials-stat-row" justify="start" align="middle">
                    Total number of trials:
                    {' '}
                    {data.metadata[0].results_count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')}
                  </Row>
                </Col>
                <Col key="trials-modal-btn-col" span={16}>
                  <Row id="trials-modal-btn-row" justify="end">
                    <Space align="end">
                      <Tooltip title="View dashboard">
                        <Button
                          key="btn_dashboard"
                          onClick={() => {
                            return this.setModalVisible(true, 'Dashboard');
                          }}
                          icon={<BarChartOutlined />}
                        />
                      </Tooltip>
                      <Tooltip title="View timeline">
                        <Button
                          key="btn_timeline"
                          onClick={() => {
                            return this.setModalVisible(true, 'Timeline');
                          }}
                          icon={<AlignLeftOutlined />}
                        />
                      </Tooltip>
                      <Tooltip title="Download options">
                        <Button
                          key="btn_download"
                          onClick={() => {
                            return this.setModalVisible(true, 'Download');
                          }}
                          icon={<DownloadOutlined />}
                        />
                      </Tooltip>
                      <TrialModal
                        isModalVisible={this.state.isModalVisible}
                        type={this.state.modalType}
                        data={dataPlaceholder}
                        handleOk={() => {
                          return this.setModalVisible(false, '');
                        }}
                        handleCancel={() => {
                          return this.setModalVisible(false, '');
                        }}
                      />
                    </Space>
                  </Row>
                </Col>
              </Row>
              <Table
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
