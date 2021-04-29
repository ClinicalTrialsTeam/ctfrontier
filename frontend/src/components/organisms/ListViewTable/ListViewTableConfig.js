const columns = [
  {
    title: 'NCT ID',
    dataIndex: 'nct_id',
    key: 'nct_id',
    fixed: 'left',
    width: 120,
    sortDirections: ['descend', 'ascend'],
    sorter: (a, b) => { return a.nct_id.localeCompare(b.nct_id); },
  },
  {
    title: 'Brief Title',
    dataIndex: 'brief_title',
    key: 'brief_title',
    width: 250,
  },
  {
    title: 'Condition',
    dataIndex: 'condition_name',
    key: 'condition_name',
    width: 150,
    sortDirections: ['descend', 'ascend'],
    sorter: (a, b) => {
      return a.condition_name.localeCompare(b.condition_name);
    },
  },
  {
    title: 'Intervention',
    dataIndex: 'intervention_name',
    key: 'intervention_name',
    sorter: true,
    width: 200,
  },
  {
    title: 'Sponsor',
    dataIndex: 'sponsor_name',
    key: 'sponsor_name',
    sortDirections: ['descend', 'ascend'],
    sorter: (a, b) => { return a.sponsor_name.localeCompare(b.sponsor_name); },
    width: 150,
  },
  {
    title: 'Phase',
    dataIndex: 'study_phase',
    key: 'study_phase',
    sortDirections: ['descend', 'ascend'],
    sorter: (a, b) => { return a.study_phase.localeCompare(b.study_phase); },
    width: 100,
  },
  {
    title: 'Status',
    dataIndex: 'status',
    key: 'status',
    sortDirections: ['descend', 'ascend'],
    sorter: (a, b) => { return a.status.localeCompare(b.status); },
    width: 100,
  },
];

module.exports = {
  columns,
};
