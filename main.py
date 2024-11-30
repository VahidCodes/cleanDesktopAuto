import os
import shutil

# Specify the desktop directory
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define folder structure for file types
file_extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Others": []  # For unmatched files
}

# Function to create folders
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Organize files
def clean_desktop():
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        # Skip directories
        if os.path.isdir(item_path):
            continue

        # Determine file type
        file_extension = os.path.splitext(item)[-1].lower()
        moved = False

        for folder, extensions in file_extensions.items():
            if file_extension in extensions:
                folder_path = os.path.join(desktop_path, folder)
                create_folder(folder_path)
                shutil.move(item_path, folder_path)
                moved = True
                break

        # Move unmatched files to 'Others'
        if not moved:
            others_path = os.path.join(desktop_path, "Others")
            create_folder(others_path)
            shutil.move(item_path, others_path)

# Run the cleaner
if __name__ == "__main__":
    clean_desktop()
    print("Desktop cleaned and organized successfully!")
