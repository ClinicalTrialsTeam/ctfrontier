import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import {
  Form, Select, Divider, Row, Col, Space, Typography, Checkbox, // DatePicker,
} from 'antd';
import ctgov from '../../../apis/ctgov';
import TextInputField from '../../atoms/TextInputField/TextInputField';
import NumberInputField from '../../atoms/NumberInputField/NumberInputField';
import SelectField from '../../atoms/SelectField/SelectField';
import Button from '../../atoms/buttons/Button/Button';
import AdvancedSearchGroup from '../../molecules/AdvancedSearchGroup/AdvancedSearchGroup';

import './SearchForm.css';

import {
  recruitment, access, phases, roa, results, types, sex, ageGroup, ethnicities,
} from '../../../variables/TopLevelSearchData';

class SearchForm extends Component {
  constructor(props) {
    super(props);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleCountryChange = this.handleCountryChange.bind(this);
    this.handleRoaChange = this.handleRoaChange.bind(this);
    this.handleRecruitmentChange = this.handleRecruitmentChange.bind(this);
    this.handlePhaseChange = this.handlePhaseChange.bind(this);
    this.handleResultsChange = this.handleResultsChange.bind(this);
    this.handleTypeChange = this.handleTypeChange.bind(this);
    this.handleSexChange = this.handleSexChange.bind(this);
    this.handleAgeGroupChange = this.handleAgeGroupChange.bind(this);
    this.handleEthnicityChange = this.handleEthnicityChange.bind(this);
    this.handleSearch = this.handleSearch.bind(this);
    this.handleClear = this.handleClear.bind(this);
    this.showAdvancedOptions = this.showAdvancedOptions.bind(this);
    this.formRef = React.createRef();
    this.state = {
      intervention: '',
      condition: '',
      target: '',
      country: '',
      otherTerms: '',
      searchResults: '',
      countries: [],
      roa: [],
      recruitment: [],
      phase: [],
      results: '',
      type: '',
      sex: '',
      ageGroup: [],
      ethnicity: [],
      showAdvancedOptions: false,
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
      phase: [],
      roa: [],
      countries: [],
      type: '',
      sex: '',
      ageGroup: [],
      ethnicity: [],
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

  handleRoaChange(e) {
    this.setState({
      roa: e,
    });
  }

  handleRecruitmentChange(e) {
    this.setState({
      recruitment: e,
    });
  }

  handlePhaseChange(e) {
    this.setState({
      phase: e,
    });
  }

  handleResultsChange(e) {
    this.setState({
      results: e,
    });
  }

  handleTypeChange(e) {
    this.setState({
      type: e,
    });
  }

  handleSexChange(e) {
    this.setState({
      sex: e,
    });
  }

  handleAgeGroupChange(e) {
    this.setState({
      ageGroup: e,
    });
  }

  handleEthnicityChange(e) {
    this.setState({
      ethnicity: e,
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
      roa: this.state.roa,
      recruitment: this.state.recruitment,
      phase: this.state.phase,
      results: this.state.results,
      eligibility_criteria: '',
      type: this.state.type,
      sex: this.state.sex,
      ageGroup: this.state.ageGroup,
      ethnicity: this.state.ethnicity,
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

  showAdvancedOptions() {
    const { showAdvancedOptions } = this.state;
    this.setState({
      showAdvancedOptions: !showAdvancedOptions,
    });
  }

  render() {
    // const { RangePicker } = DatePicker;
    const { Option } = Select;
    const { Text } = Typography;
    const countryList = [];
    const roaList = [];
    const recruitmentList = [];
    const phaseList = [];
    const resultsList = [];
    const typeList = [];
    const sexList = [];
    const ageGroupList = [];
    const ethnicitiesList = [];

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

    Array.from(roa.entries()).forEach(([index, value]) => {
      roaList.push(
        <Option key={index} value={value}>{value}</Option>
      );
    });

    Array.from(recruitment.entries()).forEach(([index, value]) => {
      recruitmentList.push(
        <Option key={index} value={value}>{value}</Option>
      );
    });

    Array.from(phases.entries()).forEach(([index, value]) => {
      phaseList.push(
        <Option key={index} value={value}>{value}</Option>
      );
    });

    Array.from(results.entries()).forEach(([index, value]) => {
      resultsList.push(
        <Option key={index} value={value}>{value}</Option>
      );
    });

    Array.from(types.entries()).forEach(([index, value]) => {
      typeList.push(
        <Option key={index} value={value}>{value}</Option>
      );
    });

    Array.from(sex.entries()).forEach(([index, value]) => {
      sexList.push(
        <Option key={index} value={value}>{value}</Option>
      );
    });

    Array.from(ageGroup.entries()).forEach(([index, value]) => {
      ageGroupList.push(
        <Option key={index} value={value}>{value}</Option>
      );
    });

    Array.from(ethnicities.entries()).forEach(([index, value]) => {
      ethnicitiesList.push(
        <Option key={index} value={value}>{value}</Option>
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
    let advancedOptions;
    if (this.state.showAdvancedOptions) {
      advancedOptions = (
        <AdvancedSearchGroup
          access={access}
          recruitment={recruitment}
          handleInputChange={this.handleInputChange}
        />
      );
    } else {
      advancedOptions = '';
    }
    return (
      <>
        <Divider
          orientation="left"
          style={{ marginTop: '24px' }}
        >
          Find a study (all fields are optional)
        </Divider>
        <Form
          id="search-form"
          ref={this.formRef}
          layout="vertical"
          key="form_key"
        >
          <Row key="form_row_basic" gutter={[32, 16]}>
            <Col key="12" span={8}>
              <Text className="section-text" strong key="t_1">Disease / Treatment Details</Text>
              <TextInputField
                key="field-disease"
                label="Condition or Disease"
                title="The disease, disorder, syndrome, illness, or injury that is being studied. Conditions may also include other health-related issues, such as lifespan, quality of life, and health risks."
                name="condition"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="field-other"
                label="Additional Terms"
                title="In the search feature, the Other (Additional) Terms field is used to narrow a search. For example, you may enter the name of a drug or the NCT number of a clinical study to limit the search to study records that contain these words."
                name="other_terms"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="field-subcondition"
                label="Subcondition"
                title="Subcondition definition will go here"
                name="subcondition"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="field-intervention"
                label="Intervention / Treatment"
                title="A process or action that is the focus of a clinical study. Interventions include drugs, medical devices, procedures, vaccines, and other products that are either investigational or already available. Interventions can also include noninvasive approaches, such as education or modifying diet and exercise."
                name="intervention"
                handleInputChange={this.handleInputChange}
              />
              <SelectField
                mode="multiple"
                key="10"
                name="roa"
                label="Routes of Administration"
                title="A route of administration in pharmacology is the path by which a drug is taken into the body. Common examples include oral and intravenous administration."
                placeholder="Select the route of administration"
                options={roaList}
                handleInputChange={this.handleRoaChange}
              />
              <TextInputField
                key="field-modality"
                label="Modality"
                title="A therapeutic method or agent that involves the physical treatment of a disorder. Common modalities are small molecules (organic compounds that can often be delivered orally); large molecules or biologics, which include monoclonal antibodies (mAbs), proteins, peptides; antibody-drug conjugates; oligonucleotides (e.g. antisense oligonucleotides (ASOs), mRNA, siRNAs); gene therapy; and cell therapy (e.g. CAR T or chimeric antigen receptor T cell therapy)."
                name="modality"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="field-target"
                label="MOA or Target"
                title="Mechanism of action (MOA) describes how a drug or substance produces an effect in the body. A drug’s MOA could be how it affects a specific target in a cell, such as an enzyme, or a cell function, such as cell growth. Biological targets are most commonly proteins, such as enzymes, ion channels, and receptors."
                name="target"
                handleInputChange={this.handleInputChange}
              />
              {/* <Text className="sf-text" strong key="t_1">Dates</Text>
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
              </Row> */}
            </Col>
            <Col key="13" span={8}>
              <Text className="section-text" strong key="t_2">Trial Details</Text>
              <TextInputField
                key="field-nct"
                label="NCT Number"
                title="A unique identification code given to each clinical study record registered on ClinicalTrials.gov. The format is 'NCT' followed by an 8-digit number (for example, NCT00000419). Also called the ClinicalTrials.gov identifier."
                name="nct_id"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="field-title"
                label="Title / Acronym"
                title="The official title of a protocol used to identify a clinical study or a short title written in language intended for the lay public. The acronym or initials used to identify a clinical study (not all studies have one). For example, the title acronym for the Women's Health Initiative is 'WHI.'"
                name="title"
                handleInputChange={this.handleInputChange}
              />
              <SelectField
                mode="multiple"
                key="field-recruitment"
                name="status"
                label="Recruitment Status"
                title="Indicates the current recruitment status"
                placeholder="Select the recruitment status"
                options={recruitmentList}
                handleInputChange={this.handleRecruitmentChange}
              />
              <SelectField
                mode="multiple"
                key="field-phase"
                name="phase"
                label="Phase"
                title="The stage of a clinical trial studying a drug or biological product, based on definitions developed by the U.S. Food and Drug Administration (FDA). The phase is based on the study's objective, the number of participants, and other characteristics. There are five phases: Early Phase 1 (formerly listed as Phase 0), Phase 1, Phase 2, Phase 3, and Phase 4. Not Applicable is used to describe trials without FDA-defined phases, including trials of devices or behavioral interventions."
                placeholder="Select the phase"
                options={phaseList}
                handleInputChange={this.handlePhaseChange}
              />
              <TextInputField
                key="field-sponsor"
                label="Sponsor / Collaborators"
                title="Sponsor is the organization or person who initiates the study and who has authority and control over the study. Collaborator is an organization other than the sponsor that provides support for a clinical study. This support may include activities related to funding, design, implementation, data analysis, or reporting."
                name="target"
                handleInputChange={this.handleInputChange}
              />
              <SelectField
                key="field-results"
                name="results"
                label="Study Results"
                title="A study record that includes the summary results posted in the ClinicalTrials.gov results database. Summary results information includes participant flow, baseline characteristics, outcome measures, and adverse events (including serious adverse events)."
                placeholder="Select the phase"
                options={resultsList}
                handleInputChange={this.handleResultsChange}
              />
              <SelectField
                key="field-types"
                name="types"
                label="Study Type"
                title="Describes the nature of a clinical study. Study types include interventional studies (also called clinical trials), observational studies (including patient registries), and expanded access."
                placeholder="Select the type"
                options={typeList}
                handleInputChange={this.handleTypeChange}
              />
              {/* <Text strong key="t_22">Recruitment Status</Text>
              <Form.Item
                name="checkbox-group"
              >
                <Checkbox.Group>
                  <Row>
                    {recruitmentCheckboxes}
                  </Row>
                </Checkbox.Group>
              </Form.Item> */}
            </Col>
            <Col key="14" span={8}>
              <Text className="section-text" strong key="t_3">Patient Details</Text>
              <SelectField
                key="field-sex"
                name="sex"
                label="Sex"
                title="A type of eligibility criteria that indicates the sex of people who may participate in a clinical study (all, female, male). Sex is a person's classification as female or male based on biological distinctions. Sex is distinct from gender-based eligibility."
                placeholder="Select the participant's sex"
                options={sexList}
                handleInputChange={this.handleSexChange}
              />
              <Row key="form_row_age" gutter={[16, 8]}>
                <Col key="141" span={8}>
                  {/* <Space> */}
                  <NumberInputField
                    className="age-num"
                    min={1}
                    max={100}
                    key="field-age"
                    label="Age"
                    title="A type of eligibility criteria that indicates the age a person must be to participate in a clinical study. This may be indicated by a specific age or the following age groups:
                    Child (birth-17);
                    Adult (18-64);
                    Older Adult (65+)."
                    name="age"
                    handleInputChange={this.handleInputChange}
                  />
                  {/* </Space> */}
                </Col>
                <Col key="142" span={16}>
                  <SelectField
                    mode="multiple"
                    key="field-age-group"
                    name="age_group"
                    label="Age Group"
                    title="A type of eligibility criteria that indicates the age a person must be to participate in a clinical study. This may be indicated by a specific age or the following age groups:
                    Child (birth-17);
                    Adult (18-64);
                    Older Adult (65+)."
                    placeholder="Select the age group"
                    options={ageGroupList}
                    handleInputChange={this.handleAgeGroupChange}
                  />
                </Col>
              </Row>
              <SelectField
                mode="multiple"
                key="field-ethnicity"
                name="ethnicity"
                label="Ethnicity / Race"
                title="American Indian or Alaska Native: A person having origins in any of the original peoples of North and South America (including Central America) and who maintains tribal affiliation or community attachment.
                Asian: A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam.
                Black or African American: A person having origins in any of the Black racial groups of Africa.
                Native Hawaiian or Other Pacific Islander: A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands.
                White: A person having origins in any of the original peoples of Europe, the Middle East, or North Africa. Hispanic or Latino: A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race."
                placeholder="Select the ethnicity"
                options={phaseList}
                handleInputChange={this.handlePhaseChange}
              />
              <SelectField
                key="field-country"
                name="country"
                label="Study Location (Country)"
                title="In the search feature, the Country field is used to find clinical studies with locations in a specific country. For example, if you choose the United States, you can then narrow your search by selecting a state and identifying a city and distance."
                placeholder="Select the country"
                options={countryList}
                handleInputChange={this.handleCountryChange}
              />
              <Row key="form_row_location" gutter={[16, 8]}>
                <Col key="151" span={12}>
                  <SelectField
                    key="field-state"
                    name="state"
                    label="State"
                    title="In the search feature, the State field is used to find clinical studies with locations in a specific state within the United States. If you choose United States in the Country field, you can search for studies with locations in a specific state."
                    placeholder="Select the state"
                    options={sexList}
                    handleInputChange={this.handleSexChange}
                  />
                </Col>
                <Col key="152" span={12}>
                  <TextInputField
                    key="field-city"
                    label="City"
                    title="In the search feature, the City field is used to find clinical studies with locations in a specific city. The Distance field is used to find studies with locations within the specified distance from a city in number of miles. For example, if you choose Illinois as the state, identifying 'Chicago' as the city and '100 miles' as the distance will find all studies listing a location within 100 miles of Chicago."
                    name="city"
                    handleInputChange={this.handleInputChange}
                  />
                </Col>
              </Row>
              <TextInputField
                key="field-location-terms"
                label="Location Terms"
                title="In the search feature, the Location terms field is used to narrow a search by location-related terms other than Country, State, and City or distance. For example, you may enter a specific facility name (such as National Institutes of Health Clinical Center) or a part of a facility name (such as Veteran for studies listing Veterans Hospital or Veteran Affairs in the facility name). Note: Not all study records include this level of detail about locations."
                name="nct_id"
                handleInputChange={this.handleInputChange}
              />
              {/* <Text strong key="t_38">Phases</Text>
              <Form.Item
                name="checkbox-group"
              >
                <Checkbox.Group>
                  <Row>
                    {phasesCheckboxes}
                  </Row>
                </Checkbox.Group>
              </Form.Item> */}
            </Col>
          </Row>
          <Row key="form_row_buttons" className="form-row-buttons" justify="center">
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
                  key="10"
                  text={this.state.showAdvancedOptions === false ? 'Show advanced options' : 'Hide advanced options'}
                  clickHandler={this.showAdvancedOptions}
                />
              </Space>
            </Form.Item>
          </Row>
          {advancedOptions}
        </Form>
      </>
    );
  }
}

export default SearchForm;
