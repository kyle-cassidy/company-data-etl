from app.data.migrations.phase_1.run_phase_1_sqlite_setup import (
    create_tables_from_sql_file,
)
from app.utils.seed_adapters.seed_adapters_util import (
    seed_sp500_postgres,
    seed_sp500_sqlite,
)
from app import create_app

# sqlite
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        create_tables_from_sql_file()
        seed_sp500_sqlite()


# postgres
# if __name__ == "__main__":
# seed_sp500_postgres()
