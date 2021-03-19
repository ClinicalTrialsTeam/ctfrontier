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
    status: 'Recruting',
    sponsor: 'Akusherstvo Pro',
    studytitle: 'The Factors Affecting Dermatitis in Children Age 1-3',
    condition: 'atopic dermatitis',
  },
  {
    key: '2',
    nctid: 'NCT04307862',
    phase: 'Phase 2',
    status: 'Recruting',
    sponsor: 'Shulov Innovate for Science Ltd. 2012',
    studytitle: 'Safety, Tolerability and Efficacy of ZEP-3Na (0.1% or 1%) Compared to Placebo in Subjects With Mild to Moderate Atopic Dermatitis',
    condition: 'atopic dermatitis',
  },
  {
    key: '3',
    nctid: 'NCT04444726',
    phase: 'Not applicable',
    status: 'Recruting',
    sponsor: 'Cairo University',
    studytitle: 'Phototherpy Versus Tapwater Iontophoresis for Management of Atopic Dermatitis in Children',
    condition: 'atopic dermatitis',
  },
  {
    key: '4',
    nctid: 'NCT04218877',
    phase: 'Phase 1 Phase 2',
    status: 'Recruting',
    sponsor: 'Suzhou Zelgen Biopharmaceuticals Co.,Ltd',
    studytitle: 'Jaktinib Hydrochloride Cream For Atopic Dermatitis',
    condition: 'atopic dermatitis',
  },
  {
    key: '5',
    nctid: 'NCT04218877',
    phase: 'Phase 1',
    status: 'Completed',
    sponsor: 'Shaperon',
    studytitle: 'Jaktinib Hydrochloride Cream For Atopic Dermatitis',
    condition: 'atopic dermatitis',
  },
  {
    key: '6',
    nctid: 'NCT04218877',
    phase: 'Phase 2',
    status: 'Terminated',
    sponsor: 'Chung Shan Medical University, Golden Biotechnology Corporation',
    studytitle: 'Jaktinib Hydrochloride Cream For Atopic Dermatitis',
    condition: 'atopic dermatitis',
  },
  {
    key: '7',
    nctid: 'NCT04218877',
    phase: 'Not applicable',
    status: 'Not yet recruting',
    sponsor: 'Hospices Civils de Lyon',
    studytitle: 'Jaktinib Hydrochloride Cream For Atopic Dermatitis',
    condition: 'atopic dermatitis',
  },
  {
    key: '8',
    nctid: 'NCT04218877',
    phase: 'Phase 3',
    status: 'Completed',
    sponsor: 'Pfizer',
    studytitle: 'Jaktinib Hydrochloride Cream For Atopic Dermatitis',
    condition: 'atopic dermatitis',
  },
];

// const data = [
//   {
//     key: '1',
//     name: 'Mike',
//     age: 32,
//     address: '10 Downing Street',
//   },
//   {
//     key: '2',
//     name: 'John',
//     age: 42,
//     address: '10 Downing Street',
//   },
// ];

// const columns = [
//   {
//     title: 'Name',
//     dataIndex: 'name',
//     key: 'name',
//   },
//   {
//     title: 'Age',
//     dataIndex: 'age',
//     key: 'age',
//   },
//   {
//     title: 'Address',
//     dataIndex: 'address',
//     key: 'address',
//   },
// ];

module.exports = {
  columns,
  data,
};
