import { Card } from 'antd';
import TopLevelSearchFormFields from "../TopLevelSearchFormFields/TopLevelSearchFormFields";

import './TopLevelSearchForm.css';

function TopLevelSearchForm() {
    return (
        <Card id="frostedcard">
            <TopLevelSearchFormFields/>
        </Card>
    );
}

export default TopLevelSearchForm;
