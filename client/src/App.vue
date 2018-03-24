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
      message: 'hello',
    };
  },
  methods: {
    get() {
      weightLog.get()
        .then(this.refreshData);
    },
    refreshData(res) {
      res.sort((a, b) => (a.tweeted_at - b.tweeted_at));
      const labels = res.map(v => this.labelFormatter(v.tweeted_at));
      const data = res.map(v => v.weight);
      this.chartData = {
        labels,
        datasets: [{ data }],
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
