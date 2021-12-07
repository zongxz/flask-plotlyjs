<!--<template>-->
<!--  <div class="hello">-->
<!--    <div id="container"></div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import Highcharts from 'highcharts'-->
<!--import exportingInit from 'highcharts/modules/exporting'-->
<!--import HighchartsMore from 'highcharts/highcharts-more'-->
<!--import HighchartsLollipop from 'highcharts/modules/lollipop'-->
<!--import HighchartsGantt from 'highcharts/modules/gantt'-->

<!--exportingInit(Highcharts)-->
<!--HighchartsMore(Highcharts)-->
<!--HighchartsLollipop(Highcharts)-->
<!--HighchartsGantt(Highcharts)-->

<!--export default {-->
<!--  name: 'HelloWorld',-->
<!--  props: {-->
<!--    msg: String-->
<!--  },-->
<!--  mounted() {-->
<!--    this.moreChart();-->
<!--  },-->
<!--  data () {-->
<!--    return {-->
<!--      chartOptions: {-->
<!--        title: {-->
<!--          text: 'test'-->
<!--        },-->
<!--        legend: {-->
<!--          enabled: false-->
<!--        },-->
<!--        yAxis: {-->
<!--          title: {-->
<!--            text: ''-->
<!--          },-->
<!--          categories: ['transcript1', 'transcript2', 'transcript3', 'DNMs']-->
<!--        },-->
<!--        series: [-->
<!--          {-->
<!--            name: 'Mutation',-->
<!--            data: [{-->
<!--              x: 2,-->
<!--              y: 3,-->
<!--              color: 'red'-->
<!--            }, {-->
<!--              x: 4,-->
<!--              y: 3-->
<!--            }],-->
<!--            type: 'lollipop'-->
<!--          },-->
<!--          {-->
<!--            type: 'xrange',-->
<!--            name: 'Mutation',-->
<!--            // pointPadding: 0,-->
<!--            // groupPadding: 0,-->
<!--            borderColor: 'gray',-->
<!--            pointWidth: 20,-->
<!--            data: [{-->
<!--              x: 1,-->
<!--              x2: 3,-->
<!--              y: 0-->
<!--              // partialFill: 0.25-->
<!--            }, {-->
<!--              x: 3,-->
<!--              x2: 5,-->
<!--              y: 1-->
<!--            }, {-->
<!--              x: 5,-->
<!--              x2: 8,-->
<!--              y: 2-->
<!--            }],-->
<!--            dataLabels: {-->
<!--              enabled: true-->
<!--            }-->
<!--          }-->
<!--        ]-->
<!--      }-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    myCallback () {-->
<!--      console.log('this is callback function')-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--.highcharts-container {-->
<!--  width: 600px;-->
<!--  height: 400px;-->
<!--  border: 1px solid #ddd;-->
<!--  margin: auto;-->
<!--}-->
<!--</style>-->
