# -*- coding: utf-8 -*-
from functools import wraps
import timeit
import threading
import Queue
import time
def profile_func(func):
	"""
	Measure specific function time
	"""
	@wraps(func)
	def wrapper(*args, **kwargs):
		time_start = timeit.default_timer()
		result = func(*args, **kwargs)
		time_end = timeit.default_timer()
		print "#########"
		print "function name =>", func.__name__
		print "performance time => ", (time_end - time_start)
		print "#########"
		return result
	return wrapper

# """
# Queue
# """

# class ClosableQueue(Queue.Queue):
# 	DONE_SINGAL = object()
# 	lock = threading.Lock()

# 	def close(self):
# 		self.put(ClosableQueue.DONE_SINGAL)

# 	def __iter__(self):
# 		while True:
# 			try:
# 				item = self.get()
# 				with ClosableQueue.lock:
# 					print 'get: ', item
# 				# if item is ClosableQueue.DONE_SINGAL:
# 				# 	return
# 				yield item
# 			except Exception, e:
# 				raise e
# 			finally:
# 				self.task_done()

# """
# Thread Worker
# """
# class StoppableWorker(threading.Thread):
# 	lock = threading.Lock()

# 	def __init__(self, work_func, in_queue, out_queue):
# 		threading.Thread.__init__(self)
# 		self._work_func = work_func
# 		self._in_queue = in_queue
# 		self._out_queue = out_queue


# 	def run(self):
# 		for item in self._in_queue:
# 			with StoppableWorker.lock:
# 				print 'ready to do: ', item
# 			result = self._work_func(**item)
# 			with StoppableWorker.lock:
# 				print 'done: ', result
# 			self._out_queue.put(result)
# 		with StoppableWorker.lock:
# 			print 'finish => ', self.getName()
