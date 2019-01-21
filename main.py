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

                curated_message_for_books_list = []

                # strip white space
                for oldClines in curated_message_for_books:
                    curatedLines = oldClines.strip()
                    if curatedLines != "":
                        # list to store list of books into the dictionary for each profile
                        curated_message_for_books_list.append(curatedLines)

                # poping the first index to remove the "Books:" character, left with the actual books data
                curated_message_for_books_list.pop(0)

                # storing list into Books dictionary
                dictionary["Books"] = curated_message_for_books_list

                # break and stop iteration when it reaches the books
                break
            else:

                # poping list for books so to remove items that isnt books out
                curated_message_for_books.pop(0)
                dictionary[data[0]] = data[1]

    list_of_dictionary_profiles_data.append(dictionary)

# # TO pring all user profile and its data
# print list_of_dictionary_profiles_data


# # How to retrieve: Eg: retrieve all member names and gender

for i in list_of_dictionary_profiles_data:
    print "Name: " + i["Name"]
    print "Gender: " + i["Gender"]
    print i["Books"]
    print "\n\n"
