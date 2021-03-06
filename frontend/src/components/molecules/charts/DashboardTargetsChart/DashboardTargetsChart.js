import React from 'react';
import { Column } from '@ant-design/charts';

const DashboardChart = () => {
  // Generating some dummy data
  const myData = [
    { sponsor: 'National Cancer Institute (NCI)', trials: 123 },
    { sponsor: 'GlaxoSmithKline', trials: 45 },
    { sponsor: 'Pfizer', trials: 40 },
    { sponsor: 'Merck Sharp & Dohme Corp.', trials: 38 },
    { sponsor: 'AstraZeneca', trials: 36 },
    { sponsor: 'National Heart, Lung, and Blood Institute (NHLBI)', trials: 33 },
    { sponsor: 'National Institute of Allergy and Infectious Diseases (NIAID)', trials: 29 },
    { sponsor: 'Mayo Clinic', trials: 25 },
    { sponsor: 'M.D. Anderson Cancer Center', trials: 25 },
    { sponsor: 'Novartis Pharmaceuticals', trials: 24 },
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
        color="#677DE9"
      />
    </>
  );
};

export default DashboardChart;
