import subprocess
import sys
import os
import venv

def check_flask_installed():
    """Check if Flask is installed."""
    try:
        # Try importing Flask
        import flask
        print("Flask is already installed.")
        return True
    except ImportError:
        print("Flask not found, installing...")
        return False

def install_flask():
    """Install Flask using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
        print("Flask has been installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing Flask. Please check your permissions and try again.")
        sys.exit(1)

def create_virtual_environment():
    """Create a new virtual environment if not already present."""
    venv_dir = 'venv'
    if not os.path.exists(venv_dir):
        print(f"Creating a new virtual environment in {venv_dir}...")
        venv.create(venv_dir, with_pip=True)
    else:
        print(f"Virtual environment already exists in {venv_dir}.")

def activate_virtual_environment():
    """Activate the virtual environment."""
    venv_dir = 'venv'
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_dir, 'Scripts', 'activate.bat')
    else:  # Unix-based (Linux/macOS)
        activate_script = os.path.join(venv_dir, 'bin', 'activate')
    
    if os.path.exists(activate_script):
        print(f"Activating virtual environment using {activate_script}...")
        subprocess.call([activate_script], shell=True)
    else:
        print(f"Unable to find activation script: {activate_script}")
        sys.exit(1)

def main():
    """Main function to check Flask and setup environment."""
    # Check if Flask is installed
    if not check_flask_installed():
        # Create virtual environment if not already created
        create_virtual_environment()
        
        # Activate the virtual environment
        activate_virtual_environment()
        
        # Install Flask
        install_flask()

    # Optionally, install other dependencies here (from requirements.txt, etc.)
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    main()
