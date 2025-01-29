import os
from dotenv import load_dotenv

# .env dosyasını yükleyin
load_dotenv()

# Şifrenizi çevre değişkeninden alın
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

class Config:
    SECRET_KEY = "supersecretkey"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:{DATABASE_PASSWORD}@localhost/musicdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
