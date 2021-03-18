import React, { Component } from 'react';
import { Checkbox, Form, Row } from 'antd';
import PropTypes from 'prop-types';

class CheckBoxGroup extends Component {
  render() {
    const { checkboxes } = this.props;

    return (
      <Form.Item
        name="checkbox-group"
      >
        <Checkbox.Group>
          <Row>
            {checkboxes.map( (value) =>
              <Checkbox
                value={value}
              />
            )}
          </Row>
        </Checkbox.Group>
      </Form.Item>
        );
  }
}


        CheckBoxGroup.propTypes = {
  checkboxes: PropTypes.array.isRequired,
};

CheckBoxGroup.propTypes = {
  value: PropTypes.array.isRequired,
};

export default CheckBoxGroup;
