# -*- encoding: utf-8 -*-
# -------------------------------------------------------------------------------
# @file:        Transcript DNM visualization
# @Author:      GuoSijia
# @Purpose:     Transcript DNM visualization
# @Created:     2018-05-24
# @update:      2018-06-13 13:26
# @Software:    PyCharm
# -------------------------------------------------------------------------------
from itertools import chain
from Visulize import a
import plotly
import plotly.graph_objs as go
from plotly.graph_objs import *
from utils.dbutils import DBConnection


class DNMsOnTranscriptsPlot(object):

    def __init__(self):
        self.sym, self.exton, self.utr3, self.utr5 = range(4)
        self.start, self.end = range(2)

    def combine_list_2D(self, list_2D):
        ####合并相邻区间的二维数组#####
        i = 0
        list_2D_len = len(list_2D)
        while i < list_2D_len - 1:
            if list_2D[i][1] == list_2D[i + 1][0]:
                list_2D[i] = [list_2D[i][0], list_2D[i + 1][1]]
                list_2D.pop(i + 1)
                list_2D_len = list_2D_len - 1
            else:
                i += 1
        return list_2D

    def combine_list_3D(self, list1):
        for i in range(len(list1)):
            if list1[i]:
                list1[i] = self.combine_list_2D(list1[i])
        return list1

    def get_all_exton_region(self, list_3D):
        #####获取所有区域#####
        all_region = []
        for item in list_3D:
            for item_item in chain(item[self.exton], item[self.utr3], item[self.utr5]):
                all_region.append(item_item)
        return all_region

    def drop_duplicate(self, one_list):
        #####去除所有区域中的重复段#####
        temp_list = []
        for one in one_list:
            if one not in temp_list:
                temp_list.append(one)
        return temp_list

    def sort_list(self, all_region):
        #####对所有的外显子区域list根据第一个元素大小进行排序#####
        l = len(all_region)
        all_region = sorted(all_region, key=lambda x: x[0])
        for ii in range(l - 1):
            assert all_region[ii][self.start] <= all_region[ii + 1][self.start]
        # assert all_exton[ii][self.End]<=all_exton[ii+1][self.End]
        return all_region

    def cut_fragment(self, all_region):
        #####将所有区域切分成若干个不重复，不交叉的小段#####
        all_s = [item[self.start] for item in all_region]
        all_e = [item[self.end] for item in all_region]
        all_se = []
        for item in chain(all_s, all_e):
            all_se.append(item)
        all_se = sorted(set(all_se))
        a = all_se[:-1]
        b = all_se[1:]
        all_frag = []
        for x, y in zip(a, b):
            all_frag.append([x, y])
        return all_frag

    def get_sum(self, x_list, n):
        ####求一个list的前n项和#####
        return sum(x_list[:n])

    def get_every_frag_dnm_numbers(self, all_frag, DNM):

        DNM_list = [item[0] for item in DNM]
        DNM_list = list(set(DNM_list))
        DNM_list = sorted(DNM_list)
        num = [0] * len(all_frag)
        i = 0
        for item in all_frag:
            kk = 0
            for item_item in DNM_list:
                if item_item >= item[self.start] and item_item <= item[self.end]:
                    num[i] += 1
                kk += 1
            i += 1

        return num

    def scale_fragment(self, all_frag, DNM):
        ####规定一个新的片段，规定所有小段（包括外显子和内含子的长度均为30）#####
        ll = []
        num = self.get_every_frag_dnm_numbers(all_frag, DNM)
        for item in num:
            if item < 3:
                ll.append(22)
            else:
                ll.append(item * 10 + 2)
        # ll = [20] * len(all_frag)
        re_a = [self.get_sum(ll, n) for n in range(len(ll))]
        re_b = [self.get_sum(ll, n) for n in range(1, len(ll) + 1)]
        scale_frag = []
        for x, y in zip(re_a, re_b):
            scale_frag.append([x, y])
        return scale_frag

    def count_exton_region_in_fragment(self, list_3D, all_frag, scale_frag):
        #####遍历所有外显子区域，统计出所有小段出现在外显子的位置，并将新的小段（自定义间距后的）放到对应位置#####
        ae = list(item[self.exton] for item in list_3D)
        i = 0
        count = []
        count1 = []
        for item in ae:
            temp1 = []
            temp2 = []
            for item1 in item:
                j = 0
                for item2 in all_frag:
                    if item2[self.start] >= item1[self.start] and item2[self.end] <= item1[self.end]:
                        temp1.append(scale_frag[j])
                        temp2.append(all_frag[j])
                    j += 1
            count.append(temp1)
            count1.append(temp2)
            i += 1
        count = self.combine_list_3D(count)
        count1 = self.combine_list_3D(count1)
        return count, count1

    def count_utr_region_in_fragment(self, list_3D, all_frag, scale_frag):
        #####遍历所有utr区域，统计出所有小段出现在utr的位置，并将新的小段（自定义间距后的）放到对应位置#####
        ae_utr = []
        for item in list_3D:
            temp = []
            for item_item in chain(item[self.utr3], item[self.utr5]):
                temp.append(item_item)
            ae_utr.append(temp)
        count = []
        count1 = []
        for item in ae_utr:
            temp1 = []
            temp2 = []
            for item1 in item:
                j = 0
                for item2 in all_frag:
                    if item2[self.start] >= item1[self.start] and item2[self.end] <= item1[self.end]:
                        temp1.append(scale_frag[j])
                        temp2.append(all_frag[j])
                    j += 1
            count.append(temp1)
            count1.append(temp2)
        count = self.combine_list_3D(count)
        count1 = self.combine_list_3D(count1)
        return count, count1

    def count_to_xy(self, list_3D, count, count1):
        #####将片段转换成作画需要的坐标#####
        y = [item[0] for item in list_3D]
        xy = []
        for item, yy, z in zip(count, y, count1):
            for item_item, item_tips in zip(item, z):
                temp = [[item_item[0], yy, item_tips[0]], [item_item[1], yy, item_tips[1]]]
                xy.append(temp)
        return xy

    def DNM_sort_by_site(self, DNM):

        if DNM != [[]]:
            sorted_DNM = sorted(DNM, key=lambda x: x[0])
            return sorted_DNM
        else:
            return []

    def mapping_mutation_to_frag(self, all_frag, scale_frag, DNM=[]):

        DNM_list = [item[0] for item in DNM]
        DNM_list = list(set(DNM_list))
        DNM_list = sorted(DNM_list)
        DNM_tips = list(set([item[1] for item in DNM]))
        DNM_tips = sorted(DNM_tips, key=lambda x: x.split(',')[0])
        num = [0] * len(all_frag)
        i = 0
        DNM_frag = []
        for item in all_frag:
            temp = []
            kk = 0
            for item_item in DNM_list:
                if item_item >= item[self.start] and item_item <= item[self.end]:
                    num[i] += 1
                    temp1 = []
                    temp1.append(item_item)
                    temp1.append(DNM_tips[kk])
                    temp.append(temp1)
                kk += 1
            DNM_frag.append(temp)
            i += 1
        DNM = []
        j = 0
        for item in num:
            if item != 0:
                start = scale_frag[j][self.start] + 2
                temp = []
                for k in range(item):
                    temp1 = []
                    temp1.append(start)
                    temp1.append(start + 3)
                    temp1.append(DNM_frag[j][k][0])
                    temp1.append(DNM_frag[j][k][1])
                    temp.append(temp1)
                    start += 10
                DNM.append(temp)
            j += 1
        return DNM

    def sort_count_utr(self, count_utr):
        for i in range(len(count_utr)):
            count_utr[i] = sorted(count_utr[i], key=lambda x: x[0])
        return count_utr

    def get_trans_region(self, count):
        res = [[item[0][self.start], item[-1][self.end]] for item in count if item]
        return res

    def trans_DNM(self, trans_region, DNM, list_3D):
        y = [item[self.sym] for item in list_3D]
        res = []
        for item in DNM:
            for item2 in item:
                i = 0
                for item_item in trans_region:
                    if item2[0] >= item_item[0] and item2[1] <= item_item[1]:
                        res.append([item2[0], item2[1], y[i], item2[3]])
                    i += 1
        fin_DNM_xy = []
        for item in res:
            fin_DNM_xy.append([[item[0], 'DNMs', item[3]], [item[1], 'DNMs', item[3]]])
        return fin_DNM_xy

    def generate_xy(self, list_3D, DNM_list):
        # data_treat = Data_handing()
        DNM_list = self.DNM_sort_by_site(DNM_list)
        all_exon_region = self.get_all_exton_region(list_3D)
        all_exon_region = self.drop_duplicate(all_exon_region)
        all_exon_region = self.sort_list(all_exon_region)
        all_frag = self.cut_fragment(all_exon_region)
        scale_frag = self.scale_fragment(all_frag, DNM_list)
        count_exon, count1_exon = self.count_exton_region_in_fragment(list_3D, all_frag, scale_frag)
        count_exon_xy = self.count_to_xy(list_3D, count_exon, count1_exon)
        count_utr, count1_utr = self.count_utr_region_in_fragment(list_3D, all_frag, scale_frag)
        count_utr_xy = self.count_to_xy(list_3D, count_utr, count1_utr)

        DNM = self.mapping_mutation_to_frag(all_frag, scale_frag, DNM_list)
        count_utr = self.sort_count_utr(count_utr)
        trans_region = self.get_trans_region(count_utr)
        fin_DNM_xy = self.trans_DNM(trans_region, DNM, list_3D)
        return count_exon_xy, count_utr_xy, fin_DNM_xy

    def get_heights(self, length):
        if length <= 2:
            return 200
        elif length <= 4:
            return 400
        elif length <= 10:
            return 600
        elif length <= 13:
            return 800
        # elif length <= 20:
        #     return length * 35
        else:
            return length * 30

    @staticmethod
    def plot(gene_term):
        if gene_term.isalnum():
            dbc = DBConnection()
            if gene_term.isdigit():
                gene_data = \
                    dbc.col.find({"entrez_id": gene_term}, {"entrez_id": 1, "transcripts": 1, "dnms": 1, "_id": 0})[0]
            else:
                gene_data = \
                    dbc.col.find({"symbol": gene_term}, {"entrez_id": 1, "transcripts": 1, "dnms": 1, "_id": 0})[0]
            dnms_on_trans_plot = DNMsOnTranscriptsPlot()

            if gene_data:
                # print(gene_data)
                transcript_data = gene_data.get('transcripts')
                # print('transcript_data')
                # print(transcript_data)
                dnms_data = gene_data.get('dnms')
                # print('dnms_data')
                # print(dnms_data)
                transcript_list = []
                trans_count = 0
                dnm_list = []
                if transcript_data:
                    for trans_item in transcript_data:
                        transcript_id = trans_item.get('transcript_id')
                        # if trans_item.get('structure'):
                        transcript_structure = trans_item.get('structure')
                        region_list = []
                        for item_region in ['coding_exon_region', 'utr3_exon_region', 'utr5_exon_region']:
                            if transcript_structure.get(item_region):
                                region_list.append(transcript_structure[item_region])
                            else:
                                region_list.append([])
                        transcript_list.append([transcript_id, region_list[0], region_list[1], region_list[2]])
                    transcript_list = sorted(transcript_list, key=lambda x: x[0],
                                             reverse=True)  # 最先添加（排在最前面的）plotly画图的时候会放在越靠近x轴
                    trans_count = len(transcript_list)
                if dnms_data:
                    for dnm_item in dnms_data:
                        if dnm_item.get("Func_refGene") == 'exonic':
                            if dnm_item.get('ExonicFunc_refGene'):
                                s = '%s,%s,%s' % (
                                    dnm_item['start'], dnm_item['variant'], dnm_item['ExonicFunc_refGene'])
                            else:
                                s = '%s,%s' % (dnm_item['start'], dnm_item['variant'])
                        else:
                            if dnm_item.get('Func_refGene'):
                                s = '%s,%s,%s' % (dnm_item['start'], dnm_item['variant'], dnm_item['Func_refGene'])
                            else:
                                s = '%s,%s' % (dnm_item['start'], dnm_item['variant'])
                        dnm_list.append([dnm_item['start'], s])
                else:
                    dnm_list.append([])
                count_exon_xy, count_utr_xy, fin_DNM_xy = dnms_on_trans_plot.generate_xy(transcript_list, dnm_list)
                if trans_count:

                    return [count_exon_xy, count_utr_xy, fin_DNM_xy, trans_count]
                else:
                    return '<div>There is no corresponding data published yet, we will update it when such data available. </div>'

            else:
                return '<div>There is no corresponding data published yet, we will update it when such data available. </div>'
        else:
            return '<div>There is no corresponding data published yet, we will update it when such data available. </div>'


def getTranscript_DNMsData():
    return DNMsOnTranscriptsPlot.plot('29072')