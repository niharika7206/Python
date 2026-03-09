import os
import shutil

path = input("Enter folder path: ")

files = os.listdir(path)

folders = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3"]
}

for folder in folders:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

for file in files:
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        for folder, extensions in folders.items():
            for ext in extensions:
                if file.lower().endswith(ext):
                    shutil.move(file_path, os.path.join(path, folder, file))
                    print(file, "moved to", folder)
