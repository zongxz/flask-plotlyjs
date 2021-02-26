import math
import plotly.graph_objs as go
from utils.dbutils import DBConnection

class GtexGeneExpressPlot:

    @staticmethod
    def get_col_color_dict(col_list):
        colors_list = ['rgb(255,255,0)', 'rgb(31,119,180)', 'rgb(215,42,43)', 'rgb(140,140,140)', 'rgb(44,160,44)',
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
        col_color_dict = {}
        col_prex = sorted(set([item.split("-")[0] for item in col_list]))
        for item_k, item_v in zip(col_prex, colors_list):
            col_color_dict[item_k] = item_v
        return col_color_dict

    @staticmethod
    def normalized(alist):
        return [round(math.log2(float(item) + 1.0), 2) if item != 0 else 0 for item in alist]

    @staticmethod
    def plot(gtex_brain_data):
        if isinstance(gtex_brain_data, list):
            gtex_brain_data_dict = gtex_brain_data[0]
            # ToDO entrez_id->ENSP, may be one to many, here only consider the first ENSP gene to plot !
            x_col = sorted([item for item in gtex_brain_data_dict if item not in ['gencode_id', 'gene_symbol']])
            col_color_dict = GtexGeneExpressPlot.get_col_color_dict(x_col)
            y_data = [gtex_brain_data_dict.get(item) for item in x_col]
            color_data = [col_color_dict.get(item.split('-')[0]) for item in x_col]
            y_normalized_data = [GtexGeneExpressPlot.normalized(gtex_brain_data_dict.get(item)) for item in x_col]

            traces = [go.Box(y=yd0, name=xd0, boxpoints='outliers', marker=dict(color=cls0), line=dict(width=1)) for
                      xd0, yd0, cls0 in zip(x_col, y_data, color_data)]
            for xd, yd, cls in zip(x_col, y_normalized_data, color_data):
                traces.append(go.Box(y=yd, name=xd, boxpoints='outliers', visible=False, marker=dict(color=cls, ),
                                     line=dict(width=1)))

            visible_list_original = [True] * len(x_col) + [False] * len(x_col)
            visible_list_normalized = [False] * len(x_col) + [True] * len(x_col)

            updatemenus = list([dict(type="buttons", active=-1, pad=dict(r=30, t=20), buttons=list(
                [dict(label='original TPM', method='update', args=[{'visible': visible_list_original},
                                                                   {'title': 'TPM without normalization',
                                                                    # 'annotations': high_annotations
                                                                    }]),
                 dict(label='log<sub>2</sub> ( TPM + 1 )',
                      method='update',
                      args=[{'visible': visible_list_normalized},
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
                # title='Gene Express from GTEx(Release V7)',
                hovermode='closest',
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
                    tickangle=70,  # x轴刻度之间距离
                    titlefont=dict(
                        family='Arial',
                    )
                ),
                margin=dict(
                    l=20,
                    r=20,
                    b=230,
                    t=60,
                ),
                showlegend=False
            )

            fig = go.Figure(data=traces, layout=layout)
            return fig
        else:
            return '<div>There is no corresponding data published yet, we will update it when such data available. </div>'


def main():

    dbc = DBConnection()

    query_filed = {"entrez_id": 1, "symbol": 1, "_id": 0, 'gene_expression': 1}
    name = "NSD2"
    if name.isalnum():
        if name.isdigit():
            query_res = dbc.col.find({"entrez_id": name}, query_filed)[0]
        else:
            query_res = dbc.col.find({"symbol": name}, query_filed)[0]
        # pprint(query_res)
        if query_res.get('gene_expression'):
            if query_res['gene_expression'].get('gtex_v7_gene_tpm'):
                gtex_gene_express_pic = GtexGeneExpressPlot.plot(query_res['gene_expression']['gtex_v7_gene_tpm'])
                print(gtex_gene_express_pic)
                return gtex_gene_express_pic


if __name__ == '__main__':
    main()