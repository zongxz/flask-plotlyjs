<template>
  <div class="home">
    <Chart />
    <DNMsOnRe/>
  </div>
</template>

<script>
// @ is an alias to /src
import Chart from '../components/Bar'
// import Mouse from '../components/Mouse'
// import BrainSeq from '../components/Brainseq'
import DNMsOnRe from '../components/DNMsOnRe'

export default {
  name: 'home',
  components: {
    Chart,
    DNMsOnRe
  }
}
</script>
