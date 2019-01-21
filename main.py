
# Folder path
from os import walk

folder_path = "./profiles/"
files_in_folder = []

for(directPath, dirNames, fileNames) in walk(folder_path):
    files_in_folder.extend(fileNames)
    print files_in_folder