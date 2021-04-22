import React from 'react';
import { Column } from '@ant-design/charts';

const DashboardSponsorsChart = () => {
  // Generating some dummy data
  const myData = [
    { sponsor: 'NCI', trials: 123 },
    { sponsor: 'GlaxoSmithKline', trials: 45 },
    { sponsor: 'Pfizer', trials: 40 },
    { sponsor: 'Merck', trials: 38 },
    { sponsor: 'AstraZeneca', trials: 36 },
    { sponsor: 'NHLBI', trials: 33 },
    { sponsor: 'NIAID', trials: 29 },
    { sponsor: 'Mayo Clinic', trials: 25 },
    { sponsor: 'M.D. Anderson', trials: 25 },
    { sponsor: 'Novartis', trials: 24 },
  ];

  return (
    <>
      <Column
        data={myData}
        height={300}
        xField="sponsor"
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
            offset: 25,
          },
        }}
        color="#677DE9"
      />
    </>
  );
};

export default DashboardSponsorsChart;
