import React, { Component } from 'react';
import { Form } from 'antd';
import ctgov from '../../../apis/ctgov';
import TextInputField from '../../atoms/TextInputField/TextInputField';
import SelectField from '../../atoms/SelectField/SelectField';
import Button from '../../atoms/button/button';
import BasicSearchAccordion from '../../molecules/BasicSearchAccordion/BasicSearchAccordion';

import './TopLevelSearchFormFields.css';

import {
  recruitment, access, countries,
} from '../../../variables/TopLevelSearchData';

class TopLevelSearchFormFields extends Component {
  constructor(props) {
    super(props);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleCountryChange = this.handleCountryChange.bind(this);
    this.handleSearch = this.handleSearch.bind(this);
    this.handleClear = this.handleClear.bind(this);
    this.state = {
      condition: '',
      target: '',
      country: '',
      otherTerms: '',
      displaySearchResults: false,
      searchResults: '',
    };
  }

  handleInputChange(e) {
    const { target } = e;
    const value = target.inputType === 'checkbox' ? target.checked : target.value;
    const { name } = target;

    this.setState({
      [name]: value,
    });
  }

  handleCountryChange(e) {
    this.setState({
      country: e,
    });
  }

  async handleSearch() {
    const payload = {
      status: '',
      condition: this.state.condition,
      other_terms: this.state.otherTerms,
      country: this.state.country,
      intervention: '',
      target: this.state.target,
      nct_id: '',
      eligibility_criteria: '',
      first: '',
      last: '',
    };
    try {
      const response = await ctgov.post('basic_search', payload);
      this.setState({
        displaySearchResults: true,
        searchResults: response.data,
      });
      console.log(response.data);
    } catch (err) {
      console.log(err);
    }
  }

  handleClear() {
    this.setState({
      condition: '',
      target: '',
      country: '',
      otherTerms: '',
    });
  }

  render() {
    const layout = {
      labelCol: {
        span: 8,
      },
      wrapperCol: {
        span: 16,
      },
    };
    const tailLayout = {
      wrapperCol: {
        offset: 8,
        span: 16,
      },
    };
    const countryList = [];

    Array.from(countries.entries()).forEach(([, value]) => {
      countryList.push(
        <Option value={value}>{value}</Option>
      );
    });
    return (
      <Form
        labelCol={layout.labelCol}
        wrapperCol={layout.wrapperCol}
      >
        <TextInputField
          label="Condition or disease"
          title="The disease, disorder, syndrome, illness, or injury that is being studied. On CTFrontier.com, conditions may also include other health-related issues, such as lifespan, quality of life, and health risks."
          name="condition"
          handleInputChange={this.handleInputChange}
        />
        <TextInputField
          label="MOA or target"
          title="Mechanism of ƒaction (MOA) describes how a drug or substance produces an effect in the body. A drug’s MOA could be how it affects a specific target in a cell, such as an enzyme, or a cell function, such as cell growth. Biological targets are most commonly proteins, such as enzymes, ion channels, and receptors."
          name="target"
          handleInputChange={this.handleInputChange}
        />
        <SelectField
          name="country"
          label="Country"
          tooltip="The 'Country' field is used to find clinical studies with locations in a specific country. For example, if you choose the United States, you can then narrow your search by selecting a state and identifying a city and distance."
          placeholder="Select the country"
          options={countryList}
          name="country"
          handleInputChange={this.handleCountryChange}
        />
        <TextInputField
          label="Other terms"
          title="The 'Other' terms field is used to narrow a search. For example, you may enter the name of a drug or the NCT number of a clinical study to limit the search to study records that contain these words."
          name="otherTerms"
          handleInputChange={this.handleInputChange}
        />
        <Form.Item wrapperCol={tailLayout.wrapperCol}>
          <Button
            type="primary"
            text="Search"
            clickHandler={this.handleSearch}
          />
          <Button
            text="Clear"
            clickHandler={this.handleClear}
          />
        </Form.Item>
        <BasicSearchAccordion
          access={access}
          recruitment={recruitment}
        />
        <div>{JSON.stringify(this.state.searchResults)}</div>
      </Form>
    );
  }
}

export default TopLevelSearchFormFields;
