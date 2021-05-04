from backend.utils.dbutils import DBConnection

def getGexGeneExpressData():

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
                gtex_brain_data = query_res['gene_expression']['gtex_v7_gene_tpm']
                if isinstance(gtex_brain_data, list):
                    gtex_brain_data_dict = gtex_brain_data[0]
                    return gtex_brain_data_dict