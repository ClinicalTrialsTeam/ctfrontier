import React, { Component } from 'react';
import { Bar } from '@ant-design/charts';
import PropTypes from 'prop-types';

import {
  timelineData,
} from '../../../../variables/DummyVizData';

class TimelineChart extends Component {
  render() {
    const {
      data,
    } = this.props;

    const config = {
      color: function color(_ref) {
        const { phase } = _ref;
        if (phase === 'Early Phase 1') {
          return '#0072DD';
        }
        if (phase === 'Phase 1') {
          return '#1890FF';
        }
        if (phase === 'Phase 1 Phase 2') {
          return '#677DE9';
        }
        if (phase === 'Phase 2') {
          return '#866BCE';
        }
        if (phase === 'Phase 2 Phase 3') {
          return '#9759B1';
        }
        if (phase === 'Phase 3') {
          return '#9E4994';
        }
        if (phase === 'Phase 4') {
          return '#9D3B77';
        }
        if (phase === 'Not Applicable') {
          return '#414756';
        }
        return '#bfbfbf';
      },
    };

    return (
      <>
        <p>{data}</p>
        <Bar
          data={timelineData.reverse()}
          color={config.color}
          xField="dates"
          yField="nct_id"
          seriesField="phase"
          maxBarWidth={10}
          barStyle={{ radius: [4, 4, 4, 4] }}
          xAxis={{
            type: 'time',
            mask: 'YYYY-MM-DD',
            min: '2017-01-29',
          }}
          height={300}
          isRange
          scrollbar={{
            type: 'vertical',
          }}
          legend={{
            position: 'top-left',
          }}
        />
      </>
    );
  }
}

TimelineChart.propTypes = {
  data: PropTypes.array.isRequired,
};

export default TimelineChart;
