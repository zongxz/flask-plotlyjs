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
  name: 'DNMs',
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
      let url = 'http://127.0.0.1:5000/Transcript_DNMsData1'
      axios.get(url)
        .then((res) => {
          let sym = 0
          let exton = 1
          let utr3 = 2
          let utr5 = 3
          let start = 0
          let end = 1
          // eslint-disable-next-line camelcase
          function DNM_sort_by_site (DNM) {
            if (DNM !== [[]]) {
              // eslint-disable-next-line camelcase
              let sorted_DNM = DNM.sort()
              // eslint-disable-next-line camelcase
              return sorted_DNM
            } else {
              return []
            }
          }
          // eslint-disable-next-line camelcase
          function get_all_exton_region (list_3D) {
            // eslint-disable-next-line camelcase
            let all_region = []
            // eslint-disable-next-line camelcase
            for (let item of list_3D) {
              // eslint-disable-next-line camelcase
              for (let item_item of item[exton]) {
                all_region.push(item_item)
              }
              // eslint-disable-next-line camelcase
              for (let item_item of item[utr3]) {
                all_region.push(item_item)
              }
              // eslint-disable-next-line camelcase
              for (let item_item of item[utr5]) {
                all_region.push(item_item)
              }
            }
            // eslint-disable-next-line camelcase
            return all_region
          }
          // 判断二维数组array中是否存在一维数组element
          // eslint-disable-next-line camelcase
          function judgment_array (array, element) {
            for (let el of array) {
              if (el.length === element.length) {
                for (let index in el) {
                  if (el[index] !== element[index]) {
                    break
                  }
                  if (Number(index) === (el.length - 1)) {
                    return true
                  }
                }
              }
            }
            return false
          }
          // eslint-disable-next-line camelcase
          function drop_duplicate (one_list) {
            // eslint-disable-next-line camelcase
            let temp_list = []
            // eslint-disable-next-line camelcase
            for (let one of one_list) {
              if (!judgment_array(temp_list, one)) {
                temp_list.push(one)
              }
            }
            // eslint-disable-next-line camelcase
            return temp_list
          }
          // eslint-disable-next-line camelcase
          function sort_list (all_region) {
            let l = all_region.length
            all_region.sort()
            for (let i = 0; i < l - 1; i++) {
              console.assert(all_region[i][start] <= all_region[i + 1][start], '')
            }
            // eslint-disable-next-line camelcase
            return all_region
          }
          // eslint-disable-next-line camelcase
          function cut_fragment (all_region) {
            // eslint-disable-next-line camelcase
            let all_s = []
            // eslint-disable-next-line camelcase
            let all_e = []
            // eslint-disable-next-line camelcase
            for (let item of all_region) {
              all_s.push(item[start])
              all_e.push(item[end])
            }
            // eslint-disable-next-line camelcase
            let all_se = []
            // eslint-disable-next-line camelcase
            for (let item of all_s) {
              all_se.push(item)
            }
            // eslint-disable-next-line camelcase
            for (let item of all_e) {
              all_se.push(item)
            }
            // eslint-disable-next-line camelcase
            let new_all_se = new Set(all_se.sort())
            // eslint-disable-next-line camelcase
            all_se = Array.from(new_all_se)
            let a = all_se.slice(0, all_se.length - 1)
            let b = all_se.slice(1)
            // eslint-disable-next-line camelcase
            let all_frag = []
            for (let i = 0; i < a.length; i++) {
              all_frag.push([a[i], b[i]])
            }
            // eslint-disable-next-line camelcase
            return all_frag
          }
          // eslint-disable-next-line camelcase
          function get_every_frag_dnm_numbers (all_frag, DNM) {
            // eslint-disable-next-line camelcase
            let DNM_list = []
            for (let item of DNM) {
              DNM_list.push(item[0])
            }
            // eslint-disable-next-line camelcase
            let new_DNM_list = new Set(DNM_list)
            // eslint-disable-next-line camelcase
            DNM_list = Array.from(new_DNM_list)
            let num = Array(all_frag.length).fill(0)
            let i = 0
            // eslint-disable-next-line camelcase
            for (let item of all_frag) {
              // eslint-disable-next-line no-unused-vars
              let k = 0
              // eslint-disable-next-line camelcase
              for (let item_item of DNM_list) {
                // eslint-disable-next-line camelcase
                if (item_item >= item[start] && item_item <= item[end]) {
                  num[i] += 1
                }
                k += 1
              }
              i += 1
            }
            return num
          }
          // eslint-disable-next-line camelcase
          function get_sum (x_list, n) {
            let sum = 0
            for (let i = 0; i < n; i++) {
              sum += x_list[i]
            }
            return sum
          }
          // eslint-disable-next-line camelcase
          function scale_fragment (all_frag, DNM) {
            let ll = []
            let num = get_every_frag_dnm_numbers(all_frag, DNM)
            for (let item of num) {
              if (item < 3) {
                ll.push(22)
              } else {
                ll.push(item * 10 + 2)
              }
            }
            // eslint-disable-next-line camelcase
            let re_a = []
            for (let i = 0; i < ll.length; i++) {
              re_a.push(get_sum(ll, i))
            }
            // eslint-disable-next-line camelcase
            let re_b = []
            for (let i = 1; i < ll.length + 1; i++) {
              re_b.push(get_sum(ll, i))
            }
            // eslint-disable-next-line camelcase
            let scale_frag = []
            for (let i = 0; i < re_a.length; i++) {
              scale_frag.push([re_a[i], re_b[i]])
            }
            // eslint-disable-next-line camelcase
            return scale_frag
          }

          // eslint-disable-next-line camelcase
          function combine_list_2D (list_2D) {
            let i = 0
            // eslint-disable-next-line camelcase
            let list_2D_len = list_2D.length
            // eslint-disable-next-line camelcase
            while (i < list_2D_len - 1) {
              if (list_2D[i][1] === list_2D[i + 1][0]) {
                list_2D[i] = [list_2D[i][0], list_2D[i + 1][1]]
                list_2D.splice(i + 1, 1)
                // eslint-disable-next-line camelcase
                list_2D_len = list_2D_len - 1
              } else {
                i += 1
              }
            }
            // eslint-disable-next-line camelcase
            return list_2D
          }

          // eslint-disable-next-line camelcase
          function combine_list_3D (list1) {
            for (let i = 0; i < list1.length; i++) {
              if (list1[i] !== undefined) {
                list1[i] = combine_list_2D(list1[i])
              }
            }
            return list1
          }
          // eslint-disable-next-line camelcase
          function count_exton_region_in_fragment (list_3D, all_frag, scale_frag) {
            let ae = []
            // eslint-disable-next-line camelcase
            for (let item of list_3D) {
              ae.push(item[exton])
            }
            // eslint-disable-next-line no-unused-vars
            let i = 0
            let count = []
            let count1 = []
            for (let item of ae) {
              let temp1 = []
              let temp2 = []
              for (let item1 of item) {
                let j = 0
                for (let k = 0; k < all_frag.length; k++) {
                  let item2 = all_frag[k]
                  if (item2[start] >= item1[start] && item2[end] <= item1[end]) {
                    temp1.push(scale_frag[j])
                    temp2.push(all_frag[j])
                  }
                  j += 1
                }
              }
              count.push(temp1)
              count1.push(temp2)
              i += 1
            }
            count = combine_list_3D(count)
            count1 = combine_list_3D(count1)
            return [count, count1]
          }
          // eslint-disable-next-line camelcase
          function count_to_xy (list_3D, count, count1) {
            let y = []
            // eslint-disable-next-line camelcase
            for (let item of list_3D) {
              y.push(item[0])
            }
            let xy = []
            for (let i = 0; i < y.length; i++) {
              let item = count[i]
              let yy = y[i]
              let z = count1[i]
              for (let j = 0; j < item.length; j++) {
                // eslint-disable-next-line camelcase
                let item_item = item[j]
                // eslint-disable-next-line camelcase
                let item_tips = z[j]
                let temp = [[item_item[0], yy, item_tips[0]], [item_item[1], yy, item_tips[1]]]
                xy.push(temp)
              }
            }
            return xy
          }
          // eslint-disable-next-line camelcase
          function count_utr_region_in_fragment (list_3D, all_frag, scale_frag) {
            // eslint-disable-next-line camelcase
            let ae_utr = []
            // eslint-disable-next-line camelcase
            for (let item of list_3D) {
              let temp = []
              // eslint-disable-next-line camelcase
              for (let item_item of item[utr3]) {
                temp.push(item_item)
              }
              // eslint-disable-next-line camelcase
              for (let item_item of item[utr5]) {
                temp.push(item_item)
              }
              ae_utr.push(temp)
            }
            let count = []
            let count1 = []
            // eslint-disable-next-line camelcase
            for (let item of ae_utr) {
              let temp1 = []
              let temp2 = []
              for (let item1 of item) {
                let j = 0
                // eslint-disable-next-line camelcase
                for (let item2 of all_frag) {
                  if (item2[start] >= item1[start] && item2[end] <= item1[end]) {
                    temp1.push(scale_frag[j])
                    temp2.push(all_frag[j])
                  }
                  j += 1
                }
              }
              count.push(temp1)
              count1.push(temp2)
            }
            count = combine_list_3D(count)
            count1 = combine_list_3D(count1)
            return [count, count1]
          }
          // eslint-disable-next-line camelcase
          function mapping_mutation_to_frag (all_frag, scale_frag, DNM = []) {
            // eslint-disable-next-line camelcase
            let DNM_list = []
            for (let item of DNM) {
              DNM_list.push(item[0])
            }
            // eslint-disable-next-line camelcase
            let new_DNM_list = new Set(DNM_list)
            // eslint-disable-next-line camelcase
            DNM_list = Array.from(new_DNM_list)
            DNM_list.sort()
            // eslint-disable-next-line camelcase
            let DNM_tips = []
            for (let item of DNM) {
              DNM_tips.push(item[1])
              // eslint-disable-next-line camelcase
              let new_DNM_tips = new Set(DNM_tips)
              // eslint-disable-next-line camelcase
              DNM_tips = Array.from(new_DNM_tips)
            }
            let num = Array(all_frag.length).fill(0)
            let i = 0
            // eslint-disable-next-line camelcase
            let DNM_frag = []
            // eslint-disable-next-line camelcase
            for (let item of all_frag) {
              let temp = []
              let kk = 0
              // eslint-disable-next-line camelcase
              for (let item_item of DNM_list) {
                // eslint-disable-next-line camelcase
                if (item_item >= item[start] && item_item <= item[end]) {
                  num[i] += 1
                  let temp1 = []
                  temp1.push(item_item)
                  temp1.push(DNM_tips[kk])
                  temp.push(temp1)
                }
                kk += 1
              }
              DNM_frag.push(temp)
              i += 1
            }
            DNM = []
            let j = 0
            for (let item of num) {
              if (item !== 0) {
                let s = scale_frag[j][start] + 2
                let temp = []
                for (let k = 0; k < item; k++) {
                  let temp1 = []
                  temp1.push(s)
                  temp1.push(s + 3)
                  temp1.push(DNM_frag[j][k][0])
                  temp1.push(DNM_frag[j][k][1])
                  temp.push(temp1)
                  s += 10
                }
                DNM.push(temp)
              }
              j += 1
            }
            return DNM
          }
          // eslint-disable-next-line camelcase
          function sort_count_utr (count_utr) {
            for (let i = 0; i < count_utr.length; i++) {
              count_utr[i].sort()
            }
            // eslint-disable-next-line camelcase
            return count_utr
          }
          // eslint-disable-next-line camelcase
          function get_trans_region (count) {
            let res = []
            for (let item of count) {
              if (item !== undefined) {
                res.push([item[0][start], item[item.length - 1][end]])
              }
            }
            return res
          }
          // eslint-disable-next-line camelcase
          function trans_DNM (trans_region, DNM, list_3D) {
            let y = []
            // eslint-disable-next-line camelcase
            for (let item of list_3D) {
              y.push(item[sym])
            }
            let res = []
            for (let item of DNM) {
              for (let item2 of item) {
                let i = 0
                // eslint-disable-next-line camelcase
                for (let item_item of trans_region) {
                  if (item2[0] >= item_item[0] && item2[1] <= item_item[1]) {
                    res.push([item2[0], item2[1], y[i], item2[3]])
                  }
                  i += 1
                }
              }
            }
            // eslint-disable-next-line camelcase
            let fin_DNM_xy = []
            for (let item of res) {
              fin_DNM_xy.push([[item[0], 'DNMs', item[3]], [item[1], 'DNMs', item[3]]])
            }
            // eslint-disable-next-line camelcase
            return fin_DNM_xy
          }
          // eslint-disable-next-line camelcase
          function generate_xy (list_3D, DNM_list) {
            // eslint-disable-next-line camelcase
            DNM_list = DNM_sort_by_site(DNM_list)
            // eslint-disable-next-line camelcase
            let all_exon_region = get_all_exton_region(list_3D)
            // eslint-disable-next-line camelcase
            all_exon_region = drop_duplicate(all_exon_region)
            // eslint-disable-next-line camelcase
            all_exon_region = sort_list(all_exon_region)
            // eslint-disable-next-line camelcase
            let all_frag = cut_fragment(all_exon_region)
            // eslint-disable-next-line camelcase
            let scale_frag = scale_fragment(all_frag, DNM_list)
            // eslint-disable-next-line camelcase
            let count_exon = count_exton_region_in_fragment(list_3D, all_frag, scale_frag)[0]
            // eslint-disable-next-line camelcase
            let count1_exon = count_exton_region_in_fragment(list_3D, all_frag, scale_frag)[1]
            // eslint-disable-next-line camelcase
            let count_exon_xy = count_to_xy(list_3D, count_exon, count1_exon)
            // eslint-disable-next-line camelcase
            let count_utr = count_utr_region_in_fragment(list_3D, all_frag, scale_frag)[0]
            // eslint-disable-next-line camelcase
            let count1_utr = count_utr_region_in_fragment(list_3D, all_frag, scale_frag)[1]
            // eslint-disable-next-line camelcase
            let count_utr_xy = count_to_xy(list_3D, count_utr, count1_utr)

            let DNM = mapping_mutation_to_frag(all_frag, scale_frag, DNM_list)
            // eslint-disable-next-line camelcase
            count_utr = sort_count_utr(count_utr)
            // eslint-disable-next-line camelcase
            let trans_region = get_trans_region(count_utr)
            // eslint-disable-next-line camelcase
            let fin_DNM_xy = trans_DNM(trans_region, DNM, list_3D)
            // eslint-disable-next-line camelcase
            return [count_exon_xy, count_utr_xy, fin_DNM_xy]
          }
          // eslint-disable-next-line camelcase
          function get_DNM_color (m_type) {
            var color
            if ((['frameshift deletion', 'frameshift insertion', 'frameshift substitution',
              'splice-site mutation', 'stopgain'].includes(m_type)) || m_type.startsWith('frameshift')) {
              color = 'red'
            } else if ((['nonframeshift deletion', 'nonframeshift insertion', 'nonsynonymous snv',
              'nonframeshift substitution', 'nonsynonymous SNV', 'strat gain', 'start gain',
              'stoploss'].includes(m_type)) || m_type.startsWith('nonframeshift')) {
              color = 'pink'
            } else if (['synonymous SNV', 'exonic', 'coding complex', 'synonymous snv'].includes(m_type)) {
              color = 'purple'
            } else if (['unknown'].includes(m_type)) {
              color = 'yellow'
            } else {
              color = 'blue'
            }
            return color
          }

          // eslint-disable-next-line camelcase
          function get_heights (length) {
            if (length <= 2) {
              return 200
            } else if (length <= 4) {
              return 400
            } else if (length <= 10) {
              return 600
            } else if (length <= 13) {
              return 800
            } else {
              return length * 30
            }
          }
          // eslint-disable-next-line camelcase
          let transcript_data = res.data[0]
          // eslint-disable-next-line camelcase
          let dnms_data = res.data[1]
          // eslint-disable-next-line camelcase
          let transcript_list = []
          // // eslint-disable-next-line camelcase
          // let trans_count = 0
          // eslint-disable-next-line camelcase
          let dnm_list = []
          if (transcript_data.length !== 0) {
            for (let i = 0; i < transcript_data.length; i++) {
              // eslint-disable-next-line camelcase
              let trans_item = transcript_data[i]
              // eslint-disable-next-line camelcase,no-unused-vars
              let transcript_id = trans_item['transcript_id']
              // eslint-disable-next-line camelcase
              let transcript_structure = trans_item['structure']
              // eslint-disable-next-line camelcase
              let region_list = []
              // eslint-disable-next-line camelcase
              for (let item_region of ['coding_exon_region', 'utr3_exon_region', 'utr5_exon_region']) {
                if (typeof transcript_structure[item_region] !== 'undefined') {
                  region_list.push(transcript_structure[item_region])
                } else {
                  region_list.push([])
                }
              }
              // eslint-disable-next-line camelcase
              transcript_list.push([transcript_id, region_list[0], region_list[1], region_list[2]])
            }
            transcript_list.sort().reverse()
          }
          if (dnms_data.length !== 0) {
            // eslint-disable-next-line camelcase
            for (let dnm_item of dnms_data) {
              let s = ''
              if (dnm_item['Func_refGene'] === 'exonic') {
                if (dnm_item['ExonicFunc_refGene'] !== undefined) {
                  s = dnm_item['start'] + ',' + dnm_item['variant'] + ',' + dnm_item['ExonicFunc_refGene']
                } else {
                  s = dnm_item['start'] + ',' + dnm_item['variant']
                }
              } else {
                if (dnm_item['Func_refGene'] !== undefined) {
                  s = dnm_item['start'] + ',' + dnm_item['variant'] + ',' + dnm_item['Func_refGene']
                } else {
                  s = dnm_item['start'] + ',' + dnm_item['variant']
                }
              }
              dnm_list.push([dnm_item['start'], s])
            }
          } else {
            dnm_list.push([])
          }
          // eslint-disable-next-line camelcase,no-unused-vars
          let exton_records = generate_xy(transcript_list, dnm_list)[0]
          // eslint-disable-next-line camelcase,no-unused-vars
          let utr_records = generate_xy(transcript_list, dnm_list)[1]
          // eslint-disable-next-line camelcase,no-unused-vars
          let DNM_xy = generate_xy(transcript_list, dnm_list)[2]
          // eslint-disable-next-line camelcase
          let trans_len = transcript_list.length
          // eslint-disable-next-line camelcase
          let trace_coding = []
          // eslint-disable-next-line camelcase,no-unused-vars
          let exton_num = 0
          for (let i = 0; i < exton_records.length; i++) {
            let item = exton_records[i]
            // eslint-disable-next-line camelcase
            let trace_coding_item = {}
            if (i !== exton_records.length - 1) {
              // eslint-disable-next-line camelcase
              trace_coding_item = {
                visible: true,
                type: 'scatter',
                hoverinfo: 'text',
                showlegend: false,
                mode: 'lines',
                x: [item[0][0], item[1][0]],
                y: [item[0][1], item[1][1]],
                text: '[' + String(item[0][2]) + '-' + String(item[1][2]) + ']',
                line: {
                  color: 'rgb(72,130,180)',
                  shape: 'linear',
                  width: 10,
                  simplify: true
                }
              }

              trace_coding.push(trace_coding_item)
              // eslint-disable-next-line camelcase
              exton_num += 1
            } else {
              // eslint-disable-next-line camelcase
              trace_coding_item = {
                visible: true,
                hoverinfo: 'text',
                name: 'Exon',
                showlegend: false,
                mode: 'lines',
                x: [item[0][0], item[1][0]],
                y: [item[0][1], item[1][1]],
                text: '[' + String(item[0][2]) + '-' + String(item[1][2]) + ']',
                line: {
                  color: 'rgb(70,130,180)',
                  shape: 'linear',
                  width: 10,
                  simplify: true
                }
              }
              trace_coding.push(trace_coding_item)
              // eslint-disable-next-line camelcase
              exton_num += 1
            }
          }
          for (let i = 0; i < utr_records.length; i++) {
            var item = utr_records[i]
            // eslint-disable-next-line camelcase
            var trace_utr_item = {
              type: 'scatter',
              visible: true,
              hoverinfo: 'text',
              showlegend: false,
              mode: 'lines',
              x: [item[0][0], item[1][0]],
              y: [item[0][1], item[1][1]],
              text: '[' + String(item[0][2]) + '-' + String(item[1][2]) + ']',
              line: {
                color: 'gray',
                shape: 'linear',
                width: 5,
                simplify: true
              }
            }
            trace_coding.push(trace_utr_item)
            // eslint-disable-next-line camelcase
            exton_num += 1
          }
          for (let i = 0; i < DNM_xy.length; i++) {
            let item = DNM_xy[i]
            // eslint-disable-next-line camelcase
            let m_type = item[0][2].split(',')[2]
            // eslint-disable-next-line camelcase
            let mut_color = get_DNM_color(m_type)
            // eslint-disable-next-line camelcase
            let dnm_item = {
              type: 'scatter',
              visible: true,
              hoverinfo: 'text',
              showlegend: false,
              mode: 'lines',
              x: [item[0][0], item[1][0]],
              y: [item[0][1], item[1][1]],
              legendgroup: mut_color,
              name: mut_color,
              text: String(item[0][2]),
              hoverlabel: {
                'font': {
                  'size': 10
                }
              },
              line: {
                color: mut_color,
                shape: 'linear',
                width: 12,
                simplify: true
              }
            }
            trace_coding.push(dnm_item)
          }
          let layout = {
            paper_bgcolor: 'rgb(249, 249, 249)',
            plot_bgcolor: 'rgb(249, 249, 249)',
            width: 800,
            height: get_heights(trans_len),
            hovermode: 'closest',
            xaxis: {
              showgrid: false,
              zeroline: false,
              showline: false,
              showticklabels: false,
              autorange: true,
              titlefont: {
                family: 'Arial'
              }
            },
            yaxis: {
              titlefont: {
                family: 'Arial',
                size: 20,
                color: 'lightgrey'
              },
              ticklen: 0.1,
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
              r: 0,
              t: 20,
              pad: 0
            }
          }
          // eslint-disable-next-line camelcase
          this.data = trace_coding
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
