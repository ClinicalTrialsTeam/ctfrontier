import React from 'react';
import { Column } from '@ant-design/charts';

const DashboardPhasesChart = () => {
  // Generating some dummy data
  const myData = [
    { phase: 'Early Phase 1', trials: 11 },
    { phase: 'Phase 1', trials: 133 },
    { phase: 'Phase 1 Phase 2', trials: 385 },
    { phase: 'Phase 2', trials: 288 },
    { phase: 'Phase 2 Phase 3', trials: 433 },
    { phase: 'Phase 3', trials: 153 },
    { phase: 'Phase 4', trials: 103 },
    { phase: 'Not Applicable', trials: 209 },
  ];

  return (
    <>
      <Column
        data={myData}
        height={300}
        xField="phase"
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
        color="#866BCE"
      />
    </>
  );
};

export default DashboardPhasesChart;
