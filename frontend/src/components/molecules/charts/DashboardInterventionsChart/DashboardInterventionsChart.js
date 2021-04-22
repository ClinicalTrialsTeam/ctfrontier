import React from 'react';
import { Column } from '@ant-design/charts';

const DashboardInterventionsChart = () => {
  // Generating some dummy data
  const myData = [
    { intervention: 'Drug', trials: 675 },
    { intervention: 'Biological', trials: 2 },
    { intervention: 'Device', trials: 238 },
    { intervention: 'Dietary Supplement', trials: 110 },
    { intervention: 'Genetic', trials: 275 },
    { intervention: 'Procedure', trials: 134 },
    { intervention: 'Radiation', trials: 24 },
    { intervention: 'Behavioral', trials: 0 },
    { intervention: 'Diagnostic Test', trials: 26 },
    { intervention: 'Combination Product', trials: 3 },
    { intervention: 'None', trials: 56 },
    { intervention: 'Other', trials: 78 },
  ];

  return (
    <>
      <Column
        data={myData}
        height={300}
        xField="intervention"
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
        color="#1890FF"
      />
    </>
  );
};

export default DashboardInterventionsChart;
