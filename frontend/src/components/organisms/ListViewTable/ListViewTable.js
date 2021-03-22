import React from 'react';
import {
  Table, Space, Button, Row, Col,
} from 'antd';
import {
  GlobalOutlined, TableOutlined, BarChartOutlined, DownloadOutlined,
} from '@ant-design/icons';
import { v4 as uuidv4 } from 'uuid';

import FacetedSearchGroup from '../../molecules/FacetedSearchGroup/FacetedSearchGroup';

import {
  recruitment, access, phases,
} from '../../../variables/TopLevelSearchData';

import { columns, data } from './ListViewTableConfig';
import './ListViewTable.css';

const ListViewTable = () => {
  return (
    <div>
      <Row
        key={uuidv4()}
        gutter={{
          xs: 8,
          sm: 12,
          md: 12,
          lg: 12,
        }}
      >
        <Col key={uuidv4()} className="gutter-row" span={4}>
          <FacetedSearchGroup
            access={access}
            recruitment={recruitment}
            phases={phases}
          />
        </Col>
        <Col key={uuidv4()} className="gutter-row" span={20}>
          <Table
            rowSelection={{
              type: 'checkbox',
            }}
            columns={columns}
            dataSource={data}
            bordered
            size="small"
            title={() => {
              return (
                <Space align="end">
                  <Button key={uuidv4()} icon={<BarChartOutlined />} size="large" />
                  <Button key={uuidv4()} icon={<TableOutlined />} size="large" />
                  <Button key={uuidv4()} icon={<GlobalOutlined />} size="large" />
                  <Button key={uuidv4()} icon={<DownloadOutlined />} size="large" className="float-right" />
                </Space>
              );
            }}
          />
        </Col>
      </Row>
    </div>
  );
};

export default ListViewTable;
