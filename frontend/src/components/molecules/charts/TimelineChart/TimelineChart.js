import React, { Component } from 'react';
import { Bar } from '@antv/g2plot';
import PropTypes from 'prop-types';

import {
  timelineData,
} from '../../../../variables/DummyVizData';

class TimelineChart extends Component {
  render() {
    const {
      data,
    } = this.props;

    return (
      <>
        <p>{data}</p>
        <Bar
          data={timelineData}
          xField="values"
          yField="nct_id"
          isRange
          label={{
            position: 'middle',
            layout: [{ type: 'adjust-color' }],
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
