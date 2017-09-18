# -*- coding: utf-8 -*-
import base64

def encode2b64(source):
	"""
	encode source twice base64
	"""
	code = base64.b64encode(base64.b64encode(source))
	return code

def decode2b64(source):
	"""
	decode source twice base64
	"""
	key = base64.b64decode(base64.b64decode(source))
	return key