"""
Application Entry Point
Launches the Student Attendance Management System.
"""
import sys
import subprocess

def main():
    # Launches the application runner
    cmd = [sys.executable, "-m", "streamlit", "run", "app.py"] + sys.argv[1:]
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
