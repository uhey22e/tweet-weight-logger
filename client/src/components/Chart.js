// CommitChart.js
import { Line, mixins } from 'vue-chartjs';

export default {
  extends: Line,
  mixins: [mixins.reactiveProp],
  props: ['chartData'],
  data() {
    return {
      options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false,
        },
        scales: {
          xAxes: [{
            type: 'time',
            time: {
              unit: 'day',
              // unitStepSize: 1,
              displayFormats: {
                millisecond: 'MMM DD',
                second: 'MMM DD',
                minute: 'MMM DD',
                hour: 'MMM DD',
                day: 'MMM DD',
                week: 'MMM DD',
                month: 'MMM DD',
                quarter: 'MMM DD',
                year: 'MMM DD',
              },
              // format: 'YYYY-MM-DD',
            },
            scaleLabel: {
              display: true,
              labelString: 'Date',
            },
          }],
          yAxes: [{
            ticks: {
              min: 74,
              max: 88,
            },
            scaleLabel: {
              display: true,
              labelString: 'Weight [kg]',
            },
          }],
        },
      },
    };
  },
  mounted() {
    // Overwriting base render method with actual data.
    this.renderChart(this.chartData, this.options);
  },
};

