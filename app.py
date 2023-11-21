# from cryptography.fernet import Fernet
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import utils
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.backends import default_backend
# import sys

import requests
import json

# def doEncrypt(msg, pvt_key_file, pub_key_file, enc_file):
#     print(f"Message: {msg}")
#     print("")

#     # Symmetric Key Encryption
#     # print("Generating symmetric key")
#     # print("")
#     # key = Fernet.generate_key()
#     # print("key", key)
#     # print("")

#     # Save Symmetric Key to File
#     # with open(sym_key_file, "wb") as key_file:
#     #     key_file.write(key)

#     # # Fernet uses AES in CBC mode
#     # # https://cryptography.io/en/latest/fernet/
#     # cipher_suite = Fernet(key)
#     # encrypted_msg = cipher_suite.encrypt(msg)

#     # h = hashes.SHA256()
#     # hasher = hashes.Hash(h)
#     # hasher.update(encrypted_msg)
#     # digest = hasher.finalize()
#     # print(f"Digest: {digest}")

#     # Asymmetric Key Encryption
#     print("Generating key pair")
#     print("")
#     private_key = rsa.generate_private_key(
#         public_exponent=65537,
#         key_size=2048,
#     )

#     # Print Private Key
#     private_pem = private_key.private_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PrivateFormat.PKCS8,
#         encryption_algorithm=serialization.NoEncryption()
#     )
#     # print(f"Private Key: {private_pem}")
#     # print("")

#     public_key = private_key.public_key()

#     # Print Public Key
#     public_pem = public_key.public_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PublicFormat.SubjectPublicKeyInfo
#     )


#     # Save Private Key to File
#     print("Writing Private and Public key files\n")
#     with open(pvt_key_file, "wb") as key_file:
#         key_file.write(private_pem)

#     # Save Private Key to File
#     with open(pub_key_file, "wb") as key_file:
#         key_file.write(public_pem)

#     # Encrypted hash is 256 bytes since RSA Private key is 2048 bits
#     encrypted_hash = private_key.sign(
#         digest,
#         padding.PSS(
#             mgf=padding.MGF1(hashes.SHA256()),
#             salt_length=padding.PSS.MAX_LENGTH
#         ),
#         utils.Prehashed(h)
#     )

#     # Append the 256 byte hash to the start of the message
#     signed_enc_msg =  encrypted_hash + encrypted_msg
#     print(f"len enc hash: {len(encrypted_hash)}")
#     print(f"len signed enc hash: {len(signed_enc_msg)}")
#     #print(f"signed_enc_msg: {signed_enc_msg}")
#     # Save Encrypted Text to File
#     with open(enc_file, "wb") as bin_file:
#         bin_file.write(signed_enc_msg)


# def doDecrypt(enc_sign_file, sign_key_file, out_msg_file):

#     # Read Encrypted Text from File
#     with open(enc_sign_file, "rb") as bin_file:
#         raw_contents = bin_file.read()
#         # Separate the hash and the remaining part of the message
#         recv_encrypted_hash = raw_contents[0: 256]  # fill me in - remember we can splice with [start:end]
#         recv_encrypted_msg =  raw_contents[256: -1]  # fill me in - remember we can splice with [start:end]

#     # Read Necessary Public/Private Signature Key from File
#     with open(sign_key_file, "rb") as key_file:
#         # Use the appropriate function "load_pem_private_key" or
#         # "load_pem_public_key"
#         sign_key = serialization.load_pem_public_key(  # fill in the appropriate function name.
#             key_file.read(),
#             backend=default_backend()
#         )

#     # Hash non-signature portion of the encrypted message
#     h = hashes.SHA256()
#     hasher = hashes.Hash(h)
#     hasher.update(recv_encrypted_msg)                # fill me in - what should we hash?
#     digest = hasher.finalize()
#     print(f"Digest: {digest}")

#     # raises an InvalidSignature exception if signatures don't match
#     # Use the sign_key.verify() function
#     sign_key.verify(
#         ??????,              # fill me in
#         ??????,              # fill me in
#         padding.PSS(
#             mgf=padding.MGF1(hashes.SHA256()),
#             salt_length=padding.PSS.MAX_LENGTH
#         ),
#         utils.Prehashed(h)
#     )
#     print("Success: received and computed digest match!")


#     # print("Decrypt message")
#     # with open(sym_key_file, "rb") as key_file:
#     #     key = key_file.read()

#     # Now that we've verified the signature, decrypt the message content

#     # some code here
#     decrypted_text = # call the decrypt function appropriate to produce decrypted_text

#     print(f"Decrypted Text: {decrypted_text}")
#     print("")

#     # Save the decrypted message
#     with open(out_msg_file, "w") as out_file:
#         out_file.write(str(decrypted_text, 'utf-8'))

def my_app():
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