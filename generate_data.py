import requests
import time
import random
import string
from server import UserApp
import subprocess
import csv
import os


def generate_random_string(length):
    return ''.join([random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(length)])

ALGO_DICT = {
    0: 'MD5',
    1: 'SHA256',
    2: 'SHA512'
}

N_REQUESTS = 10000
LENGTHS = [10, 32, 100, 320, 1000]

f = open('data/train.csv', 'w')
writer = csv.writer(f)
writer.writerow(['text', 'length', 'time', 'algo'])

for index, algo in ALGO_DICT.items():
    path = os.path.abspath('server.py')
    #print(path)
    proc = subprocess.Popen(['python', path, '--algorithm', str(index)],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    time.sleep(3)  # waiting for server to go up

    print('Server is up')

    # creating correct passwords
    for _ in range(100):
        requests.post(
            'http://127.0.0.1:5000/add',
            data={'password': generate_random_string(random.choice(LENGTHS))}
        )

    print('Finished creating actual passwords')

    # sending password attempts
    for i in range(N_REQUESTS):
        length = random.choice(LENGTHS)
        to_check = generate_random_string(length)
        since = time.time()
        res = requests.post(
            'http://127.0.0.1:5000/check',
            data={'password': to_check})
        duration = time.time() - since
        writer.writerow([to_check, length, duration, algo])

        if (i+1) % 100 == 0:
            print(f'Finished making {i+1} requests for {algo}')

    proc.kill()  # ending the Django server process

f.close()  # closing data file
