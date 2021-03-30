import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import {
  Form, Select, Divider, Row, Col, Space, Typography, Checkbox, DatePicker,
} from 'antd';
import ctgov from '../../../apis/ctgov';
import TextInputField from '../../atoms/TextInputField/TextInputField';
import SelectField from '../../atoms/SelectField/SelectField';
import Button from '../../atoms/buttons/Button/Button';
import AdvancedSearchGroup from '../../molecules/AdvancedSearchGroup/AdvancedSearchGroup';

import './SearchForm.css';

import {
  recruitment, access, phases,
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
      countries: [],
    };
  }

  async componentDidMount() {
    try {
      const response = await ctgov.get('countries');
      const countries = response.data.map((item) => {
        return item.country;
      });
      this.setState({
        countries,
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

  render() {
    const { RangePicker } = DatePicker;
    const { Option } = Select;
    const { Text } = Typography;
    const countryList = [];
    const roaList = [];

    const recruitmentCheckboxes = [];
    const phasesCheckboxes = [];

    Array.from(recruitment.entries()).forEach(([index, value]) => {
      recruitmentCheckboxes.push(
        <Col key={index} span={12}>
          <Checkbox key={index} value={value} style={{ lineHeight: '32px' }}>
            {value}
          </Checkbox>
        </Col>
      );
    });

    Array.from(phases.entries()).forEach(([index, value]) => {
      phasesCheckboxes.push(
        <Col key={index} span={12}>
          <Checkbox key={index} value={value} style={{ lineHeight: '32px' }}>
            {value}
          </Checkbox>
        </Col>
      );
    });

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

    Array.from(this.state.countries.entries()).forEach(([index, value]) => {
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
          <Row key="form_row_1" gutter={[32, 16]}>
            <Col key="12" span={8}>
              <TextInputField
                key="1"
                label="Condition or disease"
                title="The disease, disorder, syndrome, illness, or injury that is being studied. Conditions may also include other health-related issues, such as lifespan, quality of life, and health risks."
                name="condition"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="2"
                label="Intervention / treatment"
                title="A process or action that is the focus of a clinical study. Interventions include drugs, medical devices, procedures, vaccines, and other products that are either investigational or already available. Interventions can also include noninvasive approaches, such as education or modifying diet and exercise."
                name="intervention"
                handleInputChange={this.handleInputChange}
              />
              <Text className="sf-text" strong key="t_1">Dates</Text>
              <Row id="dates-row" key="form_row_1_1" gutter={[16, 4]}>
                <Col key="12_1" span={12}>
                  <Form.Item
                    key="range_1"
                    label="Study start"
                  >
                    <RangePicker />
                  </Form.Item>
                  <Form.Item
                    key="range_2"
                    label="Primary completion"
                  >
                    <RangePicker />
                  </Form.Item>
                  <Form.Item
                    key="range_3"
                    label="Last update posted"
                  >
                    <RangePicker />
                  </Form.Item>
                </Col>
                <Col key="12_1" span={12}>
                  <Form.Item
                    key="range_4"
                    label="First posted"
                  >
                    <RangePicker />
                  </Form.Item>
                  <Form.Item
                    key="range_5"
                    label="Results first posted"
                  >
                    <RangePicker />
                  </Form.Item>
                </Col>
              </Row>
            </Col>
            <Col key="13" span={8}>
              <TextInputField
                key="3"
                label="Modality"
                title="A therapeutic method or agent that involves the physical treatment of a disorder. Common modalities are small molecules (organic compounds that can often be delivered orally); large molecules or biologics, which include monoclonal antibodies (mAbs), proteins, peptides; antibody-drug conjugates; oligonucleotides (e.g. antisense oligonucleotides (ASOs), mRNA, siRNAs); gene therapy; and cell therapy (e.g. CAR T or chimeric antigen receptor T cell therapy)."
                name="modality"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="4"
                label="MOA or target"
                title="Mechanism of action (MOA) describes how a drug or substance produces an effect in the body. A drug’s MOA could be how it affects a specific target in a cell, such as an enzyme, or a cell function, such as cell growth. Biological targets are most commonly proteins, such as enzymes, ion channels, and receptors."
                name="target"
                handleInputChange={this.handleInputChange}
              />
              <Text strong key="t_2">Recruitment Status</Text>
              <Form.Item
                name="checkbox-group"
              >
                <Checkbox.Group>
                  <Row>
                    {recruitmentCheckboxes}
                  </Row>
                </Checkbox.Group>
              </Form.Item>
            </Col>
            <Col key="14" span={8}>
              <TextInputField
                key="5"
                label="NCT number"
                title="A unique identification code given to each clinical study record registered on ClinicalTrials.gov. The format is 'NCT' followed by an 8-digit number (for example, NCT00000419). Also called the ClinicalTrials.gov identifier."
                name="nct_id"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="6"
                label="Sponsor"
                title="The organization or person who initiates the study and who has authority and control over the study."
                name="otherTerms"
                handleInputChange={this.handleInputChange}
              />
              <Text strong key="t_3">Phases</Text>
              <Form.Item
                name="checkbox-group"
              >
                <Checkbox.Group>
                  <Row>
                    {phasesCheckboxes}
                  </Row>
                </Checkbox.Group>
              </Form.Item>
            </Col>
          </Row>
          <Row key="form_row_2" justify="center">
            <Form.Item>
              <Space>
                <Button
                  key="btn_1"
                  inputType="primary"
                  text="Search"
                  clickHandler={this.handleSearch}
                />
                <Button
                  key="btn_2"
                  text="Clear"
                  clickHandler={this.handleClear}
                />
                <Button
                  key="btn_3"
                  text="Hide advanced options"
                  clickHandler={this.handleClear}
                />
              </Space>
            </Form.Item>
          </Row>
          <Row key="form_row_3" gutter={[16, 16]}>
            <Col key="form_col_3_1" span={12}>
              <SelectField
                key="10"
                name="roa"
                label="Routes of Administration"
                tooltip="A route of administration in pharmacology is the path by which a drug is taken into the body. Common examples include oral and intravenous administration."
                placeholder="Select the route of administration"
                options={roaList}
                handleInputChange={this.handleCountryChange}
              />
            </Col>
            <Col key="form_col_3_2" span={12}>
              <SelectField
                key="11"
                name="country"
                label="Country"
                tooltip="The 'Country' field is used to find clinical studies with locations in a specific country. For example, if you choose the United States, you can then narrow your search by selecting a state and identifying a city and distance."
                placeholder="Select the country"
                options={countryList}
                handleInputChange={this.handleCountryChange}
              />
            </Col>
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
