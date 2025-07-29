import os
import shutil

# Ask user to enter a folder path
path = input("Enter the folder path to organize: ").strip()

# Get all files in the folder
files = os.listdir(path)

for file in files:
    # Split file name and extension
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove dot from extension

    if extension == "":
        continue  # Skip files without extensions

    folder_path = os.path.join(path, extension)

    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Move file to the corresponding folder
    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))
