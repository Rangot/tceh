import requests
import json


def get_habrahabr(url: str, filename):
    r = requests.get('https://jsonplaceholder.typicode.com/comments')

    headers_dict = dict(r.headers)
    for key, value in headers_dict.items():
        print(key + ':', value)

    with open(filename, 'wb') as file:
        for chunk in r.iter_content(chunk_size=128):
            file.write(chunk)



