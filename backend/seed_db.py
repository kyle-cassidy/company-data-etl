from api.data.migrations.phase_1.run_phase_1_sqlite_setup import create_tables_from_sql_file
from api.src.utils.seed_adapters.run_seed_adapters import seed_sp500_postgres, seed_sp500_sqlite

# postgres
# if __name__ == "__main__":
    # seed_sp500_postgres()

# sqlite
if __name__ == "__main__":
    create_tables_from_sql_file()
    seed_sp500_sqlite()