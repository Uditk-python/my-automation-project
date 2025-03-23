import os
import shutil
from datetime import datetime

# 📂 Define source and backup folders
source_folder = r"C:\Users\YourName\Documents\important_files"
backup_root = r"C:\Users\YourName\Documents\backups"

# ⏳ Create a timestamped backup folder
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_folder = os.path.join(backup_root, f"backup_{timestamp}")
os.makedirs(backup_folder, exist_ok=True)

# 🔄 Backup process
for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)
    backup_path = os.path.join(backup_folder, file_name)

    if os.path.isfile(file_path):
        shutil.copy2(file_path, backup_path)  # Copies file with metadata
        print(f"✅ {file_name} backed up successfully.")

print("🚀 Backup completed!")
