# -*- coding: utf-8 -*-
import uuid
import boto3
import base64
from datetime import datetime, timedelta

def upload_base64_img(image_stream, folder_name, aws_config, filename=None):
	"""
	Private Method：Upload Merchant Image stream and create image url in AWS
	Base64: https://www.base64-image.de/
	Args:
		image_stream(base64): The base64 format of image
		folder_name(str): The upload folder in AWS
			e.g http://xxx.aws.com/dev/<folder_name>, and the dev folder from AWS Config
		aws_config(dict): The AWS Config for setting AWS parameter and upload location.
		filename(unicode): Yhe filename your would like to named
	Returns:
		aws_img_url(string): Image url from AWS
		filename(unicode or uuid.UUID): The uploaded Image filename 
		If the argument filename is None, then the default filename is uuid value
	"""
	bucket_name = aws_config['S3_BUCKET']
	domain = aws_config['S3_DOMAIN']
	folder = aws_config['VERSION_FOLDER']

	# 預設會用 uuid 作為檔案名稱
	if filename is None:
		filename = uuid.uuid4()

	# base 64換換成圖片
	imgdata = base64.b64decode(image_stream)

	file_path = folder + '/' + folder_name + '/' + str(filename)
	# 建立連線
	client = boto3.client(
		's3',
		aws_access_key_id=aws_config['AWS_ACCESS_KEY_ID'],
		aws_secret_access_key=aws_config['AWS_SECRET_ACCESS_KEY'])
	# 上傳至ＡＷＳ
	resp = client.put_object(
		ACL='public-read',
		Bucket=bucket_name,
		Key=file_path,
		Body=imgdata,
		Expires=datetime.utcnow() + timedelta(days=7)
	)
	aws_img_url = domain + '/' + bucket_name + '/' + file_path
	return aws_img_url, filename


def upload_file(file_object, folder_name, aws_config, filename=None, file_format=None):
	"""
	Private Method：Upload Merchant Image stream and create image url in AWS
	Base64: https://www.base64-image.de/
	Args:
		file_object(file): file
		folder_name(str): The upload folder in AWS
			e.g http://xxx.aws.com/dev/<folder_name>, and the dev folder from AWS Config
		aws_config(dict): The AWS Config for setting AWS parameter and upload location.
		filename(unicode): Yhe filename your would like to named
		file_format(str): e.g mp4, mp3, wav, jpg....
	Returns:
		aws_img_url(string): Image url from AWS
		filename(unicode or uuid.UUID): The uploaded Image filename
		If the argument filename is None, then the default filename is uuid value
	"""
	bucket_name = aws_config['S3_BUCKET']
	domain = aws_config['S3_DOMAIN']
	folder = aws_config['VERSION_FOLDER']

	# 預設會用 uuid 作為檔案名稱
	if filename is None:
		filename = uuid.uuid4()

	file_path = folder + '/' + folder_name + '/' + str(filename)
	if file_format:
		file_path = file_path + '.' + file_format

	# 建立連線
	client = boto3.client(
		's3',
		aws_access_key_id=aws_config['AWS_ACCESS_KEY_ID'],
		aws_secret_access_key=aws_config['AWS_SECRET_ACCESS_KEY'])
	# 上傳至AWS
	resp = client.put_object(
		ACL='public-read',
		Bucket=bucket_name,
		Key=file_path,
		Body=file_object,
		Expires=datetime.utcnow() + timedelta(days=7)
	)
	aws_img_url = domain + '/' + bucket_name + '/' + file_path
	return aws_img_url, filename



def remove_uploaded_file(aws_filename, folder_name, aws_config):
	"""
	Remove AWS S3 image file by image filename
	Args:
		aws_filename(str): The image filename on AWS S3 we created.
		folder_name(str): The upload folder in AWS
			e.g http://xxx.aws.com/dev/<folder_name>, and the dev folder from AWS Config
		aws_config(dict): The AWS Config for setting AWS parameter and upload location.
	"""
	bucket_name = aws_config['S3_BUCKET']
	domain = aws_config['S3_DOMAIN']
	folder = aws_config['VERSION_FOLDER']
	# domain = aws_config['S3_DOMAIN']
	file_path = folder + '/' + folder_name + '/' + aws_filename
	# 建立連線
	client = boto3.client(
		's3',
		aws_access_key_id=aws_config['AWS_ACCESS_KEY_ID'],
		aws_secret_access_key=aws_config['AWS_SECRET_ACCESS_KEY'])
	resp = client.delete_object(
		Bucket=bucket_name, Key=file_path
	)
	return resp
