# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
# decodebytes

class RsaSignHelper(object):
    """
    數位簽章，對支付的部分都採用此簽法
    """
    def __init__(self):
        print('RSA_HELPER init')

    def signData(self, private_key, data):
        '''
        param: private_key_loc Path to your private key
        param: package Data to be signed
        return: base64 encoded signature
        '''

        print "sign data:", data

        key = b64decode(private_key)
        rsakey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsakey)
        digest = SHA256.new()
        # 簽之前要把字串轉成byte string
        digest.update(data.encode("utf-8"))
        sign = signer.sign(digest)
        return b64encode(sign)

    def verifySign(self, public_key, signature, data):
        '''
        Verifies with a public key from whom the data came that it was indeed
        signed by their private key
        param: public_key_loc Path to public key
        param: signature String signature to be verified
        return: Boolean. True if the signature is valid; False otherwise.
        '''
        print "vertify data:", data

        pub_key = b64decode(public_key)
        rsakey = RSA.importKey(pub_key)
        signer = PKCS1_v1_5.new(rsakey)
        digest = SHA256.new()
        # 驗證之前要把字串轉成byte string
        digest.update(data.encode('utf-8'))
        # if signer.verify(digest, decodebytes(signature.encode("utf-8"))):
        if signer.verify(digest, b64decode(signature.encode("utf-8"))):
            return True
        return False


rsa_sign_helper = RsaSignHelper()
