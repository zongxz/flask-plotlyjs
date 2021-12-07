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
      const a = [{
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
          946,
          1056
        ],
        'y': [
          'ENST00000569651',
          'ENST00000569651'
        ],
        'text': 'Exon, [28883573-28884996]',
        'line': {
          'color': 'rgb(72,130,180)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '4de71c'
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
        'uid': '9efc9e'
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
          500,
          792
        ],
        'y': [
          'ENST00000566209',
          'ENST00000566209'
        ],
        'text': 'Exon, [28874487-28877585]',
        'line': {
          'color': 'rgb(72,130,180)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '5aa462'
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
          814
        ],
        'y': [
          'ENST00000563591',
          'ENST00000563591'
        ],
        'text': 'Exon, [28858148-28877605]',
        'line': {
          'color': 'rgb(72,130,180)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '5a3a79'
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
        'uid': '32b73d'
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
        'uid': '732bf8'
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
        'uid': '8797be'
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
        'uid': '4a8f41'
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
        'uid': '410248'
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
        'uid': '35cd31'
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
          1056,
          1122
        ],
        'y': [
          'ENST00000569651',
          'ENST00000569651'
        ],
        'text': 'Untranslated region, [28884996-28885214]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '96c05e'
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
          880,
          902
        ],
        'y': [
          'ENST00000569471',
          'ENST00000569471'
        ],
        'text': 'Untranslated region, [28880414-28880418]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': 'e6e59a'
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
          276,
          350
        ],
        'y': [
          'ENST00000567536',
          'ENST00000567536'
        ],
        'text': 'Untranslated region, [28857963-28858148]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': 'c688fb'
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
          468,
          500
        ],
        'y': [
          'ENST00000566209',
          'ENST00000566209'
        ],
        'text': 'Untranslated region, [28874350-28874487]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': 'f64d1a'
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
          662,
          684
        ],
        'y': [
          'ENST00000563674',
          'ENST00000563674'
        ],
        'text': 'Untranslated region, [28875198-28875266]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '428f26'
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
          234,
          350
        ],
        'y': [
          'ENST00000563591',
          'ENST00000563591'
        ],
        'text': 'Untranslated region, [28857920-28858148]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': 'fff870'
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
          836,
          858
        ],
        'y': [
          'ENST00000561629',
          'ENST00000561629'
        ],
        'text': 'Untranslated region, [28878474-28878719]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '58cdde'
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
          532,
          564
        ],
        'y': [
          'ENST00000545570',
          'ENST00000545570'
        ],
        'text': 'Untranslated region, [28874879-28875065]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '3c28a3'
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
          968,
          1034
        ],
        'y': [
          'ENST00000545570',
          'ENST00000545570'
        ],
        'text': 'Untranslated region, [28884770-28884948]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '3994de'
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
          608,
          684
        ],
        'y': [
          'ENST00000538342',
          'ENST00000538342'
        ],
        'text': 'Untranslated region, [28875126-28875266]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': 'fe55aa'
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
          990,
          1100
        ],
        'y': [
          'ENST00000538342',
          'ENST00000538342'
        ],
        'text': 'Untranslated region, [28884787-28885144]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '8d8477'
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
          716,
          748
        ],
        'y': [
          'ENST00000395532',
          'ENST00000395532'
        ],
        'text': 'Untranslated region, [28875295-28875583]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '47de78'
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
          990,
          1012
        ],
        'y': [
          'ENST00000395532',
          'ENST00000395532'
        ],
        'text': 'Untranslated region, [28884787-28884928]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': 'cefe09'
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
          586,
          684
        ],
        'y': [
          'ENST00000359285',
          'ENST00000359285'
        ],
        'text': 'Untranslated region, [28875125-28875266]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': 'dab285'
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
          968,
          1166
        ],
        'y': [
          'ENST00000359285',
          'ENST00000359285'
        ],
        'text': 'Untranslated region, [28884770-28885526]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': 'ccc83c'
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
          436,
          770
        ],
        'y': [
          'ENST00000337120',
          'ENST00000337120'
        ],
        'text': 'Untranslated region, [28874124-28877414]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '89e5a5'
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
          990,
          1144
        ],
        'y': [
          'ENST00000337120',
          'ENST00000337120'
        ],
        'text': 'Untranslated region, [28884787-28885522]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '6800f8'
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
          318,
          350
        ],
        'y': [
          'ENST00000322610',
          'ENST00000322610'
        ],
        'text': 'Untranslated region, [28858009-28858148]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': 'a9ad8d'
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
          1078,
          1166
        ],
        'y': [
          'ENST00000322610',
          'ENST00000322610'
        ],
        'text': 'Untranslated region, [28885142-28885526]',
        'line': {
          'color': 'gray',
          'shape': 'linear',
          'width': 5
        },
        'uid': '1588d3'
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
          224,
          244
        ],
        'y': [
          'Promoter',
          'Promoter'
        ],
        'text': 'p4@SH2B1, chr16:28857916..28857952,+',
        'line': {
          'color': 'rgb(255,165,0)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '57c631'
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
          266,
          286
        ],
        'y': [
          'Promoter',
          'Promoter'
        ],
        'text': 'p9@SH2B1, chr16:28857957..28857969,+',
        'line': {
          'color': 'rgb(255,165,0)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '690a96'
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
          308,
          328
        ],
        'y': [
          'Promoter',
          'Promoter'
        ],
        'text': 'p6@SH2B1, chr16:28858004..28858029,+',
        'line': {
          'color': 'rgb(255,165,0)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'dc599d'
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
          458,
          478
        ],
        'y': [
          'Promoter',
          'Promoter'
        ],
        'text': 'p8@SH2B1, chr16:28874345..28874371,+',
        'line': {
          'color': 'rgb(255,165,0)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '785a14'
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
          522,
          542
        ],
        'y': [
          'Promoter',
          'Promoter'
        ],
        'text': 'p2@SH2B1, chr16:28874860..28874896,+',
        'line': {
          'color': 'rgb(255,165,0)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '3d4f49'
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
          630,
          640
        ],
        'y': [
          'Promoter',
          'Promoter'
        ],
        'text': 'p1@SH2B1, chr16:28875133..28875195,+',
        'line': {
          'color': 'rgb(255,165,0)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'eaadb4'
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
          706,
          726
        ],
        'y': [
          'Promoter',
          'Promoter'
        ],
        'text': 'p3@SH2B1, chr16:28875268..28875317,+',
        'line': {
          'color': 'rgb(255,165,0)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '0336e8'
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
          404,
          414
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028873, [28873680 - 28873829], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '5247b5'
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
          128,
          138
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028828, [28828651 - 28828866], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '096fcd'
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
          1188,
          1198
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028945, [28945201 - 28946289], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '754de5'
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
          1220,
          1230
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028973, [28973536 - 28975907], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'c25879'
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
          160,
          170
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028844, [28844721 - 28847684], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'b42ba6'
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
          32,
          42
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028490, [28490586 - 28497469], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'b2946d'
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
          1636,
          1646
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029819, [29819165 - 29826663], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '4e2a08'
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
          1252,
          1262
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029026, [29026365 - 29027107], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '5ab8a4'
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
          192,
          202
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028849, [28849656 - 28850048], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '40474c'
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
          1540,
          1550
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029789, [29789582 - 29793001], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'b306eb'
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
          372,
          382
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028861, [28861845 - 28867395], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '553e1e'
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
          64,
          74
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028585, [28585600 - 28586469], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '0e14c4'
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
          1476,
          1486
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029708, [29708600 - 29712047], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '853036'
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
          0,
          10
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028209, [28209840 - 28213364], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '56774c'
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
          1668,
          1678
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029845, [29845192 - 29845567], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '3ecf4f'
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
          96,
          106
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I028821, [28821934 - 28826329], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'cf20bb'
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
          1412,
          1422
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029608, [29608476 - 29609919], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'd08fd3'
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
          1572,
          1582
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029803, [29803283 - 29813603], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'de49be'
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
          1348,
          1358
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029258, [29258969 - 29270285], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '9621eb'
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
          1444,
          1454
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029611, [29611214 - 29616807], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '00c9f8'
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
          1604,
          1614
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029813, [29813631 - 29817619], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '7450e8'
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
          1380,
          1390
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029273, [29273600 - 29274200], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': '34e7e9'
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
          1508,
          1518
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029736, [29736235 - 29742058], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'ebfc11'
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
          1284,
          1294
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029111, [29111064 - 29112737], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'f4306a'
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
          1316,
          1326
        ],
        'y': [
          'Enhancer',
          'Enhancer'
        ],
        'text': 'GH16I029143, [29143815 - 29145433], local',
        'line': {
          'color': 'rgb(144,238,144)',
          'shape': 'linear',
          'width': 10,
          'simplify': true
        },
        'uid': 'e43070'
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
      }]
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
      // const updatemenus = [{
      //   type: 'buttons',
      //   active: -1,
      //   pad: {
      //     r: 100,
      //     t: 20
      //   },
      //   buttons: [{
      //     label: 'original TPM',
      //     method: 'update',
      //     args: [{'visible': b}]
      //   },
      //   {
      //     label: 'log<sub>2</sub> ( TPM + 1 )',
      //     method: 'update',
      //     args: [{'visible': c}]
      //   }]
      // }]
      const layout = {
        // updatemenus: updatemenus,
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
