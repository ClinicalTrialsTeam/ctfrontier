import React, { Component } from 'react';
import { Button as AntButton } from 'antd';
import PropTypes from 'prop-types';

class Button extends Component {
  render() {
    const { type, text, clickHandler } = this.props;
    return (
      <AntButton type={type} onClick={clickHandler}>
        {text}
      </AntButton>
    );
  }
}

Button.propTypes = {
  type: PropTypes.string.isRequired,
  text: PropTypes.string.isRequired,
  clickHandler: PropTypes.func.isRequired,
};

Button.defaultProps = {
  type: 'default',
};

export default Button;
