import React, { Component } from 'react';
import { InfoCircleOutlined } from '@ant-design/icons';
import { Form, InputNumber } from 'antd';
import PropTypes from 'prop-types';

import './NumberInputField.css';

class NumberInputField extends Component {
  render() {
    const {
      size,
      max,
      min,
      label,
      title,
      name,
      handleInputChange,
    } = this.props;
    return (
      <Form.Item
        label={label}
        name={name}
        tooltip={{
          title,
          icon: <InfoCircleOutlined />,
        }}
        onChange={handleInputChange}
      >
        <InputNumber
          size={size}
          max={max}
          min={min}
        />
      </Form.Item>
    );
  }
}

NumberInputField.propTypes = {
  max: PropTypes.number,
  min: PropTypes.number,
  size: PropTypes.string,
  label: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  handleInputChange: PropTypes.func.isRequired,
};

NumberInputField.defaultProps = {
  max: 1000000,
  min: 0,
  size: 'middle',
};

export default NumberInputField;
