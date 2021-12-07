<template>
  <div>
    <div
      v-loading="loading"
      element-loading-background="rgba(255, 255, 255, 0.8)"
      v-if="isPlot">
      <Plot
        :data="data"
        :layout="layout"
      />
    </div>
    <div
      v-else>
      <h3>There is no corresponding data published yet, we will update it when such data available.</h3>
    </div>
  </div>
</template>
<script>
import Plot from 'vue-plotly.js'
// import { getVariantIsoforms } from '@/api/variant'
export default {
  name: 'GtexTransExp',
  components: {
    Plot
  },
  data () {
    return {
      data: [],
      layout: {},
      isPlot: true,
      loading: true
    }
  },
  methods: {
    GtexTranscriptExpressPlot () {
      // eslint-disable-next-line camelcase
      const brain_express = 0
      const data = [{
        'Adrenal Gland': [
          222.93371,
          440.7881,
          129.09707,
          412.8295,
          379.50894,
          222.85974,
          553.71638,
          265.29543,
          252.3208,
          40.33562,
          363.67779,
          396.03144
        ],
        'Artery - Aorta': [
          58.70515,
          27.9147,
          33.79207,
          31.28075,
          54.46161,
          100.4348,
          68.0113,
          22.98112,
          23.8753,
          69.21485,
          329.66026,
          24.90439,
          59.50293,
          27600,
          278.89936,
          98.0513,
          125.00922,
          27.10788
        ],
        'Artery - Coronary': [
          24.92676,
          96.64557,
          69.57367
        ],
        'Artery - Tibial': [
          47.89825,
          39.98815,
          5600
        ],
        'Brain - Cerebellum': [
          16.72912,
          25.19284,
          26.63112,
          29.2525
        ],
        'Brain - Cortex': [
          36.17804,
          24.41673,
          37.62419
        ],
        'Breast - Mammary Tissue': [
          65.38902,
          45.40052,
          107.21482,
          24.84573,
          32.50425,
          93.23293,
          108.78338,
          41.69186
        ],
        'Colon - Sigmoid': [
          37.75798,
          16.22852,
          53.31111,
          33.20979,
          54.46718,
          15.44978,
          30.67551,
          38.52959,
          93.9905,
          499,
          119.15531,
          19.90651,
          177.50929,
          52.46561,
          239.16268,
          28.02446
        ],
        'Colon - Transverse': [
          25.12339,
          245.2665,
          171.22399,
          187.8639,
          63.77693,
          164.41382,
          137.6748
        ],
        'Esophagus - Gastroesophageal Junction': [
          24.58229,
          21.33507,
          15.25069,
          44.36819,
          31.72369,
          42.76351,
          79.29563,
          42.22551,
          30.10278,
          107.62136,
          29.63233,
          94.09194,
          78.55832,
          39.52508,
          81.18077,
          67.1012,
          31.00737
        ],
        'Esophagus - Mucosa': [
          76.0462,
          21.75358,
          69.68496,
          15.62296,
          157.5873,
          101.74271,
          34.62914
        ],
        'Esophagus - Muscularis': [
          74.92367,
          57.24415,
          54.10831,
          63.61676,
          32.24148,
          30.68184,
          36.25497,
          94.47894,
          155.29949,
          35.50756,
          37.8531,
          189.38434,
          100.85841,
          41.34566
        ],
        'Heart - Atrial Appendage': [
          126.8177,
          76.21091,
          96.82586,
          49.93083,
          102.49172,
          66.89699,
          219.61994,
          82.34048,
          84.02994,
          163.67002,
          45.4005,
          96.95148,
          55.19511,
          88.58321,
          29.25567,
          283.15742
        ],
        'Heart - Left Ventricle': [
          84.21877,
          49.07347,
          37.544,
          75.83501,
          107.88151,
          108.19537,
          71.95788,
          95.71748,
          80.05983,
          44.58182,
          80000,
          28.8389,
          56.66764,
          21.62697
        ],
        'Liver': [
          580.1796,
          67.41767,
          199.78547,
          287.12654,
          341.76885,
          184.03464,
          144.74543,
          193.21765,
          87.18192,
          157.0904,
          104.62034
        ],
        'Lung': [
          54.81366,
          140.00786,
          31.74241,
          59.94086,
          27.08464,
          800.19155,
          157.98849,
          93.67993,
          75.85205,
          73.32424,
          46.96725,
          39.83799,
          129.55007
        ],
        'Minor Salivary Gland': [
          98.89543,
          240.73981
        ],
        'Muscle - Skeletal': [
          103.76152,
          16.4344,
          25.03311,
          46.90967,
          44.00816,
          26.161,
          205,
          20.74924,
          28.43742,
          22.5907,
          64.56254,
          120.1487,
          16.09462
        ],
        'Nerve - Tibial': [
          55.21793,
          85.29238,
          24.77444,
          21.37921,
          323.34778,
          80.02056,
          60.11747,
          231.81477,
          70.38488,
          77.09792,
          77.06667
        ],
        'Ovary': [
          74.49914,
          34.8821,
          167.82171,
          205.00243,
          94.78023,
          790.66706,
          35.74211
        ],
        'Pancreas': [
          90.12614,
          111.2208,
          92.07688,
          358.78145,
          161.94783,
          203.07046,
          112.14887,
          72.01051,
          115.11109,
          255.11733,
          26.38793,
          167.09309,
          65.74192,
          32.20487,
          93.16598
        ],
        'Pituitary': [
          99.72663,
          270.41966
        ],
        'Prostate': [
          70.50711,
          126.95947,
          254.81415,
          59.84736
        ],
        'Skin - Not Sun Exposed (Suprapubic)': [
          72.01368,
          32.69884,
          126.21397,
          78.06589,
          48.59712,
          115.80699,
          72.28962,
          58.98783,
          35.64524,
          34.8715
        ],
        'Skin - Sun Exposed (Lower leg)': [
          16.66929,
          26.08493,
          63.26239,
          16.85778,
          109.13565,
          44.57548,
          3484.33949,
          181.89119,
          106.80925,
          83.07148,
          70.62263,
          249,
          671
        ],
        'Small Intestine - Terminal Ileum': [
          179.55121,
          103.90259,
          410.96228,
          575.50446
        ],
        'Spleen': [
          208.56651,
          99.81169,
          168.81614,
          147.81207,
          70.44842,
          263.87453,
          237.05754,
          187.19294,
          223.02211,
          205.25963,
          208.56447,
          40.66186
        ],
        'Stomach': [
          215.84834,
          105.12663,
          33.51726,
          62.12088,
          367.01425,
          334.62732,
          114.52272,
          60.45282,
          295.212,
          166.13674,
          950.47601,
          152.55294,
          271.4386,
          934.66935,
          90.27063,
          72.6417,
          255.3514,
          22.73131
        ],
        'Testis': [
          285.37132,
          190.01587,
          314.95672,
          439.2026
        ],
        'Thyroid': [
          725.98532,
          941.13266,
          480.73232,
          414.03492,
          1231.1907,
          911.24359,
          1122.22943,
          206.09805,
          478.19599,
          801.92301,
          300.38827,
          1242.98557,
          945.81351,
          908.2334,
          1191.43104,
          507.30442,
          417.99232,
          22170.47778,
          499.3524,
          1193.85144,
          82.58056,
          539.65815
        ],
        'Uterus': [
          55.26498,
          26.18659,
          24.36885,
          151.63369,
          178.80237,
          85.2754,
          42.46289,
          41.41678,
          927,
          137.22961,
          106.03802
        ],
        'Vagina': [
          88.65073,
          107.1278,
          76.76795,
          111.56774,
          30.87008,
          44.60423,
          42.28049,
          119.63441,
          54.50949,
          604.02578,
          39.00244
        ],
        'reference': [
          109.88995,
          168.3281,
          51.86523,
          55.91558,
          157.99782,
          184.41961,
          48.52536,
          67.68566,
          132.53056,
          116.85689,
          232.8612,
          257.43684,
          24.60312,
          36.74598,
          184.6633,
          206.97531,
          44.07054,
          37.66876,
          109.93774,
          100.13888,
          127.64488,
          137.88733,
          189.33875,
          190.7854,
          131.14628,
          142.33882,
          52.86114,
          54.45511,
          158.49193,
          169.02257,
          210.0548,
          229.37815,
          147.93327,
          154.48553,
          245.25411,
          248.1715,
          148.84041,
          142.62392,
          89.19086,
          78.37482,
          108.60471,
          85.84124,
          41.10184,
          44.53946,
          524.77751,
          596.35466,
          136.5804,
          96.60782,
          116.56729,
          159.53274,
          85.57025,
          119.58125,
          139.19562,
          131.26481,
          180.45259,
          234.10941,
          180.58128,
          333.20863,
          96.25381,
          77.26984,
          124.10719,
          127.77826,
          77.24604,
          83.85016,
          333.17356,
          308.67321,
          268.30004,
          288.4791,
          139.28252,
          133.4016,
          285.81116,
          343.08712,
          116.86853,
          2046.9915,
          733.871,
          798.48239,
          40.7853,
          96.82853,
          132.18641,
          179.91579,
          4493.837,
          101.21345,
          1700,
          59.21642,
          91.3653,
          91.56865,
          122.90874,
          129.04458,
          57.30177,
          65.58347,
          75.37465,
          47.92698
        ]
      }]
      // eslint-disable-next-line camelcase
      function get_columns () {
        return ['Adrenal Gland', 'Artery - Aorta', 'Artery - Coronary', 'Artery - Tibial',
          'Brain - Cerebellum', 'Brain - Cortex', 'Breast - Mammary Tissue',
          'Colon - Sigmoid', 'Colon - Transverse', 'Esophagus - Gastroesophageal Junction',
          'Esophagus - Mucosa', 'Esophagus - Muscularis', 'Heart - Atrial Appendage',
          'Heart - Left Ventricle', 'Liver', 'Lung', 'Minor Salivary Gland',
          'Muscle - Skeletal', 'Nerve - Tibial', 'Ovary', 'Pancreas', 'Pituitary',
          'Prostate', 'Skin - Not Sun Exposed (Suprapubic)', 'Skin - Sun Exposed (Lower leg)',
          'Small Intestine - Terminal Ileum', 'Spleen', 'Stomach', 'Testis', 'Thyroid',
          'Uterus', 'Vagina', 'reference']
      }

      function l2 (x) {
        x = parseFloat(x)
        if (x !== 0) {
          return Math.log2(x + 1)
        } else {
          return 0
        }
      }

      function r2 (x) {
        return x.toFixed(2)
      }
      // eslint-disable-next-line camelcase
      function data_handling () {
        // const transcripts = res.data
        // console.log(transcripts)
        // eslint-disable-next-line camelcase
        const express_list = []
        for (let i = 0; i < data.length; i++) {
          const protein = data[i]
          console.log(protein)
          for (const item in protein) {
            // eslint-disable-next-line camelcase
            const item_item = protein[item]
            let sum = 0
            for (let j = 0; j < item_item.length; j++) {
              sum += item_item[j]
            }
            protein[item] = sum / item_item.length
          }
          express_list.push(protein)
        }
        // eslint-disable-next-line camelcase
        let express_average = []
        if (express_list.length >= 1) {
          // eslint-disable-next-line camelcase
          if (brain_express === 0) {
            // eslint-disable-next-line camelcase
            for (const item_trans of express_list) {
              // eslint-disable-next-line camelcase
              const list_avg = []
              // eslint-disable-next-line camelcase
              for (const item_colunms of get_columns()) {
                if (item_trans[item_colunms] !== undefined) {
                  list_avg.push(r2(l2(item_trans[item_colunms])))
                } else {
                  list_avg.push(undefined)
                }
              }
              express_average.push(list_avg)
            }
          } else {
            // eslint-disable-next-line camelcase
            for (const item_trans of express_list) {
              // eslint-disable-next-line camelcase
              const list_avg = []
              // eslint-disable-next-line camelcase
              for (const item_colunms of get_columns()) {
                if (item_trans[item_colunms] !== undefined) {
                  list_avg.push(r2(l2(item_trans['item_colunms'])))
                } else {
                  list_avg.push(undefined)
                }
              }
              // eslint-disable-next-line camelcase
              let temp_flag = 0
              for (let i = 8; i < 21; i++) {
                // eslint-disable-next-line camelcase
                const item_list_avg = list_avg[i]
                // eslint-disable-next-line camelcase
                if (item_list_avg >= 1) {
                  // eslint-disable-next-line camelcase
                  temp_flag = 1
                  break
                }
              }
              // eslint-disable-next-line camelcase
              if (temp_flag === 1) {
                express_average.push(list_avg)
              }
            }
          }
        } else {
          // eslint-disable-next-line camelcase
          express_average = []
        }
        // eslint-disable-next-line camelcase
        return express_average
      }

      // eslint-disable-next-line camelcase
      const express_average = data_handling()
      const trace = []
      // eslint-disable-next-line camelcase
      if (express_average !== undefined) {
        // eslint-disable-next-line camelcase
        const x_columns = get_columns()
        // eslint-disable-next-line camelcase
        for (const item of express_average) {
          const name = item.shift()
          trace.push({
            x: x_columns,
            y: item,
            hoverinfo: 'all',
            name: name,
            ycalendar: 180,
            hoverlabel: {
              namelength: -1
            }
          })
        }
        const layout = {
          width: 1200,
          height: 400,
          hovermode: 'closest',
          xaxis: {
            showgrid: true,
            zeroline: true,
            showline: true,
            showticklabels: true,
            tickangle: 270,
            titlefont: {
              family: 'Arial',
              color: 'black'
            }
          },
          yaxis: {
            autorange: true,
            showticklabels: false,
            titlefont: {
              family: 'Arial',
              size: 16,
              color: 'lightgrey'
            },
            exponentformat: 'e',
            showexponent: 'All'
          },
          margin: {
            l: 50,
            r: 100,
            t: 10,
            b: 250,
            pad: 0
          },
          showlegend: false
        }
        this.data = trace
        this.layout = layout
        this.isPlot = true
        this.loading = false
      } else {
        this.isPlot = false
      }
    }
  },
  // mounted() {
  //   this.variant_key = this.$route.query.variant
  //   if (this.variant_key) {
  //     this.GtexTranscriptExpressPlot(this.variant_key)
  //   }
  //   this.GtexTranscriptExpressPlot()
  // },
  created () {
    this.GtexTranscriptExpressPlot()
  }
}
</script>
<style scoped>
</style>
