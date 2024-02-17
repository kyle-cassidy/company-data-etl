import os
from os import getenv
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from api import create_app


# Determine the environment, e.g., from an environment variable
env = os.getenv('FLASK_ENV', 'testing')

if env == 'development':
    config_class = DevelopmentConfig
elif env == 'testing':
    config_class = TestingConfig
elif env == 'production':
    config_class = ProductionConfig
else:
    raise ValueError(f"Unknown FLASK_ENV: {env}")

app = create_app(config_class)
app.run(debug=True)