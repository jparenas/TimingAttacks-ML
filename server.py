"""
server.py

This file contains code to run a Flask server to add and check passwords.
"""

import os
from flask import Flask, request
from crypt_interface import EncryptInterface
import argparse


class UserApp():
    """
    This class contains an interface to bind an encryption interface with a
    Flask app.
    """

    def __init__(self, algo=None):
        self.interface = EncryptInterface(algo=algo)

    def create_app(self):
        # create and configure the app
        app = Flask(__name__, instance_relative_config=True)

        # a simple page that says hello
        @app.route('/')
        def hello():
            return 'Hello, World!'

        @app.route('/check', methods=['POST'])
        def check_password():
            password = request.form['password']
            return str(self.interface.check_password(password))

        @app.route('/add', methods=['POST'])
        def add_password():
            password = request.form['password']
            self.interface.add_password(password)

            return 'Done'

        return app


parser = argparse.ArgumentParser()
parser.add_argument('--algorithm', dest='algo', default=0, type=int,
                    help='index of the encryption algorithm')

args = parser.parse_args()
algo = args.algo

if __name__ == '__main__':
    app = UserApp(algo)
    app.create_app().run()
