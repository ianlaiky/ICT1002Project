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
        # seperate to 2 per list via ":" character

        lines = oldlines.strip()
        # print lines

        if lines != "":

            data = lines.split(":")
            # adding a exception for books since the book info is on each separate lines
            if str(data[0]).lower() == "Books".lower():
                break
            else:
                # print data[1]
                dictionary[data[0]] = data[1]

                # print data

    list_of_dictionary_profiles_data.append(dictionary)
#
print list_of_dictionary_profiles_data

# How to retireve: Eg: retireve all member names and gender

for i in list_of_dictionary_profiles_data:
    print i["Name"] + " " + i["Gender"]
