# -*- coding: utf-8 -*-
import threading
import Queue
import time

"""
Thread Worker
"""
class WebAPIWorker(threading.Thread):
	lock = threading.Lock()

	def __init__(self, work_func, in_queue, out_queue):
		threading.Thread.__init__(self)
		self._work_func = work_func
		# self._func_args = func_args
		self._out_queue = out_queue
		self._in_queue = in_queue

	def run(self):
		item = self._in_queue.get()
		# with WebAPIWorker.lock:
		# 	print 'ready to do: ', item
		result = self._work_func(**item)
		# with WebAPIWorker.lock:
		# 	print 'done: ', result
		self._out_queue.put(result)
