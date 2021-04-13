import math

import plotly.graph_objs as go

from utils.dbutils import DBConnection

def getMouseBrainExpressData():
    # mainer = MouseBrainExpressPlots('29072')
    # mainer.run()

    dbc = DBConnection()

    query_filed = {"entrez_id": 1, "symbol": 1, "_id": 0, 'gene_expression': 1}
    name = "10344"
    if name.isalnum():
        if name.isdigit():
            query_res = dbc.col.find({"entrez_id": name}, query_filed)[0]
        else:
            query_res = dbc.col.find({"symbol": name}, query_filed)[0]
        # pprint(query_res)
        if query_res.get('gene_expression'):
            if query_res['gene_expression'].get('mouse_brain_tpm'):
                if isinstance(query_res['gene_expression']['mouse_brain_tpm'], list):
                    expData = query_res['gene_expression']['mouse_brain_tpm'][0].get('expree_data')
                    return expData