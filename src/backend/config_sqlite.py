import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Common configuration (if any)
    pass

class DevelopmentConfig(Config):
    DB_URI = os.getenv('DEV_DB_URI')

class TestingConfig(Config):
    DB_URI = os.getenv('TEST_DB_URI')

class ProductionConfig(Config):
    DB_URI = os.getenv('PROD_DB_URI')

class TestingSQLiteConfig(Config):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_FILE = os.path.join(BASE_DIR, 'api', 'data', 'sp500_p1_sm.sqlite')
    DB_URI = f'sqlite:///{DB_FILE}'

def get_config():
    env = os.getenv('FLASK_ENV', 'testing_sqlite').lower()
    configs = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'testing_sqlite': TestingSQLiteConfig
    }
    if env in configs:
        return configs[env]()
    else:
        raise ValueError(f"Unknown FLASK_ENV: {env}")

current_config = get_config()