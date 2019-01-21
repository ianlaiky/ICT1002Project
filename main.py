from os import walk

# Folder path
folder_path = "./profiles/"
files_in_folder = []

for (directPath, dirNames, fileNames) in walk(folder_path):
    files_in_folder.extend(fileNames)
    print files_in_folder

list_of_dictionary_profiles_data = []

# iterating every profile, storing info to list_of_profiles_data
for i in files_in_folder:
    f = open(folder_path + i, 'r')
    message = f.readlines()
    dictionary = {}

# iterate through each profile line by line
    for oldlines in message:
        # strip whitespace
        lines = oldlines.strip()
        if lines != "":
            # separate to 2 per list via ":" character
            data = lines.split(":")
            # adding a exception for books since the book info is on each separate lines
            if str(data[0]).lower() == "Books".lower():




                break
            else:
                dictionary[data[0]] = data[1]

    list_of_dictionary_profiles_data.append(dictionary)
#
print list_of_dictionary_profiles_data

# How to retrieve: Eg: retrieve all member names and gender

for i in list_of_dictionary_profiles_data:
    print i["Name"] + " " + i["Gender"]
