import pandas as pd
import math
import pymongo
from pprint import pprint

class DataStorage:

    def __init__(self, name):
        self.name = name
        self.path = self.__login()

    def __login(self):
        client = pymongo.MongoClient("127.0.0.1", 27017)
        collection = client['psymukb'][self.name]
        return collection

    def FindByID(self, ID):
        x = self.path.find_one({'ENTREZ_ID': ID})
        return x


class Main:
    def __init__(self):
        pass

    def run(self, id):

        f = DataStorage("JR")
        data = f.FindByID(str(id))
        if data.get("BrainspanX") == None:
            return '<div><p>There is no corresponding data published yet, we will update it when such data available. </p></div>'
        else:
            del data['_id']

            return [id, data]


def main(ID):
    mainer = Main()
    # 996
    ID = str(ID)
    return mainer.run(ID)


def getBrainSpanData():
    data = main("85358")
    pprint(data)
    return data


if __name__ == '__main__':
    getBrainSpanData()