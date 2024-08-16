import os
from os.path import splitext
import shutil
import glob

#file_manager python

# Define the dictionary with extensions as keys and descriptive names as values
extension_names = {
    "txt": "Text Files",
    "pdf": "PDF Documents",
    "jpg": "JPG Pictures",
    "jpeg": "JPEG Pictures",
    "png": "PNG Pictures",
    "docx": "Word Documents",
    "xlsx": "Excel Spreadsheets",
    "pptx": "PowerPoint Presentations",
    "mp3": "MP3 Audio",
    "mp4": "MP4 Video",
    "html": "HTML Document",
    "css": "CSS Stylesheet",
    "js": "JavaScript File",
    "rar": "Compressed Files (RAR)",
    "zip": "Compressed Files (ZIP)",
    "py": "Python Files",
    "sh": "Bash Scripts"
}

def add_non_repetetive(my_string, my_list):
    if my_string and my_string[1:] not in my_list:
        my_list.append(my_string[1:])

def create_dir(my_list, paths):
    base_paths = {}
    for c in my_list:
        if c not in extension_names:
            new_dir = c.upper() + "_Files"
        else:
            new_dir = extension_names.get(c).replace(" ", "_")

        # Ensure unique directory name
        base_path = os.path.join(paths, new_dir)
        counter = 1

        while os.path.exists(base_path):
            base_path = os.path.join(paths, f"{new_dir}_{counter}")
            counter += 1
        os.mkdir(base_path)
        print(f"Created directory: {base_path}")
        base_paths[c] = base_path

    return base_paths

def moving_files(dir, ext, base_paths):
    for e in ext:
        allfiles = glob.glob(os.path.join(dir, f'*.{e}*'))
        for p in allfiles:
            dst_path = os.path.join(base_paths[e], os.path.basename(p))
            shutil.move(p, dst_path)

def delete_empty_folders(paths):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                os.rmdir(dir_path)
                print(f"Deleted empty folder: {dir_path}")
            except OSError:
                pass

while True:
    directory = input("Enter the directory path: ").strip()
    if os.path.isdir(directory):
        if len(os.listdir(directory)) == 0:
            print("The directory is empty, try again.")
        else:
            print("\n+ Starting the program...")
            break  # Exit the loop once a valid directory is found
    else:
        print("Invalid path, try again.\n")

delete_empty_folders(directory)

extension = []

for f in os.listdir(directory):
    add_non_repetetive(splitext(f)[1], extension)

# Create directories and get paths
base_paths_returned = create_dir(extension, directory)

# Move files to their respective directories
moving_files(directory, extension, base_paths_returned)
