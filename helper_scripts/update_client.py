# update_client.py
import subprocess

def update_client():
    print("Updating client repository...")
    subprocess.check_call(["git", "pull"])
    print("Reinstalling dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])
    print("Client updated successfully!")

if __name__ == "__main__":
    update_client()
