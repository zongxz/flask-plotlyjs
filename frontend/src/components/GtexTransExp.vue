<template>
  <Plot
    :data="data"
    :layout="layout"
  />
</template>

<script>
import Plot from 'vue-plotly.js'
export default {
  name: 'GtexTransExp',
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
    GtexTranscriptExpressPlot () {
      let a = [{
        'Adipose - Subcutaneous': 4.524886877828054e-05,
        'Adipose - Visceral (Omentum)': 5.633802816901409e-05,
        'Adrenal Gland': 0.0001052631578947368,
        'Artery - Aorta': 0,
        'Artery - Coronary': 0,
        'Artery - Tibial': 9.070294784580499e-05,
        'Bladder': 0,
        'Brain - Amygdala': 0,
        'Brain - Anterior cingulate cortex (BA24)': 0,
        'Brain - Caudate (basal ganglia)': 0,
        'Brain - Cerebellar Hemisphere': 0,
        'Brain - Cerebellum': 0.0003468208092485549,
        'Brain - Cortex': 0,
        'Brain - Frontal Cortex (BA9)': 0,
        'Brain - Hippocampus': 0,
        'Brain - Hypothalamus': 0,
        'Brain - Nucleus accumbens (basal ganglia)': 0,
        'Brain - Putamen (basal ganglia)': 0,
        'Brain - Spinal cord (cervical c-1)': 0,
        'Brain - Substantia nigra': 0,
        'Breast - Mammary Tissue': 0.000103448275862069,
        'Cells - EBV-transformed lymphocytes': 0,
        'Cells - Transformed fibroblasts': 0,
        'Cervix - Ectocervix': 0,
        'Cervix - Endocervix': 0,
        'Colon - Sigmoid': 8.583690987124464e-05,
        'Colon - Transverse': 7.299270072992701e-05,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 8.19672131147541e-05,
        'Esophagus - Mucosa': 0,
        'Esophagus - Muscularis': 8.108108108108108e-05,
        'Fallopian Tube': 0,
        'Heart - Atrial Appendage': 6.734006734006734e-05,
        'Heart - Left Ventricle': 3.3003300330033e-05,
        'Kidney - Cortex': 0,
        'Liver': 0,
        'Lung': 7.02576112412178e-05,
        'Minor Salivary Gland': 0,
        'Muscle - Skeletal': 3.546099290780142e-05,
        'Nerve - Tibial': 0.001666666666666667,
        'Ovary': 0.0003759398496240602,
        'Pancreas': 0,
        'Pituitary': 0,
        'Prostate': 0,
        'Skin - Not Sun Exposed (Suprapubic)': 0.0001291989664082688,
        'Skin - Sun Exposed (Lower leg)': 0.0007188160676532769,
        'Small Intestine - Terminal Ileum': 0.000145985401459854,
        'Spleen': 0.0001234567901234568,
        'Stomach': 0,
        'Testis': 7.722007722007723e-05,
        'Thyroid': 6.72645739910314e-05,
        'Uterus': 0,
        'Vagina': 0,
        'Whole Blood': 2.457002457002457e-05,
        '_id': '5b9f7faa7a55821abccf4e4b',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000321219.8'
      },
      {
        'Adipose - Subcutaneous': 18.13162895927602,
        'Adipose - Visceral (Omentum)': 14.72428169014085,
        'Adrenal Gland': 13.4528947368421,
        'Artery - Aorta': 17.49083612040134,
        'Artery - Coronary': 16.96872832369942,
        'Artery - Tibial': 22.65986394557823,
        'Bladder': 22.28181818181818,
        'Brain - Amygdala': 9.521199999999999,
        'Brain - Anterior cingulate cortex (BA24)': 12.25421487603306,
        'Brain - Caudate (basal ganglia)': 9.882999999999997,
        'Brain - Cerebellar Hemisphere': 23.13352941176471,
        'Brain - Cerebellum': 19.26346820809249,
        'Brain - Cortex': 13.24968354430379,
        'Brain - Frontal Cortex (BA9)': 16.74457364341085,
        'Brain - Hippocampus': 9.92382113821138,
        'Brain - Hypothalamus': 11.70471074380166,
        'Brain - Nucleus accumbens (basal ganglia)': 11.67387755102041,
        'Brain - Putamen (basal ganglia)': 8.081612903225812,
        'Brain - Spinal cord (cervical c-1)': 9.23021978021978,
        'Brain - Substantia nigra': 8.52534090909091,
        'Breast - Mammary Tissue': 18.26896551724139,
        'Cells - EBV-transformed lymphocytes': 16.42946153846154,
        'Cells - Transformed fibroblasts': 13.22985422740524,
        'Cervix - Ectocervix': 21.47,
        'Cervix - Endocervix': 22.998,
        'Colon - Sigmoid': 17.49309012875538,
        'Colon - Transverse': 14.02142335766423,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 18.21073770491803,
        'Esophagus - Mucosa': 12.07545454545455,
        'Esophagus - Muscularis': 19.20516216216215,
        'Fallopian Tube': 21.61142857142857,
        'Heart - Atrial Appendage': 11.28609427609428,
        'Heart - Left Ventricle': 8.47580858085809,
        'Kidney - Cortex': 10.36755555555556,
        'Liver': 5.164685714285715,
        'Lung': 20.05074941451991,
        'Minor Salivary Gland': 14.34144329896907,
        'Muscle - Skeletal': 17.85195035460995,
        'Nerve - Tibial': 19.24195652173915,
        'Ovary': 20.11947368421053,
        'Pancreas': 4.278387096774195,
        'Pituitary': 18.53775956284154,
        'Prostate': 16.39348684210527,
        'Skin - Not Sun Exposed (Suprapubic)': 17.43341085271319,
        'Skin - Sun Exposed (Lower leg)': 17.88818181818183,
        'Small Intestine - Terminal Ileum': 15.91875912408758,
        'Spleen': 20.59777777777779,
        'Stomach': 9.797442748091605,
        'Testis': 20.66069498069498,
        'Thyroid': 23.46224215246635,
        'Uterus': 25.36081081081081,
        'Vagina': 18.10808695652173,
        'Whole Blood': 4.192825552825553,
        '_id': '5b9f7faa7a55821abccf4e4c',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000338785.3'
      },
      {
        'Adipose - Subcutaneous': 0.3365837104072398,
        'Adipose - Visceral (Omentum)': 0.3679154929577466,
        'Adrenal Gland': 0.5085789473684214,
        'Artery - Aorta': 0.4540133779264214,
        'Artery - Coronary': 0.4406936416184967,
        'Artery - Tibial': 0.4364172335600905,
        'Bladder': 0.5045454545454544,
        'Brain - Amygdala': 0.3856999999999999,
        'Brain - Anterior cingulate cortex (BA24)': 0.3553719008264462,
        'Brain - Caudate (basal ganglia)': 0.3661874999999999,
        'Brain - Cerebellar Hemisphere': 1.042058823529411,
        'Brain - Cerebellum': 1.085838150289018,
        'Brain - Cortex': 0.4152531645569619,
        'Brain - Frontal Cortex (BA9)': 0.4070542635658914,
        'Brain - Hippocampus': 0.3856910569105692,
        'Brain - Hypothalamus': 0.3130578512396692,
        'Brain - Nucleus accumbens (basal ganglia)': 0.4032653061224489,
        'Brain - Putamen (basal ganglia)': 0.3667741935483871,
        'Brain - Spinal cord (cervical c-1)': 0.3246153846153846,
        'Brain - Substantia nigra': 0.3470454545454546,
        'Breast - Mammary Tissue': 0.4098275862068964,
        'Cells - EBV-transformed lymphocytes': 0.5286153846153846,
        'Cells - Transformed fibroblasts': 0.3530903790087463,
        'Cervix - Ectocervix': 0.6133333333333334,
        'Cervix - Endocervix': 0.5740000000000001,
        'Colon - Sigmoid': 0.3669527896995707,
        'Colon - Transverse': 0.5093430656934308,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 0.4238934426229508,
        'Esophagus - Mucosa': 0.5100000000000002,
        'Esophagus - Muscularis': 0.4280270270270271,
        'Fallopian Tube': 0.5657142857142857,
        'Heart - Atrial Appendage': 0.4683501683501685,
        'Heart - Left Ventricle': 0.4918151815181515,
        'Kidney - Cortex': 0.5197777777777777,
        'Liver': 0.3404000000000001,
        'Lung': 0.5615456674473067,
        'Minor Salivary Gland': 0.5321649484536081,
        'Muscle - Skeletal': 0.4500177304964538,
        'Nerve - Tibial': 0.441400966183575,
        'Ovary': 0.5069172932330827,
        'Pancreas': 0.8295161290322582,
        'Pituitary': 0.4289071038251367,
        'Prostate': 0.509736842105263,
        'Skin - Not Sun Exposed (Suprapubic)': 0.4614470284237727,
        'Skin - Sun Exposed (Lower leg)': 0.4058562367864695,
        'Small Intestine - Terminal Ileum': 0.5893430656934306,
        'Spleen': 0.6915432098765428,
        'Stomach': 1.003625954198474,
        'Testis': 1.170926640926641,
        'Thyroid': 0.550067264573991,
        'Uterus': 0.6139639639639639,
        'Vagina': 0.595304347826087,
        'Whole Blood': 0.911056511056511,
        '_id': '5b9f7faa7a55821abccf4e4d',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000339659.4'
      },
      {
        'Adipose - Subcutaneous': 0.0001583710407239819,
        'Adipose - Visceral (Omentum)': 0.0001690140845070423,
        'Adrenal Gland': 0.0003157894736842105,
        'Artery - Aorta': 0,
        'Artery - Coronary': 0.0006358381502890173,
        'Artery - Tibial': 0.0002494331065759637,
        'Bladder': 0,
        'Brain - Amygdala': 0,
        'Brain - Anterior cingulate cortex (BA24)': 0,
        'Brain - Caudate (basal ganglia)': 0,
        'Brain - Cerebellar Hemisphere': 0,
        'Brain - Cerebellum': 0.0002890173410404624,
        'Brain - Cortex': 0.0002531645569620253,
        'Brain - Frontal Cortex (BA9)': 0,
        'Brain - Hippocampus': 0,
        'Brain - Hypothalamus': 0,
        'Brain - Nucleus accumbens (basal ganglia)': 0,
        'Brain - Putamen (basal ganglia)': 0,
        'Brain - Spinal cord (cervical c-1)': 0,
        'Brain - Substantia nigra': 0,
        'Breast - Mammary Tissue': 0.0003103448275862069,
        'Cells - EBV-transformed lymphocytes': 0.0004615384615384615,
        'Cells - Transformed fibroblasts': 0.0002332361516034986,
        'Cervix - Ectocervix': 0,
        'Cervix - Endocervix': 0,
        'Colon - Sigmoid': 0,
        'Colon - Transverse': 3.649635036496351e-05,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 0,
        'Esophagus - Mucosa': 0,
        'Esophagus - Muscularis': 0.0002702702702702703,
        'Fallopian Tube': 0,
        'Heart - Atrial Appendage': 0,
        'Heart - Left Ventricle': 0.000132013201320132,
        'Kidney - Cortex': 0,
        'Liver': 0,
        'Lung': 0.0006088992974238876,
        'Minor Salivary Gland': 0,
        'Muscle - Skeletal': 0.0003368794326241135,
        'Nerve - Tibial': 0.0005072463768115942,
        'Ovary': 0,
        'Pancreas': 0.0003629032258064516,
        'Pituitary': 0,
        'Prostate': 0,
        'Skin - Not Sun Exposed (Suprapubic)': 0.0002325581395348837,
        'Skin - Sun Exposed (Lower leg)': 0,
        'Small Intestine - Terminal Ileum': 0.000656934306569343,
        'Spleen': 0.0007407407407407408,
        'Stomach': 0,
        'Testis': 0.0006177606177606178,
        'Thyroid': 0.0004035874439461883,
        'Uterus': 0,
        'Vagina': 0,
        'Whole Blood': 0,
        '_id': '5b9f7faa7a55821abccf4e4e',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000398956.2'
      },
      {
        'Adipose - Subcutaneous': 0.0001131221719457014,
        'Adipose - Visceral (Omentum)': 0,
        'Adrenal Gland': 0,
        'Artery - Aorta': 0,
        'Artery - Coronary': 0,
        'Artery - Tibial': 0.0007709750566893425,
        'Bladder': 0,
        'Brain - Amygdala': 0,
        'Brain - Anterior cingulate cortex (BA24)': 0,
        'Brain - Caudate (basal ganglia)': 0,
        'Brain - Cerebellar Hemisphere': 0,
        'Brain - Cerebellum': 0,
        'Brain - Cortex': 0,
        'Brain - Frontal Cortex (BA9)': 0,
        'Brain - Hippocampus': 0,
        'Brain - Hypothalamus': 0,
        'Brain - Nucleus accumbens (basal ganglia)': 0,
        'Brain - Putamen (basal ganglia)': 0,
        'Brain - Spinal cord (cervical c-1)': 0,
        'Brain - Substantia nigra': 0,
        'Breast - Mammary Tissue': 0,
        'Cells - EBV-transformed lymphocytes': 0,
        'Cells - Transformed fibroblasts': 0.004431486880466473,
        'Cervix - Ectocervix': 0,
        'Cervix - Endocervix': 0,
        'Colon - Sigmoid': 0,
        'Colon - Transverse': 0,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 0,
        'Esophagus - Mucosa': 0,
        'Esophagus - Muscularis': 0.0002702702702702703,
        'Fallopian Tube': 0,
        'Heart - Atrial Appendage': 0,
        'Heart - Left Ventricle': 0,
        'Kidney - Cortex': 0,
        'Liver': 0,
        'Lung': 0.003208430913348946,
        'Minor Salivary Gland': 0,
        'Muscle - Skeletal': 0.0003900709219858156,
        'Nerve - Tibial': 0,
        'Ovary': 0,
        'Pancreas': 0,
        'Pituitary': 0,
        'Prostate': 0,
        'Skin - Not Sun Exposed (Suprapubic)': 0,
        'Skin - Sun Exposed (Lower leg)': 0,
        'Small Intestine - Terminal Ileum': 0,
        'Spleen': 0,
        'Stomach': 0,
        'Testis': 0,
        'Thyroid': 0,
        'Uterus': 0,
        'Vagina': 0,
        'Whole Blood': 0,
        '_id': '5b9f7faa7a55821abccf4e4f',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000398960.2'
      },
      {
        'Adipose - Subcutaneous': 1.290226244343891,
        'Adipose - Visceral (Omentum)': 0.8649859154929578,
        'Adrenal Gland': 0.9883157894736839,
        'Artery - Aorta': 1.212207357859531,
        'Artery - Coronary': 1.139768786127167,
        'Artery - Tibial': 1.959795918367348,
        'Bladder': 2.080909090909091,
        'Brain - Amygdala': 0.3122999999999999,
        'Brain - Anterior cingulate cortex (BA24)': 0.4678512396694214,
        'Brain - Caudate (basal ganglia)': 0.3975625,
        'Brain - Cerebellar Hemisphere': 1.553014705882353,
        'Brain - Cerebellum': 1.064335260115607,
        'Brain - Cortex': 0.591139240506329,
        'Brain - Frontal Cortex (BA9)': 0.6767441860465119,
        'Brain - Hippocampus': 0.3382926829268293,
        'Brain - Hypothalamus': 0.4323966942148759,
        'Brain - Nucleus accumbens (basal ganglia)': 0.5310884353741498,
        'Brain - Putamen (basal ganglia)': 0.2788709677419355,
        'Brain - Spinal cord (cervical c-1)': 0.3975824175824175,
        'Brain - Substantia nigra': 0.2912500000000001,
        'Breast - Mammary Tissue': 1.177344827586207,
        'Cells - EBV-transformed lymphocytes': 2.025461538461538,
        'Cells - Transformed fibroblasts': 2.029387755102041,
        'Cervix - Ectocervix': 1.755,
        'Cervix - Endocervix': 1.748,
        'Colon - Sigmoid': 1.132918454935623,
        'Colon - Transverse': 0.8316423357664225,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 1.313770491803278,
        'Esophagus - Mucosa': 0.7695823095823098,
        'Esophagus - Muscularis': 1.512864864864863,
        'Fallopian Tube': 1.411428571428572,
        'Heart - Atrial Appendage': 0.6528619528619526,
        'Heart - Left Ventricle': 0.5477887788778875,
        'Kidney - Cortex': 0.5204444444444444,
        'Liver': 0.1865142857142857,
        'Lung': 1.161803278688525,
        'Minor Salivary Gland': 1.264432989690721,
        'Muscle - Skeletal': 1.706879432624114,
        'Nerve - Tibial': 1.258357487922705,
        'Ovary': 1.394285714285714,
        'Pancreas': 0.3233870967741936,
        'Pituitary': 0.7702185792349726,
        'Prostate': 0.785065789473684,
        'Skin - Not Sun Exposed (Suprapubic)': 0.9350645994832044,
        'Skin - Sun Exposed (Lower leg)': 1.005454545454546,
        'Small Intestine - Terminal Ileum': 1.021313868613138,
        'Spleen': 0.806543209876543,
        'Stomach': 0.7267938931297705,
        'Testis': 0.8445559845559846,
        'Thyroid': 1.557488789237669,
        'Uterus': 1.838378378378378,
        'Vagina': 1.084173913043479,
        'Whole Blood': 0.1650859950859952,
        '_id': '5b9f7faa7a55821abccf4e50',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000426672.1'
      },
      {
        'Adipose - Subcutaneous': 0,
        'Adipose - Visceral (Omentum)': 0,
        'Adrenal Gland': 0,
        'Artery - Aorta': 0,
        'Artery - Coronary': 0,
        'Artery - Tibial': 0,
        'Bladder': 0,
        'Brain - Amygdala': 0,
        'Brain - Anterior cingulate cortex (BA24)': 0,
        'Brain - Caudate (basal ganglia)': 0,
        'Brain - Cerebellar Hemisphere': 0,
        'Brain - Cerebellum': 0,
        'Brain - Cortex': 0,
        'Brain - Frontal Cortex (BA9)': 0,
        'Brain - Hippocampus': 0,
        'Brain - Hypothalamus': 0,
        'Brain - Nucleus accumbens (basal ganglia)': 0,
        'Brain - Putamen (basal ganglia)': 0,
        'Brain - Spinal cord (cervical c-1)': 0,
        'Brain - Substantia nigra': 0,
        'Breast - Mammary Tissue': 0,
        'Cells - EBV-transformed lymphocytes': 0,
        'Cells - Transformed fibroblasts': 0,
        'Cervix - Ectocervix': 0,
        'Cervix - Endocervix': 0,
        'Colon - Sigmoid': 0,
        'Colon - Transverse': 0,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 0,
        'Esophagus - Mucosa': 0,
        'Esophagus - Muscularis': 0,
        'Fallopian Tube': 0,
        'Heart - Atrial Appendage': 0,
        'Heart - Left Ventricle': 0,
        'Kidney - Cortex': 0,
        'Liver': 0,
        'Lung': 0,
        'Minor Salivary Gland': 0,
        'Muscle - Skeletal': 0,
        'Nerve - Tibial': 0,
        'Ovary': 0,
        'Pancreas': 0,
        'Pituitary': 0,
        'Prostate': 0,
        'Skin - Not Sun Exposed (Suprapubic)': 0,
        'Skin - Sun Exposed (Lower leg)': 0,
        'Small Intestine - Terminal Ileum': 0,
        'Spleen': 0,
        'Stomach': 0,
        'Testis': 0,
        'Thyroid': 0,
        'Uterus': 0,
        'Vagina': 0,
        'Whole Blood': 0,
        '_id': '5b9f7faa7a55821abccf4e51',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000451934.1'
      },
      {
        'Adipose - Subcutaneous': 0.2022398190045248,
        'Adipose - Visceral (Omentum)': 0.1105352112676057,
        'Adrenal Gland': 0.1078421052631579,
        'Artery - Aorta': 0.1503678929765886,
        'Artery - Coronary': 0.1183815028901734,
        'Artery - Tibial': 0.14578231292517,
        'Bladder': 0.2854545454545455,
        'Brain - Amygdala': 0.0247,
        'Brain - Anterior cingulate cortex (BA24)': 0.03595041322314049,
        'Brain - Caudate (basal ganglia)': 0.04443750000000001,
        'Brain - Cerebellar Hemisphere': 0.0938970588235294,
        'Brain - Cerebellum': 0.1072254335260115,
        'Brain - Cortex': 0.0420886075949367,
        'Brain - Frontal Cortex (BA9)': 0.04651162790697674,
        'Brain - Hippocampus': 0.03788617886178863,
        'Brain - Hypothalamus': 0.02652892561983471,
        'Brain - Nucleus accumbens (basal ganglia)': 0.04945578231292517,
        'Brain - Putamen (basal ganglia)': 0.03927419354838711,
        'Brain - Spinal cord (cervical c-1)': 0.02428571428571429,
        'Brain - Substantia nigra': 0.02670454545454546,
        'Breast - Mammary Tissue': 0.1593103448275862,
        'Cells - EBV-transformed lymphocytes': 0.1746923076923077,
        'Cells - Transformed fibroblasts': 0.1476093294460641,
        'Cervix - Ectocervix': 0.05666666666666667,
        'Cervix - Endocervix': 0.202,
        'Colon - Sigmoid': 0.1072103004291846,
        'Colon - Transverse': 0.09686131386861313,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 0.1293442622950819,
        'Esophagus - Mucosa': 0.1061179361179361,
        'Esophagus - Muscularis': 0.1294324324324324,
        'Fallopian Tube': 0.2557142857142857,
        'Heart - Atrial Appendage': 0.06360269360269365,
        'Heart - Left Ventricle': 0.05343234323432345,
        'Kidney - Cortex': 0.1022222222222222,
        'Liver': 0.03491428571428571,
        'Lung': 0.1344730679156909,
        'Minor Salivary Gland': 0.1869072164948453,
        'Muscle - Skeletal': 0.1175709219858156,
        'Nerve - Tibial': 0.1364009661835749,
        'Ovary': 0.1292481203007518,
        'Pancreas': 0.05641129032258064,
        'Pituitary': 0.07207650273224044,
        'Prostate': 0.05894736842105262,
        'Skin - Not Sun Exposed (Suprapubic)': 0.1202067183462533,
        'Skin - Sun Exposed (Lower leg)': 0.1336786469344609,
        'Small Intestine - Terminal Ileum': 0.1471532846715329,
        'Spleen': 0.1593827160493827,
        'Stomach': 0.09748091603053438,
        'Testis': 0.2053281853281854,
        'Thyroid': 0.1929820627802691,
        'Uterus': 0.1274774774774775,
        'Vagina': 0.1415652173913043,
        'Whole Blood': 0.01656019656019656,
        '_id': '5b9f7faa7a55821abccf4e52',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000455097.1'
      },
      {
        'Adipose - Subcutaneous': 4.852828054298641,
        'Adipose - Visceral (Omentum)': 3.375239436619718,
        'Adrenal Gland': 3.507210526315791,
        'Artery - Aorta': 4.014013377926419,
        'Artery - Coronary': 4.015375722543353,
        'Artery - Tibial': 6.216848072562356,
        'Bladder': 7.802727272727271,
        'Brain - Amygdala': 0.7476999999999996,
        'Brain - Anterior cingulate cortex (BA24)': 1.339586776859504,
        'Brain - Caudate (basal ganglia)': 1.0919375,
        'Brain - Cerebellar Hemisphere': 5.060955882352941,
        'Brain - Cerebellum': 3.434797687861271,
        'Brain - Cortex': 1.533481012658228,
        'Brain - Frontal Cortex (BA9)': 2.25829457364341,
        'Brain - Hippocampus': 0.8927642276422757,
        'Brain - Hypothalamus': 1.386859504132231,
        'Brain - Nucleus accumbens (basal ganglia)': 1.642925170068027,
        'Brain - Putamen (basal ganglia)': 0.6637903225806453,
        'Brain - Spinal cord (cervical c-1)': 1.465824175824176,
        'Brain - Substantia nigra': 0.7827272727272725,
        'Breast - Mammary Tissue': 4.485103448275862,
        'Cells - EBV-transformed lymphocytes': 6.527615384615385,
        'Cells - Transformed fibroblasts': 6.400903790087468,
        'Cervix - Ectocervix': 5.359999999999999,
        'Cervix - Endocervix': 7.294,
        'Colon - Sigmoid': 3.729442060085835,
        'Colon - Transverse': 3.221350364963502,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 4.307704918032785,
        'Esophagus - Mucosa': 2.767764127764128,
        'Esophagus - Muscularis': 5.017972972972974,
        'Fallopian Tube': 5.854285714285714,
        'Heart - Atrial Appendage': 2.111010101010101,
        'Heart - Left Ventricle': 1.639306930693068,
        'Kidney - Cortex': 2.126666666666666,
        'Liver': 0.6554285714285711,
        'Lung': 4.625784543325532,
        'Minor Salivary Gland': 4.008762886597939,
        'Muscle - Skeletal': 5.11840425531915,
        'Nerve - Tibial': 4.567101449275369,
        'Ovary': 5.093909774436089,
        'Pancreas': 0.8083064516129035,
        'Pituitary': 3.517049180327868,
        'Prostate': 3.037368421052631,
        'Skin - Not Sun Exposed (Suprapubic)': 3.70640826873385,
        'Skin - Sun Exposed (Lower leg)': 4.120676532769555,
        'Small Intestine - Terminal Ileum': 3.817737226277374,
        'Spleen': 3.579753086419752,
        'Stomach': 2.137977099236641,
        'Testis': 5.971621621621619,
        'Thyroid': 6.116816143497757,
        'Uterus': 6.386756756756757,
        'Vagina': 3.916956521739131,
        'Whole Blood': 0.3928501228501229,
        '_id': '5b9f7faa7a55821abccf4e53',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000455387.2'
      },
      {
        'Adipose - Subcutaneous': 2.520135746606335,
        'Adipose - Visceral (Omentum)': 1.868901408450704,
        'Adrenal Gland': 2.253631578947367,
        'Artery - Aorta': 2.447959866220733,
        'Artery - Coronary': 2.199595375722542,
        'Artery - Tibial': 3.338117913832199,
        'Bladder': 4.618181818181818,
        'Brain - Amygdala': 0.6644,
        'Brain - Anterior cingulate cortex (BA24)': 0.9766942148760333,
        'Brain - Caudate (basal ganglia)': 0.8273125,
        'Brain - Cerebellar Hemisphere': 2.917279411764705,
        'Brain - Cerebellum': 2.201849710982658,
        'Brain - Cortex': 1.166075949367088,
        'Brain - Frontal Cortex (BA9)': 1.393178294573644,
        'Brain - Hippocampus': 0.6673170731707317,
        'Brain - Hypothalamus': 0.9461983471074378,
        'Brain - Nucleus accumbens (basal ganglia)': 1.021564625850341,
        'Brain - Putamen (basal ganglia)': 0.567741935483871,
        'Brain - Spinal cord (cervical c-1)': 0.8830769230769231,
        'Brain - Substantia nigra': 0.5432954545454546,
        'Breast - Mammary Tissue': 2.417275862068966,
        'Cells - EBV-transformed lymphocytes': 4.221769230769232,
        'Cells - Transformed fibroblasts': 3.967055393586003,
        'Cervix - Ectocervix': 2.783333333333333,
        'Cervix - Endocervix': 3.774,
        'Colon - Sigmoid': 2.203862660944206,
        'Colon - Transverse': 1.873649635036496,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 2.590368852459015,
        'Esophagus - Mucosa': 1.669828009828011,
        'Esophagus - Muscularis': 3.045324324324325,
        'Fallopian Tube': 3.047142857142857,
        'Heart - Atrial Appendage': 1.423299663299664,
        'Heart - Left Ventricle': 1.098151815181518,
        'Kidney - Cortex': 1.411333333333333,
        'Liver': 0.4256,
        'Lung': 2.440936768149885,
        'Minor Salivary Gland': 2.25680412371134,
        'Muscle - Skeletal': 2.925833333333333,
        'Nerve - Tibial': 2.381111111111109,
        'Ovary': 2.964135338345866,
        'Pancreas': 0.5916129032258063,
        'Pituitary': 2.119890710382515,
        'Prostate': 1.773947368421052,
        'Skin - Not Sun Exposed (Suprapubic)': 1.87284237726098,
        'Skin - Sun Exposed (Lower leg)': 1.979915433403807,
        'Small Intestine - Terminal Ileum': 2.155693430656933,
        'Spleen': 2.021049382716048,
        'Stomach': 1.396297709923664,
        'Testis': 2.143281853281852,
        'Thyroid': 3.564820627802693,
        'Uterus': 3.74072072072072,
        'Vagina': 2.304173913043479,
        'Whole Blood': 0.3272481572481575,
        '_id': '5b9f7faa7a55821abccf4e54',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000462274.1'
      },
      {
        'Adipose - Subcutaneous': 0.6286877828054297,
        'Adipose - Visceral (Omentum)': 0.2591549295774647,
        'Adrenal Gland': 0.2196315789473684,
        'Artery - Aorta': 0.1991973244147157,
        'Artery - Coronary': 0.1436994219653179,
        'Artery - Tibial': 0.5260090702947846,
        'Bladder': 0.5927272727272727,
        'Brain - Amygdala': 0.09579999999999998,
        'Brain - Anterior cingulate cortex (BA24)': 0.05479338842975207,
        'Brain - Caudate (basal ganglia)': 0.0619375,
        'Brain - Cerebellar Hemisphere': 0.1855882352941176,
        'Brain - Cerebellum': 0.1501734104046243,
        'Brain - Cortex': 0.080253164556962,
        'Brain - Frontal Cortex (BA9)': 0.08697674418604652,
        'Brain - Hippocampus': 0.07593495934959349,
        'Brain - Hypothalamus': 0.1207438016528925,
        'Brain - Nucleus accumbens (basal ganglia)': 0.0836734693877551,
        'Brain - Putamen (basal ganglia)': 0.01612903225806452,
        'Brain - Spinal cord (cervical c-1)': 0.08428571428571428,
        'Brain - Substantia nigra': 0.08318181818181819,
        'Breast - Mammary Tissue': 0.4287931034482759,
        'Cells - EBV-transformed lymphocytes': 0.7266153846153846,
        'Cells - Transformed fibroblasts': 0.3709037900874635,
        'Cervix - Ectocervix': 0.5716666666666667,
        'Cervix - Endocervix': 0.702,
        'Colon - Sigmoid': 0.137381974248927,
        'Colon - Transverse': 0.182007299270073,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 0.1181557377049181,
        'Esophagus - Mucosa': 0.1476904176904177,
        'Esophagus - Muscularis': 0.1156486486486486,
        'Fallopian Tube': 0.2014285714285714,
        'Heart - Atrial Appendage': 0.1400673400673401,
        'Heart - Left Ventricle': 0.05330033003300329,
        'Kidney - Cortex': 0.144,
        'Liver': 0.03657142857142857,
        'Lung': 0.3744262295081967,
        'Minor Salivary Gland': 0.2688659793814432,
        'Muscle - Skeletal': 0.1823936170212766,
        'Nerve - Tibial': 0.4127777777777777,
        'Ovary': 0.2977443609022556,
        'Pancreas': 0.1349193548387096,
        'Pituitary': 0.322568306010929,
        'Prostate': 0.08092105263157895,
        'Skin - Not Sun Exposed (Suprapubic)': 0.6573901808785534,
        'Skin - Sun Exposed (Lower leg)': 0.9438266384778008,
        'Small Intestine - Terminal Ileum': 0.2517518248175183,
        'Spleen': 0.1508641975308642,
        'Stomach': 0.1537404580152671,
        'Testis': 0.8065250965250965,
        'Thyroid': 0.3043273542600898,
        'Uterus': 0.1833333333333333,
        'Vagina': 0.1791304347826087,
        'Whole Blood': 0.09828009828009827,
        '_id': '5b9f7faa7a55821abccf4e55',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000498351.1'
      },
      {
        'Adipose - Subcutaneous': 0.4485067873303167,
        'Adipose - Visceral (Omentum)': 0.3445352112676057,
        'Adrenal Gland': 0.6628947368421053,
        'Artery - Aorta': 0.86752508361204,
        'Artery - Coronary': 0.7226589595375724,
        'Artery - Tibial': 0.6764625850340134,
        'Bladder': 1.386363636363636,
        'Brain - Amygdala': 0.3857,
        'Brain - Anterior cingulate cortex (BA24)': 0.5103305785123966,
        'Brain - Caudate (basal ganglia)': 0.3808750000000001,
        'Brain - Cerebellar Hemisphere': 0.815073529411765,
        'Brain - Cerebellum': 0.8709248554913297,
        'Brain - Cortex': 0.5275316455696204,
        'Brain - Frontal Cortex (BA9)': 0.5361240310077519,
        'Brain - Hippocampus': 0.3948780487804878,
        'Brain - Hypothalamus': 0.5134710743801651,
        'Brain - Nucleus accumbens (basal ganglia)': 0.495034013605442,
        'Brain - Putamen (basal ganglia)': 0.3754838709677421,
        'Brain - Spinal cord (cervical c-1)': 0.3728571428571431,
        'Brain - Substantia nigra': 0.3514772727272727,
        'Breast - Mammary Tissue': 0.3988965517241381,
        'Cells - EBV-transformed lymphocytes': 0.6057692307692305,
        'Cells - Transformed fibroblasts': 0.5933527696793003,
        'Cervix - Ectocervix': 0.4883333333333333,
        'Cervix - Endocervix': 0.4480000000000001,
        'Colon - Sigmoid': 0.4972103004291847,
        'Colon - Transverse': 0.3428467153284672,
        'Entrez_id': '1859',
        'Esophagus - Gastroesophageal Junction': 0.5743852459016398,
        'Esophagus - Mucosa': 0.3610565110565113,
        'Esophagus - Muscularis': 0.7669999999999995,
        'Fallopian Tube': 0.802857142857143,
        'Heart - Atrial Appendage': 0.4124915824915824,
        'Heart - Left Ventricle': 0.3501980198019802,
        'Kidney - Cortex': 0.4793333333333334,
        'Liver': 0.0977142857142857,
        'Lung': 0.4686182669789228,
        'Minor Salivary Gland': 0.3051546391752578,
        'Muscle - Skeletal': 0.5154255319148933,
        'Nerve - Tibial': 0.6205555555555557,
        'Ovary': 0.6257142857142858,
        'Pancreas': 0.1131854838709677,
        'Pituitary': 0.8945901639344265,
        'Prostate': 0.7443421052631578,
        'Skin - Not Sun Exposed (Suprapubic)': 0.2259689922480621,
        'Skin - Sun Exposed (Lower leg)': 0.2551374207188162,
        'Small Intestine - Terminal Ileum': 0.3779562043795621,
        'Spleen': 0.7675308641975312,
        'Stomach': 0.3029770992366412,
        'Testis': 1.144478764478765,
        'Thyroid': 1.066726457399103,
        'Uterus': 0.6575675675675676,
        'Vagina': 0.4771304347826088,
        'Whole Blood': 0.1342014742014743,
        '_id': '5b9f7faa7a55821abccf4e56',
        'gene_id': 'ENSG00000157540.15',
        'transcript_id': 'ENST00000608928.1'
      }]
      // eslint-disable-next-line camelcase
      let brain_express = 0

      // eslint-disable-next-line camelcase
      function get_columns () {
        return ['Adipose - Subcutaneous', 'Adipose - Visceral (Omentum)', 'Adrenal Gland', 'Artery - Aorta',
          'Artery - Coronary', 'Artery - Tibial', 'Bladder', 'Brain - Amygdala',
          'Brain - Anterior cingulate cortex (BA24)', 'Brain - Caudate (basal ganglia)',
          'Brain - Cerebellar Hemisphere', 'Brain - Cerebellum', 'Brain - Cortex',
          'Brain - Frontal Cortex (BA9)', 'Brain - Hippocampus', 'Brain - Hypothalamus',
          'Brain - Nucleus accumbens (basal ganglia)', 'Brain - Putamen (basal ganglia)',
          'Brain - Spinal cord (cervical c-1)', 'Brain - Substantia nigra', 'Breast - Mammary Tissue',
          'Cells - EBV-transformed lymphocytes', 'Cells - Transformed fibroblasts', 'Cervix - Ectocervix',
          'Cervix - Endocervix', 'Colon - Sigmoid', 'Colon - Transverse',
          'Esophagus - Gastroesophageal Junction', 'Esophagus - Mucosa', 'Esophagus - Muscularis',
          'Fallopian Tube', 'Heart - Atrial Appendage', 'Heart - Left Ventricle', 'Kidney - Cortex', 'Liver',
          'Lung', 'Minor Salivary Gland', 'Muscle - Skeletal', 'Nerve - Tibial', 'Ovary', 'Pancreas',
          'Pituitary', 'Prostate', 'Skin - Not Sun Exposed (Suprapubic)', 'Skin - Sun Exposed (Lower leg)',
          'Small Intestine - Terminal Ileum', 'Spleen', 'Stomach', 'Testis', 'Thyroid', 'Uterus', 'Vagina',
          'Whole Blood']
      }

      // eslint-disable-next-line camelcase,no-unused-vars
      function get_brain_columns () {
        return ['Brain - Amygdala', 'Brain - Anterior cingulate cortex (BA24)', 'Brain - Caudate (basal ganglia)',
          'Brain - Cerebellar Hemisphere', 'Brain - Cerebellum', 'Brain - Cortex',
          'Brain - Frontal Cortex (BA9)', 'Brain - Hippocampus', 'Brain - Hypothalamus',
          'Brain - Nucleus accumbens (basal ganglia)', 'Brain - Putamen (basal ganglia)',
          'Brain - Spinal cord (cervical c-1)', 'Brain - Substantia nigra']
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
        // eslint-disable-next-line camelcase
        let express_list = a
        // eslint-disable-next-line camelcase
        let express_average = []
        if (express_list.length >= 1) {
          // eslint-disable-next-line camelcase
          if (brain_express === 0) {
            // eslint-disable-next-line camelcase
            for (let item_trans of express_list) {
              // eslint-disable-next-line camelcase
              const list_avg = []
              list_avg.push(item_trans['transcript_id'])
              // eslint-disable-next-line camelcase
              for (let item_colunms of get_columns()) {
                if (item_trans[item_colunms] !== undefined) {
                  list_avg.push(r2(l2(item_trans[item_colunms])))
                } else {
                  list_avg.push(undefined)
                }
              }
              express_average.push(list_avg)
              // console.log(list_avg)
            }
          } else {
            // eslint-disable-next-line camelcase
            for (let item_trans of express_list) {
              // eslint-disable-next-line camelcase
              let list_avg = []
              list_avg.push(item_trans['transcript_id'])
              // eslint-disable-next-line camelcase
              for (let item_colunms of get_columns()) {
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
                let item_list_avg = list_avg[i]
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
      let express_average = data_handling()
      let trace = []
      // eslint-disable-next-line camelcase
      if (express_average !== []) {
        // eslint-disable-next-line camelcase
        let x_columns = get_columns()
        // eslint-disable-next-line camelcase
        for (let item of express_average) {
          trace.push({
            x: x_columns,
            y: item,
            hoverinfo: 'all',
            name: item[0],
            ycalendar: 180,
            hoverlabel: {
              namelength: -1
            }
          })
        }
        let layout = {
          width: 1600,
          height: 600,
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
          showlegend: true
        }
        this.data = trace
        this.layout = layout
      }
    }
  },
  mounted () {
    this.GtexTranscriptExpressPlot()
  }
}
</script>

<style scoped>

</style>
