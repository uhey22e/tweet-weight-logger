import axios from 'axios';

export default {
  get: () => {
    const url = 'https://api.weight-logger.uhey22e.tokyo/v1/weight_log';
    return axios.get(url)
      .then(res => res.data);
  },
};

