import subprocess


def run_streamlit_app():
    # Run the Streamlit dashboard
    subprocess.run(["streamlit", "run", "frontend/dashboard/app.py"], check=True)


if __name__ == "__main__":
    run_streamlit_app()
