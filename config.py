import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = ['headers', 'cookies']
    JWT_COOKIE_SECURE = True  # Ensure this is True in production (requires HTTPS)
    JWT_ACCESS_COOKIE_NAME = 'access_token'  # Cookie name for the JWT token
    JWT_COOKIE_CSRF_PROTECT = True  # Protect cookies from CSRF attacks
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True  # Set to True if using HTTPS
