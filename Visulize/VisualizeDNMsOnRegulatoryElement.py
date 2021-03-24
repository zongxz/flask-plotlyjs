from itertools import chain
from utils.dbutils import DBConnection


class DNMsOnRegulatoryPlot:

    def __init__(self):
        pass

    def get_list_2D_region(self, list_2D):
        ##### for coding region #####
        if list_2D:
            start_list = [item[0] for item in list_2D]
            end_list = [item[1] for item in list_2D]
            min_value = min(min(start_list), min(end_list))
            max_value = max(max(start_list), max(end_list))
            return [min_value, max_value]
        else:
            return []

    def get_list_2D_start_end(self, list_2D):
        ##### for utr region #####
        list_2D_flatten = list(chain.from_iterable(list_2D))
        sorted_list = sorted(list_2D_flatten)
        return [sorted_list[0], sorted_list[-1]]

    def get_transcript_region(self, strand, trans_structure):
        # get exon and intron region of one transcript
        if strand:
            if strand == "+":
                if trans_structure.get("utr5_exon_region"):
                    if trans_structure.get("utr3_exon_region"):
                        return [self.get_list_2D_start_end(trans_structure["utr5_exon_region"])[1],
                                self.get_list_2D_start_end(trans_structure["utr3_exon_region"])[0]]
                    else:
                        if trans_structure.get("coding_exon_region"):
                            return [self.get_list_2D_start_end(trans_structure["utr5_exon_region"])[1],
                                    self.get_list_2D_region(trans_structure["coding_exon_region"])[1]]
                        else:
                            return []
                else:
                    if trans_structure.get("coding_exon_region"):
                        if trans_structure.get("utr3_exon_region"):
                            return [self.get_list_2D_region(trans_structure["coding_exon_region"])[0],
                                    self.get_list_2D_start_end(trans_structure["utr3_exon_region"])[0]]
                        else:
                            return self.get_list_2D_region(trans_structure["coding_exon_region"])
                    else:
                        return []
            else:  # strand == "-"
                if trans_structure.get("utr3_exon_region"):
                    if trans_structure.get("utr5_exon_region"):
                        return [self.get_list_2D_start_end(trans_structure["utr3_exon_region"])[1],
                                self.get_list_2D_start_end(trans_structure["utr5_exon_region"])[0]]
                    else:
                        if trans_structure.get("coding_exon_region"):
                            return [self.get_list_2D_start_end(trans_structure["utr3_exon_region"])[1],
                                    self.get_list_2D_region(trans_structure["coding_exon_region"])[1]]
                        else:
                            return []
                else:
                    if trans_structure.get("coding_exon_region"):
                        if trans_structure.get("utr5_exon_region"):
                            return [self.get_list_2D_region(trans_structure["coding_exon_region"])[0],
                                    self.get_list_2D_start_end(trans_structure["utr5_exon_region"])[0]]
                        else:
                            return self.get_list_2D_region(trans_structure["coding_exon_region"])
                    else:
                        return []
        else:
            return []

    def get_trans_data(self, one_trans_structure, transcript_id, strand):
        res = []
        res.append(transcript_id)
        res.append(self.get_transcript_region(strand, one_trans_structure))
        if one_trans_structure.get('utr3_exon_region'):
            res.append(self.get_list_2D_start_end(one_trans_structure['utr3_exon_region']))
        else:
            res.append([])
        if one_trans_structure.get('utr5_exon_region'):
            res.append(self.get_list_2D_start_end(one_trans_structure['utr5_exon_region']))
        else:
            res.append([])
        return res

    def drop_duplication(self, a_list, b_list, c_list):
        a_copy_list = []
        b_copy_list = []
        c_copy_list = []
        for i, item in enumerate(c_list):
            if item not in c_copy_list:
                c_copy_list.append(item)
                b_copy_list.append(b_list[i])
                a_copy_list.append(a_list[i])
        return [a_copy_list, b_copy_list, c_copy_list]

    def get_promoter_and_enhancer_data(self, promoter_data, enhancer_data, dnm_data):
        promoter_res = []
        enhancer_res = []
        temp_promoter = []
        temp_promoter_frag = []
        temp_promoter_tips = []
        if promoter_data:
            for item_pro in promoter_data:
                if item_pro.get('start') and item_pro.get('end'):
                    tips = '%s, %s' % (item_pro.get('short_descripton'), item_pro.get('cage_peak_id'))
                    temp_promoter.append('Promoter')
                    temp_promoter_frag.append([item_pro['start'], item_pro['end']])
                    temp_promoter_tips.append(tips)

        temp_enhancer = []
        temp_enhancer_frag = []
        temp_enhancer_tips = []
        if enhancer_data:
            for item_enh in enhancer_data:
                if item_enh.get('start') and item_enh.get('end'):
                    tips = '%s, [%s - %s], local' % (
                        item_enh.get('genehancer_id'), item_enh.get('start'), item_enh.get('end'))
                    # genehancer_id
                    temp_enhancer.append('Enhancer')
                    temp_enhancer_frag.append([item_enh['start'], item_enh['end']])
                    temp_enhancer_tips.append(tips)

        if dnm_data:
            for dnm_item in dnm_data:
                if dnm_item.get('re-annotation'):
                    if dnm_item['re-annotation'].get('enhancer_id'):
                        if dnm_item['re-annotation'].get('enh_start') and dnm_item['re-annotation'].get('enh_end'):
                            tips = '%s, [%s-%s], targetgene' % (dnm_item['re-annotation']['enhancer_id'],
                                                                dnm_item['re-annotation']['enh_start'].replace('"', ''),
                                                                dnm_item['re-annotation']['enh_end'].replace('"', ''))
                            temp_enhancer.append('Enhancer')
                            temp_enhancer_frag.append([int(dnm_item['re-annotation']['enh_start']),
                                                       int(dnm_item['re-annotation']['enh_end'])])
                            temp_enhancer_tips.append(tips)

                    if dnm_item['re-annotation'].get('promoter_id'):
                        if dnm_item['re-annotation'].get('pro_start') and dnm_item['re-annotation'].get('pro_end'):
                            print('p1111')
                            tips = '%s, [%s-%s], targetgene' % (dnm_item['re-annotation']['promoter_id'],
                                                                dnm_item['re-annotation']['pro_start'].replace('"', ''),
                                                                dnm_item['re-annotation']['pro_end'].replace('"', ''))
                            temp_promoter.append('Promoter')
                            temp_promoter_frag.append([int(dnm_item['re-annotation']['pro_start']),
                                                       int(dnm_item['re-annotation']['pro_end'])])
                            temp_promoter_tips.append(tips)
        if temp_enhancer and temp_enhancer_frag and temp_enhancer_tips:
            temp_enhancer, temp_enhancer_frag, temp_enhancer_tips = self.drop_duplication(temp_enhancer,
                                                                                          temp_enhancer_frag,
                                                                                          temp_enhancer_tips)
            enhancer_res.append(temp_enhancer)
            enhancer_res.append(temp_enhancer_frag)
            enhancer_res.append(temp_enhancer_tips)
        if temp_promoter and temp_promoter_frag and temp_promoter_tips:
            # assert len(temp_promoter) == len(temp_promoter_frag) == len(temp_promoter_tips)
            temp_promoter, temp_promoter_frag, temp_promoter_tips = self.drop_duplication(temp_promoter,
                                                                                          temp_promoter_frag,
                                                                                          temp_promoter_tips)
            promoter_res.append(temp_promoter)
            promoter_res.append(temp_promoter_frag)
            promoter_res.append(temp_promoter_tips)

        return [promoter_res, enhancer_res]

    def get_dnms_data(self, dnms_data):
        dnm_list = []
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
                dnm_list.append([dnm_item['start'], 'DNMs', s])
        else:
            dnm_list.append([])
        return dnm_list

    def hb_list_2D(self, test):
        ####合并相邻区间的二维数组#####
        i = 0
        l = len(test)
        while i < l - 1:
            if test[i][1] == test[i + 1][0]:
                test[i] = [test[i][0], test[i + 1][1]]
                test.pop(i + 1)
                l = l - 1
            else:
                i += 1
        return test

    def hb_list_3D(self, list1):

        for i in range(len(list1)):
            if list1[i] != []:
                list1[i] = self.hb_list_2D(list1[i])
        return list1

    def get_all_region(self, trans_data, regulatory_element_data):
        #####获取所有区域#####
        all_region = []
        for item in trans_data:
            if item[1] != []:
                all_region.append(item[1])
            if item[2] != []:
                all_region.append(item[2])
            if item[3] != []:
                all_region.append(item[3])

        for item in regulatory_element_data:
            if item != []:
                for item_item in item[1]:
                    if item_item != []:
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
        #####对所有的区域list根据第一个元素大小进行排序#####
        l = len(all_region)
        all_region = sorted(all_region, key=lambda x: x[0])
        for ii in range(l - 1):
            assert all_region[ii][0] <= all_region[ii + 1][0]
        return all_region

    def cut_fragment(self, all_region):
        #####将所有区域切分成若干个不重复，不交叉的小段#####
        all_s = [item[0] for item in all_region]
        all_e = [item[1] for item in all_region]
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
                if item_item >= item[0] and item_item <= item[1]:
                    num[i] += 1
                kk += 1
            i += 1

        return num

    def scale_fragment(self, all_frag, DNM, regulatory_element_data):
        ####规定一个新的片段，规定所有小段（包括外显子和内含子的长度均为20）#####

        num = self.get_every_frag_dnm_numbers(all_frag, DNM)
        # ll = [20] * len(all_frag)
        ll = []
        pe = []
        if regulatory_element_data[0] != []:
            promoter_frag = regulatory_element_data[0][1]
            for item in promoter_frag:
                pe.append(item)
        if regulatory_element_data[1] != []:
            enhancer_frag = regulatory_element_data[1][1]
            for item in enhancer_frag:
                pe.append(item)
        # for item in chain(promoter_frag, enhancer_frag):
        # 	pe.append(item)
        pe_drop_dupliction = []
        for item in pe:
            if item not in pe_drop_dupliction:
                pe_drop_dupliction.append(item)
        flag = [0] * len(all_frag)
        for index, item in enumerate(all_frag):
            for item1 in pe_drop_dupliction:
                if item[0] >= item1[0] and item[1] <= item1[1]:
                    flag[index] = 1
        for item1, item2 in zip(flag, num):
            if item1 == 1:
                ll.append(10)
            else:
                if item2 < 3:
                    ll.append(22)
                else:
                    ll.append(item2 * 10 + 2)
            # ll.append(20)
        re_a = [self.get_sum(ll, n) for n in range(len(ll))]
        re_b = [self.get_sum(ll, n) for n in range(1, len(ll) + 1)]
        scale_frag = []
        for x, y in zip(re_a, re_b):
            scale_frag.append([x, y])
        return scale_frag

    def count_exton_region_in_fragment(self, all_frag, scale_frag, trans_data):
        #####遍历所有外显子区域，统计出所有小段出现在外显子的位置，并将新的小段（自定义间距后的）放到对应位置#####
        ae = list(item[1] for item in trans_data)
        count = []
        count1 = []
        for i, item in enumerate(ae):
            temp1 = []
            temp2 = []
            if item == []:
                temp1.append([])
                temp2.append([])
                count.append(temp1)
                count1.append(temp2)
            else:
                for j, item2 in enumerate(all_frag):
                    if item2[0] >= item[0] and item2[1] <= item[1]:
                        temp1.append(scale_frag[j])
                        temp2.append(all_frag[j])
                count.append(temp1)
                count1.append(temp2)
        sort_count = count
        for index, item in enumerate(sort_count):
            if item != [[]]:
                sort_count[index] = sorted(item, key=lambda x: x[0])

        count = self.hb_list_3D(count)
        count1 = self.hb_list_3D(count1)
        try:
            for index, item in enumerate(count1):
                if item != [[]]:
                    count1[index] = sorted(item, key=lambda x: x[0])
        except:
            pass
        return count, count1

    def count_utr_region_in_fragment(self, all_frag, scale_frag, trans_data):
        #####遍历所有utr区域，统计出所有小段出现在utr的位置，并将新的小段（自定义间距后的）放到对应位置#####
        ae_utr = []
        for item in trans_data:
            temp = []
            if item[2] != []:  # !=[None,None]
                temp.append(item[2])
            if item[3] != []:
                temp.append(item[3])
            ae_utr.append(temp)
        count = []
        count1 = []
        for item in ae_utr:
            temp1 = []
            temp2 = []
            if item == [[]] or item == []:
                temp1.append([])
                temp2.append([])
                count.append(temp1)
                count1.append(temp2)
            else:
                for i, item1 in enumerate(item):
                    for j, item2 in enumerate(all_frag):
                        if item2[0] >= item1[0] and item2[1] <= item1[1]:
                            temp1.append(scale_frag[j])
                            temp2.append(all_frag[j])
                count.append(temp1)
                count1.append(temp2)
        sort_count = count
        for index, item in enumerate(sort_count):
            if item != [[]] and item != []:
                sort_count[index] = sorted(item, key=lambda x: x[0])

        count = self.hb_list_3D(count)
        count1 = self.hb_list_3D(count1)
        for index, item in enumerate(count1):
            if item != [[]] and item != []:
                count1[index] = sorted(item, key=lambda x: x[0])
        return count, count1

    def count_promoter_region_in_fragment(self, all_frag, scale_frag, regulatory_element_data):
        #####遍历所有启动子区域，统计出所有小段出现在启动子的位置，并将新的小段（自定义间距后的）放到对应位置#####
        if regulatory_element_data[0] != []:
            ae_promoter = regulatory_element_data[0][1]
            count = []
            count1 = []
            for i, item in enumerate(ae_promoter):
                temp = []
                temp1 = []
                for j, item2 in enumerate(all_frag):
                    if item2[0] >= item[0] and item2[1] <= item[1]:
                        temp.append(scale_frag[j])
                        temp1.append(all_frag[j])
                count.append(temp)
                count1.append(temp1)
            count = self.hb_list_3D(count)
            count1 = self.hb_list_3D(count1)
            return count, count1

    def count_enhancer_region_in_fragment(self, all_frag, scale_frag, regulatory_element_data):
        #####遍历所有增强子区域，统计出所有小段出现在启动子的位置，并将新的小段（自定义间距后的）放到对应位置#####
        if regulatory_element_data[1] != []:
            ae_enhancer = regulatory_element_data[1][1]
            count = []
            count1 = []
            for i, item in enumerate(ae_enhancer):
                temp = []
                temp1 = []
                for j, item2 in enumerate(all_frag):
                    if item2[0] >= item[0] and item2[1] <= item[1]:
                        temp.append(scale_frag[j])
                        temp1.append(all_frag[j])
                count.append(temp)
                count1.append(temp1)
            count = self.hb_list_3D(count)
            count1 = self.hb_list_3D(count1)
            return count, count1

    def convert_trans_to_xy(self, count, count1, trans_data):
        #####将转录本（utr，外显子内含子）片段准换成作画需要的坐标#####
        y = [item[0] for item in trans_data if not (item[1] == [] and item[2] == [] and item[3] == [])]
        xy = []
        for item, yy, z in zip(count, y, count1):
            for item_item, item_tips in zip(item, z):
                if item_item != [] and item_item != [[]]:
                    temp = [[item_item[0], yy, item_tips[0]], [item_item[1], yy, item_tips[1]]]
                    xy.append(temp)
        # final_xy = []
        # for item in xy:
        # 	for item_item in item:
        # 		final_xy.append(item_item)
        return xy

    def convert_utr_to_xy(self, count, count1, trans_data):
        #####将转录本（utr，外显子内含子）片段准换成作画需要的坐标#####
        y = [item[0] for item in trans_data if not (item[1] == [] and item[2] == [] and item[3] == [])]
        xy = []
        for item, yy, z in zip(count, y, count1):
            if item != [[]]:
                for item_item, item_tips in zip(item, z):
                    temp = [[item_item[0], yy, item_tips[0]], [item_item[1], yy, item_tips[1]]]
                    xy.append(temp)
        # final_xy = []
        # for item in xy:
        # 	for item_item in item:
        # 		final_xy.append(item_item)
        return xy

    def convert_regulatory_elements_to_xy(self, count, p_or_e, regulatory_element_data):
        #####将调控原件（启动子，增强子）片段准换成作画需要的坐标#####
        xy = []
        if p_or_e == 'Promoter':
            tips = regulatory_element_data[0][2]
        elif p_or_e == 'Enhancer':
            tips = regulatory_element_data[1][2]
        else:
            tips = 'Error'
        for i, item in enumerate(count):
            for item_item in item:
                temp = [[item_item[0], p_or_e, tips[i]], [item_item[1], p_or_e, tips[i]]]
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
        DNM_tips = [item[1] for item in DNM]
        un_sorted_DNM_hover = [item[2] for item in DNM]
        DNM_hover = sorted(un_sorted_DNM_hover, key=lambda x: x[0])
        num = [0] * len(all_frag)
        i = 0
        DNM_frag = []
        for item in all_frag:
            temp = []
            kk = 0
            for item_item in DNM_list:
                if item_item >= item[0] and item_item <= item[1]:
                    num[i] += 1
                    temp1 = []
                    temp1.append(item_item)
                    temp1.append(DNM_tips[kk])
                    temp1.append(DNM_hover[kk])
                    temp.append(temp1)
                kk += 1
            DNM_frag.append(temp)
            i += 1
        DNM = []
        j = 0
        for item in num:
            if item != 0:
                start = scale_frag[j][0] + 2
                temp = []
                for k in range(item):
                    temp1 = []
                    temp1.append(start)
                    temp1.append(start + 3)
                    temp1.append(DNM_frag[j][k][0])
                    temp1.append(DNM_frag[j][k][1])
                    temp1.append(DNM_frag[j][k][2])
                    temp.append(temp1)
                    start += 10
                DNM.append(temp)
            j += 1
        final_DNM = []
        for item in DNM:
            for item_item in item:
                final_DNM.append(item_item)
        return final_DNM

    def convert_dnms_to_xy(self, dnm_data):
        xy = []
        for item in dnm_data:
            temp = [[item[0], item[3], item[4]], [item[1], item[3], item[4]]]
            xy.append(temp)
        return xy

    @staticmethod
    def plot(gene_term):
        dnms_on_re_plot = DNMsOnRegulatoryPlot()
        if gene_term.isalnum():
            dbc = DBConnection()
            if gene_term.isdigit():
                gene_data = dbc.col.find({"entrez_id": gene_term},
                                         {"entrez_id": 1, "_id": 0, "dnms": 1, "transcripts": 1, "promoter": 1,
                                          "enhancer": 1, "symbol": 1})[0]
            else:
                gene_data = dbc.col.find({"symbol": gene_term},
                                         {"entrez_id": 1, "_id": 0, "dnms": 1, "transcripts": 1, "promoter": 1,
                                          "enhancer": 1, "symbol": 1})[0]
            transcript_list = []
            if gene_data:
                if gene_data.get("transcripts"):
                    for index, item in enumerate(gene_data["transcripts"]):
                        if item.get('structure'):
                            transcript_list.append(
                                dnms_on_re_plot.get_trans_data(item['structure'], item.get('transcript_id'),
                                                               item.get("strand")))
                transcript_list = sorted(transcript_list, key=lambda x: x[0],
                                         reverse=True)  # 最先添加（排在最前面的）plotly画图的时候会放在越靠近x轴
                trans_count = len(transcript_list)
                re_data = dnms_on_re_plot.get_promoter_and_enhancer_data(gene_data.get('promoter'),
                                                                         gene_data.get('enhancer'),
                                                                         gene_data.get('dnms'))
                dnms_list = dnms_on_re_plot.get_dnms_data(gene_data.get("dnms"))
                all_region = dnms_on_re_plot.get_all_region(transcript_list, re_data)
                all_region = dnms_on_re_plot.drop_duplicate(all_region)
                all_region = dnms_on_re_plot.sort_list(all_region)
                dnm_data = dnms_on_re_plot.DNM_sort_by_site(dnms_list)
                all_frag = dnms_on_re_plot.cut_fragment(all_region)
                scale_frag = dnms_on_re_plot.scale_fragment(all_frag, dnm_data, re_data)

                exton_count, exton_count1 = dnms_on_re_plot.count_exton_region_in_fragment(all_frag, scale_frag,
                                                                                           transcript_list)
                exton_plot_data = dnms_on_re_plot.convert_trans_to_xy(exton_count, exton_count1, transcript_list)

                utr_count, utr_count1 = dnms_on_re_plot.count_utr_region_in_fragment(all_frag, scale_frag,
                                                                                     transcript_list)
                utr_plot_data = dnms_on_re_plot.convert_utr_to_xy(utr_count, utr_count1, transcript_list)

                if re_data[0] != []:
                    promoter_count, promoter_count1 = dnms_on_re_plot.count_promoter_region_in_fragment(all_frag,
                                                                                                        scale_frag,
                                                                                                        re_data)
                    promoter_plot_data = dnms_on_re_plot.convert_regulatory_elements_to_xy(promoter_count, 'Promoter',
                                                                                           re_data)
                else:
                    promoter_plot_data = None

                if re_data[1] != []:
                    enhancer_count, enhancer_count1 = dnms_on_re_plot.count_enhancer_region_in_fragment(all_frag,
                                                                                                        scale_frag,
                                                                                                        re_data)
                    enhancer_plot_data = dnms_on_re_plot.convert_regulatory_elements_to_xy(enhancer_count, 'Enhancer',
                                                                                           re_data)
                else:
                    enhancer_plot_data = None

                final_dnm = dnms_on_re_plot.mapping_mutation_to_frag(all_frag, scale_frag, dnm_data)
                dnm_plot_data = dnms_on_re_plot.convert_dnms_to_xy(final_dnm)
                l = [exton_plot_data, utr_plot_data, promoter_plot_data,
                     enhancer_plot_data, dnm_plot_data, trans_count]
                print(l)
                return l

        else:
            return '<div>There is no corresponding data published yet, we will update it when such data available. </div>'


def getDNMsOnRegulatoryData():
    # main(57680)
    return DNMsOnRegulatoryPlot.plot("29072")
    # dnms_on_re_plot = DNMsOnRegulatoryPlot()
    # dnms_on_re_plot.plot_dnms_on_re(a.l[0], a.l[1], a.l[2], a.l[3], a.l[4], a.l[5])
