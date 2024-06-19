import os
from dotenv import load_dotenv

load_dotenv()
base_dir = os.path.abspath(os.path.dirname(__file__))
class Config:
     SECRET_KEY = os.environ.get("SECRET_KEY") or "attention is all you need"
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or f"sqlite:///{os.path.join(base_dir,'app.db')}"
     MAIL_SERVER = os.environ.get('MAIL_SERVER')
     MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
     MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
     MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
     MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
     ADMINS = ['chukwukwadoromnwattah@gmail.com']


con = Config()
