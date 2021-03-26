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
  recruitment, access, phases,
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
            <Space>
              <Button key="fs-button-submit" className="facet-button" size="large">
                Update
              </Button>
              <Button key="fs-button-clear" className="facet-button" size="large">
                Clear
              </Button>
            </Space>
            <FacetedSearchGroup
              access={access}
              recruitment={recruitment}
              phases={phases}
            />
          </Col>
          <Col key="trails_table-col" className="gutter-row" span={20}>
            <Table
              className="trials-table"
              key="trials-table"
              rowSelection={{
                type: 'checkbox',
              }}
              columns={columns}
              dataSource={parsedResults}
              size="small"
              title={() => {
                return (
                  <Space align="end">
                    <Button key="btn_dashboard" icon={<BarChartOutlined />} size="large" />
                    <Button key="btn_other" icon={<TableOutlined />} size="large" />
                    <Button key="btn_map" icon={<GlobalOutlined />} size="large" />
                    <Button key="btn_download" icon={<DownloadOutlined />} size="large" className="float-right" />
                  </Space>
                );
              }}
            />
          </Col>
        </Row>
      </Card>
    </div>
  );
};

export default ListViewTable;
