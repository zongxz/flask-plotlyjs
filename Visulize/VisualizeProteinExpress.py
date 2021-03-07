import plotly.graph_objs as go
from utils.dbutils import DBConnection
from Visulize import a
class ProteinExpressPlot(object):
    def __init__(self):
        self.all_tissue = ['adipocyte', 'adrenal gland', 'amniocyte', 'arachnoid cyst', 'ascites', 'blood',
                           'blood platelet',
                           'bone', 'bone marrow stromal cell', 'brain', 'breast', 'cardia', 'cerebral cortex',
                           'B-lymphocyte',
                           'cerebrospinal fluid', 'cerumen', 'cervical mucosa', 'colon', 'colon muscle',
                           'colonic epithelial cell',
                           'cytotoxic T-lymphocyte', 'esophagus', 'gall bladder', 'gut', 'hair follicle', 'heart',
                           'helper T-lymphocyte', 'ileum epithelial cell', 'kidney', 'liver', 'lung', 'lymph node',
                           'mesenchymal stem cell', 'milk', 'monocyte', 'myometrium', 'nasopharynx',
                           'natural killer cell',
                           'oral epithelium', 'osteosarcoma cell', 'ovary', 'pancreas', 'pancreatic islet',
                           'pancreatic juice',
                           'placenta', 'prefrontal cortex', 'prostate gland', 'proximal fluid (coronary sinus)',
                           'rectum',
                           'renal cell carcinoma cell', 'retina', 'saliva', 'salivary gland', 'seminal plasma',
                           'seminal vesicle',
                           'skin', 'spermatozoon', 'spinal cord', 'spleen', 'stomach', 'synovial fluid', 'testis',
                           'thyroid gland',
                           'tonsil', 'urinary bladder', 'urine', 'uterine cervix', 'uterus', 'vitreous humor']

    def set_weight(self, w):
        if w <= 5:
            return 200
        elif w > 5 and w <= 30:
            return w * 20 + 300
        else:
            return w * 20 + 300

    @staticmethod
    def plot(protein_exp_data):
        all_tissues = ProteinExpressPlot().all_tissue
        result_list = []
        x_list = []
        y_list = []
        array_list = []
        id_list = []
        if isinstance(protein_exp_data, list):
            for item_protein_exp in protein_exp_data:
                # print(item_protein_exp)
                express_value = ['undefined'] * len(all_tissues)
                error_value = ['undefined'] * len(all_tissues)
                x = []
                y = []
                array = []
                result_list.append(item_protein_exp.get('express_data'))
                for item_item in item_protein_exp.get('express_data'):
                    for index, item_tissue in enumerate(all_tissues):
                        if item_item.get('TISSUE_NAME') == item_tissue:
                            # print(item_item['NORMALIZED_INTENSITY'])
                            express_value[index] = item_item['NORMALIZED_INTENSITY']
                            error_value[index] = (float(item_item['MAX_NORMALIZED_INTENSITY']) - float(
                                item_item['MIN_NORMALIZED_INTENSITY'])) / 2

                for index, item_tissue in enumerate(all_tissues):
                    x.append(item_tissue)
                    y.append(express_value[index])
                    array.append(error_value[index])
                id_list.append(item_protein_exp.get("uniprotkb_ac"))
                x_list.append(x)
                y_list.append(y)
                array_list.append(array)


            print(array_list)
            if len(x_list) == len(y_list) and len(x_list) != 0:
                trace = []
                for x_item, y_item, array_item, id_item in zip(x_list, y_list, array_list, id_list):
                    for i, item in enumerate(x_item):
                        if item in ["brain", 'arachnoid cyst', 'cerebral cortex', 'cerebrospinal fluid',
                                    'prefrontal cortex', 'spinal cord']:
                            x_item[i] = "<b>" + x_item[i].capitalize() + "</b>"
                        else:
                            x_item[i] = x_item[i].capitalize()
                    trace.append(dict(
                        x=x_item,
                        y=y_item,
                        name=id_item,
                        # orientation='h',
                        hoverinfo='all',
                        error_y=dict(
                            type='data',
                            array=array_item,
                            visible='true'
                        )
                    ))
                layout = dict(
                    paper_bgcolor='rgb(249, 249, 249)',
                    plot_bgcolor='rgb(249, 249, 249)',
                    barmode='stack',
                    height=400,
                    width=1300,
                    title='<br>Median protein expression</br>',
                    # yaxis=dict(range=[0, 10]),
                    # titlefont=dict(size=25), plot_bgcolor='#EFECEA',
                    hovermode='closest',
                    margin=dict(  # x,y轴label距离图纸四周的距离
                        l=50,
                        r=20,
                        b=150,
                        t=40,
                        pad=0
                    ),
                    xaxis=dict(
                        # autorange='true',
                        # title='Diffient Brain region',
                        # titlefont=dict(
                        # 	family='Arial, sans-serif',
                        # 	size=18,
                        # 	color='lightgrey'
                        # ),
                        # title='log <sub>10</sub> normalized iBAQ intensit',
                        titlefont=dict(
                            # family='Arial, sans-serif',
                            size=8,
                            # color='lightgrey'
                        ),
                        showgrid='true',
                        zeroline='true',
                        showline='true',
                        showticklabels='true',
                        tickangle=50,  # x轴刻度之间距离

                        # automargin=False,
                        # separatethousands='true',
                    ), yaxis=dict(
                        title='log <sub>10</sub> normalized iBAQ intensity',
                        # range=[0,],
                        # weight=0.5,
                        # tickmode='linear',
                        # ticks='outside',
                        showgrid='true',
                        autorange='true',

                        # gridwidth=0.5,
                        showticklabels='true',
                        # tickwidth=10,
                        # tickangle=60,
                        # tickfont=dict(
                        # 	# family='Old Standard TT, serif',
                        # 	# size=14,
                        # 	# color='black'
                        # ),
                        exponentformat='e',
                        # showexponent='All'

                    )
                )
                # fig = go.Figure(data=trace, layout=layout)
                return [trace, layout]
            else:
                return '<div> There is no corresponding data published yet, we will update it when such data available.  </div>'
        else:
            return '<div> There is no corresponding data published yet, we will update it when such data available.  </div>'


if __name__ == '__main__':
    # main("8945")
    # main("7468")
    # main("29072")
    # dbc = DBConnection()
    #
    # query_filed = {"entrez_id": 1, "symbol": 1, "_id": 0, 'gene_expression': 1}
    # name = "7468"
    # if name.isalnum():
    #     if name.isdigit():
    #         query_res = dbc.col.find({"entrez_id": name}, query_filed)[0]
    #     else:
    #         query_res = dbc.col.find({"symbol": name}, query_filed)[0]
    #     # pprint(query_res)
    #     if query_res.get('gene_expression'):
    #         if query_res['gene_expression'].get('protein_express'):
    #             gtex_gene_express_pic = ProteinExpressPlot.plot(query_res['gene_expression']['protein_express'])
    #             # pprint(query_res['gene_expression']['human_epc_tpm'])
    ProteinExpressPlot.plot(a.a)