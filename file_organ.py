import os
import shutil

# Define the folder path
folderpath = r"C:\Users\ANNE MARIE\Desktop\New_folder"

# Change the current working directory
os.chdir(folderpath)

# Check the files
file_list = os.listdir()
print(file_list)

# Get the extensions of the files in the directory
list_extension = []
for fl in file_list:
    extension = fl.split(".")[-1]
    list_extension.append(extension)
    print(list_extension)

# Remove duplicates from the list of extensions
list_extension = list(set(list_extension))
print(len(list_extension))

# Create folders for each extension and move files into corresponding folders
for ex in list_extension:
    os.makedirs(ex, exist_ok=True)  # Create folder if it doesn't exist
    for fl in file_list:
        if fl.endswith(ex):
            shutil.move(os.path.join(folderpath, fl), os.path.join(folderpath, ex, fl))
            print(f'Moved {fl} to {ex} folder')