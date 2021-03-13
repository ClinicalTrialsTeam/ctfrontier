import './TopLevelSearchLogo.css';
import logo from './logo.png';

function TopLevelSearchLogo() {
    return (
        <div className="ctf-logo-wrapper">
            <img src={logo} className="ctf-logo" alt="logo" />
            <span className="ctf-logo"></span>
        </div>
    );
}

export default TopLevelSearchLogo;