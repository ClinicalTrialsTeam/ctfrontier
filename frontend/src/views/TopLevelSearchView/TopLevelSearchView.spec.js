import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import { Layout } from 'antd';

import Adapter from '@wojtekmaj/enzyme-adapter-react-17';

import TopLevelSearchView from './TopLevelSearchView';

// Configure adapter
Enzyme.configure({ adapter: new Adapter() });

describe('src > views > TopLevelSearchView', () => {
  it('should render without throwing an error', async () => {
    expect(
      shallow(<TopLevelSearchView />).contains(<Layout className="layout" />)
    );
  });
});
