import json
import hashlib


def main():
    d = {
        1: 'one',
        2: 'two',
        "list": [1, 2, 3.5, 4],
        "true": True,
        "None": None,
        "tuple": (1, 3, 4)
    }
    save(d)
    res = load()
    assert res['true'] == d['true']


def save(o):
    s = json.dumps(o, indent=2)
    # m = hashlib.md5()
    # m.update("000005fab4534d05api_key9a0554259914a86fb9e7eb014e4e5d52permswrite")
    # m.hexdigest()
    with open('my.json', 'w') as f:
        f.write(s)


def load():
    with open('my.json', 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    main()
