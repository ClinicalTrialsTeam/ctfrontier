const columns = [
  {
    title: 'NCT ID',
    dataIndex: 'nctid',
    key: 'nctid',
  },
  {
    title: 'Phase',
    dataIndex: 'phase',
    key: 'phase',
  },
  {
    title: 'Status',
    dataIndex: 'status',
    key: 'status',
  },
  {
    title: 'Sponsor',
    dataIndex: 'sponsor',
    key: 'sponsor',
  },
  {
    title: 'Study Title',
    dataIndex: 'studytitle',
    key: 'studytitle',
  },
  {
    title: 'Condition',
    dataIndex: 'condition',
    key: 'condition',
  },
  {
    title: 'Other',
    dataIndex: 'other',
    key: 'other',
  },
];

const data = [
  {
    key: '1',
    nctid: 'NCT04218877',
    phase: '',
    status: 'Recruiting',
    sponsor: 'Akusherstvo Pro',
    studytitle: 'The Factors Affecting Dermatitis in Children Age 1-3',
    condition: 'Atopic Dermatitis',
  },
  {
    key: '2',
    nctid: 'NCT04307862',
    phase: 'Phase 2',
    status: 'Recruiting',
    sponsor: 'Shulov Innovate for Science Ltd. 2012',
    studytitle: 'Safety, Tolerability and Efficacy of ZEP-3Na (0.1% or 1%) Compared to Placebo in Subjects With Mild to Moderate Atopic Dermatitis',
    condition: 'Atopic Dermatitis',
  },
  {
    key: '3',
    nctid: 'NCT04444726',
    phase: 'Not applicable',
    status: 'Recruiting',
    sponsor: 'Cairo University',
    studytitle: 'Phototherpy Versus Tapwater Iontophoresis for Management of Atopic Dermatitis in Children',
    condition: 'Atopic Dermatitis',
  },
  {
    key: '4',
    nctid: 'NCT04218877',
    phase: 'Phase 1 Phase 2',
    status: 'Recruiting',
    sponsor: 'Suzhou Zelgen Biopharmaceuticals Co.,Ltd',
    studytitle: 'Jaktinib Hydrochloride Cream For Atopic Dermatitis',
    condition: 'Atopic Dermatitis',
  },
  {
    key: '5',
    nctid: 'NCT04218877',
    phase: 'Phase 1',
    status: 'Completed, Has Results',
    sponsor: 'Shaperon',
    studytitle: 'A Phase I Study of HY209 Gel in Healthy Male Volunteers for Atopic Dermatitis',
    condition: 'Atopic Dermatitis',
  },
  {
    key: '6',
    nctid: 'NCT04218877',
    phase: 'Phase 2',
    status: 'Terminated',
    sponsor: 'Chung Shan Medical University, Golden Biotechnology Corporation',
    studytitle: 'A Phase II, Placebo-controlled Trial Evaluating the Efficacy of Antroquinonol in Patients With Atopic Dermatitis',
    condition: 'Atopic Dermatitis',
  },
  {
    key: '7',
    nctid: 'NCT04715087',
    phase: 'Not applicable',
    status: 'Not yet recruting',
    sponsor: 'Hospices Civils de Lyon',
    studytitle: 'Staphylococcus Aureus in Atopic Dermatitis Immunopathology',
    condition: 'Atopic Dermatitis',
  },
  {
    key: '8',
    nctid: 'NCT03796676',
    phase: 'Phase 3',
    status: 'Completed',
    sponsor: 'Pfizer',
    studytitle: 'JAK1 Inhibitor With Medicated Topical Therapy in Adolescents With Atopic Dermatitis',
    condition: 'Atopic Dermatitis',
  },
];

module.exports = {
  columns,
  data,
};
