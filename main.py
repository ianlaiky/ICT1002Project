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
    curated_message_for_books = list(message)
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
                # print curated_message_for_books
                curated_message_for_books_list = []
                for index,oldClines in enumerate(curated_message_for_books):
                    curatedLines = oldClines.strip()
                    if curatedLines !="":
                        curated_message_for_books_list.append(curatedLines)
                        # print curated_message_for_books_list
                curated_message_for_books_list.pop(0)
                # print curated_message_for_books_list
                dictionary["Books"]=curated_message_for_books_list

                break
            else:
                curated_message_for_books.pop(0)
                dictionary[data[0]] = data[1]

    list_of_dictionary_profiles_data.append(dictionary)
#
# print list_of_dictionary_profiles_data
#
# # How to retrieve: Eg: retrieve all member names and gender
#
for i in list_of_dictionary_profiles_data:
    print "Name: "+ i["Name"]
    print "Gender: "+ i["Gender"]
    print i["Books"]

