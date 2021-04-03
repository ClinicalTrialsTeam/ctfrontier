/* eslint-disable react/require-default-props */
import React, { Component } from 'react';
import { InfoCircleOutlined } from '@ant-design/icons';
import { Form, InputNumber } from 'antd';
import PropTypes from 'prop-types';

import './NumberInputField.css';

class NumberInputField extends Component {
  render() {
    const {
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
  label: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  handleInputChange: PropTypes.func.isRequired,
};

export default NumberInputField;
