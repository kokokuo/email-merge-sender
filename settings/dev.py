# -*- coding: utf-8 -*-
import os
import string
class Config(object):
	DEBUG = True
	ENV_NAME = 'dev'
	
	# CORS SITE : 設定只有哪些網址可以連入
	CORS_SITE = [
		'http://localhost:3000',
		'http://localhost:3010',

		'https://dev.business.uchange2.com',
	]

	SITE_PORT = '7002'

	# LogSash 相關設定
	LOGSTASH_HOST = '10.0.20.143'
	# 9002 -> tcp for python-logstash, 9001 -> filebeat, 9000 -> http for restful
	LOGSTASH_PORT = 9002
	LOGSTASH_TYPE = 'naomiwork' + '@' + ENV_NAME