import requests


def get_habrahabr():
    r = requests.get('http://habrahabr.ru/')
    print(r.status_code)
    print(r.headers)
    print(r.content)


def find_pet_by_tag(tag):
    params = {'tags': tag}
    headers = {
        'Accept': 'application/json'
        # 'Accept':'application/xml'
    }
    url = 'http://petstore.swagger.io/v2/pet/3'
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code, r.headers)
    print(r.content)


if __name__ == '__main__':
    # get_habrahabr()
    find_pet_by_tag('string')
