<template>
  <div>
<!--    <el-radio-group v-model="radioButton1" size="medium" >-->
<!--            <el-radio-button :label=[0,0] >1</el-radio-button>-->
<!--        </el-radio-group>-->
<!--    <el-radio-group v-model="radioButton1" size="medium" >-->
<!--            <el-radio-button :label=[1,0]>2</el-radio-button>-->
<!--        </el-radio-group>-->
<!--    <el-radio-group v-model="radioButton1" size="medium" >-->
<!--            <el-radio-button :label=[0,1]>2</el-radio-button>-->
<!--        </el-radio-group>-->
<!--    <el-radio-group v-model="radioButton1" size="medium" >-->
<!--            <el-radio-button :label=[1,1]>2</el-radio-button>-->
<!--        </el-radio-group>-->
<!--    <div-->
<!--      v-if="radioButton1[0] === 0">-->
<!--      <plotlyButton/>-->
<!--    </div>-->
<!--    <div-->
<!--      v-else-if="radioButton1[0] === 1"-->
<!--    >-->
<!--      <TransOneDNM/>-->
<!--    </div>-->
<!--    <div-->
<!--      v-if="radioButton1[1] === 0">-->
<!--      <gtex/>-->
<!--    </div>-->
<!--    <div-->
<!--      v-else-if="radioButton1[1] === 1"-->
<!--    >-->
<!--      <GtexTransExp/>-->
<!--    </div>-->
<!--    <div>-->
<!--      <GtexTranBrain/>-->
<!--    </div>-->
    <div>
      <ProteinIsoformBrainExpress/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import Mouse from '../components/Mouse'
// import BrainSeq from '../components/Brainseq'
import DNMs from '../components/DNMs'
import DNMsOnRe from '../components/DNMsOnRe'
import DNMsOnRe2 from '../components/DNMsOnRe2'
import GeneSpan from '../components/GeneSpan'
import PPI from '../components/PPI'
import MiPPIs from '../components/MiPPIs'
import PPItest from '../components/PPItest'
import DNMsOnReHiChart from '../components/DNMsOnReHiChart'
import GtexTransExp from '../components/GtexTransExp'
import Gtex from '../components/Gtex'
import ProteinExpress from '../components/ProteinExpress'
import BrainSpan from '../components/BrainSpan'
import plotlyButton from '../components/plotlyButton'
import TransOneDNM from '../components/TransOneDNM'
import GtexTranBrain from '../components/GtexTranscriptsBrainExpression'
import ProteinIsoformBrainExpress from '../components/ProteinIsoformBrainExpress'
export default {
  name: 'home',
  components: {
    DNMs,
    DNMsOnRe,
    DNMsOnRe2,
    GeneSpan,
    PPI,
    PPItest,
    MiPPIs,
    DNMsOnReHiChart,
    GtexTransExp,
    Gtex,
    ProteinExpress,
    BrainSpan,
    plotlyButton,
    TransOneDNM,
    GtexTranBrain,
    ProteinIsoformBrainExpress
  },
  data () {
    return {
      radioButton1: [0, 0],
      radioButton2: 1
    }
  }
}
</script>
