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
  name: 'GeneSpan',
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
      let url = 'http://127.0.0.1:5000/brainSpanData'
      axios.get(url)
        .then((res) => {
          // eslint-disable-next-line camelcase
          function brain_dic () {
            // eslint-disable-next-line camelcase
            let brain_list = {'10': ['13', 'amygdala', '20-39Y'],
              '22': ['12', 'cerebellum', '12-19Y'],
              '100': ['8', 'cortex', '0-5M'],
              '179': ['2', 'striatum', '8-9PCW'],
              '96': ['8', 'cortex', '0-5M'],
              '158': ['14', 'cortex', '40Y'],
              '117': ['10', 'cortex', '1-5Y'],
              '137': ['12', 'cortex', '12-19Y'],
              '113': ['10', 'cortex', '1-5Y'],
              '53': ['4', 'cortex', '13-15PCW'],
              '140': ['12', 'cortex', '12-19Y'],
              '38': ['3', 'cortex', '10-12PCW'],
              '70': ['6', 'cortex', '19-23PCW'],
              '183': ['6', 'striatum', '19-23PCW'],
              '55': ['4', 'cortex', '13-15PCW'],
              '24': ['14', 'cerebellum', '40Y'],
              '157': ['14', 'cortex', '40Y'],
              '73': ['6', 'cortex', '19-23PCW'],
              '185': ['8', 'striatum', '0-5M'],
              '126': ['11', 'cortex', '6-11Y'],
              '145': ['13', 'cortex', '20-39Y'],
              '175': ['13', 'hippocampus', '20-39Y'],
              '74': ['6', 'cortex', '19-23PCW'],
              '45': ['3', 'cortex', '10-12PCW'],
              '88': ['7', 'cortex', '24-37PCW'],
              '7': ['10', 'amygdala', '1-5Y'],
              '65': ['5', 'cortex', '16-18PCW'],
              '78': ['6', 'cortex', '19-23PCW'],
              '156': ['14', 'cortex', '40Y'],
              '119': ['10', 'cortex', '1-5Y'],
              '104': ['9', 'cortex', '6-11M'],
              '76': ['6', 'cortex', '19-23PCW'],
              '69': ['6', 'cortex', '19-23PCW'],
              '184': ['7', 'striatum', '24-37PCW'],
              '60': ['5', 'cortex', '16-18PCW'],
              '17': ['7', 'cerebellum', '24-37PCW'],
              '182': ['5', 'striatum', '16-18PCW'],
              '39': ['3', 'cortex', '10-12PCW'],
              '85': ['7', 'cortex', '24-37PCW'],
              '169': ['6', 'hippocampus', '19-23PCW'],
              '49': ['4', 'cortex', '13-15PCW'],
              '177': ['2', 'striatum', '8-9PCW'],
              '148': ['13', 'cortex', '20-39Y'],
              '18': ['8', 'cerebellum', '0-5M'],
              '187': ['11', 'striatum', '6-11Y'],
              '149': ['13', 'cortex', '20-39Y'],
              '142': ['12', 'cortex', '12-19Y'],
              '13': ['3', 'cerebellum', '10-12PCW'],
              '97': ['8', 'cortex', '0-5M'],
              '20': ['10', 'cerebellum', '1-5Y'],
              '42': ['3', 'cortex', '10-12PCW'],
              '153': ['13', 'cortex', '20-39Y'],
              '12': ['2', 'cerebellum', '8-9PCW'],
              '71': ['6', 'cortex', '19-23PCW'],
              '56': ['4', 'cortex', '13-15PCW'],
              '132': ['11', 'cortex', '6-11Y'],
              '58': ['5', 'cortex', '16-18PCW'],
              '164': ['14', 'cortex', '40Y'],
              '84': ['7', 'cortex', '24-37PCW'],
              '26': ['2', 'cortex', '8-9PCW'],
              '90': ['7', 'cortex', '24-37PCW'],
              '89': ['7', 'cortex', '24-37PCW'],
              '116': ['10', 'cortex', '1-5Y'],
              '87': ['7', 'cortex', '24-37PCW'],
              '201': ['12', 'thalamus', '12-19Y'],
              '44': ['3', 'cortex', '10-12PCW'],
              '166': ['3', 'hippocampus', '10-12PCW'],
              '8': ['11', 'amygdala', '6-11Y'],
              '43': ['3', 'cortex', '10-12PCW'],
              '32': ['2', 'cortex', '8-9PCW'],
              '172': ['10', 'hippocampus', '1-5Y'],
              '25': ['2', 'cortex', '8-9PCW'],
              '155': ['14', 'cortex', '40Y'],
              '167': ['4', 'hippocampus', '13-15PCW'],
              '129': ['11', 'cortex', '6-11Y'],
              '122': ['11', 'cortex', '6-11Y'],
              '178': ['2', 'striatum', '8-9PCW'],
              '46': ['4', 'cortex', '13-15PCW'],
              '165': ['2', 'hippocampus', '8-9PCW'],
              '64': ['5', 'cortex', '16-18PCW'],
              '1': ['3', 'amygdala', '10-12PCW'],
              '174': ['12', 'hippocampus', '12-19Y'],
              '202': ['13', 'thalamus', '20-39Y'],
              '168': ['5', 'hippocampus', '16-18PCW'],
              '108': ['9', 'cortex', '6-11M'],
              '109': ['9', 'cortex', '6-11M'],
              '139': ['12', 'cortex', '12-19Y'],
              '79': ['6', 'cortex', '19-23PCW'],
              '198': ['9', 'thalamus', '6-11M'],
              '147': ['13', 'cortex', '20-39Y'],
              '86': ['7', 'cortex', '24-37PCW'],
              '128': ['11', 'cortex', '6-11Y'],
              '134': ['12', 'cortex', '12-19Y'],
              '59': ['5', 'cortex', '16-18PCW'],
              '72': ['6', 'cortex', '19-23PCW'],
              '23': ['13', 'cerebellum', '20-39Y'],
              '127': ['11', 'cortex', '6-11Y'],
              '195': ['6', 'thalamus', '19-23PCW'],
              '162': ['14', 'cortex', '40Y'],
              '94': ['8', 'cortex', '0-5M'],
              '66': ['5', 'cortex', '16-18PCW'],
              '57': ['5', 'cortex', '16-18PCW'],
              '37': ['3', 'cortex', '10-12PCW'],
              '131': ['11', 'cortex', '6-11Y'],
              '81': ['7', 'cortex', '24-37PCW'],
              '152': ['13', 'cortex', '20-39Y'],
              '159': ['14', 'cortex', '40Y'],
              '11': ['14', 'amygdala', '40Y'],
              '16': ['6', 'cerebellum', '19-23PCW'],
              '154': ['13', 'cortex', '20-39Y'],
              '144': ['13', 'cortex', '20-39Y'],
              '14': ['4', 'cerebellum', '13-15PCW'],
              '40': ['3', 'cortex', '10-12PCW'],
              '31': ['2', 'cortex', '8-9PCW'],
              '82': ['7', 'cortex', '24-37PCW'],
              '54': ['4', 'cortex', '13-15PCW'],
              '123': ['11', 'cortex', '6-11Y'],
              '136': ['12', 'cortex', '12-19Y'],
              '121': ['10', 'cortex', '1-5Y'],
              '61': ['5', 'cortex', '16-18PCW'],
              '110': ['9', 'cortex', '6-11M'],
              '67': ['5', 'cortex', '16-18PCW'],
              '146': ['13', 'cortex', '20-39Y'],
              '91': ['7', 'cortex', '24-37PCW'],
              '34': ['2', 'cortex', '8-9PCW'],
              '193': ['4', 'thalamus', '13-15PCW'],
              '80': ['6', 'cortex', '19-23PCW'],
              '192': ['3', 'thalamus', '10-12PCW'],
              '194': ['5', 'thalamus', '16-18PCW'],
              '99': ['8', 'cortex', '0-5M'],
              '190': ['14', 'striatum', '40Y'],
              '93': ['8', 'cortex', '0-5M'],
              '133': ['12', 'cortex', '12-19Y'],
              '19': ['9', 'cerebellum', '6-11M'],
              '150': ['13', 'cortex', '20-39Y'],
              '186': ['10', 'striatum', '1-5Y'],
              '77': ['6', 'cortex', '19-23PCW'],
              '63': ['5', 'cortex', '16-18PCW'],
              '107': ['9', 'cortex', '6-11M'],
              '114': ['10', 'cortex', '1-5Y'],
              '200': ['11', 'thalamus', '6-11Y'],
              '143': ['12', 'cortex', '12-19Y'],
              '124': ['11', 'cortex', '6-11Y'],
              '120': ['10', 'cortex', '1-5Y'],
              '112': ['10', 'cortex', '1-5Y'],
              '203': ['14', 'thalamus', '40Y'],
              '191': ['2', 'thalamus', '8-9PCW'],
              '130': ['11', 'cortex', '6-11Y'],
              '28': ['2', 'cortex', '8-9PCW'],
              '196': ['7', 'thalamus', '24-37PCW'],
              '15': ['5', 'cerebellum', '16-18PCW'],
              '105': ['9', 'cortex', '6-11M'],
              '163': ['14', 'cortex', '40Y'],
              '138': ['12', 'cortex', '12-19Y'],
              '125': ['11', 'cortex', '6-11Y'],
              '118': ['10', 'cortex', '1-5Y'],
              '5': ['7', 'amygdala', '24-37PCW'],
              '173': ['11', 'hippocampus', '6-11Y'],
              '141': ['12', 'cortex', '12-19Y'],
              '160': ['14', 'cortex', '40Y'],
              '180': ['3', 'striatum', '10-12PCW'],
              '36': ['3', 'cortex', '10-12PCW'],
              '30': ['2', 'cortex', '8-9PCW'],
              '3': ['5', 'amygdala', '16-18PCW'],
              '151': ['13', 'cortex', '20-39Y'],
              '135': ['12', 'cortex', '12-19Y'],
              '4': ['6', 'amygdala', '19-23PCW'],
              '68': ['5', 'cortex', '16-18PCW'],
              '98': ['8', 'cortex', '0-5M'],
              '50': ['4', 'cortex', '13-15PCW'],
              '115': ['10', 'cortex', '1-5Y'],
              '106': ['9', 'cortex', '6-11M'],
              '75': ['6', 'cortex', '19-23PCW'],
              '176': ['14', 'hippocampus', '40Y'],
              '161': ['14', 'cortex', '40Y'],
              '171': ['8', 'hippocampus', '0-5M'],
              '41': ['3', 'cortex', '10-12PCW'],
              '2': ['4', 'amygdala', '13-15PCW'],
              '83': ['7', 'cortex', '24-37PCW'],
              '52': ['4', 'cortex', '13-15PCW'],
              '27': ['2', 'cortex', '8-9PCW'],
              '189': ['13', 'striatum', '20-39Y'],
              '33': ['2', 'cortex', '8-9PCW'],
              '181': ['4', 'striatum', '13-15PCW'],
              '199': ['10', 'thalamus', '1-5Y'],
              '48': ['4', 'cortex', '13-15PCW'],
              '21': ['11', 'cerebellum', '6-11Y'],
              '47': ['4', 'cortex', '13-15PCW'],
              '95': ['8', 'cortex', '0-5M'],
              '6': ['8', 'amygdala', '0-5M'],
              '111': ['10', 'cortex', '1-5Y'],
              '92': ['8', 'cortex', '0-5M'],
              '51': ['4', 'cortex', '13-15PCW'],
              '9': ['12', 'amygdala', '12-19Y'],
              '29': ['2', 'cortex', '8-9PCW'],
              '0': ['2', 'amygdala', '8-9PCW'],
              '103': ['9', 'cortex', '6-11M'],
              '188': ['12', 'striatum', '12-19Y'],
              '197': ['8', 'thalamus', '0-5M'],
              '170': ['7', 'hippocampus', '24-37PCW'],
              '62': ['5', 'cortex', '16-18PCW'],
              '102': ['8', 'cortex', '0-5M'],
              '101': ['8', 'cortex', '0-5M'],
              '35': ['3', 'cortex', '10-12PCW']}
            // eslint-disable-next-line camelcase
            return brain_list
          }
          // eslint-disable-next-line camelcase
          function dict_gene2 (id, data) {
            // eslint-disable-next-line camelcase,no-unused-vars
            let brainSpan_key = brain_dic()
            // eslint-disable-next-line camelcase
            let data_brainSpan = data['BrainspanX'][0]
            delete data_brainSpan['ENTREZ_ID']
            // eslint-disable-next-line camelcase
            let data_brainSpan_key = []
            // eslint-disable-next-line camelcase
            let data_brainSpan_value = []
            // eslint-disable-next-line camelcase
            for (let item in data_brainSpan) {
              data_brainSpan_key.push(Number(item))
              data_brainSpan_value.push(parseFloat(data_brainSpan[item]))
            }
            // eslint-disable-next-line camelcase,no-unused-vars
            let others_type = ['amygdala', 'cerebellum', 'hippocampus', 'thalamus']
            // let newData = {}
            // eslint-disable-next-line camelcase,no-unused-vars
            let max_value = Math.log2(Math.max(...data_brainSpan_value) + 1.0)
            // eslint-disable-next-line camelcase
            // eslint-disable-next-line camelcase
            let list_others_data = []
            for (let i = 0; i < 4; i++) {
              list_others_data[i] = []
              for (let j = 0; j < 13; j++) {
                list_others_data[i][j] = ''
              }
            }
            let brainSpanData = []
            // eslint-disable-next-line camelcase
            for (let item in brainSpan_key) {
              brainSpanData.push(brainSpan_key[item])
            }
            brainSpanData.sort(function (x, y) {
              return x[1] - y[1]
            })
            for (let i = 0; i < brainSpanData.length; i++) {
              if (others_type.includes(brainSpanData[i][1])) {
                // eslint-disable-next-line camelcase
                let loc_type = others_type.indexOf(brainSpanData[i][1])
                let p = brainSpanData[i][0]
                list_others_data[loc_type][p - 2] = Math.log2(data_brainSpan_value[i] + 1.0)
              }
            }
            // eslint-disable-next-line camelcase
            let list_special_cortex = []
            for (let i = 0; i < 13; i++) {
              list_special_cortex[i] = []
            }
            // eslint-disable-next-line camelcase
            let list_special_striatum = []
            for (let i = 0; i < 13; i++) {
              list_special_striatum[i] = []
            }
            for (let i = 0; i < brainSpanData.length; i++) {
              if (['cortex'].includes(brainSpanData[i][1])) {
                let p = brainSpanData[i][0]
                list_special_cortex[p - 2].push(Math.log2(data_brainSpan_value[i] + 1.0))
              }
              if (['striatum'].includes(brainSpanData[i][1])) {
                let p = brainSpanData[i][0]
                list_special_striatum[p - 2].push(Math.log2(data_brainSpan_value[i] + 1.0))
              }
            }
            // eslint-disable-next-line camelcase
            return [others_type, list_others_data, list_special_striatum, list_special_cortex, max_value]
          }
          let id = res.data[0]
          let data = res.data[1]
          console.log(data)
          // eslint-disable-next-line camelcase
          let others_type = dict_gene2(id, data)[0]
          // eslint-disable-next-line camelcase
          let list_others_data = dict_gene2(id, data)[1]
          // eslint-disable-next-line camelcase
          let list_special_striatum = dict_gene2(id, data)[2]
          // eslint-disable-next-line camelcase
          let list_special_cortex = dict_gene2(id, data)[3]
          // let max = res.data[5]
          let traces = []
          // eslint-disable-next-line camelcase,no-unused-vars
          let line_special = []
          let colors = ['rgb(127,127,127)', 'rgb(188,189,34)', '#BC3C29FF', '#20854EFF',
            'rgb(0,0,0)', 'rgb(188,188,34)', 'rgb(144,238,144)']
          // eslint-disable-next-line camelcase
          if (others_type !== 0) {
            // eslint-disable-next-line no-unused-vars
            let i = 0
            let attr = ['Early fetal\n8-9PCW', 'Early fetal\n10-12PCW', 'Early mid-fetal\n13PCW-15PCW',
              'Early mid-fetal\n16PCW-18PCW',
              'Late mid-fetal\n19PCW-23PCW', 'Late fetal\n24PCW-37PCW',
              'Neonatal and early infancy\n0M(birth)-5M',
              'Late infancy\n6M-11M', 'Early childhood\n1Y-5Y', 'Middle and late childhood\n6Y-11Y',
              'Adolescence\n12Y-19Y', 'Young adulthood\n20Y-39Y', 'Middle adulthood\n40Y']
            // eslint-disable-next-line camelcase
            let list_tmp_striatum_ave = []
            // eslint-disable-next-line camelcase
            let list_tmp_striatum_num = []
            for (let j = 0; j < 13; j++) {
              list_tmp_striatum_ave.push(0)
              list_tmp_striatum_num.push(0)
            }
            for (let j = 0; j < 13; j++) {
              if (list_special_striatum[j].length !== 0) {
                for (let k = 0; k < list_special_striatum[j].length; k++) {
                  let item = list_special_striatum[j][k]

                  list_tmp_striatum_ave[j] += item
                  list_tmp_striatum_num[j] += 1
                }
              }
              if (list_special_striatum[j].length === 0) {
                list_tmp_striatum_ave[j] = ''
              }
            }

            for (let j = 0; j < 13; j++) {
              if (list_tmp_striatum_ave[j] !== '') {
                list_tmp_striatum_ave[j] = list_tmp_striatum_ave[j] / list_tmp_striatum_num[j]
              }
            }
            traces.push({
              x: attr,
              y: list_tmp_striatum_ave,
              type: 'scatter',
              name: 'striatum',
              line: {
                shape: 'spline',
                color: 'rgb(155, 48, 255)'
              },
              mode: 'lines'
            })
            // eslint-disable-next-line camelcase
            let list_tmp_cortex_ave = []
            // eslint-disable-next-line camelcase
            let list_tmp_cortex_num = []
            for (let j = 0; j < 13; j++) {
              list_tmp_cortex_ave.push(0)
              list_tmp_cortex_num.push(0)
            }
            for (let j = 0; j < 13; j++) {
              if (list_special_cortex[j].length !== 0) {
                for (let k = 0; k < list_special_cortex[j].length; k++) {
                  let item = list_special_cortex[j][k]
                  list_tmp_cortex_ave[j] += item
                  list_tmp_cortex_num[j] += 1
                }
              }
              if (list_special_cortex[j].length === 0) {
                list_tmp_cortex_ave[j] = ''
              }
            }
            for (let j = 0; j < 13; j++) {
              if (list_tmp_cortex_ave[j] !== '') {
                list_tmp_cortex_ave[j] = list_tmp_cortex_ave[j] / list_tmp_cortex_num[j]
              }
            }
            traces.push({
              x: attr,
              y: list_tmp_cortex_ave,
              type: 'scatter',
              name: 'cortex',
              line: {
                shape: 'spline',
                color: 'rgb(122,197,205)'
              },
              mode: 'lines'
            })
            // eslint-disable-next-line camelcase
            let max_length_striatum = 0
            for (let j = 0; j < list_special_striatum.length; j++) {
              let item = list_special_striatum[j]
              // eslint-disable-next-line camelcase
              if (item.length >= max_length_striatum) {
                // eslint-disable-next-line camelcase
                max_length_striatum = item.length
              }
            }

            for (let j = 0; j < 13; j++) {
              let len = list_special_striatum[j].length
              // eslint-disable-next-line camelcase
              if (len < max_length_striatum) {
                // eslint-disable-next-line camelcase
                let l = max_length_striatum - len
                for (let k = 0; k < l; k++) {
                  list_special_striatum[j].push('')
                }
              }
            }
            // eslint-disable-next-line camelcase
            let max_length_cortex = 0
            for (let j = 0; j < list_special_cortex.length; j++) {
              let item = list_special_cortex[j]
              // eslint-disable-next-line camelcase
              if (item.length >= max_length_cortex) {
                // eslint-disable-next-line camelcase
                max_length_cortex = item.length
              }
            }

            for (let j = 0; j < 13; j++) {
              let len = list_special_cortex[j].length
              // eslint-disable-next-line camelcase
              if (len < max_length_cortex) {
                // eslint-disable-next-line camelcase
                let l = max_length_cortex - len
                for (let k = 0; k < l; k++) {
                  list_special_cortex[j].push('')
                }
              }
            }
            // eslint-disable-next-line camelcase
            for (let j = 0; j < max_length_striatum; j++) {
              // eslint-disable-next-line camelcase
              let list_tmp_striatum = []
              for (let k = 0; k < 13; k++) {
                list_tmp_striatum.push(list_special_striatum[k][j])
              }

              traces.push({
                x: attr,
                y: list_tmp_striatum,
                type: 'scatter',
                mode: 'markers',
                marker: {
                  color: 'rgb(155, 48, 255)'
                },
                showlegend: false,
                hoverinfo: 'all',
                name: 'striatum'
              })
            }

            // eslint-disable-next-line camelcase
            for (let j = 0; j < max_length_cortex; j++) {
              // eslint-disable-next-line camelcase
              let list_linshi_cortex = []
              for (let k = 0; k < 13; k++) {
                list_linshi_cortex.push(list_special_cortex[k][j])
              }
              traces.push({
                x: attr,
                y: list_linshi_cortex,
                type: 'scatter',
                mode: 'markers',
                marker: {
                  color: 'rgb(122,197,205)'
                },
                showlegend: false,
                name: 'cortex'
              })
            }
            let t = 0
            for (let j = 0; j < others_type.length; j++) {
              let item = others_type[j]
              traces.push({
                x: attr,
                y: list_others_data[t],
                name: item,
                line: {
                  shape: 'spline',
                  color: colors[j]
                },
                mode: 'lines'
              })
              t += 1
            }
          }
          let layout = {
            paper_bgcolor: 'rgb(249, 249, 249)',
            plot_bgcolor: 'rgb(249, 249, 249)',
            width: 1000,
            height: 400,
            hovermode: 'closest',
            xaxis: {
              showgrid: true,
              zeroline: true,
              showline: true,
              showticklabels: true,
              tickangle: 25,
              titlefont: {
                family: 'Arial'
              }
            },
            yaxis: {
              autorange: true,
              showgrid: true,
              zeroline: true,
              title: 'log<sub>2</sub> ( RPKM + 1 )',
              titlefont:
                        {
                          family: 'Arial'
                        }
            },
            margin: {
              l: 50,
              r: 10,
              t: 30,
              b: 100
            },
            showlegend: true
          }
          this.data = traces
          this.layout = layout
          // let a = 85358
          // let b = {'_id': '5b6297da5404074d469d8d42', 'hippocampus': [{'endothelial': '0', 'neurons': '0', 'oligodendrocytes': '1.33', 'hybrid': '0', 'microglia': '0', 'OPC': '0.88', 'ENTREZ_ID': '85358'}], 'cortex': [{'endothelial': '9.703', 'neurons': '4.507', 'oligodendrocytes': '0.354', 'hybrid': '11.772', 'fetal_quiescent': '3.162', 'microglia': '0', 'fetal_replicating': '0.88', 'OPC': '0', 'astrocytes': '5.125', 'ENTREZ_ID': '85358'}], 'Symbol': 'SHANK3', 'BrainspanX': [{'0': '3.53753', '1': '3.61649', '2': '4.72832', '3': '5.01201', '4': '7.13319', '5': '8.71985', '6': '29.29917', '7': '17.66796', '8': '18.53293', '9': '24.92579', '10': '20.21056', '11': '15.5256', '12': '7.31276', '13': '3.97841', '14': '8.33412', '15': '5.54567', '16': '5.6013', '17': '7.30069', '18': '21.56792', '19': '62.01878', '20': '36.25003', '21': '32.28297', '22': '30.38393', '23': '33.40044', '24': '24.0422', '25': '2.43373', '26': '2.91428', '27': '3.2505', '28': '1.66714', '29': '3.48779', '30': '3.73505', '31': '3.94151', '32': '3.82901', '33': '2.93128', '34': '3.24922', '35': '3.02441', '36': '3.80441', '37': '2.38254', '38': '2.42518', '39': '4.26287', '40': '3.19014', '41': '2.68379', '42': '3.18345', '43': '4.37465', '44': '2.61253', '45': '4.51499', '46': '3.27505', '47': '2.89887', '48': '2.02891', '49': '2.99498', '50': '3.98869', '51': '4.23403', '52': '3.97014', '53': '2.99538', '54': '3.29341', '55': '3.40256', '56': '5.10893', '57': '5.26511', '58': '5.16007', '59': '5.73451', '60': '6.76094', '61': '2.49263', '62': '5.79406', '63': '4.43926', '64': '6.22729', '65': '5.9712', '66': '6.71098', '67': '6.30768', '68': '5.53755', '69': '7.7415', '70': '8.00552', '71': '7.60335', '72': '8.08336', '73': '6.95585', '74': '5.9778', '75': '6.37257', '76': '6.74351', '77': '10.06933', '78': '9.35845', '79': '8.99193', '80': '7.10773', '81': '11.13945', '82': '11.28603', '83': '10.36835', '84': '19.11009', '85': '11.05136', '86': '11.43224', '87': '9.9039', '88': '12.03641', '89': '9.38305', '90': '12.66701', '91': '11.69013', '92': '24.23163', '93': '23.2708', '94': '18.5256', '95': '23.63621', '96': '23.3736', '97': '31.57223', '98': '28.536', '99': '18.26992', '100': '20.08821', '101': '18.50969', '102': '36.08047', '103': '25.08998', '104': '37.27468', '105': '23.8377', '106': '22.12258', '107': '33.16521', '108': '27.75505', '109': '32.43419', '110': '47.927', '111': '17.67176', '112': '17.64551', '113': '16.72618', '114': '14.56832', '115': '19.33634', '116': '22.57847', '117': '15.63344', '118': '19.76724', '119': '16.41198', '120': '17.79843', '121': '17.71962', '122': '17.53217', '123': '15.77588', '124': '19.84996', '125': '17.84878', '126': '11.47035', '127': '10.07869', '128': '15.94575', '129': '23.15445', '130': '19.2657', '131': '13.56893', '132': '21.40749', '133': '31.8937', '134': '21.22387', '135': '28.52801', '136': '25.75007', '137': '20.77339', '138': '21.99901', '139': '27.25498', '140': '18.085', '141': '23.341', '142': '26.87731', '143': '22.93984', '144': '20.84204', '145': '22.40481', '146': '26.28298', '147': '24.23343', '148': '26.26679', '149': '24.70762', '150': '24.26084', '151': '24.68089', '152': '29.18717', '153': '23.97391', '154': '22.95025', '155': '26.54602', '156': '24.57831', '157': '20.32545', '158': '18.68125', '159': '25.93062', '160': '21.59007', '161': '28.66567', '162': '24.09728', '163': '31.98459', '164': '19.58349', '165': '2.84296', '166': '3.01869', '167': '3.96987', '168': '8.25592', '169': '11.23978', '170': '10.70437', '171': '28.82424', '172': '21.58145', '173': '19.41228', '174': '37.9102', '175': '28.90805', '176': '10.27462', '177': '2.33138', '178': '3.98294', '179': '3.4694', '180': '4.48871', '181': '6.76578', '182': '9.35446', '183': '10.07762', '184': '10.6435', '185': '41.00731', '186': '25.06335', '187': '15.90896', '188': '20.20993', '189': '18.73582', '190': '24.50144', '191': '5.08034', '192': '6.78965', '193': '8.49096', '194': '13.43145', '195': '22.79324', '196': '9.08083', '197': '38.85873', '198': '37.36085', '199': '22.46157', '200': '27.82773', '201': '31.20842', '202': '40.73363', '203': '17.95042', 'ENTREZ_ID': '85358'}], 'Gsef': [{'Microglia-GW12': '0', 'OPC-GW26': '9.001666667', 'Neurons-GW10': '6.406236559', 'OPC-GW19': '1.5325', 'Stem cells-GW13': '2.242857143', 'OPC-GW23': '19.1184', 'Neurons-GW23': '4.673932584', 'Microglia-GW19': '0', 'Stem cells-GW19': '0', 'Astrocytes-GW23': '0', 'Stem cells-GW12': '0', 'Stem cells-GW16': '0.90495935', 'OPC-GW12': '0', 'Microglia-GW13': '0', 'GABAergic neurons-GW23': '7.98045977', 'Stem cells-GW23': '0', 'Neurons-GW09': '0.169714286', 'GABAergic neurons-GW09': '0', 'OPC-GW16': '31.99285714', 'Neurons-GW26': '1.742627119', 'Microglia-GW08': '0', 'GABAergic neurons-GW10': '0', 'Stem cells-GW10': '2.208452381', 'GABAergic neurons-GW19': '0', 'Microglia-GW26': '5.37025', 'Microglia-GW16': '0.248181818', 'Microglia-GW23': '7.592', 'GABAergic neurons-GW12': '0', 'Stem cells-GW08': '0', 'Stem cells-GW09': '0', 'Neurons-GW08': '0', 'GABAergic neurons-GW08': '0', 'Neurons-GW12': '0.244603175', 'GABAergic neurons-GW16': '4.56060241', 'Stem cells-GW26': '1.255', 'Astrocytes-GW26': '6.77015873', 'Microglia-GW10': '0', 'Neurons-GW19': '0.401097561', 'Astrocytes-GW19': '0', 'Neurons-GW16': '2.783633028', 'Neurons-GW13': '0', 'GABAergic neurons-GW26': '9.0960199', 'ENTREZ_ID': '85358'}], 'barreslab': [{'Newly Formed Oligodendrocyte': '2.6', 'Microglia': '4.0', 'Neuron': '9.8', 'Endothelial Cells': '11.5', 'Myelinating Oligodendrocytes': '3.8', 'Astrocytes': '5.3', 'Oligodendrocyte Precursor Cell': '8.0', 'mean (all other cells)': '5.9', 'ENTREZ_ID': '85358'}], 'ENTREZ_ID': '85358'}

          // dict_gene2(a, b)
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
