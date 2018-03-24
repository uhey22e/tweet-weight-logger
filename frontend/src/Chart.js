// CommitChart.js
import { Line, mixins } from 'vue-chartjs'

export default {
  extends: Line,
  mixins: [mixins.reactiveProp],
  props: ['chartData'],
  data () {
    return {
      options: {
        responsive: true,
        legend: {
          display: false,
        },
      },
    };
  },
  mounted () {
    // Overwriting base render method with actual data.
    this.renderChart(this.chartData, this.options);
  }
}
