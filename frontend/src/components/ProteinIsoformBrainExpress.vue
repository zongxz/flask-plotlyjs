<template>
  <div>
    <div
      v-loading="loading"
        element-loading-background="rgba(255, 255, 255, 1)"
        style="z-index: 0"
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

export default {
  name: 'ProteinExpress',
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
    proteinIsoformPlot () {
      const isoform_list = 'all'
      const data = {
        'ExonicFunc_refGene': 'nonsynonymous SNV',
        'Func_refGene': 'exonic',
        'Gene_refGene': 'SH2B1',
        'alt': 'A',
        'chr': '16',
        'end': 28880342,
        'proteins': [
          {
            'Ensembl': 'ENSG00000178188',
            'GeneID': '25970',
            'NCBI_TaxID': '9606',
            'PDB': [
              '5W3R'
            ],
            'ProteomicsDB': [
              '82346',
              '82347',
              '82348'
            ],
            'RefSeq': 'XP_016878605.1',
            'RefSeq_NT': [
              'NM_001308294.1',
              'XM_017023114.1',
              'XM_017023115.1',
              'XM_017023116.1'
            ],
            'UniProtKB-ID': 'SH2B1_HUMAN',
            'proteomicsdb_protein_expression': {
              'entrez_id': '25970',
              'express_data': [
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.822239000679115',
                  'MIN_NORMALIZED_INTENSITY': '3.822239000679115',
                  'NORMALIZED_INTENSITY': '3.822239000679115',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000142',
                  'TISSUE_NAME': 'brain',
                  'TISSUE_SAP_SYNONYM': 'brain',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '4.62451127498711',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749971')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.016057937681893',
                  'MIN_NORMALIZED_INTENSITY': '3.016057937681893',
                  'NORMALIZED_INTENSITY': '3.016057937681893',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000562',
                  'TISSUE_NAME': 'heart',
                  'TISSUE_SAP_SYNONYM': 'heart',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '4.142296747399034',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749972')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.615303403350095',
                  'MIN_NORMALIZED_INTENSITY': '3.420628258941124',
                  'NORMALIZED_INTENSITY': '3.51796583114561',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 2,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000763',
                  'TISSUE_NAME': 'lung',
                  'TISSUE_SAP_SYNONYM': 'lung',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '4.761226126422234',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749973')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.203146442666908',
                  'MIN_NORMALIZED_INTENSITY': '3.125936809353895',
                  'NORMALIZED_INTENSITY': '3.71938226166613',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 3,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000975',
                  'TISSUE_NAME': 'ovary',
                  'TISSUE_SAP_SYNONYM': 'ovary',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '4.908659305701326',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749974')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.960647918409282',
                  'MIN_NORMALIZED_INTENSITY': '3.960647918409282',
                  'NORMALIZED_INTENSITY': '3.960647918409282',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000988',
                  'TISSUE_NAME': 'pancreas',
                  'TISSUE_SAP_SYNONYM': 'pancreas',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '5.299313557780795',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749975')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.018236584393673',
                  'MIN_NORMALIZED_INTENSITY': '4.018236584393673',
                  'NORMALIZED_INTENSITY': '4.018236584393673',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001129',
                  'TISSUE_NAME': 'prostate gland',
                  'TISSUE_SAP_SYNONYM': 'prostate',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '5.563683199317786',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749976')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.539946842175577',
                  'MIN_NORMALIZED_INTENSITY': '4.539946842175577',
                  'NORMALIZED_INTENSITY': '4.539946842175577',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001175',
                  'TISSUE_NAME': 'retina',
                  'TISSUE_SAP_SYNONYM': 'eye',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '6.282305668053451',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749977')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.773386097368435',
                  'MIN_NORMALIZED_INTENSITY': '3.773386097368435',
                  'NORMALIZED_INTENSITY': '3.773386097368435',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001279',
                  'TISSUE_NAME': 'spinal cord',
                  'TISSUE_SAP_SYNONYM': 'spinal_cord',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '5.510217229526129',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749978')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.691466375705097',
                  'MIN_NORMALIZED_INTENSITY': '4.691466375705097',
                  'NORMALIZED_INTENSITY': '4.691466375705097',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001363',
                  'TISSUE_NAME': 'testis',
                  'TISSUE_SAP_SYNONYM': 'testis',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '6.039342134757804',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749979')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.052070240713455',
                  'MIN_NORMALIZED_INTENSITY': '4.052070240713455',
                  'NORMALIZED_INTENSITY': '4.052070240713455',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0002807',
                  'TISSUE_NAME': 'prefrontal cortex',
                  'TISSUE_SAP_SYNONYM': 'brain',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '5.475687326801305',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('692625988537499710')"
                  }
                }
              ],
              'uniprotkb_ac': 'Q9NRF2'
            },
            'uniprotkb_ac': 'Q9NRF2'
          },
          {
            'GeneID': '25970',
            'NCBI_TaxID': '9606',
            'RefSeq': 'XP_016878605.1',
            'RefSeq_NT': [
              'NM_001145795.1',
              'NM_001308293.1',
              'XM_017023114.1',
              'XM_017023115.1',
              'XM_017023116.1'
            ],
            'UniProtKB-ID': 'A0A024QZD2_HUMAN',
            'uniprotkb_ac': 'A0A024QZD2'
          },
          {
            'GeneID': '25970',
            'NCBI_TaxID': '9606',
            'RefSeq': 'NP_056318.2',
            'RefSeq_NT': [
              'NM_001145796.1',
              'NM_001145812.1',
              'NM_015503.2'
            ],
            'UniProtKB-ID': 'A0A024QZC2_HUMAN',
            'uniprotkb_ac': 'A0A024QZC2'
          },
          {
            'Ensembl': 'ENSG00000178188',
            'Ensembl_PRO': [
              'ENSP00000438784'
            ],
            'Ensembl_TRS': [
              'ENST00000538342'
            ],
            'GeneID': '25970',
            'NCBI_TaxID': '9606',
            'ProteomicsDB': [
              '4546'
            ],
            'RefSeq': 'NP_001295223.1',
            'RefSeq_NT': [
              'NM_001145795.1',
              'NM_001145796.1',
              'NM_001145797.1',
              'NM_001308294.1'
            ],
            'UniProtKB-ID': 'B4DLN5_HUMAN',
            'uniprotkb_ac': 'B4DLN5'
          },
          {
            'GeneID': '25970',
            'NCBI_TaxID': '9606',
            'RefSeq': 'NP_001139269.1',
            'RefSeq_NT': [
              'NM_001145797.1'
            ],
            'UniProtKB-ID': 'A0A024QZ92_HUMAN',
            'uniprotkb_ac': 'A0A024QZ92'
          },
          {
            'GeneID': '25970',
            'NCBI_TaxID': '9606',
            'RefSeq': 'NP_001295222.1',
            'RefSeq_NT': [
              'NM_001145795.1',
              'NM_001145796.1',
              'NM_001145797.1',
              'NM_001308293.1'
            ],
            'UniProtKB-ID': 'B3KNV5_HUMAN',
            'uniprotkb_ac': 'B3KNV5'
          },
          {
            'Ensembl_PRO': [
              'ENSP00000321221',
              'ENSP00000481709',
              'ENSP00000507475'
            ],
            'Ensembl_TRS': [
              'ENST00000322610',
              'ENST00000618521',
              'ENST00000684370'
            ],
            'RefSeq': 'NP_001295222.1',
            'RefSeq_NT': [
              'NM_001145795.1',
              'NM_001308293.1'
            ],
            'proteomicsdb_protein_expression': {
              'entrez_id': '25970',
              'uniprotkb_ac': 'Q9NRF2-1'
            },
            'uniprotkb_ac': 'Q9NRF2-1'
          },
          {
            'Ensembl_PRO': [
              'ENSP00000337163',
              'ENSP00000378903'
            ],
            'Ensembl_TRS': [
              'ENST00000337120',
              'ENST00000395532'
            ],
            'RefSeq': 'NP_056318.2',
            'RefSeq_NT': [
              'NM_001145796.1',
              'NM_001145812.1',
              'NM_015503.2'
            ],
            'proteomicsdb_protein_expression': {
              'entrez_id': '25970',
              'express_data': [
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.855662756166064',
                  'MIN_NORMALIZED_INTENSITY': '3.855662756166064',
                  'NORMALIZED_INTENSITY': '3.855662756166064',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000142',
                  'TISSUE_NAME': 'brain',
                  'TISSUE_SAP_SYNONYM': 'brain',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '4.657935030474059',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262619518693511')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.049481693168842',
                  'MIN_NORMALIZED_INTENSITY': '3.049481693168842',
                  'NORMALIZED_INTENSITY': '3.049481693168842',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000562',
                  'TISSUE_NAME': 'heart',
                  'TISSUE_SAP_SYNONYM': 'heart',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '4.175720502885983',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262619518693512')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.648727158837046',
                  'MIN_NORMALIZED_INTENSITY': '3.454052014428073',
                  'NORMALIZED_INTENSITY': '3.55138958663256',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 2,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000763',
                  'TISSUE_NAME': 'lung',
                  'TISSUE_SAP_SYNONYM': 'lung',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '4.794649881909184',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262619518693513')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.236570198153859',
                  'MIN_NORMALIZED_INTENSITY': '3.159360564840844',
                  'NORMALIZED_INTENSITY': '3.75280601715308',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 3,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000975',
                  'TISSUE_NAME': 'ovary',
                  'TISSUE_SAP_SYNONYM': 'ovary',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '4.942083061188275',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262619518693514')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.994071673896233',
                  'MIN_NORMALIZED_INTENSITY': '3.994071673896233',
                  'NORMALIZED_INTENSITY': '3.994071673896233',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000988',
                  'TISSUE_NAME': 'pancreas',
                  'TISSUE_SAP_SYNONYM': 'pancreas',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '5.332737313267745',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262619518693515')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.051660339880621',
                  'MIN_NORMALIZED_INTENSITY': '4.051660339880621',
                  'NORMALIZED_INTENSITY': '4.051660339880621',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001129',
                  'TISSUE_NAME': 'prostate gland',
                  'TISSUE_SAP_SYNONYM': 'prostate',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '5.597106954804735',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262619518693516')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.573370597662526',
                  'MIN_NORMALIZED_INTENSITY': '4.573370597662526',
                  'NORMALIZED_INTENSITY': '4.573370597662526',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001175',
                  'TISSUE_NAME': 'retina',
                  'TISSUE_SAP_SYNONYM': 'eye',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '6.3157294235404',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262619518693517')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.806809852855385',
                  'MIN_NORMALIZED_INTENSITY': '3.806809852855385',
                  'NORMALIZED_INTENSITY': '3.806809852855385',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001279',
                  'TISSUE_NAME': 'spinal cord',
                  'TISSUE_SAP_SYNONYM': 'spinal_cord',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '5.543640985013078',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262619518693518')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.724890131192047',
                  'MIN_NORMALIZED_INTENSITY': '4.724890131192047',
                  'NORMALIZED_INTENSITY': '4.724890131192047',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001363',
                  'TISSUE_NAME': 'testis',
                  'TISSUE_SAP_SYNONYM': 'testis',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '6.072765890244754',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262619518693519')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.085493996200404',
                  'MIN_NORMALIZED_INTENSITY': '4.085493996200404',
                  'NORMALIZED_INTENSITY': '4.085493996200404',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0002807',
                  'TISSUE_NAME': 'prefrontal cortex',
                  'TISSUE_SAP_SYNONYM': 'brain',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-2',
                  'UNNORMALIZED_INTENSITY': '5.509111082288254',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('692626195186935110')"
                  }
                }
              ],
              'uniprotkb_ac': 'Q9NRF2-2'
            },
            'uniprotkb_ac': 'Q9NRF2-2'
          },
          {
            'proteomicsdb_protein_expression': {
              'entrez_id': '25970',
              'express_data': [
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.822239000679115',
                  'MIN_NORMALIZED_INTENSITY': '3.822239000679115',
                  'NORMALIZED_INTENSITY': '3.822239000679115',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000142',
                  'TISSUE_NAME': 'brain',
                  'TISSUE_SAP_SYNONYM': 'brain',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '4.62451127498711',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749971')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.016057937681893',
                  'MIN_NORMALIZED_INTENSITY': '3.016057937681893',
                  'NORMALIZED_INTENSITY': '3.016057937681893',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000562',
                  'TISSUE_NAME': 'heart',
                  'TISSUE_SAP_SYNONYM': 'heart',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '4.142296747399034',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749972')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.615303403350095',
                  'MIN_NORMALIZED_INTENSITY': '3.420628258941124',
                  'NORMALIZED_INTENSITY': '3.51796583114561',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 2,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000763',
                  'TISSUE_NAME': 'lung',
                  'TISSUE_SAP_SYNONYM': 'lung',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '4.761226126422234',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749973')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.203146442666908',
                  'MIN_NORMALIZED_INTENSITY': '3.125936809353895',
                  'NORMALIZED_INTENSITY': '3.71938226166613',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 3,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000975',
                  'TISSUE_NAME': 'ovary',
                  'TISSUE_SAP_SYNONYM': 'ovary',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '4.908659305701326',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749974')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.960647918409282',
                  'MIN_NORMALIZED_INTENSITY': '3.960647918409282',
                  'NORMALIZED_INTENSITY': '3.960647918409282',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000988',
                  'TISSUE_NAME': 'pancreas',
                  'TISSUE_SAP_SYNONYM': 'pancreas',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '5.299313557780795',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749975')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.018236584393673',
                  'MIN_NORMALIZED_INTENSITY': '4.018236584393673',
                  'NORMALIZED_INTENSITY': '4.018236584393673',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001129',
                  'TISSUE_NAME': 'prostate gland',
                  'TISSUE_SAP_SYNONYM': 'prostate',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '5.563683199317786',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749976')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.539946842175577',
                  'MIN_NORMALIZED_INTENSITY': '4.539946842175577',
                  'NORMALIZED_INTENSITY': '4.539946842175577',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001175',
                  'TISSUE_NAME': 'retina',
                  'TISSUE_SAP_SYNONYM': 'eye',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '6.282305668053451',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749977')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.773386097368435',
                  'MIN_NORMALIZED_INTENSITY': '3.773386097368435',
                  'NORMALIZED_INTENSITY': '3.773386097368435',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001279',
                  'TISSUE_NAME': 'spinal cord',
                  'TISSUE_SAP_SYNONYM': 'spinal_cord',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '5.510217229526129',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749978')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.691466375705097',
                  'MIN_NORMALIZED_INTENSITY': '4.691466375705097',
                  'NORMALIZED_INTENSITY': '4.691466375705097',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001363',
                  'TISSUE_NAME': 'testis',
                  'TISSUE_SAP_SYNONYM': 'testis',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '6.039342134757804',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262598853749979')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.052070240713455',
                  'MIN_NORMALIZED_INTENSITY': '4.052070240713455',
                  'NORMALIZED_INTENSITY': '4.052070240713455',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0002807',
                  'TISSUE_NAME': 'prefrontal cortex',
                  'TISSUE_SAP_SYNONYM': 'brain',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2',
                  'UNNORMALIZED_INTENSITY': '5.475687326801305',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('692625988537499710')"
                  }
                }
              ],
              'uniprotkb_ac': 'Q9NRF2'
            },
            'uniprotkb_ac': 'Q9NRF2'
          },
          {
            'Ensembl_PRO': [
              'ENSP00000352232'
            ],
            'Ensembl_TRS': [
              'ENST00000359285'
            ],
            'RefSeq': 'NP_001139269.1',
            'RefSeq_NT': [
              'NM_001145797.1'
            ],
            'proteomicsdb_protein_expression': {
              'entrez_id': '25970',
              'express_data': [
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.791204766939145',
                  'MIN_NORMALIZED_INTENSITY': '3.791204766939145',
                  'NORMALIZED_INTENSITY': '3.791204766939145',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000142',
                  'TISSUE_NAME': 'brain',
                  'TISSUE_SAP_SYNONYM': 'brain',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '4.593477041247141',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262659908409071')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '2.985023703941924',
                  'MIN_NORMALIZED_INTENSITY': '2.985023703941924',
                  'NORMALIZED_INTENSITY': '2.985023703941924',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000562',
                  'TISSUE_NAME': 'heart',
                  'TISSUE_SAP_SYNONYM': 'heart',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '4.111262513659065',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262659908409072')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.584269169610127',
                  'MIN_NORMALIZED_INTENSITY': '3.389594025201155',
                  'NORMALIZED_INTENSITY': '3.486931597405641',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 2,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000763',
                  'TISSUE_NAME': 'lung',
                  'TISSUE_SAP_SYNONYM': 'lung',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '4.730191892682265',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262659908409073')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.17211220892694',
                  'MIN_NORMALIZED_INTENSITY': '3.094902575613925',
                  'NORMALIZED_INTENSITY': '3.688348027926161',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 3,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000975',
                  'TISSUE_NAME': 'ovary',
                  'TISSUE_SAP_SYNONYM': 'ovary',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '4.877625071961357',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262659908409074')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.929613684669315',
                  'MIN_NORMALIZED_INTENSITY': '3.929613684669315',
                  'NORMALIZED_INTENSITY': '3.929613684669315',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0000988',
                  'TISSUE_NAME': 'pancreas',
                  'TISSUE_SAP_SYNONYM': 'pancreas',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '5.268279324040827',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262659908409075')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.987202350653703',
                  'MIN_NORMALIZED_INTENSITY': '3.987202350653703',
                  'NORMALIZED_INTENSITY': '3.987202350653703',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001129',
                  'TISSUE_NAME': 'prostate gland',
                  'TISSUE_SAP_SYNONYM': 'prostate',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '5.532648965577817',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262659908409076')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.508912608435609',
                  'MIN_NORMALIZED_INTENSITY': '4.508912608435609',
                  'NORMALIZED_INTENSITY': '4.508912608435609',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001175',
                  'TISSUE_NAME': 'retina',
                  'TISSUE_SAP_SYNONYM': 'eye',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '6.251271434313482',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262659908409077')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '3.742351863628466',
                  'MIN_NORMALIZED_INTENSITY': '3.742351863628466',
                  'NORMALIZED_INTENSITY': '3.742351863628466',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001279',
                  'TISSUE_NAME': 'spinal cord',
                  'TISSUE_SAP_SYNONYM': 'spinal_cord',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '5.47918299578616',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262659908409078')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.660432141965128',
                  'MIN_NORMALIZED_INTENSITY': '4.660432141965128',
                  'NORMALIZED_INTENSITY': '4.660432141965128',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0001363',
                  'TISSUE_NAME': 'testis',
                  'TISSUE_SAP_SYNONYM': 'testis',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '6.008307901017835',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('69262659908409079')"
                  }
                },
                {
                  'AFFINITY_PURIFICATION': '',
                  'EXPERIMENT_ID': -1,
                  'EXPERIMENT_NAME': '',
                  'EXPERIMENT_SCOPE': '',
                  'EXPERIMENT_SCOPE_NAME': '',
                  'MAX_NORMALIZED_INTENSITY': '4.021036006973486',
                  'MIN_NORMALIZED_INTENSITY': '4.021036006973486',
                  'NORMALIZED_INTENSITY': '4.021036006973486',
                  'PROJECT_ID': -1,
                  'PROJECT_NAME': '',
                  'PROJECT_STATUS': '',
                  'SAMPLES': 1,
                  'SAMPLE_ID': -1,
                  'SAMPLE_NAME': '',
                  'TISSUE_ID': 'BTO:0002807',
                  'TISSUE_NAME': 'prefrontal cortex',
                  'TISSUE_SAP_SYNONYM': 'brain',
                  'UNIQUE_IDENTIFIER': 'Q9NRF2-3',
                  'UNNORMALIZED_INTENSITY': '5.444653093061336',
                  '__metadata': {
                    'type': 'proteomicsdb.logic.api.proteinexpression.CA_EXPRESSION_PROFILE_APIType',
                    'uri': "http://www.proteomicsdb.org/proteomicsdb/logic/api/proteinexpression.xsodata/CA_EXPRESSION_PROFILE_API('692626599084090710')"
                  }
                }
              ],
              'uniprotkb_ac': 'Q9NRF2-3'
            },
            'uniprotkb_ac': 'Q9NRF2-3'
          }
        ],
        'ref': 'G',
        'regulatory_elements': [
          {
            'enhancer': [
              {
                'chr': 'chr16',
                'end': 28873829,
                'genehancer_id': 'GH16I028873',
                'score': '0.63',
                'start': 28873680
              },
              {
                'chr': 'chr16',
                'end': 28828866,
                'genehancer_id': 'GH16I028828',
                'score': '0.29',
                'start': 28828651
              },
              {
                'chr': 'chr16',
                'end': 28946289,
                'genehancer_id': 'GH16I028945',
                'score': '1.51',
                'start': 28945201
              },
              {
                'chr': 'chr16',
                'end': 28975907,
                'genehancer_id': 'GH16I028973',
                'score': '2.11',
                'start': 28973536
              },
              {
                'chr': 'chr16',
                'end': 28847684,
                'genehancer_id': 'GH16I028844',
                'score': '2.1',
                'start': 28844721
              },
              {
                'chr': 'chr16',
                'end': 28497469,
                'genehancer_id': 'GH16I028490',
                'score': '2.29',
                'start': 28490586
              },
              {
                'chr': 'chr16',
                'end': 29826663,
                'genehancer_id': 'GH16I029819',
                'score': '2.37',
                'start': 29819165
              },
              {
                'chr': 'chr16',
                'end': 29027107,
                'genehancer_id': 'GH16I029026',
                'score': '0.6',
                'start': 29026365
              },
              {
                'chr': 'chr16',
                'end': 28850048,
                'genehancer_id': 'GH16I028849',
                'score': '0.24',
                'start': 28849656
              },
              {
                'chr': 'chr16',
                'end': 29793001,
                'genehancer_id': 'GH16I029789',
                'score': '2.29',
                'start': 29789582
              },
              {
                'chr': 'chr16',
                'end': 28867395,
                'genehancer_id': 'GH16I028861',
                'score': '2.11',
                'start': 28861845
              },
              {
                'chr': 'chr16',
                'end': 28586469,
                'genehancer_id': 'GH16I028585',
                'score': '0.59',
                'start': 28585600
              },
              {
                'chr': 'chr16',
                'end': 29712047,
                'genehancer_id': 'GH16I029708',
                'score': '1.14',
                'start': 29708600
              },
              {
                'chr': 'chr16',
                'end': 28213364,
                'genehancer_id': 'GH16I028209',
                'score': '2.3',
                'start': 28209840
              },
              {
                'chr': 'chr16',
                'end': 29845567,
                'genehancer_id': 'GH16I029845',
                'score': '0.58',
                'start': 29845192
              },
              {
                'chr': 'chr16',
                'end': 28826329,
                'genehancer_id': 'GH16I028821',
                'score': '2.33',
                'start': 28821934
              },
              {
                'chr': 'chr16',
                'end': 29609919,
                'genehancer_id': 'GH16I029608',
                'score': '0.67',
                'start': 29608476
              },
              {
                'chr': 'chr16',
                'end': 29813603,
                'genehancer_id': 'GH16I029803',
                'score': '2.36',
                'start': 29803283
              },
              {
                'chr': 'chr16',
                'end': 29270285,
                'genehancer_id': 'GH16I029258',
                'score': '1.65',
                'start': 29258969
              },
              {
                'chr': 'chr16',
                'end': 29616807,
                'genehancer_id': 'GH16I029611',
                'score': '1.69',
                'start': 29611214
              },
              {
                'chr': 'chr16',
                'end': 29817619,
                'genehancer_id': 'GH16I029813',
                'score': '2.3',
                'start': 29813631
              },
              {
                'chr': 'chr16',
                'end': 29274200,
                'genehancer_id': 'GH16I029273',
                'score': '1.63',
                'start': 29273600
              },
              {
                'chr': 'chr16',
                'end': 29742058,
                'genehancer_id': 'GH16I029736',
                'score': '1.2',
                'start': 29736235
              },
              {
                'chr': 'chr16',
                'end': 29112737,
                'genehancer_id': 'GH16I029111',
                'score': '0.66',
                'start': 29111064
              },
              {
                'chr': 'chr16',
                'end': 29145433,
                'genehancer_id': 'GH16I029143',
                'score': '0.66',
                'start': 29143815
              }
            ],
            'entrez_id': '25970',
            'promoter': [
              {
                'cage_peak_id': 'chr16:28857916..28857952,+',
                'chr': 'chr16',
                'description': 'CAGE_peak_4_at_SH2B1_5end',
                'end': 28857952,
                'entrez_id': '25970',
                'short_descripton': 'p4@SH2B1',
                'start': 28857916,
                'unprot_id': '0'
              },
              {
                'cage_peak_id': 'chr16:28857957..28857969,+',
                'chr': 'chr16',
                'description': 'CAGE_peak_9_at_SH2B1_5end',
                'end': 28857969,
                'entrez_id': '25970',
                'short_descripton': 'p9@SH2B1',
                'start': 28857957,
                'unprot_id': '0'
              },
              {
                'cage_peak_id': 'chr16:28858004..28858029,+',
                'chr': 'chr16',
                'description': 'CAGE_peak_6_at_SH2B1_5end',
                'end': 28858029,
                'entrez_id': '25970',
                'short_descripton': 'p6@SH2B1',
                'start': 28858004,
                'unprot_id': '0'
              },
              {
                'cage_peak_id': 'chr16:28874345..28874371,+',
                'chr': 'chr16',
                'description': 'CAGE_peak_8_at_SH2B1_5end',
                'end': 28874371,
                'entrez_id': '25970',
                'short_descripton': 'p8@SH2B1',
                'start': 28874345,
                'unprot_id': 'Q9NRF2'
              },
              {
                'cage_peak_id': 'chr16:28874860..28874896,+',
                'chr': 'chr16',
                'description': 'CAGE_peak_2_at_SH2B1_5end',
                'end': 28874896,
                'entrez_id': '25970',
                'short_descripton': 'p2@SH2B1',
                'start': 28874860,
                'unprot_id': 'F5GXU7'
              },
              {
                'cage_peak_id': 'chr16:28875133..28875195,+',
                'chr': 'chr16',
                'description': 'CAGE_peak_1_at_SH2B1_5end',
                'end': 28875195,
                'entrez_id': '25970',
                'short_descripton': 'p1@SH2B1',
                'start': 28875133,
                'unprot_id': 'B4DLN5'
              },
              {
                'cage_peak_id': 'chr16:28875268..28875317,+',
                'chr': 'chr16',
                'description': 'CAGE_peak_3_at_SH2B1_5end',
                'end': 28875317,
                'entrez_id': '25970',
                'short_descripton': 'p3@SH2B1',
                'start': 28875268,
                'unprot_id': 'Q9NRF2'
              }
            ],
            'symbol': 'SH2B1'
          }
        ],
        'start': 28880342,
        'transcripts': [
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000458097'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000563591.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.8300452488687784,
              'Adipose - Visceral (Omentum)': 0.6073752310536057,
              'Adrenal Gland': 1.1437596899224807,
              'Artery - Aorta': 1.0049768518518523,
              'Artery - Coronary': 0.8854583333333336,
              'Artery - Tibial': 1.037647058823531,
              'Bladder': 0.9538095238095239,
              'Brain - Amygdala': 0.8138157894736843,
              'Brain - Anterior cingulate cortex (BA24)': 1.113125,
              'Brain - Caudate (basal ganglia)': 0.9294715447154479,
              'Brain - Cerebellar Hemisphere': 2.6804651162790716,
              'Brain - Cerebellum': 2.7839834024896244,
              'Brain - Cortex': 1.4518823529411777,
              'Brain - Frontal Cortex (BA9)': 1.3263157894736841,
              'Brain - Hippocampus': 0.7954314720812179,
              'Brain - Hypothalamus': 0.8999999999999997,
              'Brain - Nucleus accumbens (basal ganglia)': 1.1328455284552845,
              'Brain - Putamen (basal ganglia)': 0.7872195121951224,
              'Brain - Spinal cord (cervical c-1)': 0.8988679245283017,
              'Brain - Substantia nigra': 0.7542446043165472,
              'Breast - Mammary Tissue': 0.8714379084967318,
              'Cells - Cultured fibroblasts': 1.0603769841269846,
              'Cells - EBV-transformed lymphocytes': 0.3686206896551725,
              'Cervix - Ectocervix': 1.2144444444444447,
              'Cervix - Endocervix': 1.6149999999999998,
              'Colon - Sigmoid': 0.9703753351206429,
              'Colon - Transverse': 0.8215270935960586,
              'Esophagus - Gastroesophageal Junction': 0.9627199999999998,
              'Esophagus - Mucosa': 0.5300900900900906,
              'Esophagus - Muscularis': 0.9857087378640782,
              'Fallopian Tube': 1.2655555555555553,
              'Heart - Atrial Appendage': 0.5582051282051279,
              'Heart - Left Ventricle': 0.37671296296296325,
              'Kidney - Cortex': 0.6518823529411762,
              'Kidney - Medulla': 0.7275,
              'Liver': 0.19300884955752218,
              'Lung': 0.6256055363321803,
              'Minor Salivary Gland': 0.9265432098765435,
              'Muscle - Skeletal': 0.38691158156911587,
              'Nerve - Tibial': 1.3807592891760905,
              'Ovary': 1.6387222222222226,
              'Pancreas': 0.2939939024390244,
              'Pituitary': 1.548197879858656,
              'Prostate': 1.0349387755102042,
              'Skin - Not Sun Exposed (Suprapubic)': 0.61228476821192,
              'Skin - Sun Exposed (Lower leg)': 0.679557774607703,
              'Small Intestine - Terminal Ileum': 0.8308556149732628,
              'Spleen': 0.6998755186721994,
              'Stomach': 0.6096100278551528,
              'Testis': 0.8071745152354567,
              'Thyroid': 1.844578866768761,
              'Uterus': 1.6873239436619716,
              'Vagina': 0.9259615384615384,
              'Whole Blood': 0.06423841059602645,
              'ensembl_id': 'ENST00000563591'
            },
            'proteomicsDB_id': [
              '43203'
            ],
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28877415,
                  28877605
                ]
              ],
              'transcript_exon_region': [
                [
                  28857920,
                  28858148
                ],
                [
                  28874988,
                  28875075
                ],
                [
                  28877332,
                  28877605
                ]
              ],
              'utr5': [
                28857920,
                28877414
              ],
              'utr5_exon_region': [
                [
                  28857920,
                  28858148
                ],
                [
                  28874988,
                  28875075
                ],
                [
                  28877332,
                  28877414
                ]
              ]
            },
            'trans_end': 28877605,
            'trans_start': 28857920,
            'transcript_id': 'ENST00000563591',
            'uniprotKB_id': [
              'H3BVF6_HUMAN'
            ],
            'uniprotkb_ac': [
              'H3BVF6'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000455236'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000567536.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.07060331825037706,
              'Adipose - Visceral (Omentum)': 0.10695009242144166,
              'Adrenal Gland': 0.14782945736434108,
              'Artery - Aorta': 0.23134259259259254,
              'Artery - Coronary': 0.19054166666666675,
              'Artery - Tibial': 0.14250377073906495,
              'Bladder': 0.09809523809523812,
              'Brain - Amygdala': 0.07131578947368418,
              'Brain - Anterior cingulate cortex (BA24)': 0.10022727272727275,
              'Brain - Caudate (basal ganglia)': 0.09170731707317073,
              'Brain - Cerebellar Hemisphere': 0.18534883720930226,
              'Brain - Cerebellum': 0.22917012448132773,
              'Brain - Cortex': 0.10623529411764708,
              'Brain - Frontal Cortex (BA9)': 0.0969377990430622,
              'Brain - Hippocampus': 0.06441624365482233,
              'Brain - Hypothalamus': 0.060891089108910876,
              'Brain - Nucleus accumbens (basal ganglia)': 0.09707317073170736,
              'Brain - Putamen (basal ganglia)': 0.08897560975609761,
              'Brain - Spinal cord (cervical c-1)': 0.07962264150943398,
              'Brain - Substantia nigra': 0.04446043165467627,
              'Breast - Mammary Tissue': 0.08549019607843135,
              'Cells - Cultured fibroblasts': 0.22198412698412703,
              'Cells - EBV-transformed lymphocytes': 0.07206896551724139,
              'Cervix - Ectocervix': 0.10777777777777778,
              'Cervix - Endocervix': 0.133,
              'Colon - Sigmoid': 0.1367024128686328,
              'Colon - Transverse': 0.10455665024630542,
              'Esophagus - Gastroesophageal Junction': 0.12757333333333334,
              'Esophagus - Mucosa': 0.061189189189189204,
              'Esophagus - Muscularis': 0.14794174757281553,
              'Fallopian Tube': 0.4855555555555556,
              'Heart - Atrial Appendage': 0.0561072261072261,
              'Heart - Left Ventricle': 0.04326388888888886,
              'Kidney - Cortex': 0.13423529411764704,
              'Kidney - Medulla': 0.21000000000000002,
              'Liver': 0.07044247787610619,
              'Lung': 0.12143598615916955,
              'Minor Salivary Gland': 0.09598765432098766,
              'Muscle - Skeletal': 0.04206724782067249,
              'Nerve - Tibial': 0.16702746365105015,
              'Ovary': 0.1205555555555556,
              'Pancreas': 0.07798780487804882,
              'Pituitary': 0.242720848056537,
              'Prostate': 0.16979591836734692,
              'Skin - Not Sun Exposed (Suprapubic)': 0.03802980132450331,
              'Skin - Sun Exposed (Lower leg)': 0.03881597717546362,
              'Small Intestine - Terminal Ileum': 0.12368983957219257,
              'Spleen': 0.10473029045643156,
              'Stomach': 0.09495821727019492,
              'Testis': 0.08811634349030467,
              'Thyroid': 0.2943338437978563,
              'Uterus': 0.21147887323943665,
              'Vagina': 0.14051282051282055,
              'Whole Blood': 0.013033112582781463,
              'ensembl_id': 'ENST00000567536'
            },
            'proteomicsDB_id': [
              '41443'
            ],
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28880556,
                  28880610
                ]
              ],
              'transcript_exon_region': [
                [
                  28857963,
                  28858148
                ],
                [
                  28872938,
                  28873068
                ],
                [
                  28874988,
                  28875075
                ],
                [
                  28880528,
                  28880610
                ]
              ],
              'utr5': [
                28857963,
                28880555
              ],
              'utr5_exon_region': [
                [
                  28857963,
                  28858148
                ],
                [
                  28872938,
                  28873068
                ],
                [
                  28874988,
                  28875075
                ],
                [
                  28880528,
                  28880555
                ]
              ]
            },
            'trans_end': 28880610,
            'trans_start': 28857963,
            'transcript_id': 'ENST00000567536',
            'uniprotKB_id': [
              'H3BPB4_HUMAN'
            ],
            'uniprotkb_ac': [
              'H3BPB4'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000321221',
              'ENSP00000481709'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000322610.8',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.5488687782805428,
              'Adipose - Visceral (Omentum)': 0.7612199630314235,
              'Adrenal Gland': 1.2582170542635653,
              'Artery - Aorta': 1.0970370370370366,
              'Artery - Coronary': 1.0847916666666668,
              'Artery - Tibial': 1.1332126696832574,
              'Bladder': 1.424761904761905,
              'Brain - Amygdala': 0.7646052631578947,
              'Brain - Anterior cingulate cortex (BA24)': 1.1879545454545462,
              'Brain - Caudate (basal ganglia)': 1.1955691056910573,
              'Brain - Cerebellar Hemisphere': 5.118465116279068,
              'Brain - Cerebellum': 5.689958506224066,
              'Brain - Cortex': 2.0142745098039216,
              'Brain - Frontal Cortex (BA9)': 1.7241148325358846,
              'Brain - Hippocampus': 0.7620812182741119,
              'Brain - Hypothalamus': 1.088168316831683,
              'Brain - Nucleus accumbens (basal ganglia)': 1.4210975609756096,
              'Brain - Putamen (basal ganglia)': 0.8222926829268292,
              'Brain - Spinal cord (cervical c-1)': 0.5446540880503143,
              'Brain - Substantia nigra': 0.5876258992805757,
              'Breast - Mammary Tissue': 0.6972113289760357,
              'Cells - Cultured fibroblasts': 1.1496825396825399,
              'Cells - EBV-transformed lymphocytes': 0.39913793103448275,
              'Cervix - Ectocervix': 1.1444444444444446,
              'Cervix - Endocervix': 1.278,
              'Colon - Sigmoid': 1.1430831099195713,
              'Colon - Transverse': 1.1458374384236452,
              'Esophagus - Gastroesophageal Junction': 1.0667466666666656,
              'Esophagus - Mucosa': 0.7403423423423429,
              'Esophagus - Muscularis': 1.1823883495145642,
              'Fallopian Tube': 1.2522222222222221,
              'Heart - Atrial Appendage': 0.49412587412587405,
              'Heart - Left Ventricle': 0.407083333333333,
              'Kidney - Cortex': 1.08235294117647,
              'Kidney - Medulla': 1.4,
              'Liver': 0.35424778761061954,
              'Lung': 0.8966782006920415,
              'Minor Salivary Gland': 0.9302469135802477,
              'Muscle - Skeletal': 0.37570361145703574,
              'Nerve - Tibial': 0.9361066235864299,
              'Ovary': 1.1261666666666665,
              'Pancreas': 0.41323170731707315,
              'Pituitary': 2.7202826855123674,
              'Prostate': 1.2046938775510214,
              'Skin - Not Sun Exposed (Suprapubic)': 0.5589735099337745,
              'Skin - Sun Exposed (Lower leg)': 0.5464764621968614,
              'Small Intestine - Terminal Ileum': 0.8734759358288771,
              'Spleen': 0.8292531120331955,
              'Stomach': 0.8375208913649019,
              'Testis': 1.046454293628809,
              'Thyroid': 2.1134456355283313,
              'Uterus': 1.4621126760563372,
              'Vagina': 0.9142307692307693,
              'Whole Blood': 0.08607947019867546,
              'ensembl_id': 'ENST00000322610'
            },
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28877415,
                  28878354
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884026
                ],
                [
                  28884767,
                  28885141
                ]
              ],
              'transcript_exon_region': [
                [
                  28858009,
                  28858148
                ],
                [
                  28872938,
                  28873068
                ],
                [
                  28874988,
                  28875075
                ],
                [
                  28877332,
                  28878354
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884026
                ],
                [
                  28884767,
                  28885526
                ]
              ],
              'utr3': [
                28885142,
                28885526
              ],
              'utr3_exon_region': [
                [
                  28885142,
                  28885526
                ]
              ],
              'utr5': [
                28858009,
                28877414
              ],
              'utr5_exon_region': [
                [
                  28858009,
                  28858148
                ],
                [
                  28872938,
                  28873068
                ],
                [
                  28874988,
                  28875075
                ],
                [
                  28877332,
                  28877414
                ]
              ]
            },
            'trans_end': 28885526,
            'trans_start': 28858009,
            'transcript_id': 'ENST00000322610',
            'uniprotkb_ac': [
              'Q9NRF2-1'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000337163',
              'ENSP00000378903'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000337120.5',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 3.3283710407239773,
              'Adipose - Visceral (Omentum)': 2.8888539741219974,
              'Adrenal Gland': 6.624806201550393,
              'Artery - Aorta': 3.841898148148144,
              'Artery - Coronary': 4.209291666666667,
              'Artery - Tibial': 2.6452639517345395,
              'Bladder': 4.229523809523809,
              'Brain - Amygdala': 1.7475657894736838,
              'Brain - Anterior cingulate cortex (BA24)': 2.519999999999999,
              'Brain - Caudate (basal ganglia)': 2.4626422764227636,
              'Brain - Cerebellar Hemisphere': 11.054465116279076,
              'Brain - Cerebellum': 13.813319502074695,
              'Brain - Cortex': 4.483333333333335,
              'Brain - Frontal Cortex (BA9)': 3.483779904306219,
              'Brain - Hippocampus': 1.8206598984771571,
              'Brain - Hypothalamus': 2.683663366336633,
              'Brain - Nucleus accumbens (basal ganglia)': 2.812764227642275,
              'Brain - Putamen (basal ganglia)': 1.8560975609756099,
              'Brain - Spinal cord (cervical c-1)': 1.793459119496854,
              'Brain - Substantia nigra': 1.627697841726619,
              'Breast - Mammary Tissue': 3.7495206971677564,
              'Cells - Cultured fibroblasts': 3.8446230158730144,
              'Cells - EBV-transformed lymphocytes': 4.38155172413793,
              'Cervix - Ectocervix': 4.86888888888889,
              'Cervix - Endocervix': 7.245,
              'Colon - Sigmoid': 5.3410991957104565,
              'Colon - Transverse': 6.396157635467978,
              'Esophagus - Gastroesophageal Junction': 5.284639999999997,
              'Esophagus - Mucosa': 3.850972972972971,
              'Esophagus - Muscularis': 5.053728155339806,
              'Fallopian Tube': 6.816666666666667,
              'Heart - Atrial Appendage': 2.0596503496503518,
              'Heart - Left Ventricle': 1.9240740740740747,
              'Kidney - Cortex': 4.4701176470588235,
              'Kidney - Medulla': 8.3675,
              'Liver': 2.1061504424778765,
              'Lung': 4.842335640138409,
              'Minor Salivary Gland': 5.4498148148148156,
              'Muscle - Skeletal': 1.6045579078455785,
              'Nerve - Tibial': 5.226478190630049,
              'Ovary': 6.240055555555557,
              'Pancreas': 2.9311890243902434,
              'Pituitary': 12.38579505300355,
              'Prostate': 7.287551020408163,
              'Skin - Not Sun Exposed (Suprapubic)': 2.946970198675497,
              'Skin - Sun Exposed (Lower leg)': 3.2830813124108422,
              'Small Intestine - Terminal Ileum': 8.804278074866312,
              'Spleen': 9.785850622406636,
              'Stomach': 4.6054874651810636,
              'Testis': 9.415872576177286,
              'Thyroid': 11.95220520673813,
              'Uterus': 7.6437323943661974,
              'Vagina': 4.411089743589743,
              'Whole Blood': 1.156675496688742,
              'ensembl_id': 'ENST00000337120'
            },
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28877415,
                  28878354
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884026
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28884786
                ]
              ],
              'transcript_exon_region': [
                [
                  28874124,
                  28878354
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884026
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28885522
                ]
              ],
              'utr3': [
                28884787,
                28885522
              ],
              'utr3_exon_region': [
                [
                  28884787,
                  28885522
                ]
              ],
              'utr5': [
                28874124,
                28877414
              ],
              'utr5_exon_region': [
                [
                  28874124,
                  28877414
                ]
              ]
            },
            'trans_end': 28885522,
            'trans_start': 28874124,
            'transcript_id': 'ENST00000337120',
            'uniprotkb_ac': [
              'Q9NRF2-2'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000457214'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000566209.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.017873303167420817,
              'Adipose - Visceral (Omentum)': 0.02207024029574861,
              'Adrenal Gland': 0.02248062015503876,
              'Artery - Aorta': 0.02150462962962963,
              'Artery - Coronary': 0.02858333333333334,
              'Artery - Tibial': 0.04901960784313727,
              'Bladder': 0.030952380952380953,
              'Brain - Amygdala': 0.004078947368421053,
              'Brain - Anterior cingulate cortex (BA24)': 0.0076704545454545445,
              'Brain - Caudate (basal ganglia)': 0.003983739837398374,
              'Brain - Cerebellar Hemisphere': 0.05344186046511627,
              'Brain - Cerebellum': 0.06854771784232366,
              'Brain - Cortex': 0.01231372549019608,
              'Brain - Frontal Cortex (BA9)': 0.013205741626794259,
              'Brain - Hippocampus': 0.004467005076142131,
              'Brain - Hypothalamus': 0.005148514851485149,
              'Brain - Nucleus accumbens (basal ganglia)': 0.003536585365853658,
              'Brain - Putamen (basal ganglia)': 0.007951219512195122,
              'Brain - Spinal cord (cervical c-1)': 0.004402515723270441,
              'Brain - Substantia nigra': 0.014100719424460433,
              'Breast - Mammary Tissue': 0.0199128540305011,
              'Cells - Cultured fibroblasts': 0.008095238095238095,
              'Cells - EBV-transformed lymphocytes': 0.011609195402298851,
              'Cervix - Ectocervix': 0.021111111111111112,
              'Cervix - Endocervix': 0.037,
              'Colon - Sigmoid': 0.01005361930294906,
              'Colon - Transverse': 0.011724137931034485,
              'Esophagus - Gastroesophageal Junction': 0.015466666666666668,
              'Esophagus - Mucosa': 0.010918918918918918,
              'Esophagus - Muscularis': 0.01722330097087379,
              'Fallopian Tube': 0.022222222222222223,
              'Heart - Atrial Appendage': 0.011538461538461539,
              'Heart - Left Ventricle': 0.004837962962962964,
              'Kidney - Cortex': 0.009647058823529413,
              'Kidney - Medulla': 0.0575,
              'Liver': 0.0034070796460176993,
              'Lung': 0.020051903114186854,
              'Minor Salivary Gland': 0.02030864197530864,
              'Muscle - Skeletal': 0.023760896637608966,
              'Nerve - Tibial': 0.016688206785137317,
              'Ovary': 0.018833333333333334,
              'Pancreas': 0.0021341463414634144,
              'Pituitary': 0.02519434628975265,
              'Prostate': 0.01420408163265306,
              'Skin - Not Sun Exposed (Suprapubic)': 0.012069536423841062,
              'Skin - Sun Exposed (Lower leg)': 0.022881597717546363,
              'Small Intestine - Terminal Ileum': 0.0193048128342246,
              'Spleen': 0.01759336099585062,
              'Stomach': 0.010306406685236769,
              'Testis': 0.01883656509695291,
              'Thyroid': 0.026830015313935685,
              'Uterus': 0.01063380281690141,
              'Vagina': 0.00923076923076923,
              'Whole Blood': 0.0058145695364238414,
              'ensembl_id': 'ENST00000566209'
            },
            'proteomicsDB_id': [
              '42667'
            ],
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28877415,
                  28877585
                ]
              ],
              'transcript_exon_region': [
                [
                  28874350,
                  28874487
                ],
                [
                  28874610,
                  28874666
                ],
                [
                  28874988,
                  28875075
                ],
                [
                  28877332,
                  28877585
                ]
              ],
              'utr5': [
                28874350,
                28877414
              ],
              'utr5_exon_region': [
                [
                  28874350,
                  28874487
                ],
                [
                  28874610,
                  28874666
                ],
                [
                  28874988,
                  28875075
                ],
                [
                  28877332,
                  28877414
                ]
              ]
            },
            'trans_end': 28877585,
            'trans_start': 28874350,
            'transcript_id': 'ENST00000566209',
            'uniprotKB_id': [
              'H3BTK4_HUMAN'
            ],
            'uniprotkb_ac': [
              'H3BTK4'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000440354'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000545570.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.15485671191553554,
              'Adipose - Visceral (Omentum)': 0.09744916820702394,
              'Adrenal Gland': 0.14054263565891478,
              'Artery - Aorta': 0.21250000000000013,
              'Artery - Coronary': 0.14120833333333335,
              'Artery - Tibial': 0.23079939668174965,
              'Bladder': 0.13428571428571429,
              'Brain - Amygdala': 0.013421052631578948,
              'Brain - Anterior cingulate cortex (BA24)': 0.02107954545454545,
              'Brain - Caudate (basal ganglia)': 0.01585365853658537,
              'Brain - Cerebellar Hemisphere': 0.037674418604651164,
              'Brain - Cerebellum': 0.07950207468879669,
              'Brain - Cortex': 0.02670588235294118,
              'Brain - Frontal Cortex (BA9)': 0.03215311004784689,
              'Brain - Hippocampus': 0.01573604060913706,
              'Brain - Hypothalamus': 0.020495049504950492,
              'Brain - Nucleus accumbens (basal ganglia)': 0.013861788617886181,
              'Brain - Putamen (basal ganglia)': 0.01175609756097561,
              'Brain - Spinal cord (cervical c-1)': 0.018113207547169812,
              'Brain - Substantia nigra': 0.01287769784172662,
              'Breast - Mammary Tissue': 0.1400217864923747,
              'Cells - Cultured fibroblasts': 0.23452380952380955,
              'Cells - EBV-transformed lymphocytes': 0.21850574712643683,
              'Cervix - Ectocervix': 0.10444444444444445,
              'Cervix - Endocervix': 0.05,
              'Colon - Sigmoid': 0.12747989276139413,
              'Colon - Transverse': 0.18266009852216747,
              'Esophagus - Gastroesophageal Junction': 0.10698666666666658,
              'Esophagus - Mucosa': 0.15495495495495484,
              'Esophagus - Muscularis': 0.11611650485436897,
              'Fallopian Tube': 0.09222222222222223,
              'Heart - Atrial Appendage': 0.03822843822843822,
              'Heart - Left Ventricle': 0.031134259259259257,
              'Kidney - Cortex': 0.07823529411764707,
              'Kidney - Medulla': 0.0625,
              'Liver': 0.04836283185840708,
              'Lung': 0.18114186851211067,
              'Minor Salivary Gland': 0.21351851851851844,
              'Muscle - Skeletal': 0.08019925280199251,
              'Nerve - Tibial': 0.10922455573505654,
              'Ovary': 0.08133333333333334,
              'Pancreas': 0.044969512195121956,
              'Pituitary': 0.07975265017667846,
              'Prostate': 0.12412244897959179,
              'Skin - Not Sun Exposed (Suprapubic)': 0.2060099337748343,
              'Skin - Sun Exposed (Lower leg)': 0.2210699001426536,
              'Small Intestine - Terminal Ileum': 0.27326203208556143,
              'Spleen': 0.1879253112033194,
              'Stomach': 0.1354038997214485,
              'Testis': 0.1603324099722992,
              'Thyroid': 0.15534456355283308,
              'Uterus': 0.15985915492957747,
              'Vagina': 0.16551282051282046,
              'Whole Blood': 0.09309933774834434,
              'ensembl_id': 'ENST00000545570'
            },
            'proteomicsDB_id': [
              '24530'
            ],
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28875066,
                  28875075
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884079
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28884769
                ]
              ],
              'transcript_exon_region': [
                [
                  28874879,
                  28875075
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884079
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28884948
                ]
              ],
              'utr3': [
                28884770,
                28884948
              ],
              'utr3_exon_region': [
                [
                  28884770,
                  28884948
                ]
              ],
              'utr5': [
                28874879,
                28875065
              ],
              'utr5_exon_region': [
                [
                  28874879,
                  28875065
                ]
              ]
            },
            'trans_end': 28884948,
            'trans_start': 28874879,
            'transcript_id': 'ENST00000545570',
            'uniprotKB_id': [
              'F5GXU7_HUMAN'
            ],
            'uniprotkb_ac': [
              'F5GXU7'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000352232'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000359285.5',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 14.366983408748105,
              'Adipose - Visceral (Omentum)': 12.531330868761541,
              'Adrenal Gland': 15.114341085271318,
              'Artery - Aorta': 20.515324074074076,
              'Artery - Coronary': 18.043958333333308,
              'Artery - Tibial': 20.202171945701362,
              'Bladder': 21.683333333333334,
              'Brain - Amygdala': 8.2878947368421,
              'Brain - Anterior cingulate cortex (BA24)': 8.249034090909097,
              'Brain - Caudate (basal ganglia)': 8.395243902439026,
              'Brain - Cerebellar Hemisphere': 18.542976744186046,
              'Brain - Cerebellum': 19.80780082987552,
              'Brain - Cortex': 10.90164705882353,
              'Brain - Frontal Cortex (BA9)': 9.85095693779904,
              'Brain - Hippocampus': 9.153756345177666,
              'Brain - Hypothalamus': 8.545346534653465,
              'Brain - Nucleus accumbens (basal ganglia)': 7.60105691056911,
              'Brain - Putamen (basal ganglia)': 7.588975609756092,
              'Brain - Spinal cord (cervical c-1)': 14.962641509433961,
              'Brain - Substantia nigra': 10.112158273381294,
              'Breast - Mammary Tissue': 16.371895424836598,
              'Cells - Cultured fibroblasts': 12.91083333333333,
              'Cells - EBV-transformed lymphocytes': 9.616551724137933,
              'Cervix - Ectocervix': 25.99111111111111,
              'Cervix - Endocervix': 31.863000000000007,
              'Colon - Sigmoid': 22.481689008042906,
              'Colon - Transverse': 20.925123152709364,
              'Esophagus - Gastroesophageal Junction': 19.886133333333337,
              'Esophagus - Mucosa': 12.58034234234235,
              'Esophagus - Muscularis': 18.95780582524274,
              'Fallopian Tube': 27.563333333333333,
              'Heart - Atrial Appendage': 10.690466200466199,
              'Heart - Left Ventricle': 8.531851851851847,
              'Kidney - Cortex': 16.616941176470586,
              'Kidney - Medulla': 22.732499999999998,
              'Liver': 6.057654867256641,
              'Lung': 15.701470588235289,
              'Minor Salivary Gland': 17.302283950617287,
              'Muscle - Skeletal': 12.894483188044834,
              'Nerve - Tibial': 24.611502423263335,
              'Ovary': 31.17222222222223,
              'Pancreas': 7.614573170731704,
              'Pituitary': 26.088657243816243,
              'Prostate': 24.661959183673464,
              'Skin - Not Sun Exposed (Suprapubic)': 14.792466887417218,
              'Skin - Sun Exposed (Lower leg)': 15.019486447931518,
              'Small Intestine - Terminal Ileum': 21.8492513368984,
              'Spleen': 24.734149377593365,
              'Stomach': 13.071086350974928,
              'Testis': 24.362326869806097,
              'Thyroid': 32.27644716692189,
              'Uterus': 31.786830985915476,
              'Vagina': 20.175384615384615,
              'Whole Blood': 3.960741721854302,
              'ensembl_id': 'ENST00000359285'
            },
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28877415,
                  28878354
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884079
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28884769
                ]
              ],
              'transcript_exon_region': [
                [
                  28875125,
                  28875266
                ],
                [
                  28877332,
                  28878354
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884079
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28885526
                ]
              ],
              'utr3': [
                28884770,
                28885526
              ],
              'utr3_exon_region': [
                [
                  28884770,
                  28885526
                ]
              ],
              'utr5': [
                28875125,
                28877414
              ],
              'utr5_exon_region': [
                [
                  28875125,
                  28875266
                ],
                [
                  28877332,
                  28877414
                ]
              ]
            },
            'trans_end': 28885526,
            'trans_start': 28875125,
            'transcript_id': 'ENST00000359285',
            'uniprotkb_ac': [
              'Q9NRF2-3'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000438784'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000538342.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 10.942986425339361,
              'Adipose - Visceral (Omentum)': 9.390369685767096,
              'Adrenal Gland': 13.547054263565895,
              'Artery - Aorta': 13.525810185185197,
              'Artery - Coronary': 11.800666666666665,
              'Artery - Tibial': 14.193725490196071,
              'Bladder': 14.10809523809524,
              'Brain - Amygdala': 5.495526315789475,
              'Brain - Anterior cingulate cortex (BA24)': 5.064715909090906,
              'Brain - Caudate (basal ganglia)': 5.635040650406502,
              'Brain - Cerebellar Hemisphere': 6.504325581395354,
              'Brain - Cerebellum': 5.910331950207468,
              'Brain - Cortex': 6.0100784313725475,
              'Brain - Frontal Cortex (BA9)': 5.380143540669858,
              'Brain - Hippocampus': 5.431522842639591,
              'Brain - Hypothalamus': 4.941584158415841,
              'Brain - Nucleus accumbens (basal ganglia)': 5.274349593495938,
              'Brain - Putamen (basal ganglia)': 5.266439024390246,
              'Brain - Spinal cord (cervical c-1)': 6.558553459119498,
              'Brain - Substantia nigra': 5.939568345323737,
              'Breast - Mammary Tissue': 11.75211328976035,
              'Cells - Cultured fibroblasts': 9.336825396825391,
              'Cells - EBV-transformed lymphocytes': 5.338218390804598,
              'Cervix - Ectocervix': 16.49111111111111,
              'Cervix - Endocervix': 18.563000000000002,
              'Colon - Sigmoid': 15.436246648793551,
              'Colon - Transverse': 13.548546798029536,
              'Esophagus - Gastroesophageal Junction': 13.49882666666667,
              'Esophagus - Mucosa': 8.205387387387402,
              'Esophagus - Muscularis': 12.800718446601945,
              'Fallopian Tube': 17.768888888888892,
              'Heart - Atrial Appendage': 6.84062937062937,
              'Heart - Left Ventricle': 4.946527777777776,
              'Kidney - Cortex': 10.816705882352945,
              'Kidney - Medulla': 9.985,
              'Liver': 4.58048672566372,
              'Lung': 10.582301038062285,
              'Minor Salivary Gland': 12.350925925925925,
              'Muscle - Skeletal': 5.486936488169374,
              'Nerve - Tibial': 15.550904684975759,
              'Ovary': 18.211222222222222,
              'Pancreas': 5.686676829268292,
              'Pituitary': 19.58572438162544,
              'Prostate': 15.792489795918371,
              'Skin - Not Sun Exposed (Suprapubic)': 10.071258278145699,
              'Skin - Sun Exposed (Lower leg)': 10.336904422253923,
              'Small Intestine - Terminal Ileum': 12.347754010695182,
              'Spleen': 14.091369294605801,
              'Stomach': 10.025598885793872,
              'Testis': 18.721662049861482,
              'Thyroid': 22.475895865237376,
              'Uterus': 19.63133802816903,
              'Vagina': 13.156794871794869,
              'Whole Blood': 3.056198675496688,
              'ensembl_id': 'ENST00000538342'
            },
            'proteomicsDB_id': [
              '4546'
            ],
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28878720,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884026
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28884786
                ]
              ],
              'transcript_exon_region': [
                [
                  28875126,
                  28875266
                ],
                [
                  28878694,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884026
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28885144
                ]
              ],
              'utr3': [
                28884787,
                28885144
              ],
              'utr3_exon_region': [
                [
                  28884787,
                  28885144
                ]
              ],
              'utr5': [
                28875126,
                28878719
              ],
              'utr5_exon_region': [
                [
                  28875126,
                  28875266
                ],
                [
                  28878694,
                  28878719
                ]
              ]
            },
            'trans_end': 28885144,
            'trans_start': 28875126,
            'transcript_id': 'ENST00000538342',
            'uniprotKB_id': [
              'B4DLN5_HUMAN'
            ],
            'uniprotkb_ac': [
              'B4DLN5'
            ]
          },
          {
            'chr': '16',
            'entrez_id': '25970',
            'gencode_id': 'ENST00000563674.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 2.8402111613876317,
              'Adipose - Visceral (Omentum)': 3.0421626617375246,
              'Adrenal Gland': 4.701124031007749,
              'Artery - Aorta': 3.2776157407407394,
              'Artery - Coronary': 3.7444166666666647,
              'Artery - Tibial': 2.253936651583708,
              'Bladder': 4.624285714285714,
              'Brain - Amygdala': 1.3159868421052632,
              'Brain - Anterior cingulate cortex (BA24)': 1.374943181818182,
              'Brain - Caudate (basal ganglia)': 1.6915040650406499,
              'Brain - Cerebellar Hemisphere': 6.874372093023262,
              'Brain - Cerebellum': 8.208257261410786,
              'Brain - Cortex': 2.2338039215686285,
              'Brain - Frontal Cortex (BA9)': 1.5851196172248807,
              'Brain - Hippocampus': 1.6064974619289327,
              'Brain - Hypothalamus': 1.46608910891089,
              'Brain - Nucleus accumbens (basal ganglia)': 1.600203252032519,
              'Brain - Putamen (basal ganglia)': 1.4539999999999997,
              'Brain - Spinal cord (cervical c-1)': 1.7666037735849063,
              'Brain - Substantia nigra': 1.4664748201438855,
              'Breast - Mammary Tissue': 3.4682135076252747,
              'Cells - Cultured fibroblasts': 2.8680357142857122,
              'Cells - EBV-transformed lymphocytes': 3.046034482758617,
              'Cervix - Ectocervix': 5.858888888888889,
              'Cervix - Endocervix': 6.872999999999999,
              'Colon - Sigmoid': 5.008927613941021,
              'Colon - Transverse': 6.480221674876847,
              'Esophagus - Gastroesophageal Junction': 4.228533333333333,
              'Esophagus - Mucosa': 4.577693693693697,
              'Esophagus - Muscularis': 4.004718446601942,
              'Fallopian Tube': 5.695555555555556,
              'Heart - Atrial Appendage': 2.0300932400932425,
              'Heart - Left Ventricle': 1.8473842592592589,
              'Kidney - Cortex': 5.050941176470587,
              'Kidney - Medulla': 6.8825,
              'Liver': 3.339690265486727,
              'Lung': 4.42169550173011,
              'Minor Salivary Gland': 5.046172839506173,
              'Muscle - Skeletal': 0.980834371108344,
              'Nerve - Tibial': 5.443037156704359,
              'Ovary': 7.714944444444446,
              'Pancreas': 2.476493902439023,
              'Pituitary': 7.995159010600709,
              'Prostate': 7.562612244897955,
              'Skin - Not Sun Exposed (Suprapubic)': 2.663625827814567,
              'Skin - Sun Exposed (Lower leg)': 2.6014978601997165,
              'Small Intestine - Terminal Ileum': 7.0094652406417115,
              'Spleen': 9.052406639004149,
              'Stomach': 3.5354317548746512,
              'Testis': 6.666094182825482,
              'Thyroid': 9.636294027565095,
              'Uterus': 7.114084507042253,
              'Vagina': 5.5702564102564125,
              'Whole Blood': 1.0758807947019877,
              'ensembl_id': 'ENST00000563674'
            },
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'transcript_exon_region': [
                [
                  28875198,
                  28875266
                ],
                [
                  28884248,
                  28884590
                ],
                [
                  28884767,
                  28885076
                ]
              ],
              'utr3': [
                28875199,
                28885076
              ],
              'utr3_exon_region': [
                [
                  28875198,
                  28875266
                ],
                [
                  28884248,
                  28884590
                ],
                [
                  28884767,
                  28885076
                ]
              ]
            },
            'trans_end': 28885076,
            'trans_start': 28875198,
            'transcript_id': 'ENST00000563674'
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000337163',
              'ENSP00000378903'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000395532.4',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.13829562594268469,
              'Adipose - Visceral (Omentum)': 0.04269870609981515,
              'Adrenal Gland': 0.025852713178294583,
              'Artery - Aorta': 0.332824074074074,
              'Artery - Coronary': 0.15587499999999999,
              'Artery - Tibial': 0.6964102564102563,
              'Bladder': 0.5700000000000001,
              'Brain - Amygdala': 0.03210526315789474,
              'Brain - Anterior cingulate cortex (BA24)': 0.06494318181818182,
              'Brain - Caudate (basal ganglia)': 0.06032520325203253,
              'Brain - Cerebellar Hemisphere': 0.5641860465116281,
              'Brain - Cerebellum': 0.3530705394190871,
              'Brain - Cortex': 0.08368627450980394,
              'Brain - Frontal Cortex (BA9)': 0.10244019138755985,
              'Brain - Hippocampus': 0.04086294416243654,
              'Brain - Hypothalamus': 0.06163366336633664,
              'Brain - Nucleus accumbens (basal ganglia)': 0.09463414634146344,
              'Brain - Putamen (basal ganglia)': 0.058829268292682924,
              'Brain - Spinal cord (cervical c-1)': 0.047672955974842765,
              'Brain - Substantia nigra': 0.02287769784172662,
              'Breast - Mammary Tissue': 0.12786492374727662,
              'Cells - Cultured fibroblasts': 0.028750000000000005,
              'Cells - EBV-transformed lymphocytes': 0.056206896551724124,
              'Cervix - Ectocervix': 0.17,
              'Cervix - Endocervix': 0.15000000000000002,
              'Colon - Sigmoid': 0.34764075067024125,
              'Colon - Transverse': 0.12509852216748765,
              'Esophagus - Gastroesophageal Junction': 0.24338666666666667,
              'Esophagus - Mucosa': 0.030072072072072076,
              'Esophagus - Muscularis': 0.2820970873786408,
              'Fallopian Tube': 0.2588888888888889,
              'Heart - Atrial Appendage': 0.0294871794871795,
              'Heart - Left Ventricle': 0.017083333333333336,
              'Kidney - Cortex': 0.02188235294117647,
              'Kidney - Medulla': 0.045,
              'Liver': 0.010619469026548674,
              'Lung': 0.19169550173010377,
              'Minor Salivary Gland': 0.12351851851851856,
              'Muscle - Skeletal': 0.09267745952677463,
              'Nerve - Tibial': 0.6760904684975776,
              'Ovary': 0.26649999999999996,
              'Pancreas': 0.016524390243902433,
              'Pituitary': 0.13307420494699654,
              'Prostate': 0.17216326530612247,
              'Skin - Not Sun Exposed (Suprapubic)': 0.27807947019867557,
              'Skin - Sun Exposed (Lower leg)': 0.41057061340941503,
              'Small Intestine - Terminal Ileum': 0.07860962566844919,
              'Spleen': 0.040746887966804986,
              'Stomach': 0.0937325905292479,
              'Testis': 0.14698060941828256,
              'Thyroid': 0.32854517611026035,
              'Uterus': 0.42922535211267615,
              'Vagina': 0.12666666666666662,
              'Whole Blood': 0.0056556291390728475,
              'ensembl_id': 'ENST00000395532'
            },
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28877415,
                  28878354
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884026
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28884786
                ]
              ],
              'transcript_exon_region': [
                [
                  28875295,
                  28875583
                ],
                [
                  28877332,
                  28878354
                ],
                [
                  28878651,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883304
                ],
                [
                  28883510,
                  28883722
                ],
                [
                  28883854,
                  28884026
                ],
                [
                  28884490,
                  28884590
                ],
                [
                  28884767,
                  28884928
                ]
              ],
              'utr3': [
                28884787,
                28884928
              ],
              'utr3_exon_region': [
                [
                  28884787,
                  28884928
                ]
              ],
              'utr5': [
                28875295,
                28877414
              ],
              'utr5_exon_region': [
                [
                  28875295,
                  28875583
                ],
                [
                  28877332,
                  28877414
                ]
              ]
            },
            'trans_end': 28884928,
            'trans_start': 28875295,
            'transcript_id': 'ENST00000395532',
            'uniprotkb_ac': [
              'Q9NRF2-2'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000455534'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000566176.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.034509803921568646,
              'Adipose - Visceral (Omentum)': 0.030036968576709802,
              'Adrenal Gland': 0.031007751937984496,
              'Artery - Aorta': 0.04435185185185186,
              'Artery - Coronary': 0.04779166666666666,
              'Artery - Tibial': 0.060829562594268485,
              'Bladder': 0.011428571428571429,
              'Brain - Amygdala': 0.021973684210526315,
              'Brain - Anterior cingulate cortex (BA24)': 0.036761363636363634,
              'Brain - Caudate (basal ganglia)': 0.02272357723577236,
              'Brain - Cerebellar Hemisphere': 0.1486046511627907,
              'Brain - Cerebellum': 0.22983402489626553,
              'Brain - Cortex': 0.06101960784313726,
              'Brain - Frontal Cortex (BA9)': 0.14196172248803826,
              'Brain - Hippocampus': 0.019746192893401016,
              'Brain - Hypothalamus': 0.03920792079207921,
              'Brain - Nucleus accumbens (basal ganglia)': 0.0117479674796748,
              'Brain - Putamen (basal ganglia)': 0.01526829268292683,
              'Brain - Spinal cord (cervical c-1)': 0.015597484276729558,
              'Brain - Substantia nigra': 0.002517985611510791,
              'Breast - Mammary Tissue': 0.03538126361655774,
              'Cells - Cultured fibroblasts': 0.02015873015873016,
              'Cells - EBV-transformed lymphocytes': 0.010919540229885057,
              'Cervix - Ectocervix': 0,
              'Cervix - Endocervix': 0.079,
              'Colon - Sigmoid': 0.025013404825737266,
              'Colon - Transverse': 0.02507389162561577,
              'Esophagus - Gastroesophageal Junction': 0.0368,
              'Esophagus - Mucosa': 0.013063063063063063,
              'Esophagus - Muscularis': 0.032679611650485434,
              'Fallopian Tube': 0.06666666666666667,
              'Heart - Atrial Appendage': 0.009790209790209791,
              'Heart - Left Ventricle': 0.017245370370370373,
              'Kidney - Cortex': 0.035176470588235295,
              'Kidney - Medulla': 0,
              'Liver': 0.007079646017699116,
              'Lung': 0.0347923875432526,
              'Minor Salivary Gland': 0.024814814814814814,
              'Muscle - Skeletal': 0.026674968866749686,
              'Nerve - Tibial': 0.05546042003231017,
              'Ovary': 0.038888888888888876,
              'Pancreas': 0.010152439024390244,
              'Pituitary': 0.04045936395759717,
              'Prostate': 0.026122448979591834,
              'Skin - Not Sun Exposed (Suprapubic)': 0.02355960264900662,
              'Skin - Sun Exposed (Lower leg)': 0.024935805991440803,
              'Small Intestine - Terminal Ileum': 0.013957219251336897,
              'Spleen': 0.03049792531120332,
              'Stomach': 0.021754874651810585,
              'Testis': 0.05326869806094182,
              'Thyroid': 0.060551301684532925,
              'Uterus': 0.024788732394366197,
              'Vagina': 0.01737179487179487,
              'Whole Blood': 0.005788079470198676,
              'ensembl_id': 'ENST00000566176'
            },
            'proteomicsDB_id': [
              '41642'
            ],
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28877955,
                  28877998
                ],
                [
                  28878694,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883276
                ]
              ],
              'transcript_exon_region': [
                [
                  28877955,
                  28877998
                ],
                [
                  28878694,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883276
                ]
              ]
            },
            'trans_end': 28883276,
            'trans_start': 28877955,
            'transcript_id': 'ENST00000566176',
            'uniprotKB_id': [
              'H3BPZ4_HUMAN'
            ],
            'uniprotkb_ac': [
              'H3BPZ4'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000454601'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000561629.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.5945098039215684,
              'Adipose - Visceral (Omentum)': 0.4773752310536043,
              'Adrenal Gland': 0.8820155038759683,
              'Artery - Aorta': 0.4954166666666668,
              'Artery - Coronary': 0.49441666666666656,
              'Artery - Tibial': 0.38015082956259405,
              'Bladder': 0.3976190476190477,
              'Brain - Amygdala': 0.14401315789473682,
              'Brain - Anterior cingulate cortex (BA24)': 0.2202272727272727,
              'Brain - Caudate (basal ganglia)': 0.22154471544715448,
              'Brain - Cerebellar Hemisphere': 1.205906976744186,
              'Brain - Cerebellum': 1.6298340248962655,
              'Brain - Cortex': 0.43588235294117655,
              'Brain - Frontal Cortex (BA9)': 0.3402870813397129,
              'Brain - Hippocampus': 0.17081218274111679,
              'Brain - Hypothalamus': 0.22504950495049506,
              'Brain - Nucleus accumbens (basal ganglia)': 0.25369918699187,
              'Brain - Putamen (basal ganglia)': 0.1657560975609756,
              'Brain - Spinal cord (cervical c-1)': 0.14031446540880496,
              'Brain - Substantia nigra': 0.1374820143884892,
              'Breast - Mammary Tissue': 0.5477124183006536,
              'Cells - Cultured fibroblasts': 0.7694246031746036,
              'Cells - EBV-transformed lymphocytes': 0.4090229885057473,
              'Cervix - Ectocervix': 1.0544444444444447,
              'Cervix - Endocervix': 1.073,
              'Colon - Sigmoid': 0.7142091152815006,
              'Colon - Transverse': 0.9571182266009853,
              'Esophagus - Gastroesophageal Junction': 0.6989333333333337,
              'Esophagus - Mucosa': 0.5693153153153152,
              'Esophagus - Muscularis': 0.6140970873786409,
              'Fallopian Tube': 0.9477777777777777,
              'Heart - Atrial Appendage': 0.25165501165501164,
              'Heart - Left Ventricle': 0.24502314814814816,
              'Kidney - Cortex': 0.5669411764705884,
              'Kidney - Medulla': 0.5425000000000001,
              'Liver': 0.3031858407079647,
              'Lung': 0.5310034602076124,
              'Minor Salivary Gland': 0.8559876543209879,
              'Muscle - Skeletal': 0.13787048567870488,
              'Nerve - Tibial': 0.7324394184168015,
              'Ovary': 1.106555555555555,
              'Pancreas': 0.38009146341463396,
              'Pituitary': 1.150353356890459,
              'Prostate': 0.9964489795918371,
              'Skin - Not Sun Exposed (Suprapubic)': 0.3714072847682116,
              'Skin - Sun Exposed (Lower leg)': 0.4532524964336662,
              'Small Intestine - Terminal Ileum': 1.0514438502673804,
              'Spleen': 1.1285062240663901,
              'Stomach': 0.5843732590529246,
              'Testis': 1.1380332409972291,
              'Thyroid': 1.3052833078101076,
              'Uterus': 1.2136619718309865,
              'Vagina': 0.7721794871794871,
              'Whole Blood': 0.16173509933774824,
              'ensembl_id': 'ENST00000561629'
            },
            'proteomicsDB_id': [
              '41040'
            ],
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28878720,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880597,
                  28880704
                ],
                [
                  28883100,
                  28883235
                ]
              ],
              'transcript_exon_region': [
                [
                  28878474,
                  28878753
                ],
                [
                  28880326,
                  28880418
                ],
                [
                  28880597,
                  28880704
                ],
                [
                  28883100,
                  28883235
                ]
              ],
              'utr5': [
                28878474,
                28878719
              ],
              'utr5_exon_region': [
                [
                  28878474,
                  28878719
                ]
              ]
            },
            'trans_end': 28883235,
            'trans_start': 28878474,
            'transcript_id': 'ENST00000561629',
            'uniprotKB_id': [
              'H3BMY3_HUMAN'
            ],
            'uniprotkb_ac': [
              'H3BMY3'
            ]
          },
          {
            'chr': '16',
            'entrez_id': '25970',
            'gencode_id': 'ENST00000569471.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.5688536953242836,
              'Adipose - Visceral (Omentum)': 0.6002218114602592,
              'Adrenal Gland': 1.0939147286821698,
              'Artery - Aorta': 0.5200231481481485,
              'Artery - Coronary': 0.6329583333333331,
              'Artery - Tibial': 0.3573604826546001,
              'Bladder': 0.5728571428571428,
              'Brain - Amygdala': 0.3360526315789474,
              'Brain - Anterior cingulate cortex (BA24)': 0.38312500000000005,
              'Brain - Caudate (basal ganglia)': 0.3971138211382113,
              'Brain - Cerebellar Hemisphere': 1.6256279069767439,
              'Brain - Cerebellum': 1.9991701244813274,
              'Brain - Cortex': 0.6541176470588237,
              'Brain - Frontal Cortex (BA9)': 0.5066028708133976,
              'Brain - Hippocampus': 0.34715736040609135,
              'Brain - Hypothalamus': 0.4123267326732671,
              'Brain - Nucleus accumbens (basal ganglia)': 0.4115040650406501,
              'Brain - Putamen (basal ganglia)': 0.3260975609756098,
              'Brain - Spinal cord (cervical c-1)': 0.3857861635220127,
              'Brain - Substantia nigra': 0.3679136690647482,
              'Breast - Mammary Tissue': 0.6311764705882348,
              'Cells - Cultured fibroblasts': 0.6592857142857149,
              'Cells - EBV-transformed lymphocytes': 0.9011494252873562,
              'Cervix - Ectocervix': 0.5655555555555556,
              'Cervix - Endocervix': 0.968,
              'Colon - Sigmoid': 0.7811796246648797,
              'Colon - Transverse': 1.4064039408867002,
              'Esophagus - Gastroesophageal Junction': 0.7476266666666666,
              'Esophagus - Mucosa': 0.876720720720721,
              'Esophagus - Muscularis': 0.6952815533980584,
              'Fallopian Tube': 1.0466666666666666,
              'Heart - Atrial Appendage': 0.3341958041958039,
              'Heart - Left Ventricle': 0.351388888888889,
              'Kidney - Cortex': 0.8214117647058826,
              'Kidney - Medulla': 1.2175,
              'Liver': 0.5357522123893805,
              'Lung': 0.828771626297578,
              'Minor Salivary Gland': 0.8912345679012351,
              'Muscle - Skeletal': 0.20100871731008702,
              'Nerve - Tibial': 0.6594184168012921,
              'Ovary': 1.0763333333333334,
              'Pancreas': 0.4751219512195124,
              'Pituitary': 1.4787985865724376,
              'Prostate': 1.063510204081632,
              'Skin - Not Sun Exposed (Suprapubic)': 0.4749668874172183,
              'Skin - Sun Exposed (Lower leg)': 0.3837232524964336,
              'Small Intestine - Terminal Ileum': 1.6366844919786083,
              'Spleen': 1.8592946058091304,
              'Stomach': 0.8161559888579394,
              'Testis': 1.4106371191135731,
              'Thyroid': 1.6313476263399687,
              'Uterus': 0.999718309859155,
              'Vagina': 0.6021153846153846,
              'Whole Blood': 0.2408609271523179,
              'ensembl_id': 'ENST00000569471'
            },
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'transcript_exon_region': [
                [
                  28880414,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883711
                ]
              ],
              'utr3': [
                28880415,
                28883711
              ],
              'utr3_exon_region': [
                [
                  28880414,
                  28880418
                ],
                [
                  28880528,
                  28880704
                ],
                [
                  28883100,
                  28883711
                ]
              ]
            },
            'trans_end': 28883711,
            'trans_start': 28880414,
            'transcript_id': 'ENST00000569471'
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000457724'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000569651.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 0.2634992458521873,
              'Adipose - Visceral (Omentum)': 0.233475046210721,
              'Adrenal Gland': 0.1375193798449613,
              'Artery - Aorta': 0.1535185185185185,
              'Artery - Coronary': 0.1744583333333333,
              'Artery - Tibial': 0.185505279034691,
              'Bladder': 0.1823809523809524,
              'Brain - Amygdala': 3.1213815789473687,
              'Brain - Anterior cingulate cortex (BA24)': 6.059886363636369,
              'Brain - Caudate (basal ganglia)': 4.203821138211382,
              'Brain - Cerebellar Hemisphere': 16.036325581395346,
              'Brain - Cerebellum': 16.423651452282154,
              'Brain - Cortex': 8.833843137254895,
              'Brain - Frontal Cortex (BA9)': 8.232248803827753,
              'Brain - Hippocampus': 3.744619289340102,
              'Brain - Hypothalamus': 5.138861386138614,
              'Brain - Nucleus accumbens (basal ganglia)': 5.237235772357727,
              'Brain - Putamen (basal ganglia)': 3.7709268292682903,
              'Brain - Spinal cord (cervical c-1)': 1.2520125786163532,
              'Brain - Substantia nigra': 1.8099280575539576,
              'Breast - Mammary Tissue': 0.27054466230936847,
              'Cells - Cultured fibroblasts': 0.0928571428571429,
              'Cells - EBV-transformed lymphocytes': 0.2973563218390804,
              'Cervix - Ectocervix': 0.1288888888888889,
              'Cervix - Endocervix': 0.093,
              'Colon - Sigmoid': 0.20761394101876668,
              'Colon - Transverse': 0.1807881773399015,
              'Esophagus - Gastroesophageal Junction': 0.16789333333333334,
              'Esophagus - Mucosa': 0.10236036036036034,
              'Esophagus - Muscularis': 0.1772038834951457,
              'Fallopian Tube': 0.2733333333333333,
              'Heart - Atrial Appendage': 0.21547785547785558,
              'Heart - Left Ventricle': 0.2570601851851851,
              'Kidney - Cortex': 0.15258823529411766,
              'Kidney - Medulla': 0.2,
              'Liver': 0.06800884955752212,
              'Lung': 0.341955017301038,
              'Minor Salivary Gland': 0.14617283950617282,
              'Muscle - Skeletal': 0.3639476961394767,
              'Nerve - Tibial': 0.1953796445880453,
              'Ovary': 0.26411111111111113,
              'Pancreas': 0.06570121951219511,
              'Pituitary': 0.7078091872791518,
              'Prostate': 0.2128979591836736,
              'Skin - Not Sun Exposed (Suprapubic)': 0.11779801324503313,
              'Skin - Sun Exposed (Lower leg)': 0.12439372325249638,
              'Small Intestine - Terminal Ileum': 0.20245989304812825,
              'Spleen': 0.18041493775933612,
              'Stomach': 0.15303621169916434,
              'Testis': 0.6350969529085876,
              'Thyroid': 0.2162633996937214,
              'Uterus': 0.3040140845070424,
              'Vagina': 0.18455128205128207,
              'Whole Blood': 0.42647682119205294,
              'ensembl_id': 'ENST00000569651'
            },
            'proteomicsDB_id': [
              '42982'
            ],
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28883573,
                  28883722
                ],
                [
                  28883854,
                  28884079
                ],
                [
                  28884767,
                  28884995
                ]
              ],
              'transcript_exon_region': [
                [
                  28883573,
                  28883722
                ],
                [
                  28883854,
                  28884079
                ],
                [
                  28884767,
                  28885214
                ]
              ],
              'utr3': [
                28884996,
                28885214
              ],
              'utr3_exon_region': [
                [
                  28884996,
                  28885214
                ]
              ]
            },
            'trans_end': 28885214,
            'trans_start': 28883573,
            'transcript_id': 'ENST00000569651',
            'uniprotKB_id': [
              'H3BUN7_HUMAN'
            ],
            'uniprotkb_ac': [
              'H3BUN7'
            ]
          },
          {
            'chr': '16',
            'ensembl_pro': [
              'ENSP00000457315'
            ],
            'entrez_id': '25970',
            'gencode_id': 'ENST00000568868.1',
            'gene_symbol': 'SH2B1',
            'gtex_v8_transcript_expression': {
              'Adipose - Subcutaneous': 1.8453092006033183,
              'Adipose - Visceral (Omentum)': 1.9274676524953789,
              'Adrenal Gland': 2.4494186046511652,
              'Artery - Aorta': 2.0940046296296297,
              'Artery - Coronary': 2.397041666666667,
              'Artery - Tibial': 1.3813273001508288,
              'Bladder': 2.834761904761905,
              'Brain - Amygdala': 0.9800657894736842,
              'Brain - Anterior cingulate cortex (BA24)': 1.1792613636363638,
              'Brain - Caudate (basal ganglia)': 1.3393089430894305,
              'Brain - Cerebellar Hemisphere': 6.7409302325581315,
              'Brain - Cerebellum': 8.48352697095436,
              'Brain - Cortex': 2.2592941176470602,
              'Brain - Frontal Cortex (BA9)': 1.7794258373205742,
              'Brain - Hippocampus': 1.2990862944162436,
              'Brain - Hypothalamus': 1.269950495049505,
              'Brain - Nucleus accumbens (basal ganglia)': 1.290813008130082,
              'Brain - Putamen (basal ganglia)': 1.069121951219512,
              'Brain - Spinal cord (cervical c-1)': 1.4413207547169813,
              'Brain - Substantia nigra': 1.1010791366906474,
              'Breast - Mammary Tissue': 2.2307625272331153,
              'Cells - Cultured fibroblasts': 1.4676190476190478,
              'Cells - EBV-transformed lymphocytes': 1.826091954022989,
              'Cervix - Ectocervix': 4.697777777777778,
              'Cervix - Endocervix': 4.736,
              'Colon - Sigmoid': 3.0089276139410175,
              'Colon - Transverse': 3.9975615763546815,
              'Esophagus - Gastroesophageal Junction': 2.5989866666666654,
              'Esophagus - Mucosa': 2.5553693693693678,
              'Esophagus - Muscularis': 2.4383883495145606,
              'Fallopian Tube': 3.303333333333333,
              'Heart - Atrial Appendage': 1.2929836829836836,
              'Heart - Left Ventricle': 1.1773379629629621,
              'Kidney - Cortex': 2.9967058823529413,
              'Kidney - Medulla': 5.2175,
              'Liver': 1.8955752212389378,
              'Lung': 2.907456747404843,
              'Minor Salivary Gland': 3.019753086419753,
              'Muscle - Skeletal': 0.8359900373599003,
              'Nerve - Tibial': 3.6273828756058157,
              'Ovary': 5.042999999999999,
              'Pancreas': 1.485823170731707,
              'Pituitary': 4.407950530035333,
              'Prostate': 4.841795918367348,
              'Skin - Not Sun Exposed (Suprapubic)': 1.7047185430463574,
              'Skin - Sun Exposed (Lower leg)': 1.6116547788873032,
              'Small Intestine - Terminal Ileum': 4.526042780748662,
              'Spleen': 5.3949377593360985,
              'Stomach': 1.9816155988857942,
              'Testis': 3.8827423822714633,
              'Thyroid': 6.279127105666157,
              'Uterus': 4.822464788732395,
              'Vagina': 3.5483333333333325,
              'Whole Blood': 0.7247284768211917,
              'ensembl_id': 'ENST00000568868'
            },
            'proteomicsDB_id': [
              '42731'
            ],
            'source': 'gencode',
            'strand': '+',
            'structure': {
              'coding_exon_region': [
                [
                  28883660,
                  28883722
                ],
                [
                  28883854,
                  28884134
                ]
              ],
              'transcript_exon_region': [
                [
                  28883660,
                  28883722
                ],
                [
                  28883854,
                  28884134
                ]
              ]
            },
            'trans_end': 28884134,
            'trans_start': 28883660,
            'transcript_id': 'ENST00000568868',
            'uniprotKB_id': [
              'H3BTT2_HUMAN'
            ],
            'uniprotkb_ac': [
              'H3BTT2'
            ]
          }
        ],
        'variant_description': 'chr16 g.28880342G>A'
      }
      function get_weight (w) {
        if (w <= 10) {
          return 200
        } else if (w > 10 && w <= 30) {
          return w * 2 + 200
        } else {
          return 800
        }
      }
      function data_handling () {
        const x_list = []
        const y_list = []
        const array_list = []
        const id_list = []
        if (isoform_list === 'all') {
          const results = data['proteins']
          const flag = new Array(results.length).fill(0)
          for (let i = 0; i < results.length; i++) {
            const item = results[i]
            if ('proteomicsdb_protein_expression' in item) {
              if ('express_data' in item['proteomicsdb_protein_expression']) {
                const express_data = item['proteomicsdb_protein_expression']['express_data']
                if (express_data !== undefined && item['uniprotkb_ac'].indexOf('-')) {
                  for (let j = 0; j < express_data.length; j++) {
                    const item_item = express_data[j]
                    if (['brain', 'arachnoid cyst', 'cerebral cortex', 'cerebrospinal fluid',
                      'prefrontal cortex', 'spinal cord'].includes(item_item['TISSUE_NAME'])) {
                      flag[i] = 1
                    }
                  }
                }
              }
            }
          }
          for (let i = 0; i < results.length; i++) {
            const item = results[i]
            if (flag[i] !== 0) {
              if ('proteomicsdb_protein_expression' in item) {
                if ('express_data' in item['proteomicsdb_protein_expression']) {
                  const express_data = item['proteomicsdb_protein_expression']['express_data']
                  const x = []
                  const y = []
                  const array = []
                  for (let j = 0; j < express_data.length; j++) {
                    const item_item = express_data[j]
                    x.push(item_item['TISSUE_NAME'])
                    y.push(item_item['NORMALIZED_INTENSITY'])
                    const min = parseFloat(item_item['MIN_NORMALIZED_INTENSITY'])
                    const max = parseFloat(item_item['MAX_NORMALIZED_INTENSITY'])
                    const error = (max - min) / 2
                    array.push(error)
                  }
                  id_list.push(item['UniProtKB-ID'])
                  x_list.push(x)
                  y_list.push(y)
                  array_list.push(array)
                }
              }
            }
          }
          return [x_list, y_list, array_list, id_list]
        } else {
          const results = data['proteins']
          const flag = new Array(results.length).fill(0)
          for (let i = 0; i < results.length; i++) {
            const item = results[i]
            if ('proteomicsdb_protein_expression' in item) {
              if ('express_data' in item['proteomicsdb_protein_expression']) {
                for (const item_item of item['proteomicsdb_protein_expressiona']['express_data']) {
                  if (['brain', 'arachnoid cyst', 'cerebral cortex', 'cerebrospinal fluid',
                    'prefrontal cortex', 'spinal cord'].includes(item_item['TISSUE_NAME']) &&
                      item['NORMALIZED_INTENSITY'] >= 0.5) {
                    flag[i] = 1
                  }
                }
              }
            }
          }
          for (let i = 0; i < results.length; i++) {
            const item = results[i]
            const x = []
            const y = []
            const array = []
            if (flag[i] !== 0) {
              if ('proteomicsdb_protein_expression' in item) {
                if ('express_data' in item['proteomicsdb_protein_expression']) {
                  for (const item_item of item['proteomicsdb_protein_expressiona']['express_data']) {
                    x.push(item_item['TISSUE_NAME'])
                    y.push(item_item['NORMALIZED_INTENSITY'])
                    const min = parseFloat(item_item['MIN_NORMALIZED_INTENSITY'])
                    const max = parseFloat(item_item['MAX_NORMALIZED_INTENSITY'])
                    const error = (max - min) / 2
                    array.push(error)
                  }
                  id_list.push(item['UniProtKB-ID'])
                  x_list.push(x)
                  y_list.push(y)
                  array_list.push(array)
                }
                if (item['UniProtKB-ID'] !== undefined && isoform_list.indexOf(item['UniProtKB-ID'])) {
                  id_list.push(item['UniProtKB-ID'])
                  x_list.push(x)
                  y_list.push(y)
                  array_list.push(array)
                }
              }
            }
          }
          return [x_list, y_list, array_list, id_list]
        }
      }
      const x_list = data_handling()[0]
      const y_list = data_handling()[1]
      const array_list = data_handling()[2]
      const id_list = data_handling()[3]
      console.log(id_list)
      if ((x_list.length === y_list.length) && (x_list.length !== 0)) {
        const tarces = []
        for (let i = 0; i < x_list.length; i++) {
          const x_item = x_list[i]
          const y_item = y_list[i]
          const array_item = array_list[i]
          const id_item = id_list[i]
          for (let j = 0; j < x_item.length; j++) {
            if (['brain', 'arachnoid cyst', 'cerebral cortex', 'cerebrospinal fluid',
              'prefrontal cortex', 'spinal cord'].includes(x_item[j])) {
              x_item[j] = '<b>' + x_item[j] + '&nbsp;</b>'
            } else {
              x_item[j] = x_item[j] + '&nbsp;'
            }
          }
          tarces.push({
            y: x_item,
            x: y_item,
            name: id_item,
            type: 'bar',
            orientation: 'h',
            hoverinfo: 'all',
            error_x: {
              type: 'data',
              array: array_item,
              visible: true
            }
          })
        }
        let l_height = 400
        if (x_list.length >= 1) {
          l_height = get_weight(x_list[0].length * id_list.length)
        }
        const layout = {
          paper_bgcolor: 'rgb(249, 249, 249)',
          plot_bgcolor: 'rgb(249, 249, 249)',
          barmode: 'stack',
          height: l_height,
          width: 800,
          title: '<br>Median protein expression</br>',
          hovermode: 'closest',
          xaxis: {
            title: 'log <sub>10</sub> normalized iBAQ intensity',
            showgrid: true,
            zeroline: true,
            showline: true,
            showticklabels: true,
            titlefont: {
              family: 'Arial, sans-serif',
              size: 18
            }
          },
          yaxis: {
            autorange: true,
            showgrid: true,
            showticklabels: true,
            exponentformat: 'e',
            showexponent: 'ALL'
          },
          margin: {
            l: 250,
            r: 120,
            b: 80,
            t: 40,
            pad: 0
          }
        }
        this.data = tarces
        this.layout = layout
        this.isPlot = true
        this.loading = false
      } else {
        this.isPlot = false
        this.loading = false
      }
    }
  },
  // mounted () {
  //   this.variant_key = this.$route.query.variant
  //   if (this.variant_key) {
  //     this.proteinIsoformPlot(this.variant_key)
  //   }
  //   this.proteinIsoformPlot()
  // },
  created () {
    this.proteinIsoformPlot()
  }
}
</script>
<style scoped>
</style>
