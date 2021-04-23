import React, { Component } from 'react';
import { Button as AntButton } from 'antd';
import PropTypes from 'prop-types';

class Button extends Component {
  render() {
    const {
      inputType, text, loading, clickHandler,
    } = this.props;
    return (
      <AntButton type={inputType} onClick={clickHandler} loading={loading}>
        {text}
      </AntButton>
    );
  }
}

Button.propTypes = {
  inputType: PropTypes.string,
  text: PropTypes.string.isRequired,
  loading: PropTypes.bool,
  clickHandler: PropTypes.func.isRequired,
};

Button.defaultProps = {
  inputType: 'default',
  loading: false,
};

export default Button;
