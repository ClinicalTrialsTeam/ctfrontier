import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import { Layout } from 'antd';

import Adapter from '@wojtekmaj/enzyme-adapter-react-17';

import SearchView from './SearchView';

// Configure adapter
Enzyme.configure({ adapter: new Adapter() });

describe('src > views > SearchView', () => {
  it('should render without throwing an error', async () => {
    expect(
      shallow(<SearchView />).contains(<Layout className="layout" />)
    );
  });
});
