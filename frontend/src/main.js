// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Plotly from 'plotly.js-dist'

Vue.config.productionTip = false

Vue.component('reactive-chart', {
  props: ['chart'],
  template: '<div :ref="chart.uuid"></div>',
  mounted () {
    Plotly.plot(this.$refs[this.chart.uuid], this.chart.traces, this.chart.layout)
  },
  watch: {
    chart: {
      handler: function () {
        Plotly.react(
          this.$refs[this.chart.uuid],
          this.chart.traces,
          this.chart.layout
        )
      },
      deep: true
    }
  }
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
