import json


class JsonDb(object):
    def __init__(self, file_path: str):
        self.db_path = file_path

    def load(self):
        try:
            with open(self.db_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    def save(self, data):
        with open(self.db_path, 'w') as f:
            f.write(json.dumps(data, indent=4))
