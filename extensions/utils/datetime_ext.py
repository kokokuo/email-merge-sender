# -*- coding: utf-8 -*-
import datetime
import pytz
"""
日期時間擴充功能
"""


# 日期格式， e.g 2002-10-27 06:00:00 EST-0500
FMT = '%Y-%m-%d %H:%M:%S %Z%z'

def convert_utc_to_localtime(utc_datetime, timezone_str):
	"""
	轉換 utc 時間為指定的 local 時間，如果輸入的時區有錯，則保持原來的 UTC
	Args:
		utc_datetime(datetime): utc 時間
		timezone(str): 指定轉換的時區，採用 tz database 列表
	Returns
		timezone_dt(datetime): 回傳轉換好的時區時間
	"""
	# 取得 tzinfo 的時區
	if timezone_str in pytz.common_timezones:
		tz = pytz.timezone(timezone_str)
		# 取得時區資訊的 dateime
		dateime_include_tzinfo = pytz.utc.localize(utc_datetime, is_dst=None)
		timezone_dt = dateime_include_tzinfo.astimezone(tz)
		return timezone_dt
	return utc_datetime


def convert_localtime_to_utc(local_datetime, timezone_str):
	"""
	轉換 local 時間為指定的 utc 時間，如果輸入的時區有錯，則保持原來的 LOCAL
	Args:
		local_datetime(datetime): local 時間
		timezone(str): 指定轉換的時區，採用 tz database 列表
	Returns
		utc_dt(datetime): 回傳轉換的utc時間
	"""
	if timezone_str in pytz.common_timezones:
		local = pytz.timezone(timezone_str)
		# local 時區加入到時間中
		local_dt = local.localize(local_datetime, is_dst=None)
		utc_dt = local_dt.astimezone(pytz.utc)
		return utc_dt

	return local_datetime

def convert_datetime_to_str(datetime_obj, format=FMT):
	"""
	轉換成字串
	預設的格式：FMT = '%Y-%m-%d %H:%M:%S %Z%z'
	"""
	if datetime_obj:
		return datetime_obj.strftime(format)
	return None

def convert_str_to_datetime(datetime_str, format=FMT):
	"""
	字串轉換成時間
	字串預設可支援的格式：FMT = '%Y-%m-%d %H:%M:%S %Z%z'
	"""
	if datetime_str:
		return datetime.datetime.strptime(datetime_str, format)
	return None


def is_timeover(check_datetime):
	"""
	依據傳入的時間，驗證是否此時間已經超過現在
	Args:
		check_datetime(datetime): 要傳入檢查的時間
	Returns:
		(bool): 超過 -> True, 尚未超過現在時間 -> False
	"""
	utc_now_seconds = datetime.datetime.utcnow()
	delta = check_datetime - utc_now_seconds
	seconds_interval = delta.total_seconds()
	if seconds_interval > 0.0:
		return True
	return False


def format_to_time_range(begin_hour, begin_minute, end_hour, end_minute):
	"""
	格式化起始時間與結束時間為時間範圍，輸入起始的小時與分鐘，結束的小時與分鐘，格式化為
	{:02}:{:02} - {:02}:{:02}, e.g 07:22 - 22:17
	如果資料沒有給齊，會回傳 None
	Args:
		begin_hour(int): 開始的小時 e.g 7
		begin_minute(int): 開始的分鐘 e.g 22
		end_hour(int):結束的小時 e.g 12
		end_minute(int):結束的分鐘 e.g 45
	Returns:
		time_range(str): 回傳時間範圍的格式 e.g 07:22 - 22:17 
	"""
	TIME_FORMAT = "{:02d}:{:02d}"
	time_range = None
	if begin_hour and end_hour:
		begin_biz_time = begin_hour
		end_biz_time = end_hour

		if begin_minute:
			begin_biz_time = TIME_FORMAT.format(begin_biz_time, begin_minute)
		else:
			begin_biz_time = TIME_FORMAT.format(begin_biz_time, 0)

		if end_minute:
			end_biz_time = TIME_FORMAT.format(end_biz_time, end_minute)
		else:
			end_biz_time = TIME_FORMAT.format(end_biz_time, 0)

		time_range = '{} - {}'.format(begin_biz_time, end_biz_time)
	return time_range