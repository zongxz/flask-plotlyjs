<template>
  <div>
    <Plot
      :data="data"
      :layout="layout"
    />
  </div>
</template>

<script>
import Plot from 'vue-plotly.js'

export default {
  name: 'plotlyButton',
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
    createPlot () {
      const a = [
        {
          'type': 'scatter',
          'visible': true,
          'hoverinfo': 'text',
          'hoverlabel': {
            'font': {
              'size': 10
            }
          },
          'showlegend': false,
          'mode': 'lines',
          'x': [
            350,
            924
          ],
          'y': [
            'ENST00000567536',
            'ENST00000567536'
          ],
          'text': 'Exon, [28858148-28880610]',
          'line': {
            'color': 'rgb(72,130,180)',
            'shape': 'linear',
            'width': 10,
            'simplify': true
          },
          'uid': '301d35'
        },
        {
          'type': 'scatter',
          'visible': true,
          'hoverinfo': 'text',
          'hoverlabel': {
            'font': {
              'size': 10
            }
          },
          'showlegend': false,
          'mode': 'lines',
          'x': [
            564,
            968
          ],
          'y': [
            'ENST00000545570',
            'ENST00000545570'
          ],
          'text': 'Exon, [28875065-28884770]',
          'line': {
            'color': 'rgb(72,130,180)',
            'shape': 'linear',
            'width': 10,
            'simplify': true
          },
          'uid': 'f21cc4'
        },
        {
          'type': 'scatter',
          'visible': true,
          'hoverinfo': 'text',
          'hoverlabel': {
            'font': {
              'size': 10
            }
          },
          'showlegend': false,
          'mode': 'lines',
          'x': [
            684,
            990
          ],
          'y': [
            'ENST00000538342',
            'ENST00000538342'
          ],
          'text': 'Exon, [28875266-28884787]',
          'line': {
            'color': 'rgb(72,130,180)',
            'shape': 'linear',
            'width': 10,
            'simplify': true
          },
          'uid': 'b0fc37'
        },
        {
          'type': 'scatter',
          'visible': true,
          'hoverinfo': 'text',
          'hoverlabel': {
            'font': {
              'size': 10
            }
          },
          'showlegend': false,
          'mode': 'lines',
          'x': [
            748,
            990
          ],
          'y': [
            'ENST00000395532',
            'ENST00000395532'
          ],
          'text': 'Exon, [28875583-28884787]',
          'line': {
            'color': 'rgb(72,130,180)',
            'shape': 'linear',
            'width': 10,
            'simplify': true
          },
          'uid': 'b75a26'
        },
        {
          'type': 'scatter',
          'visible': true,
          'hoverinfo': 'text',
          'hoverlabel': {
            'font': {
              'size': 10
            }
          },
          'showlegend': false,
          'mode': 'lines',
          'x': [
            684,
            968
          ],
          'y': [
            'ENST00000359285',
            'ENST00000359285'
          ],
          'text': 'Exon, [28875266-28884770]',
          'line': {
            'color': 'rgb(72,130,180)',
            'shape': 'linear',
            'width': 10,
            'simplify': true
          },
          'uid': '063f71'
        },
        {
          'type': 'scatter',
          'visible': true,
          'hoverinfo': 'text',
          'hoverlabel': {
            'font': {
              'size': 10
            }
          },
          'showlegend': false,
          'mode': 'lines',
          'x': [
            770,
            990
          ],
          'y': [
            'ENST00000337120',
            'ENST00000337120'
          ],
          'text': 'Exon, [28877414-28884787]',
          'line': {
            'color': 'rgb(72,130,180)',
            'shape': 'linear',
            'width': 10,
            'simplify': true
          },
          'uid': 'e069e8'
        },
        {
          'type': 'scatter',
          'visible': true,
          'hoverinfo': 'text',
          'hoverlabel': {
            'font': {
              'size': 10
            }
          },
          'showlegend': false,
          'mode': 'lines',
          'x': [
            350,
            1078
          ],
          'y': [
            'ENST00000322610',
            'ENST00000322610'
          ],
          'text': 'Exon, [28858148-28885142]',
          'line': {
            'color': 'rgb(72,130,180)',
            'shape': 'linear',
            'width': 10,
            'simplify': true
          },
          'uid': 'b6499a'
        },
        {
          'type': 'scatter',
          'visible': true,
          'hoverinfo': 'text',
          'hoverlabel': {
            'font': {
              'size': 13
            }
          },
          'showlegend': false,
          'mode': 'lines',
          'x': [
            860,
            863
          ],
          'y': [
            'Variant',
            'Variant'
          ],
          'text': 'chr16 g.28880342G>A,nonsynonymous SNV',
          'line': {
            'color': 'red',
            'shape': 'linear',
            'width': 10,
            'simplify': true
          },
          'uid': 'c5d65b'
        }
      ]
      // const b = []
      // const c = []
      // for (let i = 0; i < 62; i++) {
      //   b.push(true)
      //   c.push(false)
      // }
      // for (let i = 0; i < 8; i++) {
      //   b.push(false)
      //   c.push(true)
      // }
      // const traces = []
      // const xList = [[8, 10], [3, 5], [5, 20], [20, 35], [6, 22], [22, 36]]
      // const yList = [[3, 3], [2, 2], [2, 2], [2, 2], [1, 1], [1, 1]]
      // for (let i = 0; i < xList.length; i++) {
      //   traces.push({
      //     type: 'scatter',
      //     visible: true,
      //     hoverinfo: 'text',
      //     hoverlabel: {
      //       'font': {
      //         'size': 10
      //       }
      //     },
      //     showlegend: false,
      //     mode: 'lines',
      //     x: xList[i],
      //     y: yList[i],
      //     line: {
      //       color: 'rgb(72,130,180)',
      //       shape: 'linear',
      //       width: 10,
      //       simplify: true
      //     }
      //   })
      // }
      // const xList1 = [[8, 10], [5, 20], [6, 22]]
      // const yList1 = [[3, 3], [2, 2], [1, 1]]
      // for (let i = 0; i < xList1.length; i++) {
      //   traces.push({
      //     type: 'scatter',
      //     visible: true,
      //     hoverinfo: 'text',
      //     hoverlabel: {
      //       'font': {
      //         'size': 10
      //       }
      //     },
      //     showlegend: false,
      //     mode: 'lines',
      //     x: xList1[i],
      //     y: yList1[i],
      //     line: {
      //       color: 'rgb(72,130,180)',
      //       shape: 'linear',
      //       width: 10,
      //       simplify: true
      //     }
      //   })
      // }
      const layout = {
        paper_bgcolor: 'rgb(249, 249, 249)',
        plot_bgcolor: 'rgb(249, 249, 249)',
        width: 1200,
        height: 540,
        hovermode: 'closest',
        spikedistance: 0,
        hoverdistance: 2,
        xaxis: {
          range: [0, 1750],
          showgrid: false,
          zeroline: false,
          showline: false,
          showticklabels: false,
          autorange: false,
          dtick: 100
        },
        yaxis: {
          range: ['ENST00000569651', 'Variant'],
          titlefont: {
            family: 'Arial, sans-serif',
            size: 20,
            color: 'lightgrey'
          },
          showticklabels: true,
          tickangle: 360,
          tickfont: {
            family: 'Arial, serif',
            size: 12,
            color: 'black'
          },
          exponentformat: 'e',
          showexponent: 'ALL'
        },
        margin: {
          l: 130,
          r: 5,
          t: 30,
          pad: 0
        }
      }
      console.log(a)
      this.data = a
      this.layout = layout
    }
  },
  created () {
    this.createPlot()
  }
}
</script>

<style scoped>

</style>
