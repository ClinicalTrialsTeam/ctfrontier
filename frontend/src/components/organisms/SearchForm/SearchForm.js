import React, { Component } from 'react';
import {
  Form, Select, Divider, Row, Col, Space, Modal,
} from 'antd';
import { v4 as uuidv4 } from 'uuid';
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
    this.state = {
      condition: '',
      target: '',
      country: '',
      otherTerms: '',
      searchResults: '',
      isModalVisible: false,
      modalMessage: '',
      modalTitle: '',
    };
  }

  async componentDidMount() {
    try {
      const response = await fetch('http://localhost:8000/ctgov/api/countries');
      this.setModalParams(true, 'Response Content', response);
    } catch (err) {
      this.setModalParams(true, 'Error Message', 'Failed to fetch countries');
    }
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
      this.setModalParams(true, 'Error Message', err);
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

  setModalParams(modalVisibility, modalTitle, modalMessage) {
    this.setState({
      isModalVisible: modalVisibility,
      modalMessage,
      modalTitle,
    });
  }

  setModalVisible(isModalVisible) {
    this.setState({
      isModalVisible,
    });
  }

  render() {
    const { Option } = Select;
    const countryList = [];

    Array.from(countries.entries()).forEach(([, value]) => {
      countryList.push(
        <Option key={uuidv4()} value={value}>{value}</Option>
      );
    });
    return (
      <>
        <Modal
          // key=Math.random().toString(36).substr(2, 9)
          title={this.state.modalTitle}
          visible={this.state.isModalVisible}
          onOk={() => { return this.setModalVisible(false); }}
          onCancel={() => { return this.setModalVisible(false); }}
        >
          <p>{this.state.modalMessage}</p>
        </Modal>
        <Divider
          orientation="left"
          style={{ marginTop: '24px' }}
        >
          Find a study (all fields are optional)
        </Divider>
        <Form
          layout="vertical"
        >
          <Row gutter={[16, 16]}>
            <Col key={uuidv4()} span={8}>
              <TextInputField
                key={uuidv4()}
                label="NCT number"
                title="A unique identification code given to each clinical study record registered on ClinicalTrials.gov. The format is 'NCT' followed by an 8-digit number (for example, NCT00000419). Also called the ClinicalTrials.gov identifier."
                name="nct_id"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key={uuidv4()}
                label="Condition or disease"
                title="The disease, disorder, syndrome, illness, or injury that is being studied. On CTFrontier.com, conditions may also include other health-related issues, such as lifespan, quality of life, and health risks."
                name="condition"
                handleInputChange={this.handleInputChange}
              />
            </Col>
            <Col key={uuidv4()} span={8}>
              <TextInputField
                key={uuidv4()}
                label="Intervention / treatment"
                title="A process or action that is the focus of a clinical study. Interventions include drugs, medical devices, procedures, vaccines, and other products that are either investigational or already available. Interventions can also include noninvasive approaches, such as education or modifying diet and exercise."
                name="intervention"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key={uuidv4()}
                label="MOA or target"
                title="Mechanism of action (MOA) describes how a drug or substance produces an effect in the body. A drug’s MOA could be how it affects a specific target in a cell, such as an enzyme, or a cell function, such as cell growth. Biological targets are most commonly proteins, such as enzymes, ion channels, and receptors."
                name="target"
                handleInputChange={this.handleInputChange}
              />
            </Col>
            <Col key={uuidv4()} span={8}>
              <SelectField
                key={uuidv4()}
                name="country"
                label="Country"
                tooltip="The 'Country' field is used to find clinical studies with locations in a specific country. For example, if you choose the United States, you can then narrow your search by selecting a state and identifying a city and distance."
                placeholder="Select the country"
                options={countryList}
                handleInputChange={this.handleCountryChange}
              />
              <TextInputField
                key={uuidv4()}
                label="Other terms"
                title="The 'Other' terms field is used to narrow a search. For example,  you may enter the name of a drug or the NCT number of a clinical study to limit the search to study records that contain these words."
                name="otherTerms"
                handleInputChange={this.handleInputChange}
              />
            </Col>
          </Row>
          <Row key={uuidv4()} justify="center">
            <Form.Item>
              <Space>
                <Button
                  key={uuidv4()}
                  type="primary"
                  text="Search"
                  clickHandler={this.handleSearch}
                />
                <Button
                  key={uuidv4()}
                  text="Clear"
                  clickHandler={this.handleClear}
                />
                <Button
                  key={uuidv4()}
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
