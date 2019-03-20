import pdfkit
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	
	CSRF_ENABLED = True
	SECRET_KEY = 'together_we_can'
	SECURITY_PASSWORD_SALT = "yes_we_can"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	#SQLALCHEMY_ECHO = True

	MAIL_SERVER='smtp.gmail.com'
	MAIL_PORT= 465
	MAIL_USE_SSL=True
	MAIL_USERNAME = "recop.baste@gmail.com"
	MAIL_PASSWORD = "recopcomex"
	MAIL_ASCII_ATTACHMENTS = True 

	PDF_CONFIG = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
	
	POSTS_PER_PAGE = 12

	CELERY_BROKER_URL='redis://localhost:6379/0'
	CELERY_RESULT_BACKEND='redis://localhost:6379/0'