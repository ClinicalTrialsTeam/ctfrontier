import React, { Component } from 'react';
import { Button as AntButton } from 'antd';
import PropTypes from 'prop-types';

class Button extends Component {
  render() {
    const {
      inputType, text, loading, clickHandler, disabled,
    } = this.props;
    return (
      <AntButton type={inputType} onClick={clickHandler} loading={loading} disabled={disabled}>
        {text}
      </AntButton>
    );
  }
}

Button.propTypes = {
  inputType: PropTypes.string,
  text: PropTypes.string.isRequired,
  loading: PropTypes.bool,
  disabled: PropTypes.bool,
  clickHandler: PropTypes.func.isRequired,
};

Button.defaultProps = {
  inputType: 'default',
  loading: false,
  disabled: false,
};

export default Button;
