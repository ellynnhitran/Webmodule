#mongodb://<dbuser>:<dbpassword>@ds253891.mlab.com:53891/c4t4

import mongoengine

host = "ds253891.mlab.com"
port = 53891
db_name = "c4t4"
user_name = "tuenhi2001"
password = "Tuenhi0123456"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())