# -*- coding: utf-8 -*-
import sys
import logging
from flask import Flask

reload(sys)
sys.setdefaultencoding('utf-8')
print 'new app => ' + sys.getdefaultencoding()

def create_app(config):
	"""
	init database db, and config
	"""
	app = Flask(__name__)
	app.config.from_object(config)
	
	from app import views
	app.register_blueprint(views.index_bp)
	return app
