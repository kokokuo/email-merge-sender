# from utils import email
from flask import Blueprint, render_template

APP_PORTAL_BLUEPRINT = 'app_portal'

index_bp = Blueprint(
	__name__,
	APP_PORTAL_BLUEPRINT)

@index_bp.route('/')
def index():
	return render_template('index.html')


@index_bp.route('/template/mail/keypair')
def mail_matched_template():
	return render_template('matched.html')
