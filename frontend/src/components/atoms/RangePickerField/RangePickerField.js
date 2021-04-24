import React, { Component } from 'react';
import { InfoCircleOutlined } from '@ant-design/icons';
import { Form, DatePicker } from 'antd';
import PropTypes from 'prop-types';

const { RangePicker } = DatePicker;

class RangePickerField extends Component {
  render() {
    const {
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
      >
        <RangePicker onChange={handleInputChange} />
      </Form.Item>
    );
  }
}

RangePickerField.propTypes = {
  label: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  handleInputChange: PropTypes.func.isRequired,
};

export default RangePickerField;
