#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 22:42
# @Author  : Sijia
# @Email   : guosijia007@yeah.net
# @File    : VisualizeBrainseqExpress.py
# @Software: PyCharm

import math
from pprint import pprint

import plotly.graph_objs as go
import plotly

from backend.utils.dbutils import DBConnection


class BrainSeqExpressPlot:

    # TODO: 1. entrez_id may map to many ENSG, currently only consider one to one
    # TODO: 2. can't visualize sample id, which point is which sample_id ?

    @staticmethod
    def normalized(alist):
        return [round(math.log2(item + 1.0), 2) if item != 0 else 0 for item in alist]

    @staticmethod
    def plot(brainseq_exp_data):
        if isinstance(brainseq_exp_data, list):
            brainseq_exp_data = brainseq_exp_data[0]
            traces = []
            control_exp = brainseq_exp_data.get('control_expression')
            scz_exp = brainseq_exp_data.get('scz_expression')
            if control_exp:
                control_key = list(control_exp.keys())

                control_notes = ['Sample id: ' + item + ',\n Exp: ' + str(control_exp.get(item)) for item in
                                 control_key]

                control_val = [control_exp.get(item) for item in control_key]
                control_val_normalized = BrainSeqExpressPlot.normalized(control_val)
                control_x = ['control (n=%d)' % len(control_val)] * len(control_val)
                traces.append(
                    go.Box(x=control_x, y=control_val, name='Control', boxpoints='all', line=dict(width=1),
                           marker=dict(size=2.5), pointpos=0))
                traces.append(
                    go.Box(x=control_x, y=control_val_normalized, name='Control', boxpoints='all', line=dict(width=1),
                           marker=dict(size=3), pointpos=0, visible=False, hoverinfo='text', text=control_notes))

            if scz_exp:
                scz_key = list(scz_exp.keys())
                scz_notes = ['Sample id: ' + item + ',\n Exp: ' + str(scz_exp.get(item)) for item in scz_key]
                scz_val = [scz_exp.get(item) for item in scz_key]
                scz_val_normalized = BrainSeqExpressPlot.normalized(scz_val)
                scz_x = ['schizophrenia (n=%d)' % len(scz_val)] * len(scz_val)
                traces.append(go.Box(x=scz_x, y=scz_val, name='Schizophrenia', boxpoints='all', line=dict(width=1),
                                     marker=dict(size=2.5), pointpos=0))
                traces.append(
                    go.Box(x=scz_x, y=scz_val_normalized, name='Schizophrenia', boxpoints='all', line=dict(width=1),
                           marker=dict(size=3), pointpos=0, hoverinfo='text', text=scz_notes, visible=False))
            print(traces)
            print(len(traces))
            if control_exp and scz_exp:
                visible_list_original = [True, False, True, False]
                visible_list_normalized = [False, True, False, True]
                updatemenus = list([dict(type="buttons", active=-1, pad=dict(r=30, t=20), buttons=list(
                    [dict(label='original RPKM', method='update', args=[{'visible': visible_list_original},
                                                                        {'title': 'RPKM without normalization',
                                                                         # 'annotations': high_annotations
                                                                         }]),
                     dict(label='log<sub>2</sub> ( RPKM + 1 )',
                          method='update',
                          args=[{'visible': visible_list_normalized},
                                {'title': 'Adjusted expression (log<sub>2</sub>(RPKM+1))',
                                 # 'annotations': low_annotations
                                 }]),
                     ]))])
            layout = go.Layout(
                updatemenus=updatemenus,
                paper_bgcolor='rgb(249, 249, 249)',
                plot_bgcolor='rgb(249, 249, 249)',
                height=400,
                width=800,
                # title='Gene Express from GTEx(Release V7)',
                # hovermode='closest',
                yaxis=dict(
                    autorange=True,
                    showgrid=True,
                    zeroline=False,
                    # dtick=10,
                    # title='TPM',
                    titlefont=dict(
                        family='Arial',
                    ),
                ),
                xaxis=dict(
                    showgrid=True,
                    zeroline=False,
                    showline=False,
                    showticklabels=True,
                    # tickangle=70,  # x轴刻度之间距离
                    titlefont=dict(
                        family='Arial',
                    )
                ),
                # margin=dict(
                #     l=20,
                #     r=20,
                #     b=230,
                #     t=60,
                # ),
                showlegend=True
            )

            fig = go.Figure(data=traces, layout=layout)
            # plotly.offline.plot(fig, show_link=False)
            return plotly.offline.plot(fig, show_link=False, output_type="div") # include_plotlyjs=False
        else:
            return '<div> There is no corresponding data published yet, we will update it when such data available.  </div>'
        pass


def main():
    dbc = DBConnection()

    query_filed = {"entrez_id": 1, "symbol": 1, "_id": 0, 'gene_expression': 1}
    name = "SHANK3"
    if name.isalnum():
        if name.isdigit():
            query_res = dbc.col.find({"entrez_id": name}, query_filed)[0]
        else:
            query_res = dbc.col.find({"symbol": name}, query_filed)[0]
        # pprint(query_res)
        if query_res.get('gene_expression'):
            if query_res['gene_expression'].get('brainseq_gene_expression_rpkm'):
                gtex_gene_express_pic = BrainSeqExpressPlot.plot(
                    query_res['gene_expression']['brainseq_gene_expression_rpkm'])
                print(query_res['gene_expression']['brainseq_gene_expression_rpkm'])
                # pprint(query_res['gene_expression']['human_epc_tpm'])


if __name__ == '__main__':
    main()
