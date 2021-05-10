import React, { Component } from 'react';
import { Bar } from '@ant-design/charts';
import PropTypes from 'prop-types';

class TimelineChart extends Component {
  render() {
    function search(nameKey, myArray) {
      const tempArray = [];
      for (let i = 0; i < myArray.length; i++) {
        if (myArray[i].nct_id === nameKey) {
          tempArray.push(myArray[i].brief_title);
          tempArray.push(myArray[i].phase);
          tempArray.push(myArray[i].start_date);
          tempArray.push(myArray[i].completion_date);
          tempArray.push(myArray[i].sponsor);
          tempArray.push(myArray[i].status);
        }
      }
      return tempArray;
    }
    const {
      data,
    } = this.props;

    console.log(data);

    let minDate = '2040-01-01';
    let maxDate = '1970-01-01';
    const timelineData = [];

    data.forEach((element) => {
      const startDate = element.study_start_date;
      if (startDate < minDate) {
        minDate = startDate;
      }
      const endDate = element.primary_completion_date;
      if (endDate > maxDate) {
        maxDate = endDate;
      }
    });

    data.forEach((element) => {
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
        brief_title: element.brief_title,
        status: element.status,
        start_date: (!element.study_start_date) ? 'unknown' : element.study_start_date,
        completion_date: (!element.primary_completion_date) ? 'unknown' : element.primary_completion_date,
        sponsor: element.sponsor_name,
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
          data={timelineData}
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
          tooltip={{
            position: 'bottom',
            customContent: (title) => {
              const resultObject = search(title, timelineData);
              const briefTitle = resultObject[0];
              const phase = resultObject[1];
              const startDate = resultObject[2];
              const completionDate = resultObject[3];
              const sponsor = resultObject[4];
              const status = resultObject[5];
              return (
                <div width="100px">
                  <br />
                  <p><b>{title}</b></p>
                  <p>
                    <b>Title: </b>
                    {briefTitle}
                  </p>
                  <p>
                    <b>Phase: </b>
                    {phase}
                  </p>
                  <p>
                    <b>Dates: </b>
                    {' from '}
                    {startDate}
                    {' to '}
                    {completionDate}
                  </p>
                  <p>
                    <b>Sponsor: </b>
                    {sponsor}
                  </p>
                  <p>
                    <b>Status: </b>
                    {status}
                  </p>
                </div>
              );
            },
          }}
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
