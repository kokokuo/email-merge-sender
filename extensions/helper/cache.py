# -*- coding: utf-8 -*-
import redis
from extensions.helper.exceptions import *
from settings import current_config as config
import json

class RedisCache(object):
	def __init__(self, **redis_kwargs):
		self._pool = redis.ConnectionPool(**redis_kwargs)
		self._redis = redis.Redis(connection_pool=self._pool)

	def get_json(self, key, source=None, expire_seconds=None):
		"""
		Read-through
		"""
		result = self._redis.get(str(key))
		if result is None:
			if source:
				data = None
				# 可以是方法或是資料
				if callable(source):
					data = json.dumps(source())
				else:
					data = json.dumps(source)
				self._redis.set(key, data)
				if expire_seconds:
					self._redis.expire(key, int(expire_seconds))
				return data
			else:
				return None
		return result

	def put_json(self, key, data, expire_seconds=None):
		'''
		Must OK, not failed
		'''
		json_data = json.dumps(data)
		result_code = self._redis.set(key, json_data)
		if expire_seconds:
			self._redis.expire(key, int(expire_seconds))
		return result_code

	def delete_key(self, key):
		'''
		If deleted, will return True, else False
		'''
		result_code = self._redis.delete(key)
		return result_code

	def search_keys_by_pattern(self, pattern):
		"""
		依照 Redis 搜尋 Key 的 pattern 尋找
		Args:
			pattern(str):參考 redis 搜尋 key 的 pattern
		Returns:
			matched_key(list): 尋找到的 key
		"""
		matched_keys = []
		for key in self._redis.scan_iter(pattern):
			matched_keys.append(key)
		return matched_keys

	def flushdb(self):
		return self._redis.flushdb()

redis_cache = RedisCache(
	host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)
