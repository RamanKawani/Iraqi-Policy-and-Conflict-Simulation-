import os
import subprocess
import sys

def check_and_install_package(package_name):
    """Check if a package is installed, and install it if not."""
    try:
        # Try to import the package
        __import__(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        print(f"{package_name} not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def install_requirements():
    """Install all requirements from requirements.txt."""
    if os.path.exists("requirements.txt"):
        print("Installing dependencies from requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    else:
        print("requirements.txt not found.")

def setup_venv():
    """Check if virtual environment is activated, if not, activate it."""
    if "VIRTUAL_ENV" not in os.environ:
        print("Virtual environment is not activated.")
        sys.exit(1)

def main():
    # Check if Flask is installed
    check_and_install_package("flask")
    
    # Install additional dependencies from requirements.txt
    install_requirements()

    # Ensure the virtual environment is activated
    setup_venv()

    # Run your app
    from app import create_app
    app = create_app()
    
    # Run the app (default to localhost:5000)
    app.run(debug=True)

if __name__ == "__main__":
    main()
