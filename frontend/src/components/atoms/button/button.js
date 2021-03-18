import React, { Component } from 'react';
import { Button as AntButton } from 'antd';
import PropTypes from 'prop-types';

class Button extends Component {
  render() {
    const { inputType, text, clickHandler } = this.props;
    return (
      <AntButton type={inputType} onClick={clickHandler}>
        {text}
      </AntButton>
    );
  }
}

Button.propTypes = {
  inputType: PropTypes.string,
  text: PropTypes.string.isRequired,
  clickHandler: PropTypes.func.isRequired,
};

Button.defaultProps = {
  inputType: 'default',
};

export default Button;
