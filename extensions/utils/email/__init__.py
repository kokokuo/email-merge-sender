# -*- coding: utf-8 -*-
from flask import copy_current_request_context
from flask_mail import Mail
from extensions.helper.exceptions import *
import threading


"""
此部分與商家、旅客有關，涵蓋 商家後台端與店家端的信件
"""

mail = Mail()

def send_async_email(msg, mail_worker_name='owl_mailhelper'):

	@copy_current_request_context
	def send_async(msg):
		mail.send(msg)

	thr = threading.Thread(name=mail_worker_name, target=send_async, args=(msg,))
	thr.start()


def get_email_locale_code(locale_code, locale_email_template):
	"""
	取得信件的內容顯示語系，如果不存在此語系，則一律回傳英文 en
	Args:
		locale_code(str): 要顯示的語系
		locale_email_template(str): 目前信件內容支持的語系
	Return:
		email_locale_code(str)
	"""
	try:
		email_locale_code = locale_code.lower()
		if locale_code.lower() not in locale_email_template:
			email_locale_code = 'en'
	except Exception as e:
		email_locale_code = 'en'

	return email_locale_code
# def send_user_url_portal(
# 	dns_url,
# 	receiver_email,
# 	portal_url_key='',
# 	url_password='',
# 	location='',
# 	stored_money='0.00',
# 	transfer_money='0.00',
# 	native_currency_code='',
# 	transfer_currency_code='',
# 	language_locale_code='',
# 	created_time=None,
# 	expired_time=None,
# 	timezone=None):
# 	"""
# 	寄送唯一隨機網址與密碼給使用者，使得使用者可以執行後續操作
# 	Args:
# 		dns_url(str): 網站伺服器的網址 DNS
# 		receiver_email(str): 收件者信件，也就是使用者輸入的信箱
# 		portal_url_key(str): 使用者登入網址的唯一隨機辨識碼
# 		url_password(str): 使用者登入 Portal 時的對應數字密碼
# 		location(unicode): 機台位置
# 		stored_money(str): 投入的金額
# 		transfer_money(str): 轉換後的金額
# 		native_currency_code(str): 原先投入的幣別碼 e.g HKD, USD, TWD, JPY, CNY
# 		transfer_currency_code(str): 轉換的幣別碼 e.g HKD, USD, TWD, JPY, CNY
# 		language_locale_code(str): 要顯示的語系: e.g zh_tw, en, zh_cn...
# 		expired_time(datetime): 過期的時間(UTC)
# 		timezone(str): 使用者的國家時區(採用 tz database 格式 e.g Asia/Taipei, US/Pacific)
# 	"""
# 	locale_email_template = ['en', 'zh_tw', 'zh_cn', 'ja_jp', 'ko_kr', 'ko']
# 	locale_subject = {
# 		'en': 'Thanks for using ADDWEUP, your left currency in \
# 			{location} Airport is already exchanged to {transfer_money} {currency_code}',
# 		'zh_tw': '謝謝使用ADDWEUP, \
# 			您在{location}投入的剩餘外幣已經轉成{transfer_money} {currency_code}',
# 		'zh_cn': '谢谢使用ADDWEUP, \
# 			您在{location}投入的剩余外币已经转成{transfer_money} {currency_code}',
# 		'ja_jp': 'ADDWEUPをご利用いただき、ありがとうございました。\
# 			{location}で入れていただいた通貨は{transfer_money}円{currency_code}に両替されました。',
# 		'ko': '애드위업을 이용해주셔서 감사합니다. 귀하는 {location} \
# 			공항에서 투입한 화폐가 {transfer_money} {currency_code} (으)로 환전이 되었습니다.',
# 		'ko_kr': '애드위업을 이용해주셔서 감사합니다. 귀하는 {location} \
# 			공항에서 투입한 화폐가 {transfer_money} {currency_code} (으)로 환전이 되었습니다.',
# 	}
# 	try:
# 		# 時間轉換
# 		local_expired_time = ''
# 		local_created_time = ''
# 		if expired_time and timezone:
# 			if not isinstance(expired_time, datetime.datetime):
# 				# 轉換成 datetime 格式
# 				expired_time = parser.parse(expired_time)
# 			local_expired_time = datetime_ext.convert_utc_to_localtime(
# 				expired_time, timezone)

# 		if created_time and timezone:
# 			if not isinstance(created_time, datetime.datetime):
# 				# 轉換成 datetime 格式
# 				created_time = parser.parse(created_time)
# 			local_created_time = datetime_ext.convert_utc_to_localtime(
# 				created_time, timezone)


# 		# Check locale_code is exist, if not, use en be default
# 		try:
# 			email_locale_code = language_locale_code.lower()
# 			if language_locale_code.lower() not in locale_email_template:
# 				email_locale_code = 'en'
# 		except Exception, e:
# 			email_locale_code = 'en'
# 		# 'Your number password = ' + url_password + '\n' \

# 		SUBJECT = locale_subject[email_locale_code].format(
# 			location=location,
# 			transfer_money=transfer_money,
# 			currency_code=transfer_currency_code
# 		)
# 		msg = Message(
# 			SUBJECT,
# 			sender=SENDOR,
# 			recipients=[
# 				receiver_email
# 			]
# 		)

# 		msg.body = render_template(
# 			'portal_email/{locale}.txt'.format(locale=email_locale_code),
# 			location=location,
# 			created_time=datetime_ext.convert_datetime_to_str(local_created_time),
# 			stored_money=stored_money,
# 			native_currency_code=native_currency_code,
# 			transfer_money=transfer_money,
# 			transfer_currency_code=transfer_currency_code,
# 			portal_url=dns_url + '/' + portal_url_key,
# 			expire_time=datetime_ext.convert_datetime_to_str(local_expired_time))

# 		# HTML Format
# 		msg.html = render_template(
# 			'portal_email/{locale}.html'.format(locale=email_locale_code),
# 			location=location,
# 			created_time=datetime_ext.convert_datetime_to_str(local_created_time),
# 			stored_money=stored_money,
# 			native_currency_code=native_currency_code,
# 			transfer_money=transfer_money,
# 			transfer_currency_code=transfer_currency_code,
# 			portal_url=dns_url + '/' + portal_url_key,
# 			expire_time=datetime_ext.convert_datetime_to_str(local_expired_time))

# 		send_async_email(msg)

# 		return True
# 	except Exception as e:
# 		raise SendEmailException(detail_msg=e)


# def send_testing_email(
# 	receiver_email,
# 	language_locale_code='',
# 	location='',
# 	timezone=None):
# 	"""
# 	寄送測試信件給使用者
# 	receiver_email(str): 收件者信件，也就是使用者輸入的信箱
# 	location(unicode): 機台位置
# 	language_locale_code(str): 要顯示的語系: e.g zh_tw, en, zh_cn...
# 	timezone(str): 使用者的國家時區(採用 tz database 格式 e.g Asia/Taipei, US/Pacific)
# 	"""
# 	try:

# 		locale_email_template = ['en', 'zh_tw', 'zh_cn', 'ja_jp', 'ko_kr', 'ko']
# 		locale_subject = {
# 			'en': 'Hello, Welcome to use ADDWEUP,this email sent in  \
# 				{location} at {current_time} to make sure you can receivce and finish our service',
# 			'zh_tw': '歡迎使用ADDWEUP, 這封信件在 {current_time} 從 {location} 寄出 \
# 				，確保您可以收到此信，完成後續的服務',
# 			'zh_cn': '欢迎使用ADDWEUP, 这封信件在 {current_time} 从 {location} 寄出 \
# 				，确保您可以收到此信，完成后续的服务',
# 			'ja_jp': 'Hello, Welcome to use ADDWEUP,this email sent in  \
# 				{location} at {current_time} to make sure you can receivce and finish our service',
# 			'ko': 'Hello, Welcome to use ADDWEUP,this email sent in  \
# 				{location} at {current_time} to make sure you can receivce and finish our service',
# 			'ko_kr': 'Hello, Welcome to use ADDWEUP,this email sent in  \
# 				{location} at {current_time} to make sure you can receivce and finish our service',
# 		}

# 		# 時間時區轉換
# 		current_time = datetime.datetime.utcnow()
# 		if timezone:
# 			current_time = datetime_ext.convert_utc_to_localtime(
# 				current_time, timezone)

# 		current_time = current_time.strftime('%Y-%m-%d %H:%M:%S %z %Z')
# 		# Check locale_code is exist, if not, use en be default
# 		try:
# 			email_locale_code = language_locale_code.lower()
# 			if language_locale_code.lower() not in locale_email_template:
# 				email_locale_code = 'zh_tw'
# 		except Exception, e:
# 			email_locale_code = 'zh_tw'
# 		# 'Your number password = ' + url_password + '\n' \


# 		SUBJECT = locale_subject[email_locale_code].format(
# 			location=location,
# 			current_time=current_time)

# 		msg = Message(
# 			SUBJECT,
# 			sender=SENDOR,
# 			recipients=[
# 				receiver_email
# 			]
# 		)
# 		msg.body = render_template(
# 			'testing_email/{locale}.txt'.format(locale=email_locale_code),
# 			location=location,
# 			current_time=current_time)

# 		msg.html = render_template(
# 			'testing_email/{locale}.html'.format(locale=email_locale_code),
# 			location=location,
# 			current_time=current_time)

# 		send_async_email(msg)
# 		return True
# 	except Exception as e:
# 		raise SendEmailException(detail_msg=e)


