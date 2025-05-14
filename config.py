import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///quotepro.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    MYPOS_CLIENT_ID = os.environ.get('MYPOS_CLIENT_ID')
    MYPOS_CLIENT_SECRET = os.environ.get('MYPOS_CLIENT_SECRET')
    MYPOS_MERCHANT_ID = os.environ.get('MYPOS_MERCHANT_ID')
    MYPOS_OAUTH_API_URL = os.environ.get('MYPOS_OAUTH_API_URL') or 'https://auth-api.mypos.com/oauth/token'
    MYPOS_TRANSACTION_API_URL = os.environ.get('MYPOS_TRANSACTION_API_URL') or 'https://transactions-api.mypos.com/v1.1/online-payments/link'