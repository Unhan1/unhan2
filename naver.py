import os
import shutil

a = '230324'

folder_path = r'c:\doit\출장비' + a

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' has been created.")
else:
    print(f"Folder '{folder_path}' already exists.")


# Set the folder path
folder_path1 = r'C:\Users\kwater\Desktop\PC자료전송 Download'

# Define the original and new file names
old_file_names = ["123.txt", "456.txt"]
new_file_names = [a + '1.txt' , a + '2.txt']

# Change the working directory to the folder path
os.chdir(folder_path1)

# Rename the files
for old_name, new_name in zip(old_file_names, new_file_names):
    os.rename(old_name, new_name)
    print(f"{old_name} has been renamed to {new_name}")

    source_file = os.path.join(folder_path1, new_name)
    destination_file = os.path.join(folder_path, new_name)
    shutil.move(source_file, destination_file)
    print(f"File '{source_file}' has been moved to '{destination_file}'")
