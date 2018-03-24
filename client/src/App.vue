<template>
  <div id="app">
    <h1>Weight chart</h1>
    <Chart :chartData="chartData" />
  </div>
</template>

<script>
import moment from 'moment';

import Chart from './components/Chart';
import weightLog from './api/weightLog';

export default {
  name: 'app',
  mounted() {
    this.get();
  },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [{
          data: [],
        }],
      },
    };
  },
  methods: {
    get() {
      weightLog.get()
        .then(this.refreshData);
    },
    refreshData(res) {
      res.sort((a, b) => (a.tweeted_at - b.tweeted_at));
      const startDate = moment.unix(res[0].tweeted_at);
      const endDate = moment.unix(res[res.length - 1].tweeted_at);
      const range = endDate.diff(startDate, 'days') + 1;
      const labels = [...Array(range).keys()].map(v => startDate.clone().add(v, 'days').toDate());
      const data = res.map(v => (
        { t: moment.unix(v.tweeted_at), y: v.weight }
      ));
      this.chartData = {
        labels,
        datasets: [{
          fill: false,
          data,
        }],
      };
    },
    labelFormatter(timestamp) {
      return moment.unix(timestamp).format('M/DD');
    },
  },
  components: {
    Chart,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
