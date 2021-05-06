<template>
  <reactive-chart :chart="chart"></reactive-chart>
</template>

<script>


export default {
  name: 'Chart',
  mounted () {
    for (let i = 0; i < 100; i++) {
      this.addData()
    }
  },
  methods: {
    addData: function () {
      this.chart.layout.datarevision = new Date().getTime()
      this.chart.traces[0].y.push(Math.random())
    }
  },
  data () {
    return {
      chart: {
        uuid: '123',
        traces: [
          {
            y: [],
            line: {
              color: '#5e9e7e',
              width: 4,
              shape: 'line'
            }
          }
        ],
        layout: {
          title: 'reactive charts',
          xaxis: {
            title: 'xaxis title'
          },
          yaxis: {
            title: 'yaxis title'
          }
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
