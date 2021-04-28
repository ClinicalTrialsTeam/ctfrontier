import React from 'react';
import { Column } from '@ant-design/charts';
import PropTypes from 'prop-types';

const DashboardPhasesChart = (props) => {
  const {
    data,
  } = props;

  const na = {
    study_phase: 'Not Applicable',
    trials_count: 0,
  };

  for (let i = data.length - 1; i >= 0; i--) {
    if (!data[i].study_phase || data[i].study_phase === 'N/A') {
      na.trials_count += data[i].trials_count;
      data.splice(i, 1);
    }
  }

  data.push(na);

  return (
    <>
      <Column
        data={data}
        height={300}
        xField="study_phase"
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
        color="#866BCE"
      />
    </>
  );
};

DashboardPhasesChart.propTypes = {
  data: PropTypes.object.isRequired,
};

export default DashboardPhasesChart;
