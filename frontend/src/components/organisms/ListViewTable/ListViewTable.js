import React from 'react';
import {
  Table, Space, Button, Row, Col,
} from 'antd';
import {
  GlobalOutlined, TableOutlined, BarChartOutlined, DownloadOutlined,
} from '@ant-design/icons';

import FacetedSearchGroup from '../../molecules/FacetedSearchGroup/FacetedSearchGroup';

import {
  recruitment, access, phases,
} from '../../../variables/TopLevelSearchData';

import { columns, data } from './ListViewTableConfig';
import './ListViewTable.css';

const rowSelection = {
  onChange: (selectedRowKeys, selectedRows) => {
    console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
  },
  getCheckboxProps: (record) => {
    return {
      name: record.name,
    };
  },
};

const ListViewTable = () => {
  return (
    <div>
      <Row gutter={{
        xs: 8,
        sm: 12,
        md: 12,
        lg: 12,
      }}
      >
        <Col className="gutter-row" span={4}>
          <FacetedSearchGroup
            access={access}
            recruitment={recruitment}
            phases={phases}
          />
        </Col>
        <Col className="gutter-row" span={20}>
          <Table
            rowSelection={{
              type: 'checkbox',
              ...rowSelection,
            }}
            columns={columns}
            dataSource={data}
            bordered
            size="small"
            title={() => {
              return (
                <Space align="end">
                  <Button icon={<BarChartOutlined />} size="large" />
                  <Button icon={<TableOutlined />} size="large" />
                  <Button icon={<GlobalOutlined />} size="large" />
                  <Button icon={<DownloadOutlined />} size="large" className="float-right" />
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
