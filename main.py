from os import walk

# Folder path
folder_path = "./profiles/"
files_in_folder = []

for (directPath, dirNames, fileNames) in walk(folder_path):
    files_in_folder.extend(fileNames)
    # print files_in_folder

list_of_dictionary_profiles_data = []

#declare unique id
uniqueId =0

# iterating every profile, storing info to list_of_profiles_data
for i in files_in_folder:
    f = open(folder_path + i, 'r')
    message = f.readlines()
    f.close()
    curated_message_for_books = list(message)
    dictionary = {}

    # iterate through each profile line by line
    for oldlines in message:
        # strip whitespace
        lines = oldlines.strip()

        if lines != "":
            if "Gender:" in lines:
                lines = lines.replace("Male","M")
                lines = lines.replace("Female","F")
                lines = lines.replace("male","M")
                lines = lines.replace("female","M")
                lines = lines.replace("m","M")
                lines = lines.replace("f","M")

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

                if "," in data[1]:
                    tempList = data[1].split(",")
                    saveList = []
                    for ix in tempList:
                        if ix !="":
                            saveList.append(ix.strip())
                    dictionary[data[0]] = saveList
                else:
                    dictionary[data[0]] = data[1].strip()

    dictionary["id"] = uniqueId
    uniqueId = int(uniqueId)+int(1)
    list_of_dictionary_profiles_data.append(dictionary)

# # TO pring all user profile and its data
# print list_of_dictionary_profiles_data


# # How to retrieve: Eg: retrieve all member names and gender

for i in list_of_dictionary_profiles_data:
    print "Unique Id"
    print i["id"]

    print "Name: " + i["Name"]
    print "Gender: " + i["Gender"]
    print "Country" + i["Country"]

    print "Acceptable_country"
    print i["Acceptable_country"]

    print "Age"
    print i["Age"]

    print "Acceptable_age_range"
    print i["Acceptable_age_range"]

    print "Likes"
    print i["Likes"]

    print "Dislikes"
    print i["Dislikes"]

    print "Books"
    print i["Books"]

    print "\n\n"


# example code
def accessBooksData(dictionary):
    print dictionary["Name"]
    print dictionary["id"]
    print dictionary["Books"]



for dict in list_of_dictionary_profiles_data:
    accessBooksData(dict)