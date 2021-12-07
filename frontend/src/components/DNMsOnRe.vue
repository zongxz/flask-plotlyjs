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
  name: 'DNMsOnRe',
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
      let url = 'http://127.0.0.1:5000/DNMsOnRegulatoryData1'
      axios.get(url)
        .then((res) => {
          // eslint-disable-next-line camelcase
          function get_list_2D_region (list_2D) {
            // eslint-disable-next-line camelcase
            if (list_2D !== undefined) {
              // eslint-disable-next-line camelcase
              let start_list = []
              // eslint-disable-next-line camelcase
              let end_list = []
              // eslint-disable-next-line camelcase
              for (let item of list_2D) {
                start_list.push(item[0])
                end_list.push(item[1])
              }
              // eslint-disable-next-line camelcase
              let min_value = Math.min(Math.min(start_list), Math.min(end_list))
              // eslint-disable-next-line camelcase
              let max_value = Math.max(Math.max(start_list), Math.max(end_list))
              // eslint-disable-next-line camelcase
              return [min_value, max_value]
            }
            return []
          }
          // eslint-disable-next-line camelcase
          function get_list_2D_start_end (list_2D) {
            // eslint-disable-next-line camelcase
            let list_2D_flatten = list_2D[0]
            // eslint-disable-next-line camelcase
            let sorted_list = list_2D_flatten.sort()
            return [sorted_list[0], sorted_list[sorted_list.length - 1]]
          }
          // eslint-disable-next-line camelcase
          function get_transcript_region (strand, trans_structure) {
            if (strand !== undefined) {
              if (strand === '+') {
                if (trans_structure['utr5_exon_region'] !== undefined) {
                  if (trans_structure['utr3_exon_region']) {
                    return [get_list_2D_start_end(trans_structure['utr5_exon_region'])[1],
                      get_list_2D_start_end(trans_structure['utr3_exon_region'])[0]]
                  } else {
                    if (trans_structure['coding_exon_region']) {
                      return [get_list_2D_start_end(trans_structure['utr5_exon_region'])[1],
                        get_list_2D_region(trans_structure['coding_exon_region'])[1]]
                    } else {
                      return []
                    }
                  }
                } else {
                  if (trans_structure['coding_exon_region']) {
                    if (trans_structure['utr3_exon_region']) {
                      return [get_list_2D_start_end(trans_structure['coding_exon_region'])[0],
                        get_list_2D_start_end(trans_structure['utr3_exon_region'])[0]]
                    } else {
                      return get_list_2D_region(trans_structure['coding_exon_region'])
                    }
                  } else {
                    return []
                  }
                }
              } else {
                if (trans_structure['utr3_exon_region'] !== undefined) {
                  if (trans_structure['utr5_exon_region']) {
                    return [get_list_2D_start_end(trans_structure['utr3_exon_region'])[1],
                      get_list_2D_start_end(trans_structure['utr5_exon_region'])[0]]
                  } else {
                    if (trans_structure['coding_exon_region']) {
                      return [get_list_2D_start_end(trans_structure['utr5_exon_region'])[1],
                        get_list_2D_region(trans_structure['coding_exon_region'])[1]]
                    } else {
                      return []
                    }
                  }
                } else {
                  if (trans_structure['coding_exon_region']) {
                    if (trans_structure['utr3_exon_region']) {
                      return [get_list_2D_start_end(trans_structure['coding_exon_region'])[0],
                        get_list_2D_start_end(trans_structure['utr3_exon_region'])[0]]
                    } else {
                      return get_list_2D_region(trans_structure['coding_exon_region'])
                    }
                  } else {
                    return []
                  }
                }
              }
            } else {
              return []
            }
          }
          // eslint-disable-next-line camelcase
          function get_trans_data (one_trans_structure, transcript_id, strand) {
            let res = []
            res.push(transcript_id)
            res.push(get_transcript_region(strand, one_trans_structure))

            if (one_trans_structure['utr3_exon_region'] !== undefined) {
              res.push(get_list_2D_start_end(one_trans_structure['utr3_exon_region']))
            } else {
              res.push([])
            }
            if (one_trans_structure['utr5_exon_region'] !== undefined) {
              res.push(get_list_2D_start_end(one_trans_structure['utr5_exon_region']))
            } else {
              res.push([])
            }
            return res
          }
          // eslint-disable-next-line camelcase
          function drop_duplication (a_list, b_list, c_list) {
            // eslint-disable-next-line camelcase
            let a_copy_list = []
            // eslint-disable-next-line camelcase
            let b_copy_list = []
            // eslint-disable-next-line camelcase
            let c_copy_list = []
            for (let i = 0; i < c_list.length; i++) {
              let item = c_list[i]
              // eslint-disable-next-line camelcase
              if (!(item in c_copy_list)) {
                c_copy_list.push(item)
                b_copy_list.push(b_list[i])
                a_copy_list.push(a_list[i])
              }
            }
            // eslint-disable-next-line camelcase
            return [a_copy_list, b_copy_list, c_copy_list]
          }
          // eslint-disable-next-line camelcase
          function get_promoter_and_enhancer_data (promoter_data, enhancer_data, dnm_data) {
            // eslint-disable-next-line camelcase
            let promoter_res = []
            // eslint-disable-next-line camelcase
            let enhancer_res = []
            // eslint-disable-next-line camelcase
            let temp_promoter = []
            // eslint-disable-next-line camelcase
            let temp_promoter_frag = []
            // eslint-disable-next-line camelcase
            let temp_promoter_tips = []
            // eslint-disable-next-line camelcase
            if (promoter_data !== undefined) {
              // eslint-disable-next-line camelcase
              for (let item_pro of promoter_data) {
                if (item_pro['start'] && item_pro['end']) {
                  let tips = item_pro['short_descripton'] + ', ' + item_pro['cage_peak_id']
                  temp_promoter.push('Promoter')
                  temp_promoter_frag.push([item_pro['start'], item_pro['end']])
                  temp_promoter_tips.push(tips)
                }
              }
            }
            // eslint-disable-next-line camelcase
            let temp_enhancer = []
            // eslint-disable-next-line camelcase
            let temp_enhancer_frag = []
            // eslint-disable-next-line camelcase
            let temp_enhancer_tips = []
            // eslint-disable-next-line camelcase
            if (enhancer_data !== undefined) {
              // eslint-disable-next-line camelcase
              for (let item_enh of enhancer_data) {
                if (item_enh['start'] && item_enh['end']) {
                  let tips = item_enh['genehancer_id'] + ', [' + item_enh['start'] + ' - ' +
                        item_enh['end'] + '], local'
                  temp_enhancer.push('Enhancer')
                  temp_enhancer_frag.push([item_enh['start'], item_enh['end']])
                  temp_enhancer_tips.push(tips)
                }
              }
            }
            // eslint-disable-next-line camelcase
            if (dnm_data !== undefined) {
              // eslint-disable-next-line camelcase
              for (let dnm_item of dnm_data) {
                if (dnm_item['annotation'] !== undefined) {
                  if (dnm_item['annotation']['enhancer_id'] !== undefined) {
                    if (dnm_item['re-annotation']['enh_start'] && dnm_item['re-annotation']['enh_end']) {
                      let tips = dnm_item['re-annotation']['enhancer_id'] + ', [' +
                                dnm_item['re-annotation']['enh_start'].replace('"', '') + '-' +
                                dnm_item['re-annotation']['enh_end'].replace('"', '') + '], targetgene'
                      temp_enhancer.push('Enhancer')
                      temp_enhancer_frag.push([Number(dnm_item['re-annotation']['enh_start']),
                        Number(dnm_item['re-annotation']['enh_end'])])
                      temp_enhancer_tips.push(tips)
                    }
                  }
                  if (dnm_item['re-annotation']['promoter_id'] !== undefined) {
                    if (dnm_item['re-annotation']['pro_start'] && dnm_item['re-annotation']['pro_end']) {
                      let tips = dnm_item['re-annotation']['promoter_id'] + ', [' +
                                dnm_item['re-annotation']['pro_start'].replace('"', '') + '-' +
                                dnm_item['re-annotation']['pro_end'].replace('"', '') + '], targetgene'
                      temp_promoter.push('Promoter')
                      temp_promoter_frag.push([Number(dnm_item['re-annotation']['pro_start']),
                        Number(dnm_item['re-annotation']['pro_end'])])
                      temp_promoter_tips.push(tips)
                    }
                  }
                }
              }
            }
            // eslint-disable-next-line camelcase
            if (temp_enhancer !== undefined && temp_enhancer_frag !== undefined && temp_enhancer_tips !== undefined) {
              // eslint-disable-next-line camelcase
              let temp_enhancer_new = drop_duplication(temp_enhancer, temp_enhancer_frag, temp_enhancer_tips)[0]
              // eslint-disable-next-line camelcase
              let temp_enhancer_frag_new = drop_duplication(temp_enhancer, temp_enhancer_frag, temp_enhancer_tips)[1]
              // eslint-disable-next-line camelcase
              let temp_enhancer_tips_new = drop_duplication(temp_enhancer, temp_enhancer_frag, temp_enhancer_tips)[2]
              enhancer_res.push(temp_enhancer_new)
              enhancer_res.push(temp_enhancer_frag_new)
              enhancer_res.push(temp_enhancer_tips_new)
            }
            // eslint-disable-next-line camelcase
            if (temp_promoter !== undefined && temp_promoter_frag !== undefined && temp_promoter_tips !== undefined) {
              // eslint-disable-next-line camelcase
              let temp_promoter_new = drop_duplication(temp_promoter, temp_promoter_frag, temp_promoter_tips)[0]
              // eslint-disable-next-line camelcase
              let temp_promoter_frag_new = drop_duplication(temp_promoter, temp_promoter_frag, temp_promoter_tips)[1]
              // eslint-disable-next-line camelcase
              let temp_promoter_tips_new = drop_duplication(temp_promoter, temp_promoter_frag, temp_promoter_tips)[2]
              promoter_res.push(temp_promoter_new)
              promoter_res.push(temp_promoter_frag_new)
              promoter_res.push(temp_promoter_tips_new)
            }
            // eslint-disable-next-line camelcase
            return [promoter_res, enhancer_res]
          }
          // eslint-disable-next-line camelcase
          function get_dnms_data (dnms_data) {
            // eslint-disable-next-line camelcase
            let dnm_list = []
            // eslint-disable-next-line camelcase
            if (dnms_data !== undefined) {
              // eslint-disable-next-line camelcase
              for (let dnm_item of dnms_data) {
                let s = ''
                if (dnm_item['Func_refGene'] === 'exonic') {
                  if (dnm_item['ExonicFunc_refGene'] !== undefined) {
                    s = dnm_item['start'] + ',' + dnm_item['variant'] +
                            ',' + dnm_item['ExonicFunc_refGene']
                  } else {
                    s = dnm_item['start'] + ',' + dnm_item['variant']
                  }
                } else {
                  if (dnm_item['Func_refGene'] !== undefined) {
                    s = dnm_item['start'] + ',' + dnm_item['variant'] +
                            ',' + dnm_item['Func_refGene']
                  } else {
                    s = dnm_item['start'] + ',' + dnm_item['variant']
                  }
                }
                dnm_list.push([dnm_item['start'], 'DNMs', s])
              }
            } else {
              dnm_list.push([])
            }
            // eslint-disable-next-line camelcase
            return dnm_list
          }
          // eslint-disable-next-line camelcase
          function hb_list_2D (test) {
            let i = 0
            let l = test.length

            while (i < l - 1) {
              if (test[i][1] === test[i + 1][0]) {
                test[i] = [test[i][0], test[i + 1][1]]
                test.splice(i + 1, 1)
                l = l - 1
              } else {
                i += 1
              }
            }
            return test
          }
          // eslint-disable-next-line camelcase
          function hb_list_3D (list1) {
            for (let i = 0; i < list1.length; i++) {
              if (list1[i].length !== 0) {
                list1[i] = hb_list_2D(list1[i])
              }
            }
            return list1
          }
          // eslint-disable-next-line camelcase
          function get_all_region (trans_data, regulatory_element_data) {
            // eslint-disable-next-line camelcase
            let all_region = []
            // eslint-disable-next-line camelcase
            for (let item of trans_data) {
              if (item[1].length !== 0) {
                all_region.push(item[1])
              }
              if (item[2].length !== 0) {
                all_region.push(item[2])
              }
              if (item[3].length !== 0) {
                all_region.push(item[3])
              }
            }
            // eslint-disable-next-line camelcase
            for (let item of regulatory_element_data) {
              if (item.length !== 0) {
                // eslint-disable-next-line camelcase
                for (let item_item of item[1]) {
                  if (item_item.length !== 0) {
                    all_region.push(item_item)
                  }
                }
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
              console.assert(all_region[i][0] <= all_region[i + 1][0], '')
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
              all_s.push(item[0])
              all_e.push(item[1])
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
                if (item_item >= item[0] && item_item <= item[1]) {
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
          function scale_fragment (all_frag, DNM, regulatory_element_data) {
            let ll = []
            let pe = []
            let num = get_every_frag_dnm_numbers(all_frag, DNM)
            if (regulatory_element_data[0].length !== 0) {
              // eslint-disable-next-line camelcase
              let promoter_frag = regulatory_element_data[0][1]
              // eslint-disable-next-line camelcase
              for (let item of promoter_frag) {
                pe.push(item)
              }
            }

            if (regulatory_element_data[1].length !== 0) {
              // eslint-disable-next-line camelcase
              let enhancer_frag = regulatory_element_data[1][1]
              // eslint-disable-next-line camelcase
              for (let item of enhancer_frag) {
                pe.push(item)
              }
            }
            // eslint-disable-next-line camelcase
            let pe_drop_dupliction = []
            for (let item of pe) {
              // eslint-disable-next-line camelcase
              if (!(item in pe_drop_dupliction)) {
                pe_drop_dupliction.push(item)
              }
            }
            let flag = Array(all_frag.length).fill(0)
            for (let i = 0; i < all_frag.length; i++) {
              let item = all_frag[i]
              // eslint-disable-next-line camelcase
              for (let item1 of pe_drop_dupliction) {
                if (item[0] >= item1[0] && item[1] <= item1[1]) {
                  flag[i] = 1
                }
              }
            }
            for (let i = 0; i < flag.length; i++) {
              let item1 = flag[i]
              let item2 = num[i]
              if (item1 === 1) {
                ll.push(10)
              } else {
                if (item2 < 3) {
                  ll.push(22)
                } else {
                  ll.push(item2 * 10 + 2)
                }
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
          function count_exton_region_in_fragment (all_frag, scale_frag, trans_data) {
            let ae = []
            // eslint-disable-next-line camelcase
            for (let item of trans_data) {
              ae.push(item[1])
            }
            let count = []
            let count1 = []
            for (let i = 0; i < ae.length; i++) {
              let item = ae[i]
              let temp1 = []
              let temp2 = []
              if (item.length === 0) {
                temp1.push([])
                temp2.push([])
                count.push(temp1)
                count1.push(temp2)
              } else {
                for (let j = 0; j < all_frag.length; j++) {
                  let item2 = all_frag[j]
                  if (item2[0] >= item[0] && item2[1] <= item[1]) {
                    temp1.push(scale_frag[j])

                    temp2.push(all_frag[j])
                  }
                }
                count.push(temp1)
                count1.push(temp2)
              }
            }
            // eslint-disable-next-line camelcase
            let sort_count = count
            for (let i = 0; i < sort_count.length; i++) {
              let item = sort_count[i]
              if (item !== [[]] && item !== []) {
                sort_count[i].sort(function (x, y) {
                  return x[0] - y[0]
                })
              }
            }
            count = hb_list_3D(count)
            count1 = hb_list_3D(count1)
            try {
              for (let i = 0; i < count1.length; i++) {
                let item = count1[i]
                if (item !== [[]] && item !== []) {
                  count1[i].sort(function (x, y) {
                    return x[0] - y[0]
                  })
                }
              }
            } catch (e) {

            }
            return [count, count1]
          }
          // eslint-disable-next-line camelcase
          function count_utr_region_in_fragment (all_frag, scale_frag, trans_data) {
            // eslint-disable-next-line camelcase
            let ae_utr = []
            // eslint-disable-next-line camelcase
            for (let item of trans_data) {
              let temp = []
              // eslint-disable-next-line camelcase
              if (item[2].length !== 0) {
                temp.push(item[2])
              }
              if (item[3].length !== 0) {
                temp.push(item[3])
              }
              ae_utr.push(temp)
            }
            let count = []
            let count1 = []
            // eslint-disable-next-line camelcase
            for (let item of ae_utr) {
              let temp1 = []
              let temp2 = []
              if (item === [[]] || item === []) {
                temp1.push([])
                temp2.push([])
                count.push(temp1)
                count1.push(temp2)
              } else {
                for (let i = 0; i < item.length; i++) {
                  let item1 = item[i]
                  for (let j = 0; j < all_frag.length; j++) {
                    let item2 = all_frag[j]
                    if (item2[0] >= item1[0] && item2[1] <= item1[1]) {
                      temp1.push(scale_frag[j])
                      temp2.push(all_frag[j])
                    }
                  }
                }
                count.push(temp1)
                count1.push(temp2)
              }
            }
            // eslint-disable-next-line camelcase
            let sort_count = count
            for (let i = 0; i < sort_count.length; i++) {
              let item = sort_count[i]
              if (item !== [[]] && item !== []) {
                sort_count[i].sort(function (x, y) {
                  return x[0] - y[0]
                })
              }
            }
            count = hb_list_3D(count)
            count1 = hb_list_3D(count1)
            for (let i = 0; i < count1.length; i++) {
              let item = count1[i]
              if (item !== [[]] && item !== []) {
                count1[i].sort(function (x, y) {
                  return x[0] - y[0]
                })
              }
            }
            return [count, count1]
          }
          // eslint-disable-next-line camelcase
          function count_promoter_region_in_fragment (all_frag, scale_frag, regulatory_element_data) {
            if (regulatory_element_data[0].length !== 0) {
              // eslint-disable-next-line camelcase
              let ae_promoter = regulatory_element_data[0][1]
              let count = []
              let count1 = []
              for (let i = 0; i < ae_promoter.length; i++) {
                let item = ae_promoter[i]
                let temp = []
                let temp1 = []
                for (let j = 0; j < all_frag.length; j++) {
                  let item2 = all_frag[j]
                  if (item2[0] >= item[0] && item2[1] <= item[1]) {
                    temp.push(scale_frag[j])
                    temp1.push(all_frag[j])
                  }
                }
                count.push(temp)
                count1.push(temp1)
              }
              count = hb_list_3D(count)
              count1 = hb_list_3D(count1)
              return [count, count1]
            }
          }
          // eslint-disable-next-line camelcase
          function count_enhancer_region_in_fragment (all_frag, scale_frag, regulatory_element_data) {
            if (regulatory_element_data[1].length !== 0) {
              // eslint-disable-next-line camelcase
              let ae_enhancer = regulatory_element_data[1][1]
              let count = []
              let count1 = []
              for (let i = 0; i < ae_enhancer.length; i++) {
                let item = ae_enhancer[i]
                let temp = []
                let temp1 = []
                for (let j = 0; j < all_frag.length; j++) {
                  let item2 = all_frag[j]
                  if (item2[0] >= item[0] && item2[1] <= item[1]) {
                    temp.push(scale_frag[j])
                    temp1.push(all_frag[j])
                  }
                }
                count.push(temp)
                count1.push(temp1)
              }
              count = hb_list_3D(count)
              count1 = hb_list_3D(count1)
              return [count, count1]
            }
          }
          // eslint-disable-next-line camelcase
          function convert_trans_to_xy (count, count1, trans_data) {
            let y = []
            // eslint-disable-next-line camelcase
            for (let item of trans_data) {
              if (!(item[1].length === 0 && item[2].length === 0 && item[3].length === 0)) {
                y.push(item[0])
              }
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
          function convert_utr_to_xy (count, count1, trans_data) {
            let y = []
            // eslint-disable-next-line camelcase
            for (let item of trans_data) {
              if (!(item[1].length === 0 && item[2].length === 0 && item[3].length === 0)) {
                y.push(item[0])
              }
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
          function convert_regulatory_elements_to_xy (count, p_or_e, regulatory_element_data) {
            let xy = []
            let tips = ''
            // eslint-disable-next-line camelcase
            if (p_or_e === 'Promoter') {
              tips = regulatory_element_data[0][2]
              // eslint-disable-next-line camelcase
            } else if (p_or_e === 'Enhancer') {
              tips = regulatory_element_data[1][2]
            } else {
              tips = 'Error'
            }

            for (let i = 0; i < count.length; i++) {
              let item = count[i]
              let temp = []
              // eslint-disable-next-line camelcase
              for (let item_item of item) {
                // eslint-disable-next-line camelcase
                temp = [[item_item[0], p_or_e, tips[i]], [item_item[1], p_or_e, tips[i]]]
                xy.push(temp)
              }
            }
            return xy
          }
          // eslint-disable-next-line camelcase
          function DNM_sort_by_site (DNM) {
            if (DNM.length !== 0) {
            // eslint-disable-next-line camelcase
              DNM.sort()
              // eslint-disable-next-line camelcase
              return DNM
            } else {
              return []
            }
          }
          // eslint-disable-next-line camelcase
          function mapping_mutation_to_frag (all_frag, scale_frag, DNM = []) {
            // eslint-disable-next-line camelcase
            let DNM_list = []
            for (let item of DNM) {
              DNM_list.push(item[0])
            }
            // eslint-disable-next-line camelcase
            let DNM_tips = []
            for (let item of DNM) {
              DNM_tips.push(item[1])
            }
            // eslint-disable-next-line camelcase
            let un_sorted_DNM_hover = []
            for (let item of DNM) {
              un_sorted_DNM_hover.push(item[2])
            }
            // eslint-disable-next-line camelcase
            let DNM_hover = un_sorted_DNM_hover.sort()
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
                if (item_item >= item[0] && item_item <= item[1]) {
                  num[i] += 1
                  let temp1 = []
                  temp1.push(item_item)
                  temp1.push(DNM_tips[kk])
                  temp1.push(DNM_hover[kk])
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
                let start = scale_frag[j][0] + 2
                let temp = []
                for (let k = 0; k < item; k++) {
                  let temp1 = []
                  temp1.push(start)
                  temp1.push(start + 3)
                  temp1.push(DNM_frag[j][k][0])
                  temp1.push(DNM_frag[j][k][1])
                  temp1.push(DNM_frag[j][k][2])
                  temp.push(temp1)
                  start += 10
                }
                DNM.push(temp)
              }
              j += 1
            }
            // eslint-disable-next-line camelcase
            let final_DNM = []
            for (let item of DNM) {
              // eslint-disable-next-line camelcase
              for (let item_item of item) {
                final_DNM.push(item_item)
              }
            }
            // eslint-disable-next-line camelcase
            return final_DNM
          }
          // eslint-disable-next-line camelcase
          function convert_dnms_to_xy (dnm_data) {
            let xy = []
            // eslint-disable-next-line camelcase
            for (let item of dnm_data) {
              let temp = [[item[0], item[3], item[4]], [item[1], item[3], item[4]]]
              xy.push(temp)
            }
            return xy
          }
          // eslint-disable-next-line camelcase
          function get_promoter_color (text) {
            var s = text.split(',')
            var len = s.length
            s = s[len - 1]
            var color
            if (s === 'permissive') {
              color = 'rgb(234,255,0)'
            } else {
              color = 'rgb(255,165,0)'
            }
            return color
          }
          // eslint-disable-next-line camelcase
          function get_enhancer_color (text) {
            var s = text.split(',')
            var len = s.length
            s = s[len - 1].trim()
            var color
            if (s === 'targetgene') {
              color = 'rgb(0,100,0)'
            } else {
              color = 'rgb(144,238,144)'
            }
            return color
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
          let gene_data = res.data
          // eslint-disable-next-line camelcase
          // let dnms_data = gene_data['dnms']
          // eslint-disable-next-line camelcase
          let transcript_list = []
          // eslint-disable-next-line camelcase
          if (gene_data !== undefined) {
            // eslint-disable-next-line camelcase
            let transcript_data = gene_data['transcripts']
            // eslint-disable-next-line camelcase
            if (transcript_data !== undefined) {
              for (let i = 0; i < transcript_data.length; i++) {
                let item = transcript_data[i]
                if (item['structure'] !== undefined) {
                  transcript_list.push(get_trans_data(item['structure'],
                    item['transcript_id'], item['strand']))
                }
              }
            }
          }
          transcript_list.sort().reverse()
          // eslint-disable-next-line camelcase
          let trans_count = transcript_list.length
          // eslint-disable-next-line camelcase
          let re_data = get_promoter_and_enhancer_data(gene_data['promoter'],
            gene_data['enhancer'], gene_data['dnms'])
          // eslint-disable-next-line camelcase
          let dnms_list = get_dnms_data(gene_data['dnms'])
          // eslint-disable-next-line camelcase
          let all_region = get_all_region(transcript_list, re_data)
          // eslint-disable-next-line camelcase
          all_region = drop_duplicate(all_region)
          // eslint-disable-next-line camelcase
          all_region = sort_list(all_region)
          // eslint-disable-next-line camelcase
          let dnm_data = DNM_sort_by_site(dnms_list)
          // eslint-disable-next-line camelcase
          let all_frag = cut_fragment(all_region)
          // eslint-disable-next-line camelcase
          let scale_frag = scale_fragment(all_frag, dnm_data, re_data)
          // eslint-disable-next-line camelcase
          let exton_count = count_exton_region_in_fragment(all_frag, scale_frag, transcript_list)[0]
          // eslint-disable-next-line camelcase
          let exton_count1 = count_exton_region_in_fragment(all_frag, scale_frag, transcript_list)[1]
          // eslint-disable-next-line camelcase,no-unused-vars
          let exton_plot_data = convert_trans_to_xy(exton_count, exton_count1, transcript_list)
          // eslint-disable-next-line camelcase
          let utr_count = count_utr_region_in_fragment(all_frag, scale_frag, transcript_list)[0]
          // eslint-disable-next-line camelcase
          let utr_count1 = count_utr_region_in_fragment(all_frag, scale_frag, transcript_list)[1]
          // eslint-disable-next-line camelcase,no-unused-vars
          let utr_plot_data = convert_utr_to_xy(utr_count, utr_count1, transcript_list)
          // eslint-disable-next-line camelcase
          let promoter_plot_data = []
          if (re_data[0].length !== 0) {
            // eslint-disable-next-line camelcase
            let promoter_count = count_promoter_region_in_fragment(all_frag, scale_frag, re_data)[0]
            // eslint-disable-next-line camelcase,no-unused-vars
            let promoter_count1 = count_promoter_region_in_fragment(all_frag, scale_frag, re_data)[1]
            // eslint-disable-next-line camelcase
            promoter_plot_data = convert_regulatory_elements_to_xy(promoter_count, 'Promoter', re_data)
          } else {
            // eslint-disable-next-line camelcase
            promoter_plot_data = undefined
          }
          // eslint-disable-next-line camelcase
          let enhancer_plot_data = []
          if (re_data[1].length !== 0) {
            // eslint-disable-next-line camelcase
            let enhancer_count = count_enhancer_region_in_fragment(all_frag, scale_frag, re_data)[0]
            // eslint-disable-next-line camelcase,no-unused-vars
            let enhancer_count1 = count_enhancer_region_in_fragment(all_frag, scale_frag, re_data)[1]
            // eslint-disable-next-line camelcase
            enhancer_plot_data = convert_regulatory_elements_to_xy(enhancer_count, 'Enhancer', re_data)
          } else {
            // eslint-disable-next-line camelcase
            enhancer_plot_data = undefined
          }
          // eslint-disable-next-line camelcase
          let final_dnm = mapping_mutation_to_frag(all_frag, scale_frag, dnm_data)
          // eslint-disable-next-line camelcase
          let dnm_plot_data = convert_dnms_to_xy(final_dnm)
          let trace = []
          for (let i = 0; i < exton_plot_data.length; i++) {
            let item = exton_plot_data[i]
            // eslint-disable-next-line camelcase
            let trace_item = {
              type: 'scatter',
              visible: true,
              hoverinfo: 'text',
              hoverlabel: {
                'font': {
                  'size': 10
                }
              },
              showlegend: false,
              mode: 'lines',
              x: [item[0][0], item[1][0]],
              y: [item[0][1], item[1][1]],
              text: String(item[0][2]) + '-' + String(item[1][2]),
              line: {
                color: 'rgb(72,130,180)',
                shape: 'linear',
                width: 10,
                simplify: true
              }
            }
            trace.push(trace_item)
          }
          for (let i = 0; i < utr_plot_data.length; i++) {
            let item = utr_plot_data[i]
            // eslint-disable-next-line camelcase
            let trace_item = {
              type: 'scatter',
              visible: true,
              hoverinfo: 'text',
              hoverlabel: {
                'font': {
                  'size': 10
                }
              },
              showlegend: false,
              mode: 'lines',
              x: [item[0][0], item[1][0]],
              y: [item[0][1], item[1][1]],
              text: String(item[0][2]) + '-' + String(item[1][2]),
              line: {
                color: 'gray',
                shape: 'linear',
                width: 5
              }
            }

            trace.push(trace_item)
          }
          if (promoter_plot_data.length !== 0) {
            for (let i = 0; i < promoter_plot_data.length; i++) {
              let item = promoter_plot_data[i]
              // eslint-disable-next-line camelcase
              let trace_item = {
                type: 'scatter',
                visible: true,
                hoverinfo: 'text',
                hoverlabel: {
                  'font': {
                    'size': 10
                  }
                },
                showlegend: false,
                mode: 'lines',
                x: [item[0][0], item[1][0]],
                y: [item[0][1], item[1][1]],
                text: String(item[0][2]),
                line: {
                  color: get_promoter_color(String(item[0][2])),
                  shape: 'linear',
                  width: 10,
                  simplify: true
                }
              }
              trace.push(trace_item)
            }
          }
          if (enhancer_plot_data.length !== 0) {
            for (let i = 0; i < enhancer_plot_data.length; i++) {
              let item = enhancer_plot_data[i]
              // eslint-disable-next-line camelcase
              let trace_item = {
                type: 'scatter',
                visible: true,
                hoverinfo: 'text',
                hoverlabel: {
                  'font': {
                    'size': 10
                  }
                },
                showlegend: false,
                mode: 'lines',
                x: [item[0][0], item[1][0]],
                y: [item[0][1], item[1][1]],
                text: String(item[0][2]),
                line: {
                  color: get_enhancer_color(String(item[0][2])),
                  shape: 'linear',
                  width: 10,
                  simplify: true
                }
              }
              trace.push(trace_item)
            }
          }
          for (let i = 0; i < dnm_plot_data.length; i++) {
            let item = dnm_plot_data[i]
            let type = item[0][2].split(',')[2]
            let c = get_DNM_color(type)
            // eslint-disable-next-line camelcase
            let trace_item = {
              type: 'scatter',
              visible: true,
              hoverinfo: 'text',
              hoverlabel: {
                'font': {
                  'size': 10
                }
              },
              showlegend: false,
              mode: 'lines',
              x: [item[0][0], item[1][0]],
              y: [item[0][1], item[1][1]],
              text: String(item[0][2]),
              line: {
                color: c,
                shape: 'linear',
                width: 10,
                simplify: true
              }
            }
            trace.push(trace_item)
          }
          console.log(trace)
          let layout = {
            paper_bgcolor: 'rgb(249, 249, 249)',
            plot_bgcolor: 'rgb(249, 249, 249)',
            width: 800,
            height: get_heights(trans_count),
            hovermode: 'closest',
            spikedistance: 0,
            hoverdistance: 2,
            xaxis: {
              showgrid: false,
              zeroline: false,
              showline: false,
              showticklabels: false,
              autorange: true,
              dtick: 100
            },
            yaxis: {
              titlefont: {
                family: 'Arial, sans-serif',
                size: 18,
                color: 'lightgrey'
              },
              showticklabels: true,
              tickangle: 360,
              tickfont: {
                family: 'Arial, serif',
                size: 10,
                color: 'black'

              },
              exponentformat: 'e',
              showexponent: 'ALL'
            },
            margin: {
              l: 110,
              r: 5,
              t: 10,
              pad: 0
            }
          }
          this.data = trace
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
