<template>
  <Plot
    :data="data"
    :layout="layout"
  />
</template>

<script>
import Plot from 'vue-plotly.js'

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
        // var color
        // if ((['frameshift deletion', 'frameshift insertion', 'frameshift substitution',
        //   'splice-site mutation', 'stopgain'].includes(m_type)) || m_type.startsWith('frameshift')) {
        //   color = 'red'
        // } else if ((['nonframeshift deletion', 'nonframeshift insertion', 'nonsynonymous snv',
        //   'nonframeshift substitution', 'nonsynonymous SNV', 'strat gain', 'start gain',
        //   'stoploss'].includes(m_type)) || m_type.startsWith('nonframeshift')) {
        //   color = 'pink'
        // } else if (['synonymous SNV', 'exonic', 'coding complex', 'synonymous snv'].includes(m_type)) {
        //   color = 'purple'
        // } else if (['unknown'].includes(m_type)) {
        //   color = 'yellow'
        // } else {
        //   color = 'blue'
        // }
        return 'red'
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
      let gene_data = {'dnms': [{'ExonicFunc_refGene': 'stopgain',
        'Func_refGene': 'exonic',
        '_id': '5fdf6084368e90466f13247b',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.00064713'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51137146,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '25363760',
        're-annotation': {},
        'ref': 'G',
        'sample_id': '10C110253',
        'start': 51137146,
        'study_name': 'DeRubeis2014',
        'validation': 'not_available',
        'variant': 'G>A'},
      {'ExonicFunc_refGene': 'frameshift substitution',
        'Func_refGene': 'exonic',
        '_id': '5fdf6085368e90466f133173',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.0090245',
          'ExAC_Freq': '0.0006',
          'gnomAD_exome_ALL': '6.38E-05'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51159932,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '25418537',
        're-annotation': {},
        'ref': '-',
        'sample_id': '14470.p1',
        'start': 51159932,
        'study_name': 'ASD3',
        'validation': 'validated',
        'variant': '->G'},
      {'ExonicFunc_refGene': 'nonsynonymous snv',
        'Func_refGene': 'exonic',
        '_id': '5fdf6085368e90466f133177',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.0073382'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51159850,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '25418537',
        're-annotation': {},
        'ref': 'A',
        'sample_id': '217-14410-5190',
        'start': 51159850,
        'study_name': 'ASD3',
        'validation': 'validated',
        'variant': 'A>G'},
      {'ExonicFunc_refGene': 'frameshift deletion',
        'Func_refGene': 'exonic',
        '_id': '5fdf6085368e90466f1331d9',
        'alt': '-',
        'annotation': {},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51121808,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '25621899',
        're-annotation': {},
        'ref': 'AG',
        'sample_id': '3-0107_000',
        'start': 51121807,
        'study_name': 'Yuen 2015',
        'validation': 'validated',
        'variant': 'AG>-'},
      {'ExonicFunc_refGene': 'frameshift substitution',
        'Func_refGene': 'exonic',
        '_id': '5fdf6087368e90466f133f57',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.0090245',
          'ExAC_Freq': '0.0006',
          'gnomAD_exome_ALL': '6.38E-05'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ID',
        'end': 51159932,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Intellectual Disability (ID)',
        'pubmed_id': '27479843',
        're-annotation': {},
        'ref': '-',
        'sample_id': 'Lelieveld_331',
        'start': 51159932,
        'study_name': 'Lelieveld2016',
        'validation': 'validated',
        'variant': '->G'},
      {'ExonicFunc_refGene': 'frameshift substitution',
        'Func_refGene': 'exonic',
        '_id': '5fdf6087368e90466f1345c4',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.0022512'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51160793,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '27525107',
        're-annotation': {},
        'ref': '-',
        'sample_id': '2-1455-003',
        'start': 51160793,
        'study_name': 'Yuen2016',
        'validation': 'validated',
        'variant': '->G'},
      {'ExonicFunc_refGene': 'frameshift substitution',
        'Func_refGene': 'exonic',
        '_id': '5fdf6088368e90466f134e1a',
        'alt': '-',
        'annotation': {'DeepSea_Score': '0.0042342'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'DD',
        'end': 51160026,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Developmental Delay (DD)',
        'pubmed_id': '28135719',
        're-annotation': {},
        'ref': 'GCCCAGCCCCCGG',
        'sample_id': 'DDD4K.00001',
        'start': 51160014,
        'study_name': 'DDD_2017',
        'validation': 'not_available',
        'variant': 'GCCCAGCCCCCGG>-'},
      {'ExonicFunc_refGene': 'frameshift substitution',
        'Func_refGene': 'exonic',
        '_id': '5fdf6088368e90466f134e1b',
        'alt': '-',
        'annotation': {'DeepSea_Score': '0.0042342'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'DD',
        'end': 51160026,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Developmental Delay (DD)',
        'pubmed_id': '28135719',
        're-annotation': {},
        'ref': 'GCCCAGCCCCCGG',
        'sample_id': 'DDD4K.00977',
        'start': 51160014,
        'study_name': 'DDD_2017',
        'validation': 'not_available',
        'variant': 'GCCCAGCCCCCGG>-'},
      {'ExonicFunc_refGene': 'frameshift substitution',
        'Func_refGene': 'exonic',
        '_id': '5fdf6088368e90466f134e1c',
        'alt': '-',
        'annotation': {'DeepSea_Score': '0.003452'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'DD',
        'end': 51160348,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Developmental Delay (DD)',
        'pubmed_id': '28135719',
        're-annotation': {},
        'ref': 'AC',
        'sample_id': 'DDD4K.03824',
        'start': 51160347,
        'study_name': 'DDD_2017',
        'validation': 'not_available',
        'variant': 'AC>-'},
      {'ExonicFunc_refGene': 'frameshift substitution',
        'Func_refGene': 'exonic',
        '_id': '5fdf608a368e90466f136750',
        'alt': 'C',
        'annotation': {'DeepSea_Score': '0.0061893'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51159110,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28263302',
        're-annotation': {},
        'ref': '-',
        'sample_id': '1-0726-003',
        'start': 51159110,
        'study_name': 'Yuen2017',
        'validation': 'validated',
        'variant': '->C'},
      {'ExonicFunc_refGene': 'nonsynonymous snv',
        'Func_refGene': 'exonic',
        '_id': '5fdf608a368e90466f1367d6',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.0015935'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51121844,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28263302',
        're-annotation': {},
        'ref': 'A',
        'sample_id': '1-0007-003',
        'start': 51121844,
        'study_name': 'Yuen2017',
        'validation': 'validated',
        'variant': 'A>G'},
      {'ExonicFunc_refGene': 'splice-site mutation',
        'Func_refGene': 'splicing',
        '_id': '5fdf608a368e90466f13688f',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.020239',
          'gnomAD_exome_ALL': '6.32E-06'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51153476,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28263302',
        're-annotation': {},
        'ref': 'G',
        'sample_id': '7-0123-003',
        'start': 51153476,
        'study_name': 'Yuen2017',
        'validation': 'validated',
        'variant': 'G>A'},
      {'ExonicFunc_refGene': 'frameshift substitution',
        'Func_refGene': 'exonic',
        '_id': '5fdf608a368e90466f13689c',
        'alt': '-',
        'annotation': {'DeepSea_Score': '0.0013438'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51159132,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28263302',
        're-annotation': {},
        'ref': 'G',
        'sample_id': 'AU009805',
        'start': 51159132,
        'study_name': 'Yuen2017',
        'validation': 'not_available',
        'variant': 'G>-'},
      {'ExonicFunc_refGene': 'nonsynonymous snv',
        'Func_refGene': 'exonic',
        '_id': '5fdf608c368e90466f1375dc',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.0054648',
          'gnomAD_genome_ALL': '3.23E-05'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51143229,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '28959963',
        're-annotation': {},
        'ref': 'C',
        'sample_id': 'Proband-592',
        'start': 51143229,
        'study_name': 'Jonsson2017',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'ExonicFunc_refGene': 'synonymous snv',
        'Func_refGene': 'exonic',
        '_id': '5fdf608c368e90466f137884',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.07233',
          'gnomAD_exome_ALL': '9.74E-06',
          'gnomAD_genome_ALL': '6.48E-05'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51153373,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '28959963',
        're-annotation': {},
        'ref': 'C',
        'sample_id': 'Proband-821',
        'start': 51153373,
        'study_name': 'Jonsson2017',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'ExonicFunc_refGene': 'frameshift insertion',
        'Func_refGene': 'exonic',
        '_id': '5fdf608d368e90466f138171',
        'alt': 'G',
        'annotation': {},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ID',
        'end': 51159933,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Intellectual Disability (ID)',
        'pubmed_id': '29942082',
        're-annotation': {},
        'ref': '-',
        'sample_id': '27479843_331',
        'start': 51159933,
        'study_name': 'Heyne 2018',
        'validation': 'validated',
        'variant': '->G'},
      {'ExonicFunc_refGene': 'nonsynonymous snv',
        'Func_refGene': 'exonic',
        '_id': '5fdf608f368e90466f139527',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.0054648',
          'gnomAD_genome_ALL': '3.23E-05'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51143229,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '30679340',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '30679340_131592',
        'start': 51143229,
        'study_name': 'Halldorsson 2019',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'ExonicFunc_refGene': 'synonymous snv',
        'Func_refGene': 'exonic',
        '_id': '5fdf608f368e90466f1399f4',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.07233',
          'gnomAD_exome_ALL': '9.74E-06',
          'gnomAD_genome_ALL': '6.48E-05'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51153373,
        'entrez_id': '85358',
        'm_type': 'codingLoc',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '30679340',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '30679340_65385',
        'start': 51153373,
        'study_name': 'Halldorsson 2019',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf6099368e90466f140e25',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.14224'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51130732,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'G',
        'sample_id': '11919.p1',
        'start': 51130732,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'G>A'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf609e368e90466f144b64',
        'alt': 'C',
        'annotation': {'DeepSea_Score': '0.026188'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51135927,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '29700473',
        're-annotation': {},
        'ref': 'G',
        'sample_id': '11700.p1',
        'start': 51135927,
        'study_name': 'Werling_2018',
        'validation': 'not_available',
        'variant': 'G>C'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60a2368e90466f147cf6',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.21604',
          'gnomAD_genome_ALL': '0.1963'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51119858,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28965761',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '13714.p1',
        'start': 51119858,
        'study_name': 'Turner_2017',
        'validation': 'not_available',
        'variant': 'C>G'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60a2368e90466f147cf7',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.18556',
          'gnomAD_genome_ALL': '0.0026'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51119962,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28965761',
        're-annotation': {},
        'ref': 'G',
        'sample_id': '11043.p1',
        'start': 51119962,
        'study_name': 'Turner_2017',
        'validation': 'not_available',
        'variant': 'G>A'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60a2368e90466f147cf8',
        'alt': '-',
        'annotation': {'DeepSea_Score': '0.059156'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51139978,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28965761',
        're-annotation': {},
        'ref': 'CAAGTG',
        'sample_id': '12367.p1',
        'start': 51139973,
        'study_name': 'Turner_2017',
        'validation': 'not_available',
        'variant': 'CAAGTG>-'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60ad368e90466f150bfe',
        'alt': 'AGG',
        'annotation': {'DeepSea_Score': '0.10831',
          'gnomAD_genome_ALL': '6.58E-05'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51117976,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28263302',
        're-annotation': {},
        'ref': '-',
        'sample_id': '7-0141-003',
        'start': 51117976,
        'study_name': 'Yuen2017',
        'validation': 'not_available',
        'variant': '->AGG'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60ad368e90466f150bff',
        'alt': 'C',
        'annotation': {'DeepSea_Score': '0.27474',
          'gnomAD_genome_ALL': '0.0006'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51120928,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28263302',
        're-annotation': {},
        'ref': 'T',
        'sample_id': '2-1195-003',
        'start': 51120928,
        'study_name': 'Yuen2017',
        'validation': 'not_available',
        'variant': 'T>C'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60ad368e90466f150c00',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.035001'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51132965,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28263302',
        're-annotation': {},
        'ref': 'G',
        'sample_id': '2-1644-004',
        'start': 51132965,
        'study_name': 'Yuen2017',
        'validation': 'not_available',
        'variant': 'G>A'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60ad368e90466f150c01',
        'alt': 'C',
        'annotation': {'DeepSea_Score': '0.023353'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51134816,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28263302',
        're-annotation': {},
        'ref': 'T',
        'sample_id': 'AU3122301',
        'start': 51134816,
        'study_name': 'Yuen2017',
        'validation': 'not_available',
        'variant': 'T>C'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60ad368e90466f150c02',
        'alt': 'TG',
        'annotation': {'DeepSea_Score': '0.19389'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51145384,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28263302',
        're-annotation': {},
        'ref': '-',
        'sample_id': 'AU3154301',
        'start': 51145384,
        'study_name': 'Yuen2017',
        'validation': 'not_available',
        'variant': '->TG'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60b5368e90466f156401',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.17052'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51121926,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '27525107',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '2-1184-003',
        'start': 51121926,
        'study_name': 'Yuen2016',
        'validation': 'not_available',
        'variant': 'C>G'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60c5368e90466f162173',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.17208'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51119023,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '30679340',
        're-annotation': {},
        'ref': 'G',
        'sample_id': '30679340_137390',
        'start': 51119023,
        'study_name': 'Halldorsson 2019',
        'validation': 'not_available',
        'variant': 'G>A'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60c5368e90466f162174',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.055621',
          'gnomAD_genome_ALL': '3.23E-05'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51151784,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '30679340',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '30679340_120516',
        'start': 51151784,
        'study_name': 'Halldorsson 2019',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60c5368e90466f162175',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.11051'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51152553,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '30679340',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '30679340_149126',
        'start': 51152553,
        'study_name': 'Halldorsson 2019',
        'validation': 'not_available',
        'variant': 'C>G'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60d9368e90466f16e542',
        'alt': 'C',
        'annotation': {'DeepSea_Score': '0.081311'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51116845,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'T',
        'sample_id': '12130.s1',
        'start': 51116845,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'T>C'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60d9368e90466f16e5ae',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.071836'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51164220,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '13077.s1',
        'start': 51164220,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60da368e90466f16e628',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.13312',
          'gnomAD_genome_ALL': '9.69E-05'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51151514,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '14127.s1',
        'start': 51151514,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60da368e90466f16e62c',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.19648'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51126183,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'G',
        'sample_id': '14157.s1',
        'start': 51126183,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'G>A'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60e3368e90466f1754bf',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.15219',
          'gnomAD_genome_ALL': '0.0023'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51118566,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '28965761',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '11615.s1',
        'start': 51118566,
        'study_name': 'Turner_2017',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60e3368e90466f1754c0',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.22389'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51140657,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '28965761',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '13251.s1',
        'start': 51140657,
        'study_name': 'Turner_2017',
        'validation': 'not_available',
        'variant': 'C>G'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60e8368e90466f178f96',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.02565',
          'gnomAD_genome_ALL': '3.23E-05'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51130159,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '27322544',
        're-annotation': {},
        'ref': 'G',
        'start': 51130159,
        'study_name': 'Goldmann 2016',
        'validation': 'not_available',
        'variant': 'G>A'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60e8368e90466f178f97',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.064993'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51140515,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '27322544',
        're-annotation': {},
        'ref': 'A',
        'start': 51140515,
        'study_name': 'Goldmann 2016',
        'validation': 'not_available',
        'variant': 'A>G'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60ee368e90466f17d3e3',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.064993'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'non-PTB',
        'end': 51140515,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Fetal non-Preterm birth (non-PTB)',
        'pubmed_id': '28388617',
        're-annotation': {},
        'ref': 'A',
        'sample_id': 'P765',
        'start': 51140515,
        'study_name': 'Li 2017',
        'validation': 'not_available',
        'variant': 'A>G'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60ee368e90466f17dd19',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.02565',
          'gnomAD_genome_ALL': '3.23E-05'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'non-PTB',
        'end': 51130159,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Fetal non-Preterm birth (non-PTB)',
        'pubmed_id': '28388617',
        're-annotation': {},
        'ref': 'G',
        'sample_id': 'P155',
        'start': 51130159,
        'study_name': 'Li 2017',
        'validation': 'not_available',
        'variant': 'G>A'},
      {'Func_refGene': 'intronic',
        '_id': '5fdf60f8368e90466f184e1e',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.11051'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51152553,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '28959963',
        're-annotation': {},
        'ref': 'C',
        'sample_id': 'Proband-122',
        'start': 51152553,
        'study_name': 'Jonsson2017',
        'validation': 'not_available',
        'variant': 'C>G'},
      {'Func_refGene': 'UTR3',
        '_id': '5fdf6101368e90466f18b996',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.047824'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51170875,
        'entrez_id': '85358',
        'm_type': 'UTR-intron-updownstream',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '30679340',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '30679340_25637',
        'start': 51170875,
        'study_name': 'Halldorsson 2019',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf611e368e90466f1a16aa',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.29257',
          'gnomAD_genome_ALL': '9.79E-05'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51071488,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '13601.p1',
        'start': 51071488,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf612c368e90466f1abc99',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.40431'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51099673,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28965761',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '12220.p1',
        'start': 51099673,
        'study_name': 'Turner_2017',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf612c368e90466f1abc9a',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.44619'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51108713,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28965761',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '13924.p1',
        'start': 51108713,
        'study_name': 'Turner_2017',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf612c368e90466f1abc9b',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.0084996'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51111054,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '28965761',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '13575.p1',
        'start': 51111054,
        'study_name': 'Turner_2017',
        'validation': 'not_available',
        'variant': 'C>A'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf614b368e90466f1c1939',
        'alt': '-',
        'annotation': {'DeepSea_Score': '0.048184'},
        'case_or_control': 'Case',
        'chr': '22',
        'disorder': 'ASD',
        'end': 51071439,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Autism (ASD)',
        'pubmed_id': '27525107',
        're-annotation': {},
        'ref': 'AGCCACCACGCCCAGCTAATTTTCTTTTTTTTTCTTTTTTTTTTT',
        'sample_id': '2-1164-003',
        'start': 51071395,
        'study_name': 'Yuen2016',
        'validation': 'not_available',
        'variant': 'AGCCACCACGCCCAGCTAATTTTCTTTTTTTTTCTTTTTTTTTTT>-'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf615f368e90466f1d0c0c',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.27792'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51083132,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '30679340',
        're-annotation': {},
        'ref': 'T',
        'sample_id': '30679340_82068',
        'start': 51083132,
        'study_name': 'Halldorsson 2019',
        'validation': 'not_available',
        'variant': 'T>A'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf615f368e90466f1d0c0d',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.28124'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51093599,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '30679340',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '30679340_14972',
        'start': 51093599,
        'study_name': 'Halldorsson 2019',
        'validation': 'not_available',
        'variant': 'C>G'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf6176368e90466f1e1b02',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.32832'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51090910,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'T',
        'sample_id': '13122.s1',
        'start': 51090910,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'T>G'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf6176368e90466f1e1b03',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.18971'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51091083,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '13122.s1',
        'start': 51091083,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'C>G'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf6176368e90466f1e1b2c',
        'alt': 'G',
        'annotation': {'DeepSea_Score': '0.11175'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51072632,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'A',
        'sample_id': '13600.s1',
        'start': 51072632,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'A>G'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf6176368e90466f1e1b75',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.16507'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51099214,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '30545852',
        're-annotation': {},
        'ref': 'T',
        'sample_id': '14372.s1',
        'start': 51099214,
        'study_name': 'An 2018',
        'validation': 'not_available',
        'variant': 'T>A'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf6184368e90466f1ebe77',
        'alt': 'T',
        'annotation': {'DeepSea_Score': '0.038033'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Sibling Control',
        'end': 51095679,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Sibling Control',
        'pubmed_id': '28965761',
        're-annotation': {},
        'ref': 'C',
        'sample_id': '13738.s1',
        'start': 51095679,
        'study_name': 'Turner_2017',
        'validation': 'not_available',
        'variant': 'C>T'},
      {'Func_refGene': 'intergenic',
        '_id': '5fdf61a1368e90466f200e63',
        'alt': 'A',
        'annotation': {'DeepSea_Score': '0.27792'},
        'case_or_control': 'Control',
        'chr': '22',
        'disorder': 'Mixed healthy control',
        'end': 51083132,
        'entrez_id': ['410', '85358'],
        'm_type': 'intergenic',
        'primary_phenotype': 'Uncharacterized (Mixed healthy control)',
        'pubmed_id': '28959963',
        're-annotation': {},
        'ref': 'T',
        'sample_id': 'Proband-240',
        'start': 51083132,
        'study_name': 'Jonsson2017',
        'validation': 'not_available',
        'variant': 'T>A'}],
      'enhancer': [{'attr_list': [{'connected_gene': 'SHANK3', 'score': 12.02},
        {'connected_gene': 'SYCE3', 'score': 11.37},
        {'connected_gene': 'RPL23AP82', 'score': 5.02},
        {'connected_gene': 'LOC105373100', 'score': 0.39},
        {'connected_gene': 'RNU6-409P', 'score': 0.28},
        {'connected_gene': 'GC22M050692', 'score': 0.28}],
      'chr': 'chr22',
      'end': 50729342,
      'entrez_ids': ['85358',
        '644186',
        '284942',
        '105373100',
        '106481307'],
      'genehancer_id': 'GH22I050726',
      'score': '0.46',
      'start': 50726715},
      {'attr_list': [{'connected_gene': 'SHANK3', 'score': 571.63},
        {'connected_gene': 'BRD1', 'score': 20.73},
        {'connected_gene': 'CPT1B', 'score': 17.2},
        {'connected_gene': 'ZBED4', 'score': 15.84},
        {'connected_gene': 'ENSG00000272836',
          'score': 15.39},
        {'connected_gene': 'LOC105373095', 'score': 13.44},
        {'connected_gene': 'RABL2B', 'score': 13.42},
        {'connected_gene': 'LMF2', 'score': 13.08},
        {'connected_gene': 'NCAPH2', 'score': 12.61},
        {'connected_gene': 'TUBGCP6', 'score': 12.27},
        {'connected_gene': 'CHKB', 'score': 11.51},
        {'connected_gene': 'CHKB-AS1', 'score': 11.48},
        {'connected_gene': 'CHKB-CPT1B', 'score': 11.47},
        {'connected_gene': 'PLXNB2', 'score': 11.41},
        {'connected_gene': 'LOC105377205', 'score': 11.3},
        {'connected_gene': 'MAPK11', 'score': 11.14},
        {'connected_gene': 'ALG12', 'score': 10.38},
        {'connected_gene': 'SYCE3', 'score': 10.29},
        {'connected_gene': 'MAPK8IP2', 'score': 7.96},
        {'connected_gene': 'ACR', 'score': 6.76},
        {'connected_gene': 'DENND6B', 'score': 4.45},
        {'connected_gene': 'ARSA', 'score': 4.4},
        {'connected_gene': 'PPP6R2', 'score': 1.15},
        {'connected_gene': 'ENSG00000212569',
          'score': 0.77}],
      'chr': 'chr22',
      'end': 50675401,
      'entrez_ids': ['85358',
        '23774',
        '1375',
        '9889',
        '105373095',
        '11158',
        '91289',
        '29781',
        '85378',
        '1120',
        '100144603',
        '386593',
        '23654',
        '105377205',
        '5600',
        '79087',
        '644186',
        '23542',
        '49',
        '414918',
        '410',
        '9701'],
      'genehancer_id': 'GH22I050670',
      'score': '2.3',
      'start': 50670607},
      {'attr_list': [{'connected_gene': 'SHANK3', 'score': 6.23},
        {'connected_gene': 'RABL2B', 'score': 4.32},
        {'connected_gene': 'SELENOO', 'score': 4.01},
        {'connected_gene': 'RNU6-409P', 'score': 0.44},
        {'connected_gene': 'GC22M050692', 'score': 0.44},
        {'connected_gene': 'LOC105373100', 'score': 0.28}],
      'chr': 'chr22',
      'end': 50701723,
      'entrez_ids': ['85358',
        '11158',
        '83642',
        '106481307',
        '105373100'],
      'genehancer_id': 'GH22I050698',
      'score': '1.6',
      'start': 50698611},
      {'attr_list': [{'connected_gene': 'SHANK3', 'score': 6.17},
        {'connected_gene': 'RNU6-409P', 'score': 0.37},
        {'connected_gene': 'GC22M050692', 'score': 0.37},
        {'connected_gene': 'LOC105373100', 'score': 0.29}],
      'chr': 'chr22',
      'end': 50708096,
      'entrez_ids': ['85358', '106481307', '105373100'],
      'genehancer_id': 'GH22I050707',
      'score': '0.2',
      'start': 50707394},
      {'attr_list': [{'connected_gene': 'SHANK3', 'score': 5.87},
        {'connected_gene': 'RNU6-409P', 'score': 0.44},
        {'connected_gene': 'GC22M050692', 'score': 0.44}],
      'chr': 'chr22',
      'end': 50685443,
      'entrez_ids': ['85358', '106481307'],
      'genehancer_id': 'GH22I050683',
      'score': '0.31',
      'start': 50683619},
      {'attr_list': [{'connected_gene': 'SHANK3', 'score': 7.73},
        {'connected_gene': 'GC22P050670', 'score': 0.39},
        {'connected_gene': 'PIR51019', 'score': 0.34}],
      'chr': 'chr22',
      'end': 50657679,
      'entrez_ids': ['85358'],
      'genehancer_id': 'GH22I050655',
      'score': '1',
      'start': 50655802},
      {'attr_list': [{'connected_gene': 'SYCE3', 'score': 10.57},
        {'connected_gene': 'RPL23AP82', 'score': 8.19},
        {'connected_gene': 'RABL2B', 'score': 6.11},
        {'connected_gene': 'ACR', 'score': 5.01},
        {'connected_gene': 'LOC105373100', 'score': 0.37},
        {'connected_gene': 'RNU6-409P', 'score': 0.31},
        {'connected_gene': 'GC22M050692', 'score': 0.31},
        {'connected_gene': 'SHANK3', 'score': 0.26}],
      'chr': 'chr22',
      'end': 50719112,
      'entrez_ids': ['644186',
        '284942',
        '11158',
        '49',
        '105373100',
        '106481307',
        '85358'],
      'genehancer_id': 'GH22I050717',
      'score': '0.43',
      'start': 50717524},
      {'attr_list': [{'connected_gene': 'SYCE3', 'score': 10.57},
        {'connected_gene': 'RPL23AP82', 'score': 8.56},
        {'connected_gene': 'RABL2B', 'score': 7.02},
        {'connected_gene': 'LOC105373100', 'score': 0.37},
        {'connected_gene': 'RNU6-409P', 'score': 0.29},
        {'connected_gene': 'GC22M050692', 'score': 0.29},
        {'connected_gene': 'SHANK3', 'score': 0.25}],
      'chr': 'chr22',
      'end': 50725846,
      'entrez_ids': ['644186',
        '284942',
        '11158',
        '105373100',
        '106481307',
        '85358'],
      'genehancer_id': 'GH22I050719',
      'score': '0.49',
      'start': 50719224},
      {'attr_list': [{'connected_gene': 'SYCE3', 'score': 11.37},
        {'connected_gene': 'LOC105373100', 'score': 0.44},
        {'connected_gene': 'RNU6-409P', 'score': 0.26},
        {'connected_gene': 'GC22M050692', 'score': 0.26},
        {'connected_gene': 'SHANK3', 'score': 0.22}],
      'chr': 'chr22',
      'end': 50732745,
      'entrez_ids': ['644186', '105373100', '106481307', '85358'],
      'genehancer_id': 'GH22I050730',
      'score': '1.01',
      'start': 50730128},
      {'attr_list': [{'connected_gene': 'MAPK11', 'score': 559.17},
        {'connected_gene': 'DENND6B', 'score': 10.32},
        {'connected_gene': 'MAPK8IP2', 'score': 9.83},
        {'connected_gene': 'SHANK3', 'score': 3.7},
        {'connected_gene': 'PPP6R2', 'score': 2.57},
        {'connected_gene': 'MOV10L1', 'score': 2.33},
        {'connected_gene': 'MLC1', 'score': 2.3},
        {'connected_gene': 'SBF1', 'score': 1.67},
        {'connected_gene': 'ACR', 'score': 1.18},
        {'connected_gene': 'PIR50517', 'score': 0.39}],
      'chr': 'chr22',
      'end': 50271973,
      'entrez_ids': ['5600',
        '414918',
        '23542',
        '85358',
        '9701',
        '54456',
        '23209',
        '6305',
        '49'],
      'genehancer_id': 'GH22I050271',
      'score': '1.24',
      'start': 50271712},
      {'attr_list': [{'connected_gene': 'ARSA', 'score': 562.93},
        {'connected_gene': 'BRD1', 'score': 75.47},
        {'connected_gene': 'ZBED4', 'score': 48.51},
        {'connected_gene': 'RABL2B', 'score': 43.4},
        {'connected_gene': 'ENSG00000272836',
          'score': 39.66},
        {'connected_gene': 'TUBGCP6', 'score': 36.62},
        {'connected_gene': 'PLXNB2', 'score': 33.13},
        {'connected_gene': 'ALG12', 'score': 31.0},
        {'connected_gene': 'CHKB', 'score': 30.9},
        {'connected_gene': 'LOC105373095', 'score': 29.52},
        {'connected_gene': 'NCAPH2', 'score': 28.86},
        {'connected_gene': 'LOC105377205', 'score': 28.54},
        {'connected_gene': 'LMF2', 'score': 19.72},
        {'connected_gene': 'MAPK8IP2', 'score': 16.79},
        {'connected_gene': 'PPP6R2', 'score': 12.66},
        {'connected_gene': 'KLHDC7B', 'score': 12.62},
        {'connected_gene': 'MAPK11', 'score': 11.2},
        {'connected_gene': 'ENSG00000273192',
          'score': 10.3},
        {'connected_gene': 'DENND6B', 'score': 10.26},
        {'connected_gene': 'SHANK3', 'score': 10.24},
        {'connected_gene': 'CPT1B', 'score': 9.13},
        {'connected_gene': 'PIR50047', 'score': 0.77}],
      'chr': 'chr22',
      'end': 50629220,
      'entrez_ids': ['410',
        '23774',
        '9889',
        '11158',
        '85378',
        '23654',
        '79087',
        '1120',
        '105373095',
        '29781',
        '105377205',
        '91289',
        '23542',
        '9701',
        '113730',
        '5600',
        '414918',
        '85358',
        '1375'],
      'genehancer_id': 'GH22I050626',
      'score': '2.17',
      'start': 50626825},
      {'attr_list': [{'connected_gene': 'ARSA', 'score': 6.62},
        {'connected_gene': 'RABL2B', 'score': 5.41},
        {'connected_gene': 'RNU6-409P', 'score': 0.39},
        {'connected_gene': 'GC22M050692', 'score': 0.39},
        {'connected_gene': 'SHANK3', 'score': 0.29},
        {'connected_gene': 'LOC105373100', 'score': 0.29}],
      'chr': 'chr22',
      'end': 50706404,
      'entrez_ids': ['410',
        '11158',
        '106481307',
        '85358',
        '105373100'],
      'genehancer_id': 'GH22I050704',
      'score': '1.09',
      'start': 50704584},
      {'attr_list': [{'connected_gene': 'ARSA', 'score': 10.58},
        {'connected_gene': 'RNU6-409P', 'score': 0.77},
        {'connected_gene': 'GC22M050692', 'score': 0.77},
        {'connected_gene': 'SHANK3', 'score': 0.39}],
      'chr': 'chr22',
      'end': 50687595,
      'entrez_ids': ['410', '106481307', '85358'],
      'genehancer_id': 'GH22I050686',
      'score': '0.67',
      'start': 50686829},
      {'attr_list': [{'connected_gene': 'BRD1', 'score': 15.9},
        {'connected_gene': 'SHANK3', 'score': 6.46},
        {'connected_gene': 'RABL2B', 'score': 6.45},
        {'connected_gene': 'RNU6-409P', 'score': 0.44},
        {'connected_gene': 'GC22M050692', 'score': 0.44},
        {'connected_gene': 'LOC105373100', 'score': 0.26}],
      'chr': 'chr22',
      'end': 50698454,
      'entrez_ids': ['23774',
        '85358',
        '11158',
        '106481307',
        '105373100'],
      'genehancer_id': 'GH22I050696',
      'score': '0.86',
      'start': 50696427},
      {'attr_list': [{'connected_gene': 'BRD1', 'score': 74.75},
        {'connected_gene': 'RABL2B', 'score': 68.93},
        {'connected_gene': 'ALG12', 'score': 62.13},
        {'connected_gene': 'PLXNB2', 'score': 59.83},
        {'connected_gene': 'ENSG00000272836',
          'score': 51.73},
        {'connected_gene': 'CHKB', 'score': 45.95},
        {'connected_gene': 'TUBGCP6', 'score': 43.97},
        {'connected_gene': 'ZBED4', 'score': 36.05},
        {'connected_gene': 'LMF2', 'score': 35.0},
        {'connected_gene': 'ENSG00000273192',
          'score': 34.03},
        {'connected_gene': 'LOC105373095', 'score': 34.0},
        {'connected_gene': 'NCAPH2', 'score': 31.26},
        {'connected_gene': 'LOC105377205', 'score': 20.63},
        {'connected_gene': 'TRABD', 'score': 18.55},
        {'connected_gene': 'DENND6B', 'score': 16.89},
        {'connected_gene': 'PPP6R2', 'score': 13.69},
        {'connected_gene': 'KLHDC7B', 'score': 12.51},
        {'connected_gene': 'MAPK11', 'score': 11.35},
        {'connected_gene': 'MLC1', 'score': 10.24},
        {'connected_gene': 'SHANK3', 'score': 10.05},
        {'connected_gene': 'MAPK8IP2', 'score': 9.89}],
      'chr': 'chr22',
      'end': 50341281,
      'entrez_ids': ['23774',
        '11158',
        '79087',
        '23654',
        '1120',
        '85378',
        '9889',
        '91289',
        '105373095',
        '29781',
        '105377205',
        '80305',
        '414918',
        '9701',
        '113730',
        '5600',
        '23209',
        '85358',
        '23542'],
      'genehancer_id': 'GH22I050339',
      'score': '0.92',
      'start': 50339166},
      {'attr_list': [{'connected_gene': 'CHKB', 'score': 12.0},
        {'connected_gene': 'MAPK8IP2', 'score': 12.0},
        {'connected_gene': 'SHANK3', 'score': 5.62},
        {'connected_gene': 'PIR51019', 'score': 0.44},
        {'connected_gene': 'GC22P050670', 'score': 0.31}],
      'chr': 'chr22',
      'end': 50642755,
      'entrez_ids': ['1120', '23542', '85358'],
      'genehancer_id': 'GH22I050640',
      'score': '1.28',
      'start': 50640913},
      {'attr_list': [{'connected_gene': 'RNU6-409P', 'score': 550.77},
        {'connected_gene': 'GC22M050692', 'score': 550.77},
        {'connected_gene': 'SHANK3', 'score': 0.37},
        {'connected_gene': 'LOC105373100', 'score': 0.25}],
      'chr': 'chr22',
      'end': 50691762,
      'entrez_ids': ['106481307', '85358', '105373100'],
      'genehancer_id': 'GH22I050691',
      'score': '0.62',
      'start': 50691633},
      {'attr_list': [{'connected_gene': 'RNU6-409P', 'score': 0.39},
        {'connected_gene': 'GC22M050692', 'score': 0.39},
        {'connected_gene': 'SHANK3', 'score': 0.31},
        {'connected_gene': 'LOC105373100', 'score': 0.28}],
      'chr': 'chr22',
      'end': 50702563,
      'entrez_ids': ['106481307', '85358', '105373100'],
      'genehancer_id': 'GH22I050701',
      'score': '0.38',
      'start': 50701888},
      {'attr_list': [{'connected_gene': 'RNU6-409P', 'score': 0.77},
        {'connected_gene': 'GC22M050692', 'score': 0.77},
        {'connected_gene': 'SHANK3', 'score': 0.39}],
      'chr': 'chr22',
      'end': 50689085,
      'entrez_ids': ['106481307', '85358'],
      'genehancer_id': 'GH22I050687',
      'score': '0.2',
      'start': 50687900},
      {'attr_list': [{'connected_gene': 'RNU6-409P', 'score': 13.2},
        {'connected_gene': 'SYCE3', 'score': 10.84},
        {'connected_gene': 'RPL23AP82', 'score': 6.32},
        {'connected_gene': 'LOC105373100', 'score': 0.34},
        {'connected_gene': 'GC22M050692', 'score': 0.34},
        {'connected_gene': 'SHANK3', 'score': 0.26}],
      'chr': 'chr22',
      'end': 50717194,
      'entrez_ids': ['106481307',
        '644186',
        '284942',
        '105373100',
        '85358'],
      'genehancer_id': 'GH22I050715',
      'score': '0.43',
      'start': 50715135},
      {'attr_list': [{'connected_gene': 'RNU6-409P', 'score': 0.34},
        {'connected_gene': 'LOC105373100', 'score': 0.34},
        {'connected_gene': 'GC22M050692', 'score': 0.34},
        {'connected_gene': 'SHANK3', 'score': 0.28}],
      'chr': 'chr22',
      'end': 50713802,
      'entrez_ids': ['106481307', '105373100', '85358'],
      'genehancer_id': 'GH22I050713',
      'score': '0.4',
      'start': 50713693},
      {'attr_list': [{'connected_gene': 'RNU6-409P', 'score': 0.37},
        {'connected_gene': 'GC22M050692', 'score': 0.37},
        {'connected_gene': 'LOC105373100', 'score': 0.31},
        {'connected_gene': 'SHANK3', 'score': 0.28}],
      'chr': 'chr22',
      'end': 50710454,
      'entrez_ids': ['106481307', '105373100', '85358'],
      'genehancer_id': 'GH22I050709',
      'score': '0.31',
      'start': 50709312}],
      'entrez_id': '85358',
      'promoter': [{'cage_peak_id': 'chr22:51135914..51135945,+',
        'chr': 'chr22',
        'description': 'CAGE_peak_1_at_SHANK3_5end',
        'end': 51135945,
        'entrez_id': '85358',
        'short_descripton': 'p1@SHANK3',
        'start': 51135914,
        'unprot_id': '0'},
      {'cage_peak_id': 'chr22:51158914..51158921,+',
        'chr': 'chr22',
        'description': 'CAGE_peak_13_at_SHANK3_5end',
        'end': 51158921,
        'entrez_id': '85358',
        'short_descripton': 'p13@SHANK3',
        'start': 51158914,
        'unprot_id': 'Q9BYB0'},
      {'cage_peak_id': 'chr22:51159849..51159895,+',
        'chr': 'chr22',
        'description': 'CAGE_peak_8_at_SHANK3_5end',
        'end': 51159895,
        'entrez_id': '85358',
        'short_descripton': 'p8@SHANK3',
        'start': 51159849,
        'unprot_id': 'Q6P5A2'}],
      'symbol': 'SHANK3',
      'transcripts': [{'chr': 'chr22',
        'entrez_id': '85358',
        'express': {'Adipose - Subcutaneous': 29.10364253393668,
          'Adipose - Visceral (Omentum)': 29.92788732394364,
          'Adrenal Gland': 5.104631578947368,
          'Artery - Aorta': 4.396856187290972,
          'Artery - Coronary': 10.77583815028902,
          'Artery - Tibial': 4.877732426303854,
          'Bladder': 8.197272727272725,
          'Brain - Amygdala': 14.7161,
          'Brain - Anterior cingulate cortex (BA24)': 15.91859504132231,
          'Brain - Caudate (basal ganglia)': 13.6908125,
          'Brain - Cerebellar Hemisphere': 79.32845588235291,
          'Brain - Cerebellum': 102.069421965318,
          'Brain - Cortex': 23.91639240506328,
          'Brain - Frontal Cortex (BA9)': 19.47054263565891,
          'Brain - Hippocampus': 17.75406504065041,
          'Brain - Hypothalamus': 8.024545454545452,
          'Brain - Nucleus accumbens (basal ganglia)': 14.45197278911564,
          'Brain - Putamen (basal ganglia)': 13.18395161290322,
          'Brain - Spinal cord (cervical c-1)': 7.834065934065936,
          'Brain - Substantia nigra': 6.581477272727272,
          'Breast - Mammary Tissue': 31.61231034482757,
          'Cells - EBV-transformed lymphocytes': 0.04299999999999997,
          'Cells - Transformed fibroblasts': 0.6268804664723031,
          'Cervix - Ectocervix': 12.98,
          'Cervix - Endocervix': 12.132,
          'Colon - Sigmoid': 5.938412017167382,
          'Colon - Transverse': 5.115912408759121,
          'Entrez_id': '85358',
          'Esophagus - Gastroesophageal Junction': 8.96450819672131,
          'Esophagus - Mucosa': 5.403759213759214,
          'Esophagus - Muscularis': 9.399702702702692,
          'Fallopian Tube': 14.61571428571428,
          'Heart - Atrial Appendage': 6.852457912457916,
          'Heart - Left Ventricle': 8.922706270627064,
          'Kidney - Cortex': 12.68111111111111,
          'Liver': 5.689485714285712,
          'Lung': 29.74529274004684,
          'Minor Salivary Gland': 5.911546391752577,
          'Muscle - Skeletal': 1.558475177304964,
          'Nerve - Tibial': 11.27830917874397,
          'Ovary': 4.307894736842106,
          'Pancreas': 2.08600806451613,
          'Pituitary': 12.4332786885246,
          'Prostate': 9.118157894736838,
          'Skin - Not Sun Exposed (Suprapubic)': 5.855762273901805,
          'Skin - Sun Exposed (Lower leg)': 5.991247357293866,
          'Small Intestine - Terminal Ileum': 6.467153284671534,
          'Spleen': 68.13870370370374,
          'Stomach': 4.798129770992362,
          'Testis': 3.969498069498072,
          'Thyroid': 18.4648206278027,
          'Uterus': 19.00270270270271,
          'Vagina': 10.47426086956522,
          'Whole Blood': 0.05928746928746922,
          'ensembl_trs_id': 'ENST00000414786.2',
          'gencode_id': 'ENSG00000251322.3',
          'transcript_id': 'ENST00000414786'},
        'gencode_id': 'ENST00000414786.2',
        'psymukb_id': 'PSY_T177761',
        'source': 'gencode',
        'strand': '+',
        'structure': {'coding_exon_region': [[51113069, 51113132],
          [51113475, 51113679],
          [51115049, 51115121],
          [51117012, 51117121],
          [51117196, 51117348],
          [51117446, 51117614],
          [51117739, 51117856],
          [51121767, 51121845],
          [51123012, 51123079],
          [51133202, 51133476],
          [51135991, 51136143],
          [51137117, 51137231],
          [51142287, 51142363],
          [51142593, 51142676],
          [51143165, 51143290],
          [51143391, 51143524],
          [51144499, 51144580],
          [51150042, 51150066],
          [51153344, 51153475],
          [51154096, 51154181],
          [51158611, 51160865],
          [51162554, 51162581],
          [51169148, 51169740]],
        'transcript_exon_region': [[51112842, 51113132],
          [51113475, 51113679],
          [51115049, 51115121],
          [51117012, 51117121],
          [51117196, 51117348],
          [51117446, 51117614],
          [51117739, 51117856],
          [51121767, 51121845],
          [51123012, 51123079],
          [51133202, 51133476],
          [51135991, 51136143],
          [51137117, 51137231],
          [51142287, 51142363],
          [51142593, 51142676],
          [51143165, 51143290],
          [51143391, 51143524],
          [51144499, 51144580],
          [51150042, 51150066],
          [51153344, 51153475],
          [51154096, 51154181],
          [51158611, 51160865],
          [51162554, 51162581],
          [51169148,
            51171726]],
        'utr3': [51169741, 51171726],
        'utr3_exon_region': [[51169741, 51171726]],
        'utr5': [51112842, 51113068],
        'utr5_exon_region': [[51112842, 51113068]]},
        'symbol': 'SHANK3',
        'transcript_id': 'ENST00000414786'},
      {'chr': 'chr22',
        'ensembl_pro': ['ENSP00000489407'],
        'entrez_id': '85358',
        'express': {'Adipose - Subcutaneous': 0.2823076923076923,
          'Adipose - Visceral (Omentum)': 0.2440563380281689,
          'Adrenal Gland': 0.03321052631578948,
          'Artery - Aorta': 0.05662207357859532,
          'Artery - Coronary': 0.09023121387283235,
          'Artery - Tibial': 0.05541950113378685,
          'Bladder': 0.1872727272727273,
          'Brain - Amygdala': 0.06690000000000002,
          'Brain - Anterior cingulate cortex (BA24)': 0.09487603305785126,
          'Brain - Caudate (basal ganglia)': 0.0530625,
          'Brain - Cerebellar Hemisphere': 0.3027205882352941,
          'Brain - Cerebellum': 0.3069942196531792,
          'Brain - Cortex': 0.08126582278481013,
          'Brain - Frontal Cortex (BA9)': 0.07674418604651162,
          'Brain - Hippocampus': 0.07016260162601627,
          'Brain - Hypothalamus': 0.05727272727272728,
          'Brain - Nucleus accumbens (basal ganglia)': 0.0758503401360544,
          'Brain - Putamen (basal ganglia)': 0.05169354838709678,
          'Brain - Spinal cord (cervical c-1)': 0.1291208791208791,
          'Brain - Substantia nigra': 0.06806818181818182,
          'Breast - Mammary Tissue': 0.2470000000000001,
          'Cells - EBV-transformed lymphocytes': 0.02092307692307693,
          'Cells - Transformed fibroblasts': 0.02399416909620991,
          'Cervix - Ectocervix': 0.04,
          'Cervix - Endocervix': 0.042,
          'Colon - Sigmoid': 0.08982832618025753,
          'Colon - Transverse': 0.04737226277372263,
          'Entrez_id': '85358',
          'Esophagus - Gastroesophageal Junction': 0.09758196721311478,
          'Esophagus - Mucosa': 0.04410319410319412,
          'Esophagus - Muscularis': 0.1401351351351351,
          'Fallopian Tube': 0.05285714285714286,
          'Heart - Atrial Appendage': 0.1035690235690235,
          'Heart - Left Ventricle': 0.1244884488448845,
          'Kidney - Cortex': 0.06955555555555554,
          'Liver': 0.02194285714285715,
          'Lung': 0.2373067915690868,
          'Minor Salivary Gland': 0.0772164948453608,
          'Muscle - Skeletal': 0.0998936170212766,
          'Nerve - Tibial': 0.1436231884057971,
          'Ovary': 0.06030075187969924,
          'Pancreas': 0.01532258064516129,
          'Pituitary': 0.05633879781420766,
          'Prostate': 0.1091447368421053,
          'Skin - Not Sun Exposed (Suprapubic)': 0.04627906976744185,
          'Skin - Sun Exposed (Lower leg)': 0.05598308668076111,
          'Small Intestine - Terminal Ileum': 0.0462043795620438,
          'Spleen': 0.2555555555555555,
          'Stomach': 0.03282442748091603,
          'Testis': 0.05405405405405406,
          'Thyroid': 0.1888116591928251,
          'Uterus': 0.1845945945945946,
          'Vagina': 0.1216521739130435,
          'Whole Blood': 0.01203931203931203,
          'ensembl_trs_id': 'ENST00000445220.2',
          'gencode_id': 'ENSG00000251322.3',
          'transcript_id': 'ENST00000445220'},
        'gencode_id': 'ENST00000445220.2',
        'psymukb_id': 'PSY_T177762',
        'source': 'gencode',
        'strand': '+',
        'structure': {'coding_exon_region': [[51113069, 51113132],
          [51113475, 51113679],
          [51115049, 51115121],
          [51117012, 51117121],
          [51117196, 51117348],
          [51117446, 51117614],
          [51117739, 51117856],
          [51121767, 51121845],
          [51123012, 51123079],
          [51133202, 51133476],
          [51135946, 51136143],
          [51137117, 51137231],
          [51142287, 51142363],
          [51142593, 51142676],
          [51143165, 51143290],
          [51143391, 51143524],
          [51144499, 51144593],
          [51153230, 51153244],
          [51153344, 51153475],
          [51154096, 51154181],
          [51158611, 51160865],
          [51162554, 51162581],
          [51169148, 51169740]],
        'transcript_exon_region': [[51113069, 51113132],
          [51113475, 51113679],
          [51115049, 51115121],
          [51117012, 51117121],
          [51117196, 51117348],
          [51117446, 51117614],
          [51117739, 51117856],
          [51121767, 51121845],
          [51123012, 51123079],
          [51133202, 51133476],
          [51135946, 51136143],
          [51137117, 51137231],
          [51142287, 51142363],
          [51142593, 51142676],
          [51143165, 51143290],
          [51143391, 51143524],
          [51144499, 51144593],
          [51153230, 51153244],
          [51153344, 51153475],
          [51154096, 51154181],
          [51158611, 51160865],
          [51162554, 51162581],
          [51169148,
            51171641]],
        'utr3': [51169741, 51171641],
        'utr3_exon_region': [[51169741, 51171641]]},
        'symbol': 'SHANK3',
        'transcript_id': 'ENST00000445220',
        'uniprotKB_id': ['A0A0U1RR93_HUMAN'],
        'uniprotkb_ac': ['A0A0U1RR93']},
      {'chr': 'chr22',
        'ensembl_pro': ['ENSP00000489147'],
        'entrez_id': '85358',
        'express': {'Adipose - Subcutaneous': 28.61753393665162,
          'Adipose - Visceral (Omentum)': 23.42557746478873,
          'Adrenal Gland': 2.485842105263158,
          'Artery - Aorta': 3.86304347826087,
          'Artery - Coronary': 8.711849710982655,
          'Artery - Tibial': 4.937256235827665,
          'Bladder': 7.569999999999999,
          'Brain - Amygdala': 13.7108,
          'Brain - Anterior cingulate cortex (BA24)': 19.69801652892562,
          'Brain - Caudate (basal ganglia)': 10.1170625,
          'Brain - Cerebellar Hemisphere': 29.52073529411764,
          'Brain - Cerebellum': 37.83595375722545,
          'Brain - Cortex': 28.50544303797468,
          'Brain - Frontal Cortex (BA9)': 23.05759689922481,
          'Brain - Hippocampus': 16.58829268292682,
          'Brain - Hypothalamus': 5.957024793388427,
          'Brain - Nucleus accumbens (basal ganglia)': 13.98795918367347,
          'Brain - Putamen (basal ganglia)': 7.78185483870968,
          'Brain - Spinal cord (cervical c-1)': 5.354505494505492,
          'Brain - Substantia nigra': 5.186249999999999,
          'Breast - Mammary Tissue': 25.81499999999998,
          'Cells - EBV-transformed lymphocytes': 0.02292307692307692,
          'Cells - Transformed fibroblasts': 0.7136734693877553,
          'Cervix - Ectocervix': 12.415,
          'Cervix - Endocervix': 14.69,
          'Colon - Sigmoid': 6.306866952789703,
          'Colon - Transverse': 4.689087591240876,
          'Entrez_id': '85358',
          'Esophagus - Gastroesophageal Junction': 8.907254098360658,
          'Esophagus - Mucosa': 3.610835380835384,
          'Esophagus - Muscularis': 9.165135135135134,
          'Fallopian Tube': 11.70714285714286,
          'Heart - Atrial Appendage': 7.371582491582495,
          'Heart - Left Ventricle': 7.352607260726064,
          'Kidney - Cortex': 6.974666666666664,
          'Liver': 1.620628571428571,
          'Lung': 18.38377049180327,
          'Minor Salivary Gland': 5.361752577319588,
          'Muscle - Skeletal': 5.884485815602834,
          'Nerve - Tibial': 11.44992753623188,
          'Ovary': 3.614812030075188,
          'Pancreas': 1.225725806451613,
          'Pituitary': 4.862950819672132,
          'Prostate': 7.545592105263163,
          'Skin - Not Sun Exposed (Suprapubic)': 4.78142118863049,
          'Skin - Sun Exposed (Lower leg)': 5.502198731501061,
          'Small Intestine - Terminal Ileum': 4.837445255474455,
          'Spleen': 32.4354938271605,
          'Stomach': 3.341297709923662,
          'Testis': 2.545868725868726,
          'Thyroid': 14.75484304932736,
          'Uterus': 18.1000900900901,
          'Vagina': 9.718173913043476,
          'Whole Blood': 0.02265356265356265,
          'ensembl_trs_id': 'ENST00000262795.3',
          'gencode_id': 'ENSG00000251322.3',
          'transcript_id': 'ENST00000262795'},
        'gencode_id': 'ENST00000262795.3',
        'psymukb_id': 'PSY_T177763',
        'source': 'gencode',
        'strand': '+',
        'structure': {'coding_exon_region': [[51113069, 51113132],
          [51113475, 51113679],
          [51115049, 51115121],
          [51117012, 51117121],
          [51117196, 51117348],
          [51117446, 51117614],
          [51117739, 51117856],
          [51121767, 51121845],
          [51123012, 51123079],
          [51133202, 51133476],
          [51135670, 51135719],
          [51135950, 51136143],
          [51137117, 51137231],
          [51142287, 51142363],
          [51142593, 51142676],
          [51143165, 51143290],
          [51143391, 51143524],
          [51144499, 51144580],
          [51150042, 51150066],
          [51153344, 51153475],
          [51154096, 51154181],
          [51158611, 51160865],
          [51169148, 51169740]],
        'transcript_exon_region': [[51113069, 51113132],
          [51113475, 51113679],
          [51115049, 51115121],
          [51117012, 51117121],
          [51117196, 51117348],
          [51117446, 51117614],
          [51117739, 51117856],
          [51121767, 51121845],
          [51123012, 51123079],
          [51133202, 51133476],
          [51135670, 51135719],
          [51135950, 51136143],
          [51137117, 51137231],
          [51142287, 51142363],
          [51142593, 51142676],
          [51143165, 51143290],
          [51143391, 51143524],
          [51144499, 51144580],
          [51150042, 51150066],
          [51153344, 51153475],
          [51154096, 51154181],
          [51158611, 51160865],
          [51169148,
            51171641]],
        'utr3': [51169741, 51171641],
        'utr3_exon_region': [[51169741, 51171641]]},
        'symbol': 'SHANK3',
        'transcript_id': 'ENST00000262795',
        'uniprotKB_id': ['A0A0U1RQS4_HUMAN'],
        'uniprotkb_ac': ['A0A0U1RQS4']},
      {'chr': 'chr22',
        'entrez_id': '85358',
        'proteomicsDB_id': ['79606'],
        'psymukb_id': 'PSY_T246482',
        'refseq_id': 'NM_033517',
        'source': 'refseq',
        'strand': '+',
        'structure': {'coding_exon_region': [[51113069, 51113132],
          [51113475, 51113679],
          [51115049, 51115121],
          [51117012, 51117121],
          [51117196, 51117348],
          [51117446, 51117614],
          [51117739, 51117856],
          [51121767, 51121845],
          [51123012, 51123079],
          [51133202, 51133474],
          [51135984, 51135989],
          [51135991, 51136143],
          [51137117, 51137231],
          [51142287, 51142363],
          [51142593, 51142676],
          [51143165, 51143290],
          [51143391, 51143524],
          [51144499, 51144580],
          [51150042, 51150066],
          [51153344, 51153475],
          [51154096, 51154181],
          [51158611, 51160865],
          [51169148, 51169740]],
        'transcript_exon_region': [[51113069, 51113132],
          [51113475, 51113679],
          [51115049, 51115121],
          [51117012, 51117121],
          [51117196, 51117348],
          [51117446, 51117614],
          [51117739, 51117856],
          [51121767, 51121845],
          [51123012, 51123079],
          [51133202, 51133474],
          [51135984, 51135989],
          [51135991, 51136143],
          [51137117, 51137231],
          [51142287, 51142363],
          [51142593, 51142676],
          [51143165, 51143290],
          [51143391, 51143524],
          [51144499, 51144580],
          [51150042, 51150066],
          [51153344, 51153475],
          [51154096, 51154181],
          [51158611, 51160865],
          [51169148,
            51171640]],
        'utr3': [51169741, 51171640],
        'utr3_exon_region': [[51169741, 51171640]]},
        'symbol': 'SHANK3',
        'transcript_id': 'NM_033517',
        'uniprotKB_id': ['SHAN3_HUMAN'],
        'uniprotkb_ac': ['Q9BYB0']}]}
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
      // for (let i = 0; i < exton_plot_data.length; i++) {
      //   let item = exton_plot_data[i]
      //   // eslint-disable-next-line camelcase
      //   let trace_item = {
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
      //     x: [item[0][0], item[1][0]],
      //     y: [item[0][1], item[1][1]],
      //     text: String(item[0][2]) + '-' + String(item[1][2]),
      //     line: {
      //       color: 'rgb(72,130,180)',
      //       shape: 'linear',
      //       width: 10,
      //       simplify: true
      //     }
      //   }
      //   trace.push(trace_item)
      // }
      // for (let i = 0; i < utr_plot_data.length; i++) {
      //   let item = utr_plot_data[i]
      //   // eslint-disable-next-line camelcase
      //   let trace_item = {
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
      //     x: [item[0][0], item[1][0]],
      //     y: [item[0][1], item[1][1]],
      //     text: String(item[0][2]) + '-' + String(item[1][2]),
      //     line: {
      //       color: 'gray',
      //       shape: 'linear',
      //       width: 5
      //     }
      //   }
      //
      //   trace.push(trace_item)
      // }
      // if (promoter_plot_data.length !== 0) {
      //   for (let i = 0; i < promoter_plot_data.length; i++) {
      //     let item = promoter_plot_data[i]
      //     // eslint-disable-next-line camelcase
      //     let trace_item = {
      //       type: 'scatter',
      //       visible: true,
      //       hoverinfo: 'text',
      //       hoverlabel: {
      //         'font': {
      //           'size': 10
      //         }
      //       },
      //       showlegend: false,
      //       mode: 'lines',
      //       x: [item[0][0], item[1][0]],
      //       y: [item[0][1], item[1][1]],
      //       text: String(item[0][2]),
      //       line: {
      //         color: get_promoter_color(String(item[0][2])),
      //         shape: 'linear',
      //         width: 10,
      //         simplify: true
      //       }
      //     }
      //     trace.push(trace_item)
      //   }
      // }
      // if (enhancer_plot_data.length !== 0) {
      //   for (let i = 0; i < enhancer_plot_data.length; i++) {
      //     let item = enhancer_plot_data[i]
      //     // eslint-disable-next-line camelcase
      //     let trace_item = {
      //       type: 'scatter',
      //       visible: true,
      //       hoverinfo: 'text',
      //       hoverlabel: {
      //         'font': {
      //           'size': 10
      //         }
      //       },
      //       showlegend: false,
      //       mode: 'lines',
      //       x: [item[0][0], item[1][0]],
      //       y: [item[0][1], item[1][1]],
      //       text: String(item[0][2]),
      //       line: {
      //         color: get_enhancer_color(String(item[0][2])),
      //         shape: 'linear',
      //         width: 10,
      //         simplify: true
      //       }
      //     }
      //     trace.push(trace_item)
      //   }
      // }
      // let traceDNM = []
      // for (let i = 0; i < dnm_plot_data.length; i++) {
      //   let item = dnm_plot_data[i]
      //   let type = item[0][2].split(',')[2]
      //   let c = get_DNM_color(type)
      //   // eslint-disable-next-line camelcase
      //   let trace_item = {
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
      //     x: [item[0][0], item[1][0]],
      //     y: [item[0][1], item[1][1]],
      //     text: String(item[0][2]),
      //     line: {
      //       color: c,
      //       shape: 'linear',
      //       width: 10,
      //       simplify: true
      //     }
      //   }
      //   traceDNM.push(trace_item)
      // }
      // trace.push(traceDNM[26])
      // // for (const item of traceDNM) {
      // // }
      // const traces = []
      // let x = traceDNM[26]['x']
      // traces.push(traceDNM[26])
      // for (const traceItem of trace) {
      //   let y = traceItem['x']
      //   if ((x[0] > y[0] && x[0] < y[1]) || (y[0] < x[1] && x[1] < y[1])) {
      //     traces.push(traceItem)
      //   }
      // }
      // console.log(trace)
      // console.log(traces)
      // const l = []
      // for (let i = 0; i < trace.length; i++) {
      //   l.push(trace[i])
      // }
      // for (let i = 0; i < traces.length; i++) {
      //   l.push(traces[i])
      // }
      // console.log(l)
      // eslint-disable-next-line camelcase
      for (let i = 0; i < exton_plot_data.length; i++) {
        const item = exton_plot_data[i]
        // eslint-disable-next-line camelcase
        const trace_item = {
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
          text: 'Exon, ' + '[' + String(item[0][2]) + '-' + String(item[1][2]) + ']',
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
        const item = utr_plot_data[i]
        // eslint-disable-next-line camelcase
        const trace_item = {
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
          text: 'Untranslated region, ' + '[' + String(item[0][2]) + '-' + String(item[1][2]) + ']',
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
          const item = promoter_plot_data[i]
          // eslint-disable-next-line camelcase
          const trace_item = {
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
          const item = enhancer_plot_data[i]
          // eslint-disable-next-line camelcase
          const trace_item = {
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
        const item = dnm_plot_data[i]
        const type = item[0][2].split(',')[2]
        const c = get_DNM_color(type)
        // eslint-disable-next-line camelcase
        const trace_item = {
          type: 'scatter',
          visible: true,
          hoverinfo: 'text',
          hoverlabel: {
            'font': {
              'size': 13
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
        // trace.push({
        //   type: 'lines',
        //   visible: true,
        //   hoverinfo: 'text',
        //   hoverlabel: {
        //     'font': {
        //       'size': 10
        //     }
        //   },
        //   showlegend: false,
        //   mode: 'lines',
        //   x: [(item[0][0] + item[1][0]) / 2, (item[0][0] + item[1][0]) / 2],
        //   y: ['Variant', trace[0]['y'][0]],
        //   text: String(item[0][2]),
        //   line: {
        //     color: 'black',
        //     width: 0.4
        //   }
        // })
      }
      console.log(trace)
      // eslint-disable-next-line camelcase
      const visible_list_original = []
      // eslint-disable-next-line camelcase
      const visible_list_normalized = []
      for (let i = 0; i < trace.length; i++) {
        visible_list_original.push(true)
        visible_list_normalized.push(false)
      }
      for (let i = 0; i < trace.length; i++) {
        visible_list_original.push(false)
        visible_list_normalized.push(true)
      }
      console.log(visible_list_original)
      console.log(visible_list_normalized)
      const updatemenus = [{
        type: 'buttons',
        active: -1,
        pad: {
          r: 30,
          t: 20
        },
        buttons: [{
          label: 'original TPM',
          method: 'update',
          args: [{'visible': visible_list_original}]
        },
        {
          label: 'log<sub>2</sub> ( TPM + 1 )',
          method: 'update',
          args: [{'visible': visible_list_normalized}]
        }]
      }]
      let layout = {
        updatemenus: updatemenus,
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
    }
  },
  created () {
    this.getData()
  }
}
</script>

<style scoped>

</style>
