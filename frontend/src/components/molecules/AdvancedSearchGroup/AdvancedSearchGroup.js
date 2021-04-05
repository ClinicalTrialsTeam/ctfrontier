import React, { Component } from 'react';
import {
  Checkbox, Col, Collapse, Form, Row,
} from 'antd';
import PropTypes from 'prop-types';
import { v4 as uuidv4 } from 'uuid';

import TextInputField from '../../atoms/TextInputField/TextInputField';

class AdvancedSearchGroup extends Component {
  render() {
    const { access, recruitment, handleInputChange } = this.props;
    const { Panel } = Collapse;

    const text = 'More content will be added here';

    const recruitmentCheckboxes = [];

    Array.from(recruitment.entries()).forEach(([, value]) => {
      recruitmentCheckboxes.push(
        <Col key={uuidv4()} span={12}>
          <Checkbox key={uuidv4()} value={value} style={{ lineHeight: '32px' }}>
            {value}
          </Checkbox>
        </Col>
      );
    });

    const accessCheckboxes = [];

    Array.from(access.entries()).forEach(([, value]) => {
      accessCheckboxes.push(
        <Col key={uuidv4()} span={12}>
          <Checkbox key={uuidv4()} value={value} style={{ lineHeight: '32px' }}>
            {value}
          </Checkbox>
        </Col>
      );
    });

    return (
      <>
        <Row key={uuidv4()} gutter={[16, 16]} style={{ marginBottom: '18px' }}>
          <Col key={uuidv4()} span={12}>
            <Collapse>
              <Panel header="Outcome Measures" key="1">
                <Form.Item
                  name="checkbox-group"
                >
                  <Checkbox.Group>
                    <Row>
                      {recruitmentCheckboxes}
                    </Row>
                  </Checkbox.Group>
                </Form.Item>
              </Panel>
            </Collapse>
          </Col>
          <Col key={uuidv4()} span={12}>
            <Collapse>
              <Panel header="Expanded Access" key="2">
                <Form.Item
                  name="checkbox-group"
                >
                  <Checkbox.Group>
                    <Row>
                      {accessCheckboxes}
                    </Row>
                  </Checkbox.Group>
                </Form.Item>
              </Panel>
            </Collapse>
          </Col>
        </Row>
        {/* <Row key={uuidv4()} gutter={[16, 16]}
         style={{ marginBottom: '18px' }}>
          <Col key={uuidv4()} span={12}>
            <Collapse>
              <Panel header="Eligibility Criteria" key="3">
                <p>{text}</p>
              </Panel>
            </Collapse>
          </Col>
          <Col key={uuidv4()} span={12}>
            <Collapse>
              <Panel header="Route of Administration" key="4">
                <p>{text}</p>
              </Panel>
            </Collapse>
          </Col>
        </Row> */}
        <Row key={uuidv4()} gutter={[16, 16]} style={{ marginBottom: '36px' }}>
          <Col key={uuidv4()} span={12}>
            <Collapse>
              <Panel header="Targeted Search" key="5">
                <TextInputField
                  key={uuidv4()}
                  label="Title / acronym"
                  title="The official title of a protocol used to identify a clinical study or a short title written in language intended for the lay public. The acronym or initials used to identify a clinical study (not all studies have one). For example, the title acronym for the Women's Health Initiative is 'WHI.'"
                  name="title"
                  handleInputChange={handleInputChange}
                />
                <TextInputField
                  key={uuidv4()}
                  label="Collaborator"
                  title="An organization other than the sponsor that provides support for a clinical study. This support may include activities related to funding, design, implementation, data analysis, or reporting."
                  name="title"
                  handleInputChange={handleInputChange}
                />
                <TextInputField
                  key={uuidv4()}
                  label="Outcome measure"
                  title="For clinical trials, a planned measurement described in the protocol that is used to determine the effect of an intervention/treatment on participants. For observational studies, a measurement or observation that is used to describe patterns of diseases or traits, or associations with exposures, risk factors, or treatment. Types of outcome measures include primary outcome measure and secondary outcome measure."
                  name="outcome"
                  handleInputChange={handleInputChange}
                />
                <TextInputField
                  key={uuidv4()}
                  label="Study IDs"
                  title="Identifiers that are assigned to a clinical study by the study's sponsor, funders, or others. They include unique identifiers from other trial study registries and National Institutes of Health grant numbers. Note: ClinicalTrials.gov assigns a unique identification code to each clinical study registered on ClinicalTrials.gov. Also called the NCT number, the format is 'NCT' followed by an 8-digit number (for example, NCT00000419)."
                  name="study_ids"
                  handleInputChange={handleInputChange}
                />
              </Panel>
            </Collapse>
          </Col>
          <Col key={uuidv4()} span={12}>
            <Collapse>
              <Panel header="Additional Criteria" key="6">
                <p>{text}</p>
              </Panel>
            </Collapse>
          </Col>
        </Row>
      </>
    );
  }
}

AdvancedSearchGroup.propTypes = {
  access: PropTypes.array.isRequired,
  recruitment: PropTypes.array.isRequired,
  handleInputChange: PropTypes.func.isRequired,
};

export default AdvancedSearchGroup;
