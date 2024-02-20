import os
from dotenv import load_dotenv

load_dotenv()

# default_config = 'testing'
class Config:
    pass

class DevelopmentConfig(Config):
    DB_HOST = os.getenv('DEV_DB_HOST')
    DB_NAME = os.getenv('DEV_DB_NAME')
    DB_USER = os.getenv('DEV_DB_USER')
    DB_PASSWORD = os.getenv('DEV_DB_PASSWORD')

class TestingConfig(Config):
    DB_HOST = os.getenv('TEST_DB_HOST')
    DB_NAME = os.getenv('TEST_DB_NAME')
    DB_USER = os.getenv('TEST_DB_USER')
    DB_PASSWORD = os.getenv('TEST_DB_PASSWORD')

class ProductionConfig(Config):
    DB_HOST = os.getenv('PROD_DB_HOST')
    DB_NAME = os.getenv('PROD_DB_NAME')
    DB_USER = os.getenv('PROD_DB_USER')
    DB_PASSWORD = os.getenv('PROD_DB_PASSWORD')

# Initialize a global variable to hold the current configuration
current_config = None

def set_config():
    global current_config
    env = os.getenv('FLASK_ENV', 'development').lower()
    if env == 'development':
        current_config = DevelopmentConfig
    elif env == 'testing':
        current_config = TestingConfig
    elif env == 'production':
        current_config = ProductionConfig
    else:
        raise ValueError(f"Unknown FLASK_ENV: {env}")

set_config()
#------------------------------------------------#













    
    
    
    # import os
# from dotenv import load_dotenv

# load_dotenv()

# # TEST_DATABASE = os.getenv('TEST_DATABASE')
# # TEST_USER = os.getenv('TEST_USER')
# # TEST_PASSWORD = os.getenv('TEST_PASSWORD')

# # DATABASE = os.getenv('DATABASE')
# # USER = os.getenv('DB_USER')
# # PASSWORD = os.getenv('DB_PASSWORD')






# import os
# from dotenv import load_dotenv

# load_dotenv()

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
    
    