import subprocess
import time

def run_flask_app():
    try:
        # Start the Flask application
        subprocess.Popen(["flask", "run"])
        print("Running Flask application")
        print("Streamlit will start in 5 seconds...")
    except subprocess.CalledProcessError:
        try:
            # If the Flask application fails to start, try running it with python3 -m flask run
            subprocess.Popen(["python3", "-m", "flask", "run"])
        except subprocess.CalledProcessError as e:
            # If the Flask application fails again, print the error
            print(e)

def run_streamlit_app():
    # Start the Streamlit dashboard
    try:
        time.sleep(3)  # Delay for 10 seconds
        print("Running Streamlit dashboard")
        subprocess.Popen(["streamlit", "run", "src/frontend/dashboard/app.py"])
    except subprocess.CalledProcessError as e:
        print(e)
        try:
            print("Trying again in 10 seconds...")
            time.sleep(10)  # Delay for 10 seconds
            subprocess.run(["python3", "-m", "streamlit", "run", "src/frontend/dashboard/app.py"])
        except subprocess.CalledProcessError as e:
            print(e)

if __name__ == "__main__":
    run_flask_app()
    run_streamlit_app()