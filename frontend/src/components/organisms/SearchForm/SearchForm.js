import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import {
  Form, Select, Divider, Row, Col, Space, Typography, Checkbox,
} from 'antd';
import { InfoCircleOutlined } from '@ant-design/icons';
import ctgov from '../../../apis/ctgov';
import TextInputField from '../../atoms/TextInputField/TextInputField';
import NumberInputField from '../../atoms/NumberInputField/NumberInputField';
import SelectField from '../../atoms/SelectField/SelectField';
import Button from '../../atoms/buttons/Button/Button';
import AdvancedSearchGroup from '../../molecules/AdvancedSearchGroup/AdvancedSearchGroup';

import './SearchForm.css';

import {
  recruitment, access, phases, roa, results,
  types, sex, ageGroup, ethnicities, distance, states,
} from '../../../variables/SelectOptionsData';

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
    this.handleStateChange = this.handleStateChange.bind(this);
    this.handleCityChange = this.handleCityChange.bind(this);
    this.handleDistanceChange = this.handleDistanceChange.bind(this);
    this.handleFunderChange = this.handleFunderChange.bind(this);
    this.handleDocumentsChange = this.handleDocumentsChange.bind(this);
    this.handleSubmissionChange = this.handleSubmissionChange.bind(this);
    this.handleSearch = this.handleSearch.bind(this);
    this.handleClear = this.handleClear.bind(this);
    this.handleLoading = this.handleLoading.bind(this);
    this.showAdvancedOptions = this.showAdvancedOptions.bind(this);
    this.showState = this.showState.bind(this);
    this.showCityDistance = this.showCityDistance.bind(this);
    this.handleStartDateChange = this.handleStartDateChange.bind(this);
    this.handlePrimaryCompletionDateChange = this.handlePrimaryCompletionDateChange.bind(this);
    this.handleFirstPostedDateChange = this.handleFirstPostedDateChange.bind(this);
    this.handleResultsFirstPostedDateChange = this.handleResultsFirstPostedDateChange.bind(this);
    this.handleLastUpdatePostedDateChange = this.handleLastUpdatePostedDateChange.bind(this);
    this.formRef = React.createRef();

    this.state = {
      condition: '',
      otherTerms: '',
      subcondition: '',
      intervention: '',
      roa: [],
      modality: '',
      target: '',
      nct_id: '',
      title: '',
      status: '',
      phase: [],
      sponsor: '',
      results: '',
      type: '',
      age: '',
      minAge: 0,
      maxAge: 100,
      sex: '',
      ethnicity: [],
      country: '',
      state: '',
      city: '',
      distance: '',
      healthy: false,
      locationTerms: '',
      studyCollaborator: '',
      studyOutcomeMeasure: '',
      studyIds: '',
      studyFunderType: '',
      studyDocumentType: '',
      studyResultsSubmitted: '',
      startDateFrom: '',
      startDateTo: '',
      primaryCompletionDateFrom: '',
      primaryCompletionDateTo: '',
      firstPostedDateFrom: '',
      firstPostedDateTo: '',
      resultsFirstPostedDateFrom: '',
      resultsFirstPostedDateTo: '',
      lastUpdatePostedDateFrom: '',
      lastUpdatePostedDateTo: '',
      countries: [],
      searchResults: '',
      showAdvancedOptions: false,
      showState: false,
      showCityDistance: false,
      recruitment: [],
      isLoading: false,
      payload: {},
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
      condition: '',
      otherTerms: '',
      subcondition: '',
      intervention: '',
      roa: [],
      modality: '',
      target: '',
      nct_id: '',
      title: '',
      status: '',
      phase: [],
      sponsor: '',
      results: '',
      type: '',
      age: '',
      minAge: 0,
      maxAge: 100,
      sex: '',
      ethnicity: [],
      country: '',
      state: '',
      city: '',
      distance: '',
      healthy: false,
      locationTerms: '',
      studyCollaborator: '',
      studyOutcomeMeasure: '',
      studyIds: '',
      studyFunderType: '',
      studyDocumentType: '',
      studyResultsSubmitted: '',
      startDateFrom: '',
      startDateTo: '',
      primaryCompletionDateFrom: '',
      primaryCompletionDateTo: '',
      firstPostedDateFrom: '',
      firstPostedDateTo: '',
      resultsFirstPostedDateFrom: '',
      resultsFirstPostedDateTo: '',
      lastUpdatePostedDateFrom: '',
      lastUpdatePostedDateTo: '',
    });
    this.formRef.current.resetFields();
  }

  handleInputChange(e) {
    const { target } = e;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const { name } = target;

    this.setState({
      [name]: value,
    });
  }

  handleCountryChange(e) {
    if (e === 'United States') {
      this.setState({
        showState: true,
        showCityDistance: true,
      });
    }
    if (e !== 'United States' && e !== '') {
      this.setState({
        state: '',
        showState: false,
        showCityDistance: true,
      });
    }
    if (e === '') {
      this.setState({
        state: '',
        city: '',
        distance: '',
        showState: false,
        showCityDistance: false,
      });
    }
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
    let type = '';
    if (e === 'Interventional Studies (Clinical Trials)') {
      type = 'Interventional';
    }
    if (e === 'Observational Studies') {
      type = 'Observational';
    }
    if (e === 'Patient Registries') {
      type = 'Patient Registry';
    }
    if (e === 'Expanded Access Studies') {
      type = 'Expanded Access';
    }
    this.setState({
      type,
    });
  }

  handleSexChange(e) {
    let sexSelection = 'All';
    if (e === 'Only Female Participants') {
      sexSelection = 'Female';
    }
    if (e === 'Only Male Participants') {
      sexSelection = 'Male';
    }
    this.setState({
      sex: sexSelection,
    });
  }

  handleAgeGroupChange(e) {
    let minAge = 0;
    let maxAge = 100;
    const lastItem = e.slice(-1)[0];
    if (e[0] === 'Adult (18-64)') {
      minAge = 18;
    }
    if (e[0] === 'Older Adult (65+)') {
      minAge = 65;
    }
    if (lastItem === 'Adult (18-64)') {
      maxAge = 64;
    }
    if (lastItem === 'Child (birth-17)') {
      maxAge = 17;
    }
    this.setState({
      minAge,
      maxAge,
    });
  }

  handleEthnicityChange(e) {
    this.setState({
      ethnicity: e,
    });
  }

  handleStateChange(e) {
    this.setState({
      state: e,
    });
  }

  handleCityChange(e) {
    this.setState({
      city: e,
    });
  }

  handleDistanceChange(e) {
    this.setState({
      distance: e,
    });
  }

  handleLoading() {
    this.setState({
      isLoading: true,
    });
  }

  handleFunderChange(e) {
    let funderType;
    if (e === 'Other U.S. Federal agency') {
      funderType = 'U.S. Fed';
    } else if (e === 'All others (individuals, universities, organizations)') {
      funderType = 'Other';
    } else {
      funderType = this.state.studyFunderType;
    }
    this.setState({
      studyFunderType: funderType,
    });
  }

  handleDocumentsChange(e) {
    let documentType = 'Study Protocol';
    if (e === 'Statistical Analysis Plans (SAPs)') {
      documentType = 'Statistical Analysis Plan';
    }
    if (e === 'Informed Consent Forms (ICFs)') {
      documentType = 'Informed Consent Forms';
    }
    this.setState({
      studyDocumentType: documentType,
    });
  }

  handleSubmissionChange(e) {
    let resultsSubmitted = 'Not Submitted';
    if (e === 'Submitted, QC review not concluded') {
      resultsSubmitted = 'Submitted';
    }
    if (e === 'Submitted with QC comments available') {
      resultsSubmitted = 'QC Done';
    }
    this.setState({
      studyResultsSubmitted: resultsSubmitted,
    });
  }

  handleStartDateChange(e) {
    this.setState({
      startDateFrom: e[0].format('YYYY-MM-DD'),
      startDateTo: e[1].format('YYYY-MM-DD'),
    });
  }

  handlePrimaryCompletionDateChange(e) {
    this.setState({
      primaryCompletionDateFrom: e[0].format('YYYY-MM-DD'),
      primaryCompletionDateTo: e[1].format('YYYY-MM-DD'),
    });
  }

  handleFirstPostedDateChange(e) {
    this.setState({
      firstPostedDateFrom: e[0].format('YYYY-MM-DD'),
      firstPostedDateTo: e[1].format('YYYY-MM-DD'),
    });
  }

  handleResultsFirstPostedDateChange(e) {
    this.setState({
      resultsFirstPostedDateFrom: e[0].format('YYYY-MM-DD'),
      resultsFirstPostedDateTo: e[1].format('YYYY-MM-DD'),
    });
  }

  handleLastUpdatePostedDateChange(e) {
    this.setState({
      lastUpdatePostedDateFrom: e[0].format('YYYY-MM-DD'),
      lastUpdatePostedDateTo: e[1].format('YYYY-MM-DD'),
    });
  }

  async handleSearch() {
    this.handleLoading();
    const payload = {
      status: this.state.status,
      condition: this.state.condition,
      other_terms: this.state.otherTerms,
      country: this.state.country,
      intervention: this.state.intervention,
      target: this.state.target,
      nct_id: this.state.nct_id,
      eligibility_criteria: '',
      modality: this.state.modality,
      sponsor: this.state.sponsor,
      phase: this.state.phase,
      start_date_from: this.state.startDateFrom,
      start_date_to: this.state.startDateTo,
      primary_completion_date_from: this.state.primaryCompletionDateFrom,
      primary_completion_date_to: this.state.primaryCompletionDateTo,
      first_posted_date_from: this.state.firstPostedDateFrom,
      first_posted_date_to: this.state.firstPostedDateTo,
      results_first_posted_date_from: this.state.resultsFirstPostedDateFrom,
      results_first_posted_date_to: this.state.resultsFirstPostedDateTo,
      last_update_posted_date_from: this.state.lastUpdatePostedDateFrom,
      last_update_posted_date_to: this.state.lastUpdatePostedDateTo,
      study_results: this.state.results,
      study_type: this.state.type,
      eligibility_age: this.state.age,
      eligibility_min_age: this.state.minAge,
      eligibility_max_age: this.state.maxAge,
      eligibility_gender: this.state.sex,
      eligibility_ethnicity: this.state.ethnicity,
      eligibility_condition: '',
      eligibility_healthy_volunteer: this.state.healthy === true ? 'Accepts Healthy Volunteers' : '',
      study_title_acronym: this.state.title,
      study_outcome_measure: this.state.studyOutcomeMeasure,
      study_collaborator: this.state.studyCollaborator,
      study_ids: this.state.studyIds,
      study_location_terms: this.state.locationTerms,
      study_funder_type: this.state.studyFunderType,
      study_document_type: this.state.studyDocumentType,
      study_results_submitted: this.state.studyResultsSubmitted,
      study_roa: this.state.roa,
      state: this.state.state,
      city: this.state.city,
      distance: this.state.distance,
      subcondition: this.state.subcondition,
      recruitment: this.state.recruitment,
      first: 0,
      last: 100,
      metadata_required: true,
    };

    try {
      const response = await ctgov.post('search_studies', payload);
      this.setState({
        searchResults: response.data,
        payload,
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

  showState(shouldShow) {
    this.setState({
      showState: shouldShow,
    });
  }

  showCityDistance(shouldShow) {
    this.setState({
      showCityDistance: shouldShow,
    });
  }

  render() {
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
    const distanceList = [];
    const statesList = [];

    const recruitmentCheckboxes = [];
    const phasesCheckboxes = [];

    const selectArrays = [
      [roa, roaList],
      [recruitment, recruitmentList],
      [phases, phaseList],
      [results, resultsList],
      [types, typeList],
      [sex, sexList],
      [ageGroup, ageGroupList],
      [ethnicities, ethnicitiesList],
      [distance, distanceList],
      [states, statesList],
    ];

    selectArrays.forEach((element) => {
      Array.from(element[0].entries()).forEach(([index, value]) => {
        element[1].push(
          <Option key={index} value={value}>{value}</Option>
        );
      });
    });

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
            state: { data: this.state.searchResults, payload: this.state.payload },
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
          handleDatePickers={{
            'range-study-start': this.handleStartDateChange,
            'range-primary-completion': this.handlePrimaryCompletionDateChange,
            'range-first-posted': this.handleFirstPostedDateChange,
            'range-results-first-posted': this.handleResultsFirstPostedDateChange,
            'range-last-update-posted': this.handleLastUpdatePostedDateChange,
          }}
          handleSelectChange={{
            handleFunderChange: this.handleFunderChange,
            handleDocumentsChange: this.handleDocumentsChange,
            handleSubmissionChange: this.handleSubmissionChange,

          }}
        />
      );
    } else {
      advancedOptions = '';
    }

    let state;
    if (this.state.showState) {
      state = (
        <SelectField
          key="field-state"
          name="state"
          label="State"
          title="In the search feature, the State field is used to find clinical studies with locations in a specific state within the United States. If you choose United States in the Country field, you can search for studies with locations in a specific state."
          placeholder="Select the state"
          options={statesList}
          handleInputChange={this.handleStateChange}
        />
      );
    } else {
      state = null;
    }

    let cityDistance;
    if (this.state.showCityDistance) {
      cityDistance = (
        <Row key="form_row_location" gutter={[16, 8]}>
          <Col key="152" span={12}>
            <TextInputField
              key="field-city"
              label="City"
              title="In the search feature, the City field is used to find clinical studies with locations in a specific city. The Distance field is used to find studies with locations within the specified distance from a city in number of miles. For example, if you choose Illinois as the state, identifying 'Chicago' as the city and '100 miles' as the distance will find all studies listing a location within 100 miles of Chicago."
              name="city"
              handleInputChange={this.handleCityChange}
            />
          </Col>
          <Col key="153" span={12}>
            <SelectField
              key="field-distance"
              name="distance"
              label="Distance"
              title="In the search feature, the City field is used to find clinical studies with locations in a specific city. The Distance field is used to find studies with locations within the specified distance from a city in number of miles. For example, if you choose Illinois as the state, identifying 'Chicago' as the city and '100 miles' as the distance will find all studies listing a location within 100 miles of Chicago."
              placeholder="Select the distance"
              options={distanceList}
              handleInputChange={this.handleDistanceChange}
            />
          </Col>
        </Row>
      );
    } else {
      cityDistance = null;
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
                name="otherTerms"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="field-subcondition"
                label="Additional Condition Parameters"
                title="Additional condition parameters, such as biomarkers, severity or stage of the disease."
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
                title="A therapeutic approach for drugs, such as small molecules, antibodies, RNAi, CAR T cell, or peptide."
                name="modality"
                handleInputChange={this.handleInputChange}
              />
              <TextInputField
                key="field-target"
                label="Mechanism of Action / Target"
                title="A biochemical interaction that a drug disrupts usually involving a specific protein (target), such as an enzyme or receptor."
                name="target"
                handleInputChange={this.handleInputChange}
              />
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
                name="sponsor"
                handleInputChange={this.handleInputChange}
              />
              <SelectField
                key="field-results"
                name="results"
                label="Study Results"
                title="A study record that includes the summary results posted in the ClinicalTrials.gov results database. Summary results information includes participant flow, baseline characteristics, outcome measures, and adverse events (including serious adverse events)."
                placeholder="Select the results"
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
            </Col>
            <Col key="14" span={8}>
              <Text className="section-text" strong key="t_3">Patient Details</Text>
              <Row key="form_row_age" gutter={[16, 8]}>
                <Col key="141" span={6}>
                  <NumberInputField
                    className="age-num"
                    min={0}
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
                </Col>
                <Col key="143" span={2}>
                  <p id="or-p">OR</p>
                </Col>
                <Col key="142" span={16}>
                  <SelectField
                    mode="multiple"
                    key="field-age-group"
                    name="ageGroup"
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
              <Row key="form_row_sex_health" gutter={[16, 8]}>
                <Col key="checkbox-healthy" span={8}>
                  <Form.Item
                    key="form-item-healthy"
                    onChange={this.handleInputChange}
                    label="Healthy"
                    tooltip={{
                      title: 'A type of eligibility criteria that indicates whether people who do not have the condition/disease being studied can participate in that clinical study.',
                      icon: <InfoCircleOutlined />,
                    }}
                  >
                    <Checkbox name="healthy">Is healthy?</Checkbox>
                  </Form.Item>
                </Col>
                <Col key="col-field-sex" span={16}>
                  <SelectField
                    key="field-sex"
                    name="sex"
                    label="Sex"
                    title="A type of eligibility criteria that indicates the sex of people who may participate in a clinical study (all, female, male). Sex is a person's classification as female or male based on biological distinctions. Sex is distinct from gender-based eligibility."
                    placeholder="Select the participant's sex"
                    options={sexList}
                    handleInputChange={this.handleSexChange}
                  />
                </Col>
              </Row>
              <SelectField
                mode="multiple"
                key="field-ethnicity"
                name="ethnicity"
                label="Race / Ethnicity"
                title="American Indian or Alaska Native: A person having origins in any of the original peoples of North and South America (including Central America) and who maintains tribal affiliation or community attachment.
                Asian: A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam.
                Black or African American: A person having origins in any of the Black racial groups of Africa.
                Native Hawaiian or Other Pacific Islander: A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands.
                White: A person having origins in any of the original peoples of Europe, the Middle East, or North Africa. Hispanic or Latino: A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race."
                placeholder="Select the ethnicity"
                options={ethnicitiesList}
                handleInputChange={this.handlePhaseChange}
              />
              <SelectField
                key="field-country"
                name="country"
                label="Patient's Location (Country)"
                title="In the search feature, the Country field is used to find clinical studies with locations in a specific country. For example, if you choose the United States, you can then narrow your search by selecting a state and identifying a city and distance."
                placeholder="Select the country"
                options={countryList}
                handleInputChange={this.handleCountryChange}
              />
              {state}
              {cityDistance}
              <TextInputField
                key="field-location-terms"
                label="Location Terms"
                title="In the search feature, the Location terms field is used to narrow a search by location-related terms other than Country, State, and City or distance. For example, you may enter a specific facility name (such as National Institutes of Health Clinical Center) or a part of a facility name (such as Veteran for studies listing Veterans Hospital or Veteran Affairs in the facility name). Note: Not all study records include this level of detail about locations."
                name="locationTerms"
                handleInputChange={this.handleInputChange}
              />
            </Col>
          </Row>
          <Row key="form_row_buttons" className="form-row-buttons" justify="center">
            <Form.Item>
              <Space>
                <Button
                  loading={this.state.isLoading}
                  key="btn_search"
                  inputType="primary"
                  text="Search"
                  clickHandler={this.handleSearch}
                />
                <Button
                  key="btn_clear"
                  text="Clear"
                  clickHandler={this.handleClear}
                />
                <Button
                  key="btn_show"
                  text={this.state.showAdvancedOptions === false ? 'Show expanded options' : 'Hide expanded options'}
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
