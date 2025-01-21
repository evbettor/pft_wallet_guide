# setup_env.py
import os
import subprocess
import sys

def setup_virtual_env(env_name="pftwalletenv"):
    print("Setting up virtual environment...")
    subprocess.check_call([sys.executable, "-m", "venv", env_name])
    activate_script = os.path.join(env_name, "Scripts", "activate") if os.name == "nt" else os.path.join(env_name, "bin", "activate")
    print(f"Virtual environment '{env_name}' created. To activate, run:")
    print(f"source {activate_script}" if os.name != "nt" else activate_script)
    print("\nInstalling dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])
    print("Dependencies installed successfully!")

if __name__ == "__main__":
    setup_virtual_env()
