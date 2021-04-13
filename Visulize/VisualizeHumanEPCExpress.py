from utils.dbutils import DBConnection


def getHumanEPCExpressData():
    dbc = DBConnection()

    query_filed = {"entrez_id": 1, "symbol": 1, "_id": 0, 'gene_expression': 1}
    name = "234"
    if name.isalnum():
        if name.isdigit():
            query_res = dbc.col.find({"entrez_id": name}, query_filed)[0]
        else:
            query_res = dbc.col.find({"symbol": name}, query_filed)[0]
        # pprint(query_res)
        if query_res.get('gene_expression'):
            if query_res['gene_expression'].get('human_epc_tpm'):
                human_epc_exp_data = query_res['gene_expression']['human_epc_tpm']
                if isinstance(human_epc_exp_data, list):
                    expData = human_epc_exp_data[0].get('express_data')
                    return expData