<template>
  <Plot
    :data="data"
    :layout="layout"
  />
</template>

<script>
import Plot from 'vue-plotly.js'
import axios from 'axios'

export default {
  name: 'Example',
  components: {
    Plot
  },
  data () {
    return {
      data: '',
      layout: ''
    }
  },
  methods: {
    getMessage () {
      const pathGenes = 'http://127.0.0.1:5000/humanEPCExpressData'
      axios.get(pathGenes)
        .then((res) => {
          this.genes = res.data

          function dropx (alist) {
            var l = []
            for (let i = 0; i < alist.length; i++) {
              if (alist[i] === '') {
                l.push(0)
              } else {
                l.push(alist[i])
              }
            }
            return l
          }

          function normalized (alist) {
            var l = []
            for (let i = 0; i < alist.length; i++) {
              if ([0, ''].includes(alist[i])) {
                l.push(0)
              } else {
                l.push(Math.log10(alist[i] + 1.0).toFixed(2))
              }
            }
            return l
          }

          // eslint-disable-next-line camelcase
          function get_x (dataType, alist) {
            var l = []
            for (let i = 0; i < alist.length; i++) {
              l.push(dataType + ' - ' + alist[i])
            }
            return l
          }
          var data = res.data
          var tarces = []
          for (let i = 0; i < data.length; i++) {
            var item = data[i]
            var dataType = item['type']
            var datas = dropx(item['data'])
            var period = item['period']
            tarces.push({
              y: datas,
              x: get_x(dataType, period),
              name: dataType,
              boxpoints: 'outliers',
              line: {
                width: 1
              },
              type: 'box'
            })
          }
          var len = tarces.length
          for (let i = 0; i < data.length; i++) {
            var item1 = data[i]
            var dataType1 = item1['type']
            var datas1 = normalized(item1['data'])
            // eslint-disable-next-line camelcase
            var period_2 = item1['period']
            tarces.push({
              y: datas1,
              x: get_x(dataType1, period_2),
              visible: false,
              name: dataType1,
              boxpoints: 'outliers',
              line: {
                width: 1
              },
              type: 'box'
            })
          }
          // eslint-disable-next-line camelcase
          var visible_list_1 = []
          // eslint-disable-next-line camelcase
          var visible_list_2 = []
          for (let i = 0; i < len; i++) {
            visible_list_1.push(true)
            visible_list_2.push(false)
          }
          for (let i = 0; i < len; i++) {
            visible_list_1.push(false)
            visible_list_2.push(true)
          }
          for (let i = 0; i < 2; i++) {
            visible_list_1.push(false)
            visible_list_2.push(false)
          }

          var updatemenus = [{
            type: 'buttons',
            active: -1,
            pad: {
              r: 30,
              t: 20
            },
            buttons: [{
              label: 'original TPM',
              method: 'update',
              args: [{'visible': visible_list_1},
                {
                  'title': 'TPM without normalization'
                }]
            },
            {
              label: 'log<sub>10</sub> ( TPM + 1 )',
              method: 'update',
              args: [{'visible': visible_list_2},
                {
                  'title': 'Normalized TPM'
                }]
            }]
          }]
          // eslint-disable-next-line no-unused-vars
          const layout = {
            updatemenus: updatemenus,
            paper_bgcolor: 'rgb(249, 249, 249)',
            plot_bgcolor: 'rgb(249, 249, 249)',
            height: 400,
            width: 1000,
            hovermode: 'closest',
            xaxis: {
              showgrid: true,
              zeroline: false,
              showline: false,
              showticklabels: true,
              tickangle: 60,
              titlefont: {
                family: 'Arial'
              }
            },
            yaxis: {
              titlefont: {
                family: 'Arial'
              }

            },
            margin: {
              l: 150,
              r: 10,
              b: 180,
              t: 30
            }
          }
          this.data = tarces
          this.layout = layout
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.getMessage()
  }
}

</script>

<style scoped>

</style>
