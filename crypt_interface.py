"""
crypt_interface.py

Author: Quan Nguyen
This interface contains multiple methods to encrypt and decrypt a message.
"""

# Built-in libraries
import random
import string

# Third-party libraries
from Crypto.Cipher import AES, Blowfish, DES
from Crypto.Hash import MD5, SHA256, SHA512
from Crypto.PublicKey import RSA


# Global variables
JOB_TO_CHOICES = {
    'cipher': [AES, Blowfish, DES],
    'hash': [MD5, SHA256, SHA512],
    'public-key': [RSA]
}

class MyInterface():
    """
    This class takes in a string in its constructor to specify the job to be
    done, which has to be one of 'cipher', 'hash', or 'public-key'.
    A random algorithm will then be selected with respect to the job.
    """
    def __init__(self, job=None):
        # checking for invalid values for job
        if job not in JOB_TO_CHOICES:
            message = 'Invalid job type.' + \
                      f'Please choose among {JOB_TO_CHOICES.keys()}'
            raise ValueError(message)

        self.job = job
        self.algo = random.choice(JOB_TO_CHOICES[job])

        if job == 'cipher':
            key = None  # some random string
