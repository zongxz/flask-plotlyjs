<template>
  <Plot
    :data="data"
    :layout="layout"
  />
</template>

<script>
import Plot from 'vue-plotly.js'

export default {
  name: 'Gtex',
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
    Gtex () {
      const a = {
        'Adrenal Gland': [
          114.58654,
          278.52088,
          148.34427,
          133.52483,
          36.80021,
          89.21836,
          293.13747,
          764.61881,
          31.97578,
          31.03212,
          181.96304,
          60.68899,
          281.79317
        ],
        'Artery - Aorta': [
          84.99587,
          17.22951,
          314.01989,
          268.34722,
          114.28075,
          238.34316,
          115.01715,
          62.33505,
          50.73783,
          160.32454,
          229.94421,
          175.5743,
          26.21188,
          84.83195
        ],
        'Artery - Coronary': [
          114.74086,
          59.32642,
          26.38263
        ],
        'Artery - Tibial': [
          21.27621,
          25.99324,
          21.88767,
          19.48638,
          80.11068,
          72.13837
        ],
        'Brain - Cerebellum': [
          265.40297,
          677.13222,
          304.25457,
          1572.679,
          811.20379
        ],
        'Brain - Cortex': [
          1694.20034,
          1096.75295,
          1539.56355,
          2080.67547
        ],
        'Breast - Mammary Tissue': [
          519.08459,
          456.16717,
          58.49651,
          184.1355,
          295.42103,
          169.08207,
          68.15162,
          850.80706,
          878.64661,
          342.54526,
          579.88231,
          66.4026
        ],
        'Colon - Sigmoid': [
          23.83563,
          122.1519,
          32.09018,
          163.1959,
          40.50338,
          34.02199,
          33.89798,
          151.32018,
          48.34296,
          56.06421,
          152.86924,
          17.09903,
          25.30852,
          223.32061,
          116.80513,
          38.80085
        ],
        'Colon - Transverse': [
          151.90584,
          56.55815,
          294.38938,
          756.1504,
          288.54725,
          18.59814
        ],
        'Esophagus - Gastroesophageal Junction': [
          147.36085,
          107.89291,
          138.51954,
          75.73338,
          38.27307,
          78.60216,
          18.87221,
          125.14086,
          26.47497,
          17.72566,
          384.28872,
          58.38309,
          163.53617,
          209.006,
          16.96727,
          17.61085,
          54.7919,
          91.30876
        ],
        'Esophagus - Mucosa': [
          131.27023,
          22.07038,
          33.55231,
          96.83646,
          244.17998,
          213.13004
        ],
        'Esophagus - Muscularis': [
          200.80026,
          163.68427,
          168.78563,
          21.5066,
          137.98043,
          604.18228,
          348.16025,
          362.1969,
          282.47576,
          342.54602,
          23.29077,
          210.5861,
          288.62728,
          320.69407,
          213.85099,
          17.532
        ],
        'Heart - Atrial Appendage': [
          147.97744,
          137.09791,
          222.5685,
          149.90199,
          30.1047,
          35.4675,
          72.94915,
          400.0351,
          75.06546,
          416.84938,
          512.0,
          25.4,
          233.0,
          274.40749,
          60.6119,
          301.44111,
          138.30741
        ],
        'Heart - Left Ventricle': [
          17.22657,
          115.84924,
          266.83878,
          17.56997,
          207.0,
          43.5,
          321.0,
          304.0,
          242.0,
          93.32972
        ],
        'Liver': [
          56.44765,
          22.15522,
          51.84619,
          36.40922,
          24.78947,
          658.53754,
          53.82569
        ],
        'Lung': [
          275.58303,
          478.14367,
          413.68189,
          298.88864,
          514.32546,
          241.51129,
          210.68395,
          1684.42613,
          140.64145,
          105.94158,
          124.31192,
          781.34339,
          814.85116,
          51.87227,
          312.45769,
          178.116
        ],
        'Minor Salivary Gland': [
          268.84508,
          364.35464
        ],
        'Muscle - Skeletal': [
          40.0,
          58.6,
          57.6,
          73.2,
          46.47277,
          168.4867,
          126.0,
          3490.0,
          51.5,
          59.1,
          79.0,
          72.6,
          541.01834,
          46.82024
        ],
        'Nerve - Tibial': [
          81.62068,
          97.85326,
          34.59879,
          28.7443,
          21.7604,
          24.48118,
          116.72327,
          18.63762,
          236.81938,
          493.54491,
          114.77098
        ],
        'Ovary': [
          125.51139,
          117.21191,
          84.1042,
          50.88502,
          102.82277,
          17.25181
        ],
        'Pancreas': [
          140.64205,
          111.6105,
          137.89219,
          33.03363,
          61.22517,
          28.55717,
          19.40403,
          74.03679,
          55.50141,
          23.47129,
          29.86454,
          76.27166,
          71.20145,
          36.50188
        ],
        'Pituitary': [
          84.0237,
          246.11514,
          281.23855
        ],
        'Prostate': [
          126.39294,
          21.94,
          17.78012
        ],
        'Skin - Not Sun Exposed (Suprapubic)': [
          135.44602,
          89.10097,
          172.88192,
          56.9203,
          54.74198,
          91.7349,
          83.45707,
          189.56321,
          1015.53353,
          646.776,
          252.67005,
          31.16665,
          207.56994,
          856.11804,
          89.57013
        ],
        'Skin - Sun Exposed (Lower leg)': [
          38.24132,
          66.66148,
          148.95501,
          34.66381,
          125.77111,
          161.60471,
          1040.86647,
          20.99406,
          49.99492,
          452.69575,
          361.21007,
          102.42512,
          146.80078
        ],
        'Small Intestine - Terminal Ileum': [
          21.24973,
          53.97849,
          763.44768,
          2144.54541
        ],
        'Spleen': [
          1038.53623,
          823.83574,
          783.6438,
          710.11585,
          446.14617,
          437.12302,
          109.2393,
          265.26588,
          610.13063,
          225.8854,
          920.50282,
          957.52103,
          3818.80678,
          1593.90573,
          3893.04998,
          2435.49824,
          698.9289
        ],
        'Stomach': [
          35.02608,
          69.04371,
          32.62236,
          47.39522,
          99.88894,
          44.42524,
          57.54807,
          20.19764,
          72.53129,
          354.65007,
          323.77518,
          725.72145,
          77.3701,
          29.24596,
          172.37308,
          236.8075,
          78.88763,
          330.39116,
          77.12107,
          22.68643
        ],
        'Testis': [
          48.46914,
          51.54945
        ],
        'Thyroid': [
          113.12901,
          290.74565,
          358.71704,
          174.53577,
          1247.34809,
          97.67636,
          221.66873,
          828.73855,
          118.91441,
          1105.77328,
          1250.0,
          635.32448,
          101.87724,
          464.4294,
          460.27743,
          147.0,
          460.0,
          521.0
        ],
        'Uterus': [
          157.80062,
          75.35115,
          146.89272,
          50.82084,
          256.31536,
          132.13071,
          728.47781,
          447.78406,
          87.96431,
          295.11256,
          340.15777,
          839.7562,
          245.73638
        ],
        'Vagina': [
          173.96036,
          281.27346,
          96.52592,
          118.83638,
          42.23199,
          427.25979,
          32.64784,
          69.83016,
          467.74973,
          15.07663,
          486.44012,
          77.91628
        ],
        'ensembl_id': 'ENSG00000251322.3',
        'reference': [
          189.81301,
          209.78546,
          63.11948,
          72.7232,
          244.13379,
          264.96945,
          187.94687,
          215.15416,
          293.81008,
          330.0447,
          51.71677,
          58.85332,
          315.29362,
          296.82276,
          158.67407,
          179.00115,
          335.49966,
          343.31899,
          230.22385,
          247.76008,
          92.95246,
          94.665,
          39.27636,
          42.16651,
          68.02322,
          105.36793,
          49.26891,
          41.99698,
          110.14019,
          108.98025,
          184.99506,
          198.24085,
          121.76226,
          134.52555,
          152.08471,
          145.5957,
          42.33818,
          36.52202,
          79.35844,
          108.47622,
          71.87202,
          69.67601,
          709.63514,
          757.06481,
          107.64267,
          108.57515,
          68.27655,
          69.34895,
          42.63504,
          37.95913,
          445.79821,
          440.74418,
          996.18468,
          1101.02721,
          57.98109,
          75.71064,
          384.73398,
          432.48803,
          1118.8343,
          1215.45238,
          430.04679,
          453.33443,
          106.79394,
          103.13668,
          33.59223,
          38.29485,
          40.83431,
          42.64642,
          30.37259,
          34.41774,
          363.35563,
          389.8112,
          309.46533,
          346.77922,
          413.81401,
          495.087,
          749.11493,
          794.42612,
          434.2381,
          442.32831,
          116.54872,
          115.74955,
          107.39486,
          115.3613,
          431.17163,
          416.891,
          482.21522,
          473.03457,
          176.32048,
          224.76938,
          219.33112,
          228.59995,
          40.58629,
          35.51199
        ]
      }

      // eslint-disable-next-line camelcase
      function get_col_color_dict (col_list) {
        // eslint-disable-next-line camelcase
        const colors_list = ['rgb(255,255,0)', 'rgb(31,119,180)', 'rgb(215,42,43)', 'rgb(140,140,140)', 'rgb(44,160,44)',
          'rgb(0,0,0)', 'rgb(188,188,34)', 'rgb(144,238,144)', 'rgb(140,86,75)', 'rgb(255,127,14)',
          'rgb(188,189,34)', 'rgb(255,193,193)', 'rgb(238,16,118)', 'rgb(0,245,255)', 'rgb(139,0,0)',
          'rgb(122,197,205)', 'rgb(255,218,185)', 'rgb(84,255,159)', 'rgb(154,205,50)', 'rgb(238,180,34)',
          'rgb(139,115,85)', 'rgb(153,50,204)', 'rgb(205,197,191)', 'rgb(131,139,131)', 'rgb(255,222,173)',
          'rgb(0, 0,139 )', 'rgb(155, 48, 255)', 'rgb(79, 48, 205)', 'rgb(139, 102, 139)',
          'rgb(139, 34, 82)', 'rgb(131, 139, 131)', 'rgb(139,99 ,108 )', 'rgb(205, 0, 0)',
          'rgb(238, 207, 161)', 'rgb(139, 134, 130)', 'rgb(139, 90, 0)', 'rgb(16, 78, 139)',
          'rgb(139, 76, 57)', 'rgb(238, 44, 44)', 'rgb(255, 20, 147)', 'rgb(255, 99, 71)',
          'rgb(255, 140, 0)', 'rgb(210, 105, 30)', 'rgb(139, 105, 105)', 'rgb(34, 139, 34)',
          'rgb(124, 252, 0)', 'rgb(205, 190, 112)', 'rgb(162, 205, 90)', 'rgb(0, 139, 69)',
          'rgb(100, 149, 237)', 'rgb(47, 79, 79)', 'rgb(255, 218, 185)', 'rgb(0, 134, 139)',
          'rgb(155, 205, 155)', 'rgb(205, 255, 112)', 'rgb(102, 205, 170)']
        // eslint-disable-next-line camelcase
        const col_color_dict = {}
        const l = []
        for (let i = 0; i < col_list.length; i++) {
          l.push(col_list[i].split('-')[0])
        }
        const set = new Set(l)
        // eslint-disable-next-line camelcase
        const col_prex = [...set].sort()
        for (let i = 0; i < col_prex.length; i++) {
          var key = col_prex[i]
          col_color_dict[key] = colors_list[i]
        }
        // eslint-disable-next-line camelcase
        return col_color_dict
      }

      function normalized (alist) {
        var l = []
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
      function get_x_col (alist) {
        var l = []
        for (let i = 0; i < alist.length; i++) {
          if (!['gencode_id', 'gene_symbol'].includes(alist[i])) {
            l.push(alist[i])
          }
        }
        return l.sort()
      }
      const data = a
      const tarces = []
      if (data !== undefined) {
        // eslint-disable-next-line camelcase
        const x_col = get_x_col(Object.keys(data))
        // eslint-disable-next-line camelcase
        const col_color_dict = get_col_color_dict(x_col)
        // eslint-disable-next-line camelcase
        const y_data = []
        // eslint-disable-next-line camelcase
        const color_data = []
        // eslint-disable-next-line camelcase
        const y_normalized_data = []
        for (let i = 0; i < x_col.length; i++) {
          const item = x_col[i]
          y_data.push(data[item])
          const key = item.split('-')[0]
          color_data.push(col_color_dict[key])
          y_normalized_data.push(normalized(data[item]))
        }
        for (let i = 0; i < x_col.length; i++) {
          tarces.push({
            y: y_data[i],
            name: x_col[i],
            boxpoints: 'outliers',
            marker: {
              color: color_data[i]
            },
            line: {
              width: 1
            },
            type: 'box'
          })
        }
        for (let i = 0; i < x_col.length; i++) {
          tarces.push({
            y: y_normalized_data[i],
            name: x_col[i],
            boxpoints: 'outliers',
            visible: false,
            marker: {
              color: color_data[i]
            },
            line: {
              width: 1
            },
            type: 'box'
          })
        }
        console.log(tarces)
        // eslint-disable-next-line camelcase
        const visible_list_original = []
        // eslint-disable-next-line camelcase
        const visible_list_normalized = []
        for (let i = 0; i < x_col.length; i++) {
          visible_list_original.push(true)
          visible_list_normalized.push(false)
        }
        for (let i = 0; i < x_col.length; i++) {
          visible_list_original.push(false)
          visible_list_normalized.push(true)
        }
        console.log(visible_list_normalized)
        console.log(visible_list_original)
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
            args: [{ 'visible': visible_list_original },
              {
                'title': 'TPM without normalization'
              }]
          },
          {
            label: 'log<sub>2</sub> ( TPM + 1 )',
            method: 'update',
            args: [{ 'visible': visible_list_normalized },
              {
                'title': 'Normalized TPM'
              }]
          }]
        }]
        const layout = {
          updatemenus: updatemenus,
          paper_bgcolor: 'rgb(249, 249, 249)',
          plot_bgcolor: 'rgb(249, 249, 249)',
          height: 500,
          width: 1200,
          hovermode: 'closest',
          xaxis: {
            showgrid: true,
            zeroline: false,
            showline: false,
            showticklabels: true,
            tickangle: 70,
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
          margin: {
            l: 20,
            r: 20,
            b: 230,
            t: 60
          },
          showlegend: false
        }
        this.data = tarces
        this.layout = layout
        this.isPlot = true
      } else {
        this.isPlot = false
      }
    }
  },
  mounted () {
    this.Gtex()
  }
}
</script>

<style scoped>

</style>
