import axios from 'axios';

export default {
  get: () => {
    const url = 'https://b55huow1uf.execute-api.ap-northeast-1.amazonaws.com/dev/weight_log';
    return axios.get(url)
      .then(res => res.data);
  },
};

