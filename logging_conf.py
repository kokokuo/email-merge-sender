# -*- coding: utf-8 -*-
from settings import current_config as config

LOGGING_CONF = {
	'version': 1,
	'disable_existing_loggers': False,
	"root": {
		"level": "NOTSET",
		"handlers": ["console"]
	},
	"loggers": {
		"info_file": {
			"level": "INFO",
			"handlers": [
				"info_file_handlers",
			]
		},
		"exception_file": {
			"level": "WARNING",
			"handlers": [
				"excep_file_handlers",
			]
		},
		"info_logstash": {
			"level": "INFO",
			"handlers": [
				"info_logstash_handlers",
			]
		},
		"exception_logstash": {
			"level": "WARNING",
			"handlers": [
				"excep_logstash_handlers",
			]
		},

	},
	"formatters": {
		"simple": {
			"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
		},
		"detail": {
			"format": "==== [pid %(process)d] %(levelname)s: %(asctime)s <%(module)s>(line %(lineno)d) -- %(name)s ====\n$> %(message)s",
			"datefmt": ""
		}
	},
	"handlers": {
		"console": {
			"class": "logging.StreamHandler",
			"level": "DEBUG",
			"formatter": "simple",
			"stream": "ext://sys.stdout"
		},
		# Files Handlers
		"info_file_handlers": {
			"class": "logging.handlers.TimedRotatingFileHandler",
			"level": "INFO",
			"formatter": "detail",
			"filename": "logs/info.log",
			"when": 'h',
			"interval": 12,
			"backupCount": 20,
			"encoding": "utf8",
			"utc": True
		},
		"excep_file_handlers": {
			"class": "logging.handlers.TimedRotatingFileHandler",
			"level": "WARNING",
			"formatter": "detail",
			"filename": "logs/exception.log",
			"when": 'h',
			"interval": 12,
			"backupCount": 20,
			"encoding": "utf8",
			"utc": True
		},
		# LogStash handlers
		"info_logstash_handlers": {
			'level': 'INFO',
			'class': 'logstash.TCPLogstashHandler',
			'host': config.LOGSTASH_HOST,
			'port': config.LOGSTASH_PORT, # Default value: 5959
			'version': 1, # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
			'message_type': config.LOGSTASH_TYPE,  # 'type' field in logstash message. Default value: 'logstash'.
			'fqdn': True, # Fully qualified domain name. Default value: false.
			# 'tags': [config.ENV_NAME], # list of tags. Default: None.
		},
		"excep_logstash_handlers": {
			'level': 'ERROR',
			'class': 'logstash.TCPLogstashHandler',
			'host': config.LOGSTASH_HOST,
			'port': config.LOGSTASH_PORT, # Default value: 5959
			'version': 1, # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
			'message_type': config.LOGSTASH_TYPE,  # 'type' field in logstash message. Default value: 'logstash'.
			'fqdn': True, # Fully qualified domain name. Default value: false.
			# 'tags': [config.ENV_NAME], # list of tags. Default: None.
		},
		
	}

}