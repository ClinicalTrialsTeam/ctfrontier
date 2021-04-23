import React, { Component } from 'react';
import { Card } from 'antd';
import SingleTrialDisplay from '../../organisms/SingleTrialDisplay/SingleTrialDisplay';

import './SingleTrialView.css';

class SingleTrialView extends Component {
  render() {
    return (
      <Card id="nct-card">
        <SingleTrialDisplay />
      </Card>
    );
  }
}

export default SingleTrialView;
