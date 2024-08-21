import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')
