import requests
import time
import random
import string


def generate_random_string(length):
    return ''.join([random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(length)])


#requests.post('http://127.0.0.1:5000/add', data={'password': 'apple'})
requests.post('http://127.0.0.1:5000/add', data={'password': '123'})
#requests.post('http://127.0.0.1:5000/add', data={'password': 'qwe'})
for _ in range(1000):
    requests.post('http://127.0.0.1:5000/add',
                  data={'password': generate_random_string(10)})


tries = ['a', 'bsv', '123']
for try_ in tries:
    since = time.time()
    res = requests.post('http://127.0.0.1:5000/check', data={'password': try_})
    duration = time.time() - since
    print('Took:', duration)
    print(f'Trying {try_}. Result: {res.text}')
