import React, { Component } from 'react';
import { InfoCircleOutlined } from '@ant-design/icons';
import { Form, Select } from 'antd';
import PropTypes from 'prop-types';

class SelectField extends Component {
  render() {
    const {
      searchValue,
      isDisabled,
      mode,
      name,
      label,
      title,
      placeholder,
      options,
      handleInputChange,
    } = this.props;
    return (
      <Form.Item
        name={name}
        label={label}
        tooltip={{
          title,
          icon: <InfoCircleOutlined />,
        }}
      >
        <Select
          searchValue={searchValue}
          disabled={isDisabled}
          mode={mode}
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
  // eslint-disable-next-line react/require-default-props
  mode: PropTypes.string,
  searchValue: PropTypes.string,
  isDisabled: PropTypes.bool,
  name: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  placeholder: PropTypes.string.isRequired,
  options: PropTypes.array.isRequired,
  handleInputChange: PropTypes.func.isRequired,
};

SelectField.defaultProps = {
  isDisabled: false,
  searchValue: '',
};

export default SelectField;
