# -*- coding: utf-8 -*-

"""
此為通用 API 模組
"""
import os
import json
import sys
import random
import itertools
import math
import traceback
def contains_key_and_has_value(check_dict, key):
	"""
	依據傳入的字典與鍵值，確認是否有此鍵且有值
	Returns:
		True: 有鍵值也有值
		False: 可能沒有鍵值或沒有值（None)
	"""
	if key in check_dict and check_dict[key]:
		return True
	return False



def stdout_encode(u, default='UTF8'):
	if sys.stdout.encoding:
		return u.encode(sys.stdout.encoding)
	return u.encode(default)

def get_relation_model_if_existed(relation_model):
	"""
	Check The Model (Relation Model) is exist or not
	e.g CountryInfo Model owns Currency relationship model
	Args:
		relation_model(DB Model): The db model
	Returns:
		relation model or None
	"""
	if relation_model:
		if hasattr(relation_model, 'id') and relation_model.id:
			return relation_model if relation_model.deleted_tag is False else None
		elif hasattr(relation_model, 'uuid') and relation_model.uuid:
			return relation_model if relation_model.deleted_tag is False else None
	return None


def generate_random_key(seed_rule, start, end=None):
	"""
	依照指定的亂數長度範圍參數，產生隨機網址碼
	Args:
		seed_rule(str):亂數的種子規則 e.g abcABC1234+
		start(int): 起始的長度
		end(int): 最長的長度 (如果沒有提供則為 start 的固定長度)
	Returns:
		url_key(str): 隨機網址碼 (長度 15 - 20)
	"""
	if end:
		url_length = random.randint(start, end)
	else:
		url_length = start
	# 產生使用者的隨機碼
	url_key = ''.join(random.sample(seed_rule, url_length))
	# 是唯一的，沒有衝突
	return url_key


def chunks(data_list, n):
	"""
	Yield successive n-sized chunks from data_list.
	e.g:
	list(chunks(range(10, 75), 10)))
	>> [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
	[20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
	[30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
	[40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
	[50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
	[60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
	[70, 71, 72, 73, 74]]
	"""
	for i in range(0, len(data_list), n):
		yield data_list[i:i + n]

def chunks_size(data_list, n):
	"""
	Yield successive n-sized chunks from data_list.
	e.g:
	list(chunks(range(10, 75), 10)))
	>> [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
	[20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
	[30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
	[40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
	[50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
	[60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
	[70, 71, 72, 73, 74]]
	"""
	size = (len(data_list) / n)
	if (len(data_list) % n) < 10:
		size += 1
	return size

def load_json_conifg(config_file_name):
	"""
	config_file_name(str): Config file name in visa api folder
	"""
	data = None
	json_path = os.path.join(os.path.dirname(__file__), config_file_name)
	with open(json_path) as json_data:
		data = json.load(json_data)
	return data


def two_lists_reverse_match(sample_list, match_list):
	"""
	反向從尾巴尋訪list。 根據 match_list 的資料 尋訪 smaple_list 有無一致
	如果 match_list 的長度 小於 smaple_list，則當 match_list 比對一致時也算作比對成功
	"""
	is_correct = True
	match_times = len(match_list)
	if sample_list > 0:
		for user_step, expected in itertools.izip(
			reversed(sample_list), reversed(match_list)):
			if user_step == expected:
				match_times -= 1
			else:
				is_correct = False
				break
		return True if is_correct and match_times == 0 else False
	return False


def is_first_list_in_second_list(first, second):
	"""
	檢查 first list 是否為 second list 的子集合
	Returns: (True | False)
	"""
	return set(first).issubset(set(second))

def floor_with_place(value, keep_decimal_place):
	"""
	無條件捨去小數點後 N 位
	Args:
		value(float): 數值
		keep_decimal_place(2): 要保留到小數點第幾位， e.g 2，表示保留到第二位，後面的位數則無條件捨去
	"""
	scale_value = math.floor(value * pow(10, keep_decimal_place))
	result = scale_value / pow(10, keep_decimal_place)
	return result
