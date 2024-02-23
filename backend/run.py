from config_sqlite import Config, current_config, Config, TestingSQLiteConfig
from api.src import create_app


app = create_app(TestingSQLiteConfig)
app.run(debug = True)