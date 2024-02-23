from api.src.utils.seed_adapters.run_seed_adapters import seed_sp500_postgres, seed_sp500_sqlite


if __name__ == "__main__":
    seed_sp500_sqlite()
    # seed_sp500_postgres()