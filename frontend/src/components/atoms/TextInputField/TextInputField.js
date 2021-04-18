import React, { Component } from 'react';
import { InfoCircleOutlined } from '@ant-design/icons';
import { Form, Input } from 'antd';
import PropTypes from 'prop-types';

class TextInputField extends Component {
  render() {
    const {
      isDisabled, label, title, name, handleInputChange,
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
        <Input
          disabled={isDisabled}
          allowClear
          name={name}
        />
      </Form.Item>
    );
  }
}

TextInputField.propTypes = {
  isDisabled: PropTypes.bool,
  label: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  handleInputChange: PropTypes.func.isRequired,
};

TextInputField.defaultProps = {
  isDisabled: false,
};

export default TextInputField;
