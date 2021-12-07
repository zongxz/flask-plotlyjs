<template>
  <div id="box" style="width: 1200px; height: 850px;">
    <div id="cy" style="width: 1400px; height: 850px;"></div>
  </div>
</template>

<script>
import cytoscape from 'cytoscape'

export default {
  name: 'MiPPIs',
  components: {},
  methods: {
    createCytoscape () {
      const data = {
        'data': {
          'AAChange_refGene': 'UBE4B:NM_001105562:exon7:c.G1069A:p.A357T',
          'CADD_phred': '12.08',
          'CADD_raw': '1.264',
          'CADD_raw_rankscore': '0.217',
          'COSMIC_DIS': '1(stomach)',
          'COSMIC_ID': 'COSM4019892',
          'DANN_rankscore': '0.475',
          'DANN_score': '0.989',
          'DNMs': [
            {
              'DisorderCategory': 'control study',
              'NumControls': '1911',
              'NumProbands': '2508',
              'PrimaryPhenotype': 'Sibling Control',
              'PubmedID': '25363768',
              'SampleID': '11696.s1',
              'SequenceType': 'exome',
              'StudyName': 'Iossifov',
              'Validation': 'validated',
              'case_or_control': 'Control',
              'disorder': 'Sibling Control',
              'psymukb_id': 'PSY_DNM0005608'
            }
          ],
          'DeepSea_Score': '0.096738',
          'Eigen-PC-raw': '-1.262',
          'Eigen-raw': '-1.239',
          'Eigen_coding_or_noncoding': 'c',
          'ExAC_AFR': '0',
          'ExAC_AMR': '0',
          'ExAC_EAS': '0',
          'ExAC_FIN': '0',
          'ExAC_Freq': '8.339e-06',
          'ExAC_NFE': '1.508e-05',
          'ExAC_OTH': '0',
          'ExAC_SAS': '0',
          'ExonicFunc_refGene': 'nonsynonymous snv',
          'FATHMM_converted_rankscore': '0.453',
          'FATHMM_pred': 'T',
          'FATHMM_score': '0.9',
          'Func_refGene': 'exonic',
          'GERP++_RS': '-0.938',
          'GERP++_RS_rankscore': '0.098',
          'Gene_refGene': 'UBE4B',
          'GenoCanyon_score': '0.895',
          'GenoCanyon_score_rankscore': '0.259',
          'HI_Rank': '25.55%',
          'Haploinsufficiency_Score': '0.329099002',
          'LRT_converted_rankscore': '0.205',
          'LRT_pred': 'N',
          'LRT_score': '0.088',
          'M-CAP_pred': 'T',
          'M-CAP_rankscore': '0.341',
          'M-CAP_score': '0.014',
          'MetaLR_pred': 'T',
          'MetaLR_rankscore': '0.210',
          'MetaLR_score': '0.049',
          'MetaSVM_pred': 'T',
          'MetaSVM_rankscore': '0.082',
          'MetaSVM_score': '-1.076',
          'MiPPI_network': {
            'edge': [
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'UBL7'
              },
              {
                'relationship': 'increasing',
                'source': 'UBE4B',
                'target': 'FBXW11'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'UBQLN1'
              },
              {
                'relationship': 'increasing',
                'source': 'UBE4B',
                'target': 'UBE4B'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'PINK1'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'TP73'
              },
              {
                'relationship': 'increasing',
                'source': 'UBE4B',
                'target': 'VCP'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'UBE2D3'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'MDM2'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'TP53'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'FEZ1'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'TP63'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'UBE2D2'
              },
              {
                'relationship': 'no effect',
                'source': 'UBE4B',
                'target': 'BTRC'
              },
              {
                'relationship': 'decreasing',
                'source': 'UBL7',
                'target': 'UBQLN1'
              },
              {
                'source': 'UBL7',
                'target': 'VCP'
              },
              {
                'source': 'UBL7',
                'target': 'UBE4B'
              },
              {
                'source': 'UBL7',
                'target': 'FBXW11'
              },
              {
                'source': 'FEZ1',
                'target': 'UBE4B'
              },
              {
                'source': 'UBE2D2',
                'target': 'UBQLN1'
              },
              {
                'source': 'UBE2D2',
                'target': 'MDM2'
              },
              {
                'source': 'UBE2D2',
                'target': 'UBE4B'
              },
              {
                'source': 'UBE2D2',
                'target': 'BTRC'
              },
              {
                'source': 'UBE2D3',
                'target': 'MDM2'
              },
              {
                'source': 'UBE2D3',
                'target': 'TP63'
              },
              {
                'source': 'UBE2D3',
                'target': 'TP73'
              },
              {
                'source': 'UBE2D3',
                'target': 'TP53'
              },
              {
                'source': 'UBE2D3',
                'target': 'UBE4B'
              },
              {
                'source': 'UBE2D3',
                'target': 'FBXW11'
              },
              {
                'source': 'UBE2D3',
                'target': 'BTRC'
              },
              {
                'source': 'UBQLN1',
                'target': 'VCP'
              },
              {
                'source': 'UBQLN1',
                'target': 'UBE4B'
              },
              {
                'source': 'MDM2',
                'target': 'TP63'
              },
              {
                'source': 'MDM2',
                'target': 'TP73'
              },
              {
                'source': 'MDM2',
                'target': 'TP53'
              },
              {
                'source': 'MDM2',
                'target': 'VCP'
              },
              {
                'source': 'MDM2',
                'target': 'UBE4B'
              },
              {
                'source': 'MDM2',
                'target': 'FBXW11'
              },
              {
                'source': 'MDM2',
                'target': 'BTRC'
              },
              {
                'source': 'TP63',
                'target': 'TP73'
              },
              {
                'source': 'TP63',
                'target': 'TP53'
              },
              {
                'source': 'TP63',
                'target': 'VCP'
              },
              {
                'source': 'TP63',
                'target': 'UBE4B'
              },
              {
                'source': 'TP63',
                'target': 'BTRC'
              },
              {
                'source': 'TP73',
                'target': 'TP53'
              },
              {
                'source': 'TP73',
                'target': 'UBE4B'
              },
              {
                'source': 'TP53',
                'target': 'VCP'
              },
              {
                'source': 'TP53',
                'target': 'UBE4B'
              },
              {
                'source': 'TP53',
                'target': 'FBXW11'
              },
              {
                'source': 'TP53',
                'target': 'BTRC'
              },
              {
                'source': 'VCP',
                'target': 'UBE4B'
              },
              {
                'source': 'VCP',
                'target': 'FBXW11'
              },
              {
                'source': 'VCP',
                'target': 'PINK1'
              },
              {
                'source': 'VCP',
                'target': 'BTRC'
              },
              {
                'source': 'UBE4B',
                'target': 'FBXW11'
              },
              {
                'source': 'UBE4B',
                'target': 'PINK1'
              },
              {
                'source': 'UBE4B',
                'target': 'BTRC'
              },
              {
                'source': 'FBXW11',
                'target': 'BTRC'
              }
            ],
            'node': [
              'UBL7',
              'FBXW11',
              'UBQLN1',
              'UBE4B',
              'PINK1',
              'TP73',
              'VCP',
              'UBE2D3',
              'MDM2',
              'TP53',
              'FEZ1',
              'TP63',
              'UBE2D2',
              'BTRC',
              'UBE4B'
            ]
          },
          'MiPPIs_pred': [
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'Q96S82',
              'partner_gene_symbol': 'UBL7',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'increasing',
              'SWISS-PROT Accessions Interactor B': 'Q9UKB1',
              'partner_gene_symbol': 'FBXW11',
              'pred_class': '3',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'Q9UMX0',
              'partner_gene_symbol': 'UBQLN1',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'increasing',
              'SWISS-PROT Accessions Interactor B': 'O95155',
              'partner_gene_symbol': 'UBE4B',
              'pred_class': '3',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'Q9BXM7',
              'partner_gene_symbol': 'PINK1',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'O15350',
              'partner_gene_symbol': 'TP73',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'increasing',
              'SWISS-PROT Accessions Interactor B': 'P55072',
              'partner_gene_symbol': 'VCP',
              'pred_class': '3',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'P61077',
              'partner_gene_symbol': 'UBE2D3',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'Q00987',
              'partner_gene_symbol': 'MDM2',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'P04637',
              'partner_gene_symbol': 'TP53',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'Q99689',
              'partner_gene_symbol': 'FEZ1',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'Q9H3D4',
              'partner_gene_symbol': 'TP63',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'P62837',
              'partner_gene_symbol': 'UBE2D2',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            },
            {
              'MiPPIs_pred_class': 'no effect',
              'SWISS-PROT Accessions Interactor B': 'Q9Y297',
              'partner_gene_symbol': 'BTRC',
              'pred_class': '2',
              'var_abbr': 'NM_001105562_A357T'
            }
          ],
          'MutationAssessor_pred': 'N',
          'MutationAssessor_score': '0.345',
          'MutationAssessor_score_rankscore': '0.112',
          'MutationTaster_converted_rankscore': '0.520',
          'MutationTaster_pred': 'D',
          'MutationTaster_score': '1.000',
          'OMIM': '',
          'Orpha': '',
          'OrphaNumber': '',
          'PROVEAN_converted_rankscore': '0.108',
          'PROVEAN_pred': 'N',
          'PROVEAN_score': '-0.24',
          'Pathway': [
            {
              'gene_symbol': 'UBE4B',
              'pathway_id': 'hsa04141',
              'pathway_name': 'Protein processing in endoplasmic reticulum',
              'source': 'KEGG'
            },
            {
              'gene_symbol': 'UBE4B',
              'pathway_id': 'hsa04120',
              'pathway_name': 'Ubiquitin mediated proteolysis',
              'source': 'KEGG'
            }
          ],
          'Phenotype_MIM': '',
          'Polyphen2_HDIV_pred': 'B',
          'Polyphen2_HDIV_rankscore': '0.026',
          'Polyphen2_HDIV_score': '0.0',
          'Polyphen2_HVAR_pred': 'B',
          'Polyphen2_HVAR_rankscore': '0.013',
          'Polyphen2_HVAR_score': '0.0',
          'SIFT_converted_rankscore': '0.139',
          'SIFT_pred': 'T',
          'SIFT_score': '0.311',
          'SiPhy_29way_logOdds': '4.424',
          'SiPhy_29way_logOdds_rankscore': '0.108',
          'SpliceAI_pred': [
            {
              'SpliceAI_pred_DP_AG': 5.0,
              'SpliceAI_pred_DP_AL': -41.0,
              'SpliceAI_pred_DP_DG': -50.0,
              'SpliceAI_pred_DP_DL': -25.0,
              'SpliceAI_pred_DS_AG': 0.0,
              'SpliceAI_pred_DS_AL': 0.0,
              'SpliceAI_pred_DS_DG': 0.0,
              'SpliceAI_pred_DS_DL': 0.0,
              'SpliceAI_pred_SYMBOL': 'UBE4B'
            }
          ],
          'VEST3_rankscore': '0.097',
          'VEST3_score': '0.096',
          'Variant': 'G>A',
          'alt': 'A',
          'big_40': '',
          'chr': '1',
          'cyto_band': '1p36.22',
          'dbSNP': 'rs772803836',
          'drug_association': '',
          'end': 10166514,
          'entrez_id': '10277',
          'fathmm-MKL_coding_pred': 'N',
          'fathmm-MKL_coding_rankscore': '0.190',
          'fathmm-MKL_coding_score': '0.161',
          'gnomAD_AF': '8.036e-06',
          'gnomAD_AFR_AF': '0',
          'gnomAD_AMR_AF': '0',
          'gnomAD_ASJ_AF': '0',
          'gnomAD_EAS_AF': '0',
          'gnomAD_FIN_AF': '0',
          'gnomAD_NFE_AF': '1.773e-05',
          'gnomAD_OTH_AF': '0',
          'gnomAD_SAS_AF': '0',
          'gnomAD_exome_AFR': '0',
          'gnomAD_exome_ALL': '8.146e-06',
          'gnomAD_exome_AMR': '0',
          'gnomAD_exome_ASJ': '0',
          'gnomAD_exome_EAS': '0',
          'gnomAD_exome_FIN': '0',
          'gnomAD_exome_NFE': '1.798e-05',
          'gnomAD_exome_OTH': '0',
          'gnomAD_exome_SAS': '0',
          'gwas_snps': '',
          'integrated_confidence_value': '0',
          'integrated_fitCons_score': '0.563',
          'integrated_fitCons_score_rankscore': '0.310',
          'mutation_location': 'codingLoc',
          'phastCons100way_vertebrate': '0.084',
          'phastCons100way_vertebrate_rankscore': '0.222',
          'phastCons20way_mammalian': '0.001',
          'phastCons20way_mammalian_rankscore': '0.043',
          'phyloP100way_vertebrate': '0.348',
          'phyloP100way_vertebrate_rankscore': '0.196',
          'phyloP20way_mammalian': '0.126',
          'phyloP20way_mammalian_rankscore': '0.213',
          'ref': 'G',
          'related_gene_names': [
            'UBE4B'
          ],
          'source': 'ssc',
          'start': 10166514,
          'variant_description': 'chr1 g.10166514G>A'
        },
        'datacounts': 1,
        'status': 200
      }
      const network = data.data['MiPPI_network']
      const len = network['node'].length
      const t = []
      let d = {
        'data': { 'group': 'attr_both' },
        'group': 'nodes',
        'grabbable': true
      }
      for (let i = 0; i < len; i++) {
        d['data']['id'] = network['node'][i]
        d['data']['name'] = network['node'][i]
        if (network['node'][i] === 'UBE4B') {
          d['data']['group'] = 'core'
        }
        t.push(d)
        d = {
          'data': { 'group': 'attr_both' },
          'group': 'nodes',
          'grabbable': true
        }
      }
      const len1 = network['edge'].length
      let d1 = {
        'data': { 'faveColor': '#BEBEBE', 'group': 'no-effect' },
        'group': 'edges'
      }
      for (let i = 0; i < len1; i++) {
        d1['data']['source'] = network['edge'][i]['source']
        d1['data']['target'] = network['edge'][i]['target']
        if (network['edge'][i]['relationship'] === 'increasing') {
          d1['data']['group'] = 'increasing'
        } else if (network['edge'][i]['relationship'] === 'decreasing') {
          d1['data']['group'] = 'decreasing'
        }
        t.push(d1)
        d1 = {
          'data': { 'faveColor': '#BEBEBE', 'group': 'no-effect' },
          'group': 'edges'
        }
      }
      console.log(t)
      const cy = window.cy = cytoscape({
        container: document.getElementById('cy'),
        boxSelectionEnabled: false,
        autounselectify: true,
        wheelSensitivity: 1,
        style: [
          {
            selector: 'node[group="attr_both"]',
            style: {
              'content': 'data(name)',
              'width': '80px',
              'height': '80px',
              'font-size': '40px',
              'text-valign': 'center',
              'text-halign': 'center',
              'background-color': '#A57079',
              'text-outline-color': '#A57079',
              'text-outline-width': '6px',
              'color': '#fff',
              'overlay-padding': '6px',
              'z-index': '10'
            }
          },
          {
            selector: 'node[group="core"]',
            style: {
              'content': 'data(name)',
              'width': '160px',
              'height': '160px',
              'font-size': '60px',
              'text-valign': 'center',
              'text-halign': 'center',
              'background-color': '#D2691E',
              'text-outline-color': '#D2691E',
              'text-outline-width': '6px',
              'color': '#fff',
              'overlay-padding': '6px',
              'z-index': '10'
            }
          },
          {
            'selector': 'edge',
            'style': {
              'curve-style': 'haystack',
              'haystack-radius': 0,
              'width': 'data(width)',
              'line-color': 'data(faveColor)'
            }
          },
          {
            'selector': 'edge[group="no-effect"]',
            'style': {
              'line-style': 'solid',
              'width': 5
            }
          },
          {
            'selector': 'edge[group="increasing"]',
            'style': {
              'line-style': 'solid',
              'width': 15
            }
          },
          {
            'selector': 'edge[group="decreasing"]',
            'style': {
              'line-style': 'dashed',
              'width': 5
              // 'line-dash-pattern': [10, 5]
            }
          }
        ]
      })
      // for (const item of t) {
      //   cy.add(item)
      // }
      cy.add(t)
      const layout = cy.layout({
        name: 'concentric',
        fit: true,
        padding: 5,
        startAngle: 3 / 2 * Math.PI,
        sweep: undefined,
        clockwise: true,
        equidistant: false,
        minNodeSpacing: 10,
        boundingBox: undefined,
        avoidOverlap: true,
        nodeDimensionsIncludeLabels: false,
        height: undefined,
        width: undefined,
        spacingFactor: undefined
      })
      layout.run()
    }
  },
  mounted () {
    this.createCytoscape()
  }
}

</script>
