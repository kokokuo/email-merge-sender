#  -*- coding:utf-8 -*-
import os


def recursive_dir(parent_path, directory):
	"""
	parent_path:string parent path
	directory:list :include files/sub directory
	"""

	for fname in directory:
		# 取得此檔案的路徑, 由上一層路徑加上此檔案
		current_path = os.path.join(parent_path, fname)
		print fname
		# 此檔案的完整路是否為目錄
		if os.path.isdir(current_path):
			print current_path + " is directory"
			# 取得子目錄
			subdir = os.listdir(current_path)
			# 把目前的路徑與子目錄傳下去
			recursive_dir(current_path, subdir)
		elif fname[-3:] == 'pyc':
			print current_path + ' is pyc..'
			os.remove(current_path)
		else:
			print current_path + " is normal file"


if __name__ == '__main__':
	BASEPATH = os.path.dirname(os.path.abspath(__file__))
	print BASEPATH
	directory = os.listdir(BASEPATH)
	recursive_dir(BASEPATH, directory)
