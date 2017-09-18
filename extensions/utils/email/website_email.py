# -*- coding: utf-8 -*-
import traceback
from flask_mail import Message
from flask import render_template
from extensions import utils
from extensions.helper.exceptions import *
from extensions.utils.email import send_async_email


"""
該部分與使用者旅客使用完 Mobile 服務後的後續操作結果信件
"""

# 寄件人
SENDOR = 'addweup@gmail.com'
DEFAULT_RECEIVER = 'service@addweup.com'


def send_contact_to_us(
	site_source,
	email,
	name,
	reason,
	source,
	reveiver_emaillist=[DEFAULT_RECEIVER],
	phone=None,
	detail=''):
	"""
	官網訪客填寫聯繫我們，由 ADDWEUP 系統信件寄送給我們
	"""


	# 補上選擇的描述原因
	SUBJECT = '聯繫我們，原因：' + reason

	try:
		msg = Message(
			SUBJECT,
			sender=SENDOR,
			recipients=reveiver_emaillist
		)

		msg.html = render_template(
			'contact_email.html',
			site_source=site_source,
			name=name,
			email=email,
			reason=reason,
			source=source,
			phone=phone,
			detail=detail)

		send_async_email(msg, mail_worker_name='owl_website_mailhelper')
		return True
	except Exception as e:
		# # 加入 Traceback 訊息
		e = utils.get_traceback_msg(e)
		raise e
