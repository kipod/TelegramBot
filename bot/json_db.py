import json


class JsonDb(object):
    def __init__(self, file_path: str):
        self.db_path = file_path
        self.load()

    def load(self):
        with open(self.db_path, 'r') as f:
            return json.load(f)

    def save(self, data):
        with open(self.db_path, 'w') as f:
            f.write(json.dumps(data, indent=4))
