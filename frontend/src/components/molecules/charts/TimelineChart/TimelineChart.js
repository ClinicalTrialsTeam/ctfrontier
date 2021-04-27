import React, { Component } from 'react';
import { Bar } from '@ant-design/charts';
import PropTypes from 'prop-types';

// import {
//   timelineData,
// } from '../../../../variables/DummyVizData';

class TimelineChart extends Component {
  render() {
    const {
      data,
    } = this.props;

    let minDate = '2040-01-01';
    let maxDate = '1970-01-01';
    const timelineData = [];

    data.search_results.forEach((element) => {
      const startDate = element.study_start_date;
      if (startDate < minDate) {
        minDate = startDate;
      }
      const endDate = element.primary_completion_date;
      if (endDate > maxDate) {
        maxDate = endDate;
      }
    });

    data.search_results.forEach((element) => {
      let elementStartDate;
      if (!element.study_start_date) {
        elementStartDate = minDate;
      } else {
        elementStartDate = element.study_start_date;
      }
      let elementEndDate;
      if (!element.primary_completion_date) {
        elementEndDate = maxDate;
      } else {
        elementEndDate = element.primary_completion_date;
      }
      timelineData.push({
        nct_id: element.nct_id,
        dates: [elementStartDate, elementEndDate],
        phase: element.study_phase,
      });
    });

    const config = {
      color: function color(_ref) {
        const { phase } = _ref;
        if (phase === 'Early Phase 1') {
          return '#17EAD9';
        }
        if (phase === 'Phase 1') {
          return '#00c4ff';
        }
        if (phase === 'Phase 1/Phase 2') {
          return '#1890FF';
        }
        if (phase === 'Phase 2') {
          return '#677DE9';
        }
        if (phase === 'Phase 2/Phase 3') {
          return '#756EED';
        }
        if (phase === 'Phase 3') {
          return '#A73EC7';
        }
        if (phase === 'Phase 4') {
          return '#c91e93';
        }
        if (phase === 'Not Applicable') {
          return '#414756';
        }
        return '#bfbfbf';
      },
      minDate,
      maxDate,
    };

    return (
      <>
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
            min: config.minDate,
            max: config.maxDate,
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
