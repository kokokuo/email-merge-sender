# -*- coding: utf-8 -*-
import os
import copy
import json
import httplib
import requests
import logging
import logging.config
import threading
from logging_conf import LOGGING_CONF
from settings import current_config as config

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s [in %(pathname)s:%(lineno)d]'

		
class LogManager(object):
	"""
	docstring for Logger
	"""
	def __init__(
		self,
		conf_name=None,
		default_name='default_app',
		default_level=logging.INFO,
		default_filename='basic.log',
		log_format=LOG_FORMAT):

		# log manager, save kinds of loggers
		self._loggers = {}
		if conf_name:
			logging.config.dictConfig(conf_name)


	def get_logger(self, name):
		logger = logging.getLogger(name)
		if logger:
			self._loggers[logger.name] = logger
		return self._loggers[name]

	def get_loggers(self):
		return self._loggers

log_manager = LogManager(conf_name=LOGGING_CONF)

"""
Get log object from configuration
"""
info_file_logger = log_manager.get_logger('info_file')
excep_file_logger = log_manager.get_logger('exception_file')

info_logstash_logger = log_manager.get_logger('info_logstash')
excep_logstash_logger = log_manager.get_logger('exception_logstash')
