from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import sys

import requests
import json

import rsa

def my_app():
    (pubKey, privKey) = rsa.newkeys(2048)
    url = 'https://api.adviceslip.com/advice'
    r = requests.get(url)

    if r.status_code == 200: # Status: OK
        data = r.json()
        
        print(data['slip']['advice'])
        message = data['slip']['advice'].encode('utf8')
        return rsa.encrypt(message, pubKey), privKey

    else:
        print("Error!")
        

MY_APP = {
    'name': 'Advice',
    'init': my_app
}


if __name__ == '__main__':
    my_app()