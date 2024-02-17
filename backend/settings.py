import os
import sys
from dotenv import load_dotenv

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")

# moved to config.py...

# class Config:
#     pass

# class DevelopmentConfig(Config):
#     DB_NAME = os.getenv('DEV_DB_NAME')
#     DB_USER = os.getenv('DEV_DB_USER')
#     DB_PASSWORD = os.getenv('DEV_DB_PASSWORD')

# class TestingConfig(Config):
#     DB_NAME = os.getenv('TEST_DB_NAME')
#     DB_USER = os.getenv('TEST_DB_USER')
#     DB_PASSWORD = os.getenv('TEST_DB_PASSWORD')

# class ProductionConfig(Config):
#     DB_NAME = os.getenv('PROD_DB_NAME')
#     DB_USER = os.getenv('PROD_DB_USER')
#     DB_PASSWORD = os.getenv('PROD_DB_PASSWORD')