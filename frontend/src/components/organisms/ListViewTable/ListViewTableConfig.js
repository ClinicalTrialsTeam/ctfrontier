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
  },
  {
    title: 'Condition',
    dataIndex: 'condition_name',
    key: 'condition_name',
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
    title: 'Status',
    dataIndex: 'status',
    key: 'status',
    sortDirections: ['descend', 'ascend'],
    sorter: (a, b) => { return a.status.localeCompare(b.status); },
    width: 120,
  },
];

module.exports = {
  columns,
};
