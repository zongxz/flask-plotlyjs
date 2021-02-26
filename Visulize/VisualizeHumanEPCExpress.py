import math

import plotly.graph_objs as go
from utils.dbutils import DBConnection

class HumanEPCExpressPlot:
    def dropx(self, alist):
        return [0 if item == "" else item for item in alist]

    def normalized(self, alist):
        return [0 if item in [0, ""] else round(math.log10(float(item) + 1.0), 2) for item in alist]

    def get_averge(self, alist, normaliaze=False):
        float_alist = [float(item) if item != "" else float(0) for item in alist]
        result = sum(float_alist) / len(float_alist)
        if normaliaze:
            return round(math.log10(sum(float_alist) / len(float_alist) + 1), 2)
        else:
            return round(result, 2)

    def sorted_threelist(self, alist, blist, clist):
        total_list = [[item_a, item_b, item_c] for item_a, item_b, item_c in zip(alist, blist, clist)]
        sort_total_list = sorted(total_list, key=lambda x: x[0])
        return [item[0] for item in sort_total_list], [item[1] for item in sort_total_list], [item[2] for item in
                                                                                              sort_total_list]
    @staticmethod
    def plot(human_epc_exp_data):
        if isinstance(human_epc_exp_data, list):
            print(len(human_epc_exp_data))
            print(human_epc_exp_data)
            expData = human_epc_exp_data[0].get('express_data')
            print(expData)
            hpe = HumanEPCExpressPlot()
            traces = []
            for item in expData:
                dataType = item['type']
                data = hpe.dropx(item['data'])
                period = item['period']
                traces.append(go.Box(
                    y=data,
                    x=[dataType + " - " + item_item for item_item in period],
                    name=dataType,
                    boxpoints='outliers',
                    line=dict(width=1),
                ))
            l = len(traces)
            for item in expData:
                dataType = item['type']
                data = hpe.normalized(item['data'])
                period = item['period']
                traces.append(go.Box(
                    y=data,
                    x=[dataType + " - " + item_item for item_item in period],
                    visible=False,
                    name=dataType,
                    boxpoints='outliers',
                    line=dict(width=1),
                ))
            visible_list_1 = [True] * l + [False] * l + [False] * 2
            visible_list_2 = [False] * l + [True] * l + [False] * 2
            updatemenus = list([
                dict(type="buttons",
                     active=-1,
                     # direction='left',
                     pad=dict(
                         # l=500,
                         r=30,
                         # b=250,
                         t=20,
                     ),
                     buttons=list([
                         dict(label='original TPM',
                              method='update',
                              args=[{'visible': visible_list_1},
                                    {'title': 'TPM without normalization',
                                     # 'annotations': high_annotations
                                     }]),
                         dict(label='log<sub>10</sub> ( TPM + 1 )',
                              method='update',
                              args=[{'visible': visible_list_2},
                                    {'title': 'Normalized TPM',
                                     # 'annotations': low_annotations
                                     }]),
                     ]))])
            layout = go.Layout(
                updatemenus=updatemenus,
                paper_bgcolor='rgb(249, 249, 249)',
                plot_bgcolor='rgb(249, 249, 249)',
                height=400,
                width=1000,
                hovermode='closest',
                xaxis=dict(
                    showgrid=True,
                    zeroline=False,
                    showline=False,
                    showticklabels=True,
                    tickangle=60,
                    titlefont=dict(
                        family='Arial',
                    ),
                ),
                yaxis=dict(
                    titlefont=dict(
                        family='Arial',
                    )

                ),
                margin=dict(
                    l=150,
                    r=10,
                    b=180,
                    t=30,
                ),
                # showlegend=False
            )
            fig = go.Figure(data=traces, layout=layout)
            return fig
        else:
            return '<div>There is no corresponding data published yet, ' \
                   'we will update it when such data available. </div>'



def main():
    # mainer = EmbryonicExpressPlot("85358")
    # mainer.run()

    dbc = DBConnection()

    query_filed = {"entrez_id": 1, "symbol": 1, "_id": 0, 'gene_expression': 1}
    name = "85358"
    if name.isalnum():
        if name.isdigit():
            query_res = dbc.col.find({"entrez_id": name}, query_filed)[0]
        else:
            query_res = dbc.col.find({"symbol": name}, query_filed)[0]
        # pprint(query_res)
        if query_res.get('gene_expression'):
            if query_res['gene_expression'].get('human_epc_tpm'):
                gtex_gene_express_pic = HumanEPCExpressPlot.plot(query_res['gene_expression']['human_epc_tpm'])
                return gtex_gene_express_pic
                # pprint(query_res['gene_expression']['human_epc_tpm'])
if __name__ == '__main__':
    main()
