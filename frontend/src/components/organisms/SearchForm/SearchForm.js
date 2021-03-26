import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import {
  Form, Select, Divider, Row, Col, Space,
} from 'antd';
import ctgov from '../../../apis/ctgov';
import TextInputField from '../../atoms/TextInputField/TextInputField';
import SelectField from '../../atoms/SelectField/SelectField';
import Button from '../../atoms/buttons/Button/Button';
import AdvancedSearchGroup from '../../molecules/AdvancedSearchGroup/AdvancedSearchGroup';

import './SearchForm.css';

import {
  recruitment, access, countries,
} from '../../../variables/TopLevelSearchData';

class SearchForm extends Component {
  constructor(props) {
    super(props);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleCountryChange = this.handleCountryChange.bind(this);
    this.handleSearch = this.handleSearch.bind(this);
    this.handleClear = this.handleClear.bind(this);
    this.formRef = React.createRef();
    this.state = {
      intervention: '',
      condition: '',
      target: '',
      country: '',
      otherTerms: '',
      searchResults: '',
    };
  }

  async handleSearch() {
    const payload = {
      status: '',
      condition: this.state.condition,
      other_terms: this.state.otherTerms,
      country: this.state.country,
      intervention: this.state.intervention,
      target: this.state.target,
      nct_id: this.state.nct_id,
      eligibility_criteria: '',
      first: '',
      last: '',
    };
    try {
      const response = await ctgov.post('basic_search', payload);
      this.setState({
        searchResults: response.data,
      });
    } catch (err) {
      console.log(err);
    }
  }

  handleClear() {
    this.setState({
      intervention: '',
      condition: '',
      target: '',
      country: '',
      otherTerms: '',
      nct_id: '',
    });
    this.formRef.current.resetFields();
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

  render() {
    const { Option } = Select;
    const countryList = [];

    if (this.state.searchResults !== '') {
      return (
        <Redirect
          push
          to={{
            pathname: '/trials',
            state: { data: this.state.searchResults },
          }}
        />
      );
    }

    Array.from(countries.entries()).forEach(([index, value]) => {
      countryList.push(
        <Option key={index} value={value}>{value}</Option>
      );
    });
    return (
      <>
        <Divider
          orientation="left"
          style={{ marginTop: '24px' }}
        >
          Find a study (all fields are optional)
        </Divider>
        <Form
          ref={this.formRef}
          layout="vertical"
          key="form_key"
        >
          <Row key="form_row_1" gutter={[16, 16]}>
            <Col key="12" span={8}>
              <TextInputField
                key="1"
                label="NCT number"
                title="A unique identification code given to each clinical study record registered on ClinicalTrials.gov. The format is 'NCT' followed by an 8-digit number (for example, NCT00000419). Also called the ClinicalTrials.gov identifier."
                name="nct_id"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="2"
                label="Condition or disease"
                title="The disease, disorder, syndrome, illness, or injury that is being studied. On CTFrontier.com, conditions may also include other health-related issues, such as lifespan, quality of life, and health risks."
                name="condition"
                handleInputChange={this.handleInputChange}
              />
            </Col>
            <Col key="13" span={8}>
              <TextInputField
                key="3"
                label="Intervention / treatment"
                title="A process or action that is the focus of a clinical study. Interventions include drugs, medical devices, procedures, vaccines, and other products that are either investigational or already available. Interventions can also include noninvasive approaches, such as education or modifying diet and exercise."
                name="intervention"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="4"
                label="MOA or target"
                title="Mechanism of action (MOA) describes how a drug or substance produces an effect in the body. A drug’s MOA could be how it affects a specific target in a cell, such as an enzyme, or a cell function, such as cell growth. Biological targets are most commonly proteins, such as enzymes, ion channels, and receptors."
                name="target"
                handleInputChange={this.handleInputChange}
              />
            </Col>
            <Col key="14" span={8}>
              <SelectField
                key="5"
                name="country"
                label="Country"
                tooltip="The 'Country' field is used to find clinical studies with locations in a specific country. For example, if you choose the United States, you can then narrow your search by selecting a state and identifying a city and distance."
                placeholder="Select the country"
                options={countryList}
                handleInputChange={this.handleCountryChange}
              />
              <TextInputField
                key="6"
                label="Other terms"
                title="The 'Other' terms field is used to narrow a search. For example,  you may enter the name of a drug or the NCT number of a clinical study to limit the search to study records that contain these words."
                name="otherTerms"
                handleInputChange={this.handleInputChange}
              />
            </Col>
          </Row>
          <Row key="form_row_2" justify="center">
            <Form.Item>
              <Space>
                <Button
                  key="8"
                  inputType="primary"
                  text="Search"
                  clickHandler={this.handleSearch}
                />
                <Button
                  key="9"
                  text="Clear"
                  clickHandler={this.handleClear}
                />
                <Button
                  key="10"
                  text="Show advanced options"
                  clickHandler={this.handleClear}
                />
              </Space>
            </Form.Item>
          </Row>
          <AdvancedSearchGroup
            access={access}
            recruitment={recruitment}
            handleInputChange={this.handleInputChange}
          />
          <div style={{ display: 'none' }}>{JSON.stringify(this.state.searchResults)}</div>
        </Form>
      </>
    );
  }
}

export default SearchForm;
