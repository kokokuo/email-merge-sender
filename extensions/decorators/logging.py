# -*- coding: utf-8 -*-
import httplib
import requests
from flask import request
import socket
import traceback
import json
from functools import wraps
from flask_restful import abort
from extensions.helper.error import *
from extensions import utils
from extensions.helper.log import info_file_logger
from extensions.helper.log import info_logstash_logger
from settings import current_config as config
"""
端點日誌紀錄裝飾器
分成 get, post, patch, delete
"""
def get_request_info():
	req_info = {
		"env": config.ENV_NAME,
		"client_ip": request.remote_addr,
		"http_method": request.environ['REQUEST_METHOD'],
		"endpoint": request.environ['PATH_INFO'],
		"agent": request.headers.get('User-Agent'),
		"req_data": request.data
	}
	return req_info

def get_logging_handler(get_func):
	"""
	GET 的日誌記錄器
	"""
	@wraps(get_func)
	def wrapper(*args, **kwargs):
		result = get_func(*args, **kwargs)
		info_file_logger.info('Reponse: Code = {}, Data: {}'.format(result[1], result[0]))
		# logstash 
		req_info = get_request_info()
		req_info['code'] = result[1]
		info_logstash_logger.info(result[0], extra=req_info)

		return result
	return wrapper

def post_logging_handler(post_func):
	"""
	POST 的日誌記錄器
	"""
	@wraps(post_func)
	def wrapper(*args, **kwargs):
		result = post_func(*args, **kwargs)
		info_file_logger.info('Reponse: Code = {}, Data: {}'.format(result[1], result[0]))
		# logstash 
		req_info = get_request_info()
		req_info['code'] = result[1]
		info_logstash_logger.info(result[0], extra=req_info)

		return result
	return wrapper

def patch_logging_handler(patch_func):
	"""
	PATCH 的日誌記錄器
	"""
	@wraps(patch_func)
	def wrapper(*args, **kwargs):
		result = patch_func(*args, **kwargs)
		info_file_logger.info('Reponse: Code = {}, Data: {}'.format(result[1], result[0]))
		# logstash 
		req_info = get_request_info()
		req_info['code'] = result[1]
		info_logstash_logger.info(result[0], extra=req_info)

		return result
	return wrapper

def delete_logging_handler(delete_func):
	"""
	DELETE 的日誌記錄器
	"""
	@wraps(delete_func)
	def wrapper(*args, **kwargs):
		result = delete_func(*args, **kwargs)
		info_file_logger.info('Reponse: Code = {}, Data: {}'.format(result[1], result[0]))
		# logstash 
		req_info = get_request_info()
		req_info['code'] = result[1]
		info_logstash_logger.info(result[0], extra=req_info)
		return result
	return wrapper
