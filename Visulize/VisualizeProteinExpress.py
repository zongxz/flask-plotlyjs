
from utils.dbutils import DBConnection



def getProteinExpressData():
    # main("8945")
    # main("7468")
    # main("29072")
    dbc = DBConnection()

    query_filed = {"entrez_id": 1, "symbol": 1, "_id": 0, 'gene_expression': 1}
    name = "7468"
    if name.isalnum():
        if name.isdigit():
            query_res = dbc.col.find({"entrez_id": name}, query_filed)[0]
        else:
            query_res = dbc.col.find({"symbol": name}, query_filed)[0]
        # pprint(query_res)
        if query_res.get('gene_expression'):
            if query_res['gene_expression'].get('protein_express'):
                gtex_gene_express_pic = query_res['gene_expression']['protein_express']
                return gtex_gene_express_pic
                # pprint(query_res['gene_expression']['human_epc_tpm'])
