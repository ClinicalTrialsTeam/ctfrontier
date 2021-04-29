/* eslint-disable no-param-reassign */
import React from 'react';
import { Column } from '@ant-design/charts';
import PropTypes from 'prop-types';

const DashboardSponsorsChart = (props) => {
  const {
    data,
  } = props;

  const contractions = ['NIAID', 'Novartis', 'NHLBI', 'Eli Lilly', 'Regeneron', 'M.D. Anderson', 'Merck', 'Incyte', 'Northwestern Uni', 'NCI'];

  data.forEach((element) => {
    contractions.forEach((contraction) => {
      if (element.name.includes(contraction)) {
        element.name = contraction;
      }
    });
  });

  return (
    <>
      <Column
        data={data}
        height={300}
        xField="name"
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
            offset: 25,
          },
        }}
        color="#677DE9"
      />
    </>
  );
};

DashboardSponsorsChart.propTypes = {
  data: PropTypes.object.isRequired,
};

export default DashboardSponsorsChart;
