<template>
  <div id="app">
    <button v-on:click="get">click here</button>
    <my-chart :chartData="chartData"></my-chart>
  </div>
</template>

<script>
import moment from 'moment'

import MyChart from './Chart.js';
import weight_log from './api/weight_log.js';

// const genRandArr = () => {
  // return [...Array(12).keys()].map(() => Math.floor(Math.random() * 30));
// };

export default {
  name: 'app',
  mounted: function () {
    this.get();
  },
  data: function () {
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
    get: function () {
      weight_log.get()
        .then(this.refreshData);
    },
    refreshData: function(res) {
      res.sort((a, b) => (a.tweeted_at - b.tweeted_at));
      const labels = res.map(v => this.labelFormatter(v.tweeted_at));
      const data = res.map(v => v.weight);
      this.chartData = {
        labels,
        datasets: [{ data }],
      };
    },
    labelFormatter: function (timestamp) {
      return moment.unix(timestamp).format('M/DD');
    },
  },
  components: {
    MyChart,
  },
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  // color: #2c3e50;
  margin-top: 60px;
}
</style>
