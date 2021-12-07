import pymongo
import json
from functools import reduce
from pprint import pprint


class DataStorage:

    def __init__(self, name):
        self.name = name
        self.path = self.__login()

    def __login(self):
        client = pymongo.MongoClient("127.0.0.1", 27017)
        collection = client['psymukb'][self.name]

        return collection

    def FindPPI(self, ID):
        a = self.FindByID(ID)
        if "ppi" in a['ppi_network']:
            x = []
            for i in a['ppi_network']["ppi"]:
                if "ENTREZ_A" in i:
                    x.append(i)
            return x
        else:
            return None
    def FindByID(self, ID):
        x = self.path.find_one({'entrez_id': ID})
        return x

class DrawBioGridPPI:
    def __init__(self):
        pass

    def FindSymbol(self, symbol_id, ppi):
        node_symbol = ''
        for item in ppi:
            if (str(symbol_id) == str(item["ENTREZ_A"])):
                node_symbol = item["Symbol_AA"]
                break
            elif (str(symbol_id) == str(item["ENTREZ_B"])):
                node_symbol = item["Symbol_B"]
                break
        return node_symbol

    def list_dict_duplicate_removal(self, data_list):  # 去重
        run_function = lambda x, y: x if y in x else x + [y]
        return reduce(run_function, [[], ] + data_list)

    # 绘制PPI图像
    def draw_biogrid_ppi(self, id, f):
        ppi = f.FindPPI(id)
        all = f.FindByID(str(id))

        arr_nodes = []
        arr_edges = []
        dict_nodes = {}
        dict_edges = {}
        ppi_network = all.get('ppi_network')
        pprint(ppi_network)
        all_ppi_point = ppi_network.get("ppi_points")
        mutation_count_list = ppi_network.get("dnm_count")
        protein_brain_exp_flag_list = ppi_network.get("protein_brain_express")
        gene_brain_exp_flag_list = ppi_network.get("gene_brain_express")

        for index, node_id in enumerate(all_ppi_point):  # 点集
            # print(index)
            node_symobel = self.FindSymbol(node_id, ppi)
            if node_symobel != 'NA':
                data_nodes = {'data': {}}
                if node_id == id:
                    data_nodes['data']['group'] = 'core'
                    data_nodes['data']['name'] = node_symobel
                else:
                    # ppipointclass = functionhelp.PPIPointClass()
                    # mutation_count = ppipointclass.get_mutation_count(node_id)
                    # protein_brain_exp_flag = ppipointclass.get_protein_brain_exp_flag(node_id)
                    # gene_brain_exp_flag = ppipointclass.get_gene_brain_exp_flag(node_id)
                    mutation_count = mutation_count_list[index]
                    protein_brain_exp_flag = protein_brain_exp_flag_list[index]
                    gene_brain_exp_flag = gene_brain_exp_flag_list[index]
                    if mutation_count != 0 and not protein_brain_exp_flag and not gene_brain_exp_flag:
                        data_nodes['data']['name'] = node_symobel + "*"
                        data_nodes['data']['group'] = 'attr'
                    elif mutation_count == 0 and protein_brain_exp_flag and not gene_brain_exp_flag:
                        data_nodes['data']['name'] = node_symobel
                        data_nodes['data']['group'] = 'attr_protein'
                    elif mutation_count == 0 and not protein_brain_exp_flag and gene_brain_exp_flag:
                        data_nodes['data']['name'] = node_symobel
                        data_nodes['data']['group'] = 'attr_gene'
                    elif mutation_count != 0 and protein_brain_exp_flag and not gene_brain_exp_flag:
                        data_nodes['data']['name'] = node_symobel + "*"
                        data_nodes['data']['group'] = 'attr_protein'
                    elif mutation_count != 0 and not protein_brain_exp_flag and gene_brain_exp_flag:
                        data_nodes['data']['name'] = node_symobel + "*"
                        data_nodes['data']['group'] = 'attr_gene'
                    elif mutation_count == 0 and gene_brain_exp_flag and protein_brain_exp_flag:
                        data_nodes['data']['name'] = node_symobel
                        data_nodes['data']['group'] = 'attr_both'
                    elif mutation_count != 0 and gene_brain_exp_flag and protein_brain_exp_flag:
                        data_nodes['data']['name'] = node_symobel + "*"
                        data_nodes['data']['group'] = 'attr_both'

                    else:
                        data_nodes['data']['group'] = 'attr'
                        data_nodes['data']['name'] = node_symobel
                data_nodes['data']['id'] = node_id
                data_nodes['data']['href'] = 'http://psymukb.net/GeneDetail/' + node_id + '/GeneInformation'
                dict_nodes['group'] = 'nodes'
                data_nodes.update(dict_nodes)
                arr_nodes.append(data_nodes)
        arr_nodes = self.list_dict_duplicate_removal(arr_nodes)  # 去重

        for item in ppi:  # 边集
            data_edges = {'data': {}}
            if item["ENTREZ_A"] == id:  # 直接作用
                data_edges['data']['faveColor'] = '#FF6347'
            elif item["ENTREZ_B"] == id:
                data_edges['data']['faveColor'] = '#FF6347'
            else:  # 间接作用
                data_edges['data']['faveColor'] = '#BEBEBE'  # 灰色
            if (int(item["Evidence"]) > 90):
                data_edges['data']['width'] = 90
            else:
                data_edges['data']['width'] = item["Evidence"]
            dict_edges['group'] = "edges"
            data_edges['data']['source'] = item["ENTREZ_A"]
            data_edges['data']['target'] = item["ENTREZ_B"]
            data_edges.update(dict_edges)
            arr_edges.append(data_edges)
        arr_edges = self.list_dict_duplicate_removal(arr_edges)
        arr_nodes.extend(arr_edges)
        results = json.dumps(arr_nodes)
        pprint(results)
        return results



class Main:
    def __init__(self):
        pass

    def run(self, id):
        f = DataStorage("genes")
        draw = DrawBioGridPPI()
        return draw.draw_biogrid_ppi(id, f)


if __name__ == '__main__':
    m = Main()
    m.run("7468")
