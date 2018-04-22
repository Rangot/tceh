import json

from files import way_better

if __name__ == '__main__':
    data = way_better('data.json')
    print('raw data is', data, type(data))
    print()

    # from string to object
    obj = json.loads(data)
    print(obj, type(obj))
    print(obj['object'], obj['boolean'])
    print()

    # from obj to string
    print('dumping obj to text: ')
    obj['new_value'] = 'secret'
    print(json.dumps(obj))