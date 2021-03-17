import React, { Component } from 'react';
import { Checkbox as AntCheckbox } from 'antd';
import PropTypes from 'prop-types';

class Checkbox extends Component {
  render() {
    const { value } = this.props;
    return (
      <AntCheckbox value={value} style={{ lineHeight: '32px' }}>
        {value}
      </AntCheckbox>
    );
  }
}

Checkbox.propTypes = {
  value: PropTypes.string.isRequired,
};


export default Checkbox;
