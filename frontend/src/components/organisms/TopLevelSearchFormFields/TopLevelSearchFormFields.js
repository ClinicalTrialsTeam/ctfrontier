import React, { useState } from 'react';
import { Form, Input, Button, Select, Collapse, Checkbox, Row, Col } from 'antd';
import { InfoCircleOutlined } from '@ant-design/icons';

// import 'antd/dist/antd.dark.css';
import './TopLevelSearchFormFields.css';

import { recruitment, access, phases, countries } from "../../../variables/TopLevelSearchData";

const TopLevelSearchFormFields = () => {
    const { Panel } = Collapse;
    const { Option } = Select;

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
    const standardLayout = {
        wrapperCol: {
            span: 24,
        },
    };

  const [form] = Form.useForm();
  const [requiredMark, setRequiredMarkType] = useState('optional');

  const onRequiredTypeChange = ({ requiredMarkValue }) => {
        setRequiredMarkType(requiredMarkValue);
  };

  const text = 'More content will be added here';

    const recruitmentCheckboxes = []

    for (const [, value] of recruitment.entries()) {
        recruitmentCheckboxes.push(
            <Col span={12}>
                <Checkbox value={value} style={{ lineHeight: '32px' }}>
                    {value}
                </Checkbox>
            </Col>
        )
    }

    const accessCheckboxes = []

    for (const [, value] of access.entries()) {
        accessCheckboxes.push(
            <Col span={12}>
                <Checkbox value={value} style={{ lineHeight: '32px' }}>
                    {value}
                </Checkbox>
            </Col>
        )
    }

    const countryList = []

    for (const [, value] of countries.entries()) {
        countryList.push(
            <Option value={value}>{value}</Option>
        )
    }

  return (
    <Form
      form={form}
      {...layout}
      initialValues={{
        requiredMark,
      }}
      onValuesChange={onRequiredTypeChange}
    //   requiredMark={requiredMark}
    >
      <Form.Item 
        label="Condition or disease" 
        tooltip={{
            title: 'The disease, disorder, syndrome, illness, or injury that is being studied. On CTFrontier.com, conditions may also include other health-related issues, such as lifespan, quality of life, and health risks.',
            icon: <InfoCircleOutlined />,
          }}
        >
        <Input />
      </Form.Item>
      <Form.Item 
        label="MOA or target" 
        tooltip={{
            title: 'Mechanism of action (MOA) describes how a drug or substance produces an effect in the body. A drug’s MOA could be how it affects a specific target in a cell, such as an enzyme, or a cell function, such as cell growth. Biological targets are most commonly proteins, such as enzymes, ion channels, and receptors.',
            icon: <InfoCircleOutlined />,
          }}
        >
        <Input />
      </Form.Item>
      <Form.Item
          name="country"
          label="Country"
          tooltip={{
            title: "The 'Country' field is used to find clinical studies with locations in a specific country. For example, if you choose the United States, you can then narrow your search by selecting a state and identifying a city and distance.",
            icon: <InfoCircleOutlined />,
          }}
        >
          <Select
            placeholder="Select the country"
            // onChange={this.onGenderChange}
            allowClear
          >
            {countryList}
          </Select>
        </Form.Item>
      <Form.Item
        label="Other terms"
        tooltip={{
          title: "The 'Other' terms field is used to narrow a search. For example, you may enter the name of a drug or the NCT number of a clinical study to limit the search to study records that contain these words.",
          icon: <InfoCircleOutlined />,
        }}
        >
        <Input />
      </Form.Item>
      <Form.Item {...tailLayout}>
        <Button type="primary">Search</Button>
        <Button
            style={{ margin: '0 8px' }}
            onClick={() => { form.resetFields();}}
            >
            Clear
        </Button>
      </Form.Item>
        <Collapse>
            <Panel header="Status" key="1">
            <Collapse>
                <Panel header="Recruitment" key="1" >
                    <Form.Item 
                        {...standardLayout}
                        name="checkbox-group">
                        <Checkbox.Group>
                            <Row>
                                {recruitmentCheckboxes}
                            </Row>
                        </Checkbox.Group>
                    </Form.Item>
                </Panel>
                <Panel header="Expanded Access" key="2">
                    <Form.Item 
                        {...standardLayout}
                        name="checkbox-group">
                        <Checkbox.Group >
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
    </Form>
  );
};

export default TopLevelSearchFormFields;