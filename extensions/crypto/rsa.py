from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto import Random
import base64

class RSA_HELPER(object):
    def __init__(self):
        print 'init'

    def generator(self, size=8192):
        random_generator = Random.new().read
        key = RSA.generate(size, random_generator)
        public = key.publickey()
        result = {
            'private_key': base64.b64encode(key.exportKey()),
            'public_key': base64.b64encode(public.exportKey())
        }
        return result

    def encrypt(self, public_key=None, json_data=None):
        """
        The encrypt data need to did base64 first and got base64 type result
        Args:
            public_key(base64): public key
            json_data(base64): source data (json format)
        Returns:
            encrypted(base64): The Base64 RSA Encrypt Data
        """
        if public_key and json_data:
            rsakey = RSA.importKey(base64.b64decode(public_key))
            rsakey = PKCS1_v1_5.new(rsakey)
            encrypted = rsakey.encrypt(base64.b64encode(json_data))
            encrypted = base64.b64encode(encrypted)
            return encrypted
        return None

    def decrypt(self, private_key=None, base64_data=None):
        """
        Decrypt data by private key
        Args:
            private_key(base64): private key from machine
            base64_data(base64): source data (encrypt)
        Returns:
            result(json): The decrypt json source data
        """
        if private_key and base64_data:
            rsakey = RSA.importKey(base64.b64decode(private_key))
            rsakey = PKCS1_v1_5.new(rsakey)
            decrypted = rsakey.decrypt(base64.b64decode(base64_data), 'Decryption Error')
            return base64.b64decode(decrypted)
        return None
rsa_helper = RSA_HELPER()
