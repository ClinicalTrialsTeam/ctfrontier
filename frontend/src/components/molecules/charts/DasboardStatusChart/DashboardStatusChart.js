import React from 'react';
import { Column } from '@ant-design/charts';
import PropTypes from 'prop-types';

const DashboardStatusChart = (props) => {
  const {
    data,
  } = props;

  return (
    <>
      <Column
        data={data}
        height={300}
        xField="status"
        yField="trials_count"
        maxColumnWidth={40}
        columnStyle={{ radius: [4, 4, 0, 0] }}
        label={{
          position: 'middle',
          style: {
            fill: '#FFFFFF',
            opacity: 0.6,
          },
        }}
        xAxis={{
          label: {
            rotate: Math.PI / 6,
            offset: 30,
          },
        }}
        color="#9759B1"
      />
    </>
  );
};

DashboardStatusChart.propTypes = {
  data: PropTypes.object.isRequired,
};

export default DashboardStatusChart;
