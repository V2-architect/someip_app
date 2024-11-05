
import pickle
import json


class Timestamp(json.JSONEncoder):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def __add__(self, ts):
        return Timestamp(self.timestamp + ts)

    def __sub__(self, ts):
        return Timestamp(self.timestamp - ts)

    def __str__(self):
        return self.timestamp.isoformat()

    def __repr__(self):
        return self.timestamp.isoformat()

    def default(self, obj):
        return self.__str__()


stat = pickle.load(open('out.bin', 'rb'))
import pdb
pdb.set_trace()

print('over')
