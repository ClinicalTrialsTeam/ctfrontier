import React, { Component } from 'react';
import { Checkbox, Col, Collapse, Form, Input, Row, Select } from 'antd';
import { InfoCircleOutlined } from '@ant-design/icons';
import { countries, recruitment } from '../../../variables/TopLevelSearchData';
import PropTypes from 'prop-types';
import CheckboxGroup from '../checkbox-group/checkbox-group';

class BasicSearchAccordion extends Component {
  render() {
    const { access, recruitment } = this.props;
    const { Panel } = Collapse;

    const standardLayout = {
      wrapperCol: {
        span: 24,
      },
    };

    const text = 'More content will be added here';

    const recruitmentCheckboxes = [];

    Array.from(recruitment.entries()).forEach(([, value]) => {
      recruitmentCheckboxes.push(
        <Col span={12}>
          <Checkbox value={value} style={{ lineHeight: '32px' }}>
            {value}
          </Checkbox>
        </Col>
      );
    });

    const accessCheckboxes = [];

    Array.from(access.entries()).forEach(([, value]) => {
      accessCheckboxes.push(
        <Col span={12}>
          <Checkbox value={value} style={{ lineHeight: '32px' }}>
            {value}
          </Checkbox>
        </Col>
      );
    });

    return (
      <Collapse>
        <Panel header="Status" key="1">
          <Collapse>
            <Panel header="Recruitment" key="1">
              <Form.Item
                wrapperCol={standardLayout.wrapperCol}
                name="checkbox-group"
              >
                <Checkbox.Group>
                  <Row>
                    {recruitmentCheckboxes}
                  </Row>
                </Checkbox.Group>
              </Form.Item>
            </Panel>
            <Panel header="Expanded Access" key="2">
              <Form.Item
                wrapperCol={standardLayout.wrapperCol}
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
        </Panel>
        <Panel header="Eligibility Criteria" key="2">
          <p>{text}</p>
        </Panel>
        <Panel header="Targeted Search" key="3">
          <Form.Item
            label="Intervention / treatment"
            tooltip={{
              title: 'A process or action that is the focus of a clinical study. Interventions include drugs, medical devices, procedures, vaccines, and other products that are either investigational or already available. Interventions can also include noninvasive approaches, such as education or modifying diet and exercise.',
              icon: <InfoCircleOutlined />,
            }}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Title / acronym"
            tooltip={{
              title: "The official title of a protocol used to identify a clinical study or a short title written in language intended for the lay public. The acronym or initials used to identify a clinical study (not all studies have one). For example, the title acronym for the Women's Health Initiative is 'WHI.'",
              icon: <InfoCircleOutlined />,
            }}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Outcome measure"
            tooltip={{
              title: 'For clinical trials, a planned measurement described in the protocol that is used to determine the effect of an intervention/treatment on participants. For observational studies, a measurement or observation that is used to describe patterns of diseases or traits, or associations with exposures, risk factors, or treatment. Types of outcome measures include primary outcome measure and secondary outcome measure.',
              icon: <InfoCircleOutlined />,
            }}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Sponsor / collaborator"
            tooltip={{
              title: 'Sponsor is the organization or person who initiates the study and who has authority and control over the study. Collaborator is an organization other than the sponsor that provides support for a clinical study. This support may include activities related to funding, design, implementation, data analysis, or reporting.',
              icon: <InfoCircleOutlined />,
            }}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Sponsor (Lead)"
            tooltip={{
              title: 'The organization or person who initiates the study and who has authority and control over the study.',
              icon: <InfoCircleOutlined />,
            }}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Study IDs"
            tooltip={{
              title: "Identifiers that are assigned to a clinical study by the study's sponsor, funders, or others. They include unique identifiers from other trial study registries and National Institutes of Health grant numbers. Note: ClinicalTrials.gov assigns a unique identification code to each clinical study registered on ClinicalTrials.gov. Also called the NCT number, the format is 'NCT' followed by an 8-digit number (for example, NCT00000419).",
              icon: <InfoCircleOutlined />,
            }}
          >
            <Input />
          </Form.Item>
        </Panel>
        <Panel header="Additional Criteria" key="4">
          <p>{text}</p>
        </Panel>
      </Collapse>
    );
  }
}

BasicSearchAccordion.propTypes = {
  access: PropTypes.array.isRequired,
  recruitment: PropTypes.array.isRequired,
};

export default BasicSearchAccordion;
