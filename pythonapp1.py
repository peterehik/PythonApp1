import json


class BaseClass:

    def toJSON(self):
        return json.dumps(self.__dict__)

    def json_deserialize(self, j):
        self.__dict__ = json.loads(j)
