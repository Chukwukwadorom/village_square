import os
from dotenv import load_dotenv

load_dotenv()
base_dir = os.path.abspath(os.path.dirname(__file__))
class Config:
     SECRET_KEY = os.environ.get("SECRET_KEY") or "attention is all you need"
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or f"sqlite:///{os.path.join(base_dir,'app.db')}"


con = Config()
