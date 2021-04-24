import React from 'react';
import { Column } from '@ant-design/charts';

const DashboardStatusChart = () => {
  // Generating some dummy data
  const myData = [
    { status: 'Not yet recruiting', trials: 36 },
    { status: 'Recruiting', trials: 173 },
    { status: 'Enrolling by invitation', trials: 11 },
    { status: 'Active, not recruiting', trials: 51 },
    { status: 'Suspended', trials: 1 },
    { status: 'Terminated', trials: 57 },
    { status: 'Completed', trials: 595 },
    { status: 'Withdrawn', trials: 34 },
    { status: 'Unknown status', trials: 58 },
  ];

  return (
    <>
      <Column
        data={myData}
        height={300}
        xField="status"
        yField="trials"
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

export default DashboardStatusChart;
