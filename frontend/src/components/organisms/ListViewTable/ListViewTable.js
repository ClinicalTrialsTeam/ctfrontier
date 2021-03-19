import React from 'react';
import {
  Table, Space, Button, Row, Col, Collapse,
} from 'antd';
import {
  GlobalOutlined, TableOutlined, BarChartOutlined, DownloadOutlined,
} from '@ant-design/icons';

import { columns, data } from './ListViewTableConfig';
import './ListViewTable.css';

const rowSelection = {
  onChange: (selectedRowKeys, selectedRows) => {
    console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
  },
  getCheckboxProps: (record) => {
    return {
      disabled: record.name === 'Disabled User',
      // Column configuration not to be checked
      name: record.name,
    };
  },
};

const { Panel } = Collapse;

const ListViewTable = () => {
  return (
    <div>
      <Row gutter={{
        xs: 8,
        sm: 16,
        md: 16,
        lg: 24,
      }}
      >
        <Col className="gutter-row" span={4}>
          <Collapse>
            <Panel header="Status" key="1">
              <p>Data</p>
            </Panel>
            <Panel header="Phase" key="2">
              <p>Data</p>
            </Panel>
            <Panel header="Administration" key="3">
              <p>Data</p>
            </Panel>
            <Panel header="Target" key="4">
              <p>Data</p>
            </Panel>
            <Panel header="Modality" key="5">
              <p>Data</p>
            </Panel>
            <Panel header="No. of patients" key="6">
              <p>Data</p>
            </Panel>
            <Panel header="Sponsor" key="7">
              <p>Data</p>
            </Panel>
            <Panel header="Sponsor Type" key="8" style={{ marginBottom: 24 }}>
              <p>Data</p>
            </Panel>
          </Collapse>
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
