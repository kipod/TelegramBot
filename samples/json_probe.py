import json


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
    with open('my.json', 'w') as f:
        f.write(s)


def load():
    with open('my.json', 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    main()
