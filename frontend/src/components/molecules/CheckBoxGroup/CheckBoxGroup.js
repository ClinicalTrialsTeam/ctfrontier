import React, { Component } from 'react';
import { InfoCircleOutlined } from '@ant-design/icons';
import { Form, Space } from 'antd';
import PropTypes from 'prop-types';

class CheckBoxGroup extends Component {
  render() {
    const {
      checkboxes,
      name,
      label,
      title,
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
        <Space direction="vertical" size="4">
          {checkboxes}
        </Space>
      </Form.Item>
    );
  }
}

CheckBoxGroup.propTypes = {
  name: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  checkboxes: PropTypes.array.isRequired,
};

export default CheckBoxGroup;
