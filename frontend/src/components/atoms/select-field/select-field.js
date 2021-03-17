import React, { Component } from 'react';
import { InfoCircleOutlined } from '@ant-design/icons';
import { Form, Input, Select } from 'antd';
import PropTypes from 'prop-types';

class SelectField extends Component {
  render() {
    const {
      name,
      label,
      tooltip,
      placeholder,
      options,
      handleInputChange,
    } = this.props;
    return (
      <Form.Item
        name={name}
        label={label}
        tooltip={{
          title: {tooltip},
          icon: <InfoCircleOutlined />,
        }}
      >
        <Select
          placeholder={placeholder}
          allowClear
          onChange={handleInputChange}
        >
          {options}
        </Select>
      </Form.Item>
    );
  }
}

SelectField.propTypes = {
  name: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  tooltip: PropTypes.string.isRequired,
  placeholder: PropTypes.string.isRequired,
  options:PropTypes.array.isRequired,
  handleInputChange: PropTypes.func.isRequired,
};

export default SelectField;
