import React from 'react';
import { useLocation } from 'react-router-dom';
import {
  Table, Space, Button, Row, Col, Card,
} from 'antd';
import {
  GlobalOutlined, TableOutlined, BarChartOutlined, DownloadOutlined,
} from '@ant-design/icons';

import FacetedSearchGroup from '../../molecules/FacetedSearchGroup/FacetedSearchGroup';

import {
  recruitment, access, phases, roa,
} from '../../../variables/TopLevelSearchData';

import { columns } from './ListViewTableConfig';
import './ListViewTable.css';

const ListViewTable = () => {
  const location = useLocation();
  const parsedResults = location.state.data.map((result) => {
    return {
      key: result.nct_id,
      nct_id: result.nct_id,
      brief_title: result.brief_title,
      condition_name: result.condition_name !== null ? result.condition_name.split('|').join(', ') : '',
      intervention_name: result.intervention_name !== null ? result.intervention_name.split('|').join(', ') : '',
      status: result.status,
    };
  });

  return (
    <div>
      <Card>
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
              <Button key="fs-button-submit" className="facet-button">
                Update
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
            />
          </Col>
          <Col key="trails_table-col" className="gutter-row" span={20}>
            <Row key="trials-table-extras">
              <Col key="trials-stat-col" span={8}>
                <Row id="trials-stat-row" justify="start" align="middle">
                  Total number of trials: 512
                </Row>
              </Col>
              <Col key="trials-modal-btn-col" span={16}>
                <Row id="trials-modal-btn-row" justify="end">
                  <Space align="end">
                    <Button key="btn_dashboard" icon={<BarChartOutlined />} />
                    <Button key="btn_other" icon={<TableOutlined />} />
                    <Button key="btn_map" icon={<GlobalOutlined />} />
                    <Button key="btn_download" icon={<DownloadOutlined />} />
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
};

export default ListViewTable;
