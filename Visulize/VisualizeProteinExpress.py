
from utils.dbutils import DBConnection


def getProteinExpressData():
    dbc = DBConnection()

    query_filed = {"entrez_id": 1, "symbol": 1, "_id": 0, 'gene_expression': 1}
    name = "51146"
    if name.isalnum():
        if name.isdigit():
            query_res = dbc.col.find({"entrez_id": name}, query_filed)[0]
        else:
            query_res = dbc.col.find({"symbol": name}, query_filed)[0]
        if query_res.get('gene_expression'):
            if query_res['gene_expression'].get('protein_express'):
                gtex_gene_express_pic = query_res['gene_expression']['protein_express']
                print(gtex_gene_express_pic)
                return gtex_gene_express_pic
