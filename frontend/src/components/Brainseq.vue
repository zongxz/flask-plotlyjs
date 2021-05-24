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
  name: 'BrainSeq',
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
      let url = 'http://127.0.0.1:5000/brainSeqData'
      axios.get(url)
        .then((res) => {
          function normalized (alist) {
            let l = []
            for (let i = 0; i < alist.length; i++) {
              if (alist[i] !== 0) {
                l.push(Math.log2(alist[i] + 1.0).toFixed(2))
              } else {
                l.push(0)
              }
            }
            return l
          }
          // eslint-disable-next-line camelcase
          let brainseq_exp_data = res.data[0]
          let traces = []
          // eslint-disable-next-line camelcase
          let control_exp = brainseq_exp_data['control_expression']
          // eslint-disable-next-line camelcase
          let scz_exp = brainseq_exp_data['scz_expression']
          if (Object.keys(control_exp).length !== 0) {
            // eslint-disable-next-line camelcase
            let control_key = Object.keys(control_exp)
            // eslint-disable-next-line camelcase
            let control_notes = []
            for (let i = 0; i < control_key.length; i++) {
              control_notes.push('Sample id: ' + control_key[i] + ',\n Exp: ' + String(control_exp[control_key[i]]))
            }
            // eslint-disable-next-line camelcase
            let control_val = []
            for (let i = 0; i < control_key.length; i++) {
              control_val.push(control_exp[control_key[i]])
            }
            // eslint-disable-next-line camelcase,no-unused-vars
            let control_val_normalized = normalized(control_val)
            // eslint-disable-next-line camelcase
            let control_x = []
            for (let i = 0; i < control_val.length; i++) {
              control_x.push('control (n=' + String(control_val.length) + ')')
            }
            traces.push({
              x: control_x,
              y: control_val,
              name: 'Control',
              boxpoints: 'all',
              line: {
                width: 1
              },
              marker: {
                size: 2.5
              },
              pointpos: 0,
              type: 'box'
            })
            traces.push({
              x: control_x,
              y: control_val_normalized,
              name: 'Control',
              boxpoints: 'all',
              line: {
                width: 1
              },
              marker: {
                size: 3
              },
              pointpos: 0,
              visible: false,
              hoverinfo: 'text',
              type: 'box',
              text: control_notes
            })
          }
          if (Object.keys(scz_exp).length !== 0) {
            // eslint-disable-next-line camelcase
            let scz_key = Object.keys(scz_exp)
            // eslint-disable-next-line camelcase
            let scz_notes = []
            for (let i = 0; i < scz_key.length; i++) {
              scz_notes.push('Sample id: ' + scz_key[i] + ',\n Exp: ' + String(control_exp[scz_key[i]]))
            }
            // eslint-disable-next-line camelcase
            let scz_val = []
            for (let i = 0; i < scz_key.length; i++) {
              scz_val.push(scz_exp[scz_key[i]])
            }
            // eslint-disable-next-line camelcase,no-unused-vars
            let scz_val_normalized = normalized(scz_val)
            // eslint-disable-next-line camelcase
            let scz_x = []
            for (let i = 0; i < scz_val.length; i++) {
              scz_x.push('schizophrenia (n=' + String(scz_val.length) + ')')
            }
            traces.push({
              x: scz_x,
              y: scz_val,
              name: 'Schizophrenia',
              boxpoints: 'all',
              line: {
                width: 1
              },
              marker: {
                size: 2.5
              },
              pointpos: 0,
              type: 'box'
            })
            traces.push({
              x: scz_x,
              y: scz_val_normalized,
              name: 'Control',
              boxpoints: 'all',
              line: {
                width: 1
              },
              marker: {
                size: 3
              },
              pointpos: 0,
              visible: false,
              hoverinfo: 'text',
              type: 'box',
              text: scz_notes
            })
          }
          console.log(traces)
          let updatemenus = []
          if (Object.keys(control_exp).length !== 0 && Object.keys(scz_exp).length !== 0) {
            // eslint-disable-next-line camelcase
            let visible_list_original = [true, false, true, false]
            // eslint-disable-next-line camelcase
            let visible_list_normalized = [false, true, false, true]
            updatemenus = [{
              type: 'buttons',
              active: -1,
              pad: {
                r: 30,
                t: 20
              },
              buttons: [{
                label: 'original RPKM',
                method: 'update',
                args: [{'visible': visible_list_original},
                  {
                    'title': 'RPKM without normalization'
                  }]
              },
              {
                label: 'log<sub>2</sub> ( RPKM + 1 )',
                method: 'update',
                args: [{'visible': visible_list_normalized},
                  {
                    'title': 'Adjusted expression (log<sub>2</sub>(RPKM+1))'
                  }]
              }]
            }]
          }
          var layout = {
            updatemenus: updatemenus,
            paper_bgcolor: 'rgb(249, 249, 249)',
            plot_bgcolor: 'rgb(249, 249, 249)',
            height: 400,
            width: 800,
            hovermode: 'closest',
            xaxis: {
              showgrid: true,
              zeroline: false,
              showline: false,
              showticklabels: true,
              titlefont: {
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
            showgrid: true
          }
          this.data = traces
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
