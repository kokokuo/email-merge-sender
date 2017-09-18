# -*- coding: utf-8 -*-
import os
import struct
from Crypto.Cipher import AES
from Crypto import Random
import base64

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class AES_HELPER(object):
	def __init__(self):
		print 'init'

	def key_generator(self, bits=256):
		random = Random.new()
		key = random.read(bits / 8)
		return base64.b64encode(key)

	def iv_generator(self):
		'''
		AES Initialization Vector is 128 bits(16 bytes).
		'''
		random = Random.new()
		key = random.read(16)
		return base64.b64encode(key)

	def encrypt(self, b64key, b64iv, data):
		key = base64.b64decode(b64key)
		iv = base64.b64decode(b64iv)

		cryptor = AES.new(key, AES.MODE_CBC, iv)
		data = pad(data)
		encrypted = cryptor.encrypt(data)
		encrypted = base64.b64encode(encrypted)
		return encrypted

	def decrypt(self, b64key, b64iv, data):
		key = base64.b64decode(b64key)
		iv = base64.b64decode(b64iv)

		cryptor = AES.new(key, AES.MODE_CBC, iv)
		decrypted = base64.b64decode(data)
		decrypted = cryptor.decrypt(decrypted)
		decrypted = unpad(decrypted)
		return decrypted

	def encrypt_filestream(self, b64key, b64iv, in_file_obj):
		""" Encrypts a file using AES (CBC mode) with the
			given key.

			key:
				The encryption key - a string that must be
				either 16, 24 or 32 bytes long. Longer keys
				are more secure.

			in_file_obj:
				Name of the input file

			chunksize:
				Sets the size of the chunk which the function
				uses to read and encrypt the file. Larger chunk
				sizes can be faster for some files and machines.
				chunksize must be divisible by 16.
		"""
		key = base64.b64decode(b64key)
		iv = base64.b64decode(b64iv)
		cryptor = AES.new(key, AES.MODE_CBC, iv)
		file_stream = in_file_obj.read()

		data = pad(file_stream)
		encrypted = cryptor.encrypt(data)
		encrypted = base64.b64encode(encrypted)
		return encrypted

	def decrypt_filestream(self, b64key, b64iv, b64data):

		key = base64.b64decode(b64key)
		iv = base64.b64decode(b64iv)
		cryptor = AES.new(key, AES.MODE_CBC, iv)
		decrypted = base64.b64decode(b64data)
		decrypted = cryptor.decrypt(decrypted)
		decrypted = unpad(decrypted)
		return decrypted


aes_helper = AES_HELPER()
