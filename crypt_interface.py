"""
crypt_interface.py

This interface contains multiple methods to encrypt and decrypt a message.
"""

# Built-in libraries
import random
import string

# Third-party libraries
from Crypto.Hash import MD5, SHA256, SHA512

# TODO: add in bcrypt


# Global variables
ALGOS = [MD5, SHA256, SHA512]  # list of encryption algorithms to be used
LENGTH = 20  # length for randomly generated salt

class EncryptInterface():
    """
    This class provides an interface to store and check passwords.

    If not prvovided an encryption algorithm when initialized, a random one
    will be chosen from the global variable `ALGOS` above. An interface object
    will store a number of correct (salted and hashed) passwords in a
    dictionary (so that look-up time can be O(1)).
    """
    def __init__(self, algo=None):
        # choose a random algorithm from `ALGOS`
        if algo is None:
            self.algo = random.choice(ALGOS)
            algo_str = str(self.algo).split()[1].split('.')[-1][:-1]
            print('Using', algo_str)
        else:
            self.algo = algo

        self.passwords = {}  # dictionary for O(1) look-up time
        self.salt = generate_random_string(LENGTH)

    def run(self):
        """To be used for debugging purposes"""
        while True:
            input_ = input('Enter password: ')
            if self.check_password(input_):
                print('Password correct!')
                break

            print('Try again...')

    def digest_string(self, string):
        """Salt and decrypt a string"""
        string += self.salt
        string = string.encode('ascii')
        string = self.algo.new(string).hexdigest()

        return string

    def add_password(self, password):
        """Add a password in the dictionary of correct passwords"""
        self.passwords[self.digest_string(password)] = True

    def check_password(self, to_check):
        """
        Check to see if a specific string is in the dictionary of correct
        passwords
        """
        return self.digest_string(to_check) in self.passwords


def generate_random_string(length):
    """
    Generate a random string of a specific length, consisting of upper-case
    characters and numbers
    """
    return ''.join([random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(length)])


if __name__ == '__main__':
    interface = EncryptInterface()
    interface.add_password('apple')
    interface.add_password('qwe123')
    interface.add_password('12345679')

    interface.run()
