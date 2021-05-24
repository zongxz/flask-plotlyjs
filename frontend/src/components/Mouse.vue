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
  name: 'MouseBrainExpress',
  components: {
    Plot
  },
  data () {
    return {
      data: [],
      layout: {}
    }
  },
  methods: {
    getData () {
      let url = 'http://127.0.0.1:5000/mouseBrainExpressData1'
      axios.get(url)
        .then((res) => {
          function dropx (alist) {
            let l = []
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
            let l = []
            for (let i = 0; i < alist.length; i++) {
              if ([0, ''].includes(alist[i])) {
                l.push(0)
              } else {
                l.push(Math.log10(alist[i] + 1.0).toFixed(2))
              }
            }
            return l
          }

          function getX (type, alist) {
            let l = []
            for (let i = 0; i < alist.length; i++) {
              l.push('<b>' + alist[i] + '</b> (' + capitalize(type) + ')')
            }
            return l
          }

          function capitalize (str) {
            let s = str.toLowerCase()
            s = s.charAt(0).toUpperCase() + s.slice(1)
            return s
          }

          // eslint-disable-next-line camelcase
          let mouse_brain_expression = res.data['data']['mouse_brain_expression']
          let data = []
          // eslint-disable-next-line camelcase
          for (let keys in mouse_brain_expression) {
            let datas = []
            let period = []
            let dict = {'data': [], 'period': []}
            let mouseDict = {}
            let expdatas = mouse_brain_expression[keys]
            for (let k in expdatas) {
              for (let i = 0; i < expdatas[k].length; i++) {
                if (expdatas[k][i] === 0.0) {
                  datas.push('')
                } else {
                  datas.push(expdatas[k][i])
                }
                period.push(k)
              }
            }
            dict['data'] = datas
            dict['period'] = period
            mouseDict[keys] = dict
            data.push(mouseDict)
          }
          let tarces = []
          for (let i = 0; i < data.length; i++) {
            let item = data[i]
            let type = ''
            let datas = []
            let period = []
            for (let k in item) {
              type = k
              datas = dropx(item[k]['data'])
              period = item[k]['period']
            }
            tarces.push({
              y: datas,
              x: getX(type, period),
              name: type,
              boxpoints: 'outliers',
              line: {width: 1},
              type: 'box'
            })
          }
          let len = tarces.length
          for (let i = 0; i < data.length; i++) {
            let item = data[i]
            let type = ''
            let datas = []
            let period = []
            for (let k in item) {
              type = k
              datas = normalized(item[k]['data'])
              period = item[k]['period']
            }

            tarces.push({
              y: datas,
              x: getX(type, period),
              name: type,
              boxpoints: 'outliers',
              line: {width: 1},
              type: 'box',
              visible: false
            })
          }
          // eslint-disable-next-line camelcase
          let visible_list_1 = []
          // eslint-disable-next-line camelcase
          let visible_list_2 = []
          for (let i = 0; i < len; i++) {
            visible_list_1.push(true)
            visible_list_2.push(false)
          }
          for (let i = 0; i < len; i++) {
            visible_list_1.push(false)
            visible_list_2.push(true)
          }
          let updatemenus = [{
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
          var layout = {
            updatemenus: updatemenus,
            paper_bgcolor: 'rgb(249, 249, 249)',
            plot_bgcolor: 'rgb(249, 249, 249)',
            height: 600,
            width: 1300,
            hovermode: 'closest',
            xaxis: {
              showgrid: true,
              zeroline: false,
              showline: false,
              showticklabels: true,
              tickangle: 50,
              titlefont: {
                size: 8,
                family: 'Arial'
              }
            },
            yaxis: {
              autorange: true,
              showgrid: true,
              zeroline: false,
              titlefont: {
                family: 'Arial'
              }

            },
            margin: {
              l: 30,
              r: 10,
              b: 250,
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
    this.getData()
  }
}

</script>

<style scoped>

</style>
