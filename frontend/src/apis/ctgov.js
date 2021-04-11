import axios from 'axios';
import rateLimit from 'axios-rate-limit';

axios.defaults.withCredentials = true;

const http = rateLimit(
  axios.create({
    baseURL: 'http://localhost:8000/ctgov/api',
  }),
  { maxRPS: 2 }
);

export default http;
