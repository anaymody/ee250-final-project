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


def genkeys():
    # generate public and private keys with 
    # rsa.newkeys method,this method accepts 
    # key length as its parameter
    # key length should be atleast 16
    publicKey, privKey = rsa.newkeys(512)

    global privateKey
    privateKey = privKey

    publicKeyFile = open("publicKeyFile.txt", "w")

    publicKeyFile.write(str(publicKey))

    publicKeyFile.close()

def encrypt(message):
    # this is the string that we will be encrypting

    # rsa.encrypt method is used to encrypt 
    # string with public key string should be 
    # encode to byte string before encryption 
    # with encode method
    encMessage = rsa.encrypt(message.encode(), 
                            privateKey)

    print("original string: ", message)
    print("encrypted string: ", encMessage)
    return encMessage

def decrypt(publicKey, encMessage):
    # the encrypted message can be decrypted 
    # with ras.decrypt method and private key
    # decrypt method returns encoded byte string,
    # use decode method to convert it to string
    # public key cannot be used for decryption
    decMessage = rsa.decrypt(encMessage, publicKey).decode()

    print("decrypted string: ", decMessage)
    return decMessage

def my_app():
    genkeys()
    url = 'https://api.adviceslip.com/advice'
    r = requests.get(url)

    if r.status_code == 200: # Status: OK
        data = r.json()
        
        print(data['slip']['advice'])
        return data['slip']['advice']

    else:
        print("Error!")
        

# def myapp_init():
#     advice = myapp()

#     output = f"Open: ${day_open}, High: ${day_high}, Close: ${day_close}"
#     print('Information for {}: {}'.format(SYMBOL, output))

    
#     return output


MY_APP = {
    'name': 'Advice',
    'init': my_app
}


if __name__ == '__main__':
    my_app()