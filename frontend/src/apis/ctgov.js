import axios from 'axios';
import rateLimit from 'axios-rate-limit';
import urljoin from 'url-join';

axios.defaults.withCredentials = true;
console.log(`REACT_APP_API_BASE_URL ${process.env.REACT_APP_API_BASE_URL}`);

const http = rateLimit(
  axios.create({
    baseURL: urljoin(process.env.REACT_APP_API_BASE_URL, 'ctgov/api'),
  }),
  { maxRPS: 2 }
);

export default http;
