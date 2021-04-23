const columns = [
  {
    title: 'NCT ID',
    dataIndex: 'nct_id',
    key: 'nct_id',
    fixed: 'left',
    width: 120,
    sorter: true,
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
    sorter: true,
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
    sorter: true,
    width: 120,
  },
];

module.exports = {
  columns,
};
