import subprocess

def run_flask_app():
    # Run the Flask application
    subprocess.run(["flask", "run"], check=True)

if __name__ == "__main__":
    run_flask_app()
