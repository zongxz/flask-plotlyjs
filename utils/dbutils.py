import json
import logging
import os

from pymongo import MongoClient

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)


class DBConnection(object):

    def __init__(self, db="psymukb", col="genes", host=None, port=None,
                 user=None, password=None):
        assert db is not None
        self.db = db
        if port is not None and not isinstance(port, int):
            port = int(port)
        try:
            # TODO: option to specify config file
            cfgfile = "./dbservers.json"
            if not os.path.exists(cfgfile):
                if os.path.exists("./conf/dbservers.json"):
                    cfgfile = "./conf/dbservers.json"
                elif os.path.exists("../conf/dbservers.json"):
                    cfgfile = "../conf/dbservers.json"
                else:
                    cfgfile = "../../conf/dbservers.json"
            logger.info("Servers configuration file: %s" % cfgfile)
            with open(cfgfile, "r") as cfgf:
                conf = json.load(cfgf)
        except IOError:
            conf = {"es_host": "localhost", "es_port": 9200,
                    "mongodb_host": "localhost", "mongodb_port": 27017}

        if host is None:
            host = conf['mongodb_host']
        if port is None and 'mongodb_port' in conf:
            port = conf['mongodb_port']

        mc = MongoClient(host, port)
        # if user is None:
        #     user = conf['mongodb_user']
        # if password is None:
        #     password = conf['mongodb_password']
        if user not in ["", None] and password not in ["", None]:
            db_auth = mc['admin']
            db_auth.authenticate(user, password)

        logger.info("New MongoDB connection: '%s:%d'" % (host, port))
        self.mdbi = mc[db]

        if col is not None:
            self.mdbcollection = col
            self.col = self.mdbi[col]


def test():
    dbc = DBConnection()
    print(dbc.col.find({"entrez_id": '1859'}, {"entrez_id": 1, "symbol": 1, "loc_chr": 1, "type_of_gene": 1, "loc_band": 1}))


if __name__ == '__main__':
    test()
