# -*- coding: utf-8 -*-
import json
from datetime import datetime
from flask import request
from flask_script import Manager, Server
from flask_cors import CORS, cross_origin
from app import create_app
from settings import current_config
from scriptcmd.gunicorn_server import GunicornServer
from extensions.utils import datetime_ext
from extensions.helper.log import info_file_logger
application = create_app(current_config)
server = Server(host='0.0.0.0', port=current_config.SITE_PORT, threaded=True)
gunicorn = GunicornServer(host='0.0.0.0', port=current_config.SITE_PORT)

manager = Manager(application)
manager.add_command('runserver', server)
manager.add_command('gunicorn', gunicorn)

cors = CORS(application, resources={
	r"/naomi/*": {
		"origins": current_config.CORS_SITE
	}})



@application.before_request
def brefore():
	# 區隔用
	slack_dividing_line = '======================================================================\n'
	message = '<ENV：{}> || <UTC Time：{}> || <ENDPOINT：{}> || <HTTP：{}> || <Client IP：{}> | <Agent：{}>'.format(
		current_config.ENV_NAME, datetime_ext.convert_datetime_to_str(datetime.utcnow()),
		request.environ['PATH_INFO'], request.environ['REQUEST_METHOD'], request.remote_addr, request.headers.get('User-Agent')
	)
	info_file_logger.info(message)
	info_file_logger.info('Request json data：' + request.data)
	
if __name__ == '__main__':
	manager.run()
