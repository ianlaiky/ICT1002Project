from os import walk

def readFolder(path):
    """
    :param path: path of profiles stored
    :return: A list of files
    """
    files_in_folder = []
    for (directPath, dirNames, fileNames) in walk(path):
        files_in_folder.extend(fileNames)

    '''
    Removes files that does not ends with ".txt"
    '''
    files_in_folder = [fi for fi in files_in_folder if fi.endswith(".txt")]

    return files_in_folder


def readFileData(folder_path, file_path):
    """
    :param folder_path: @String
    :param file_path: @String
    :return: @list --> list of messages for each profile
    """
    f = open(folder_path + file_path, 'r')
    message = f.readlines()
    f.close()
    return message


def cleaningData(dataList):
    """
    :param dataList: @list
    :return: @list --> cleaning raw data, returns cleaned data
    """
    cleanedText = []
    for line in dataList:

        lines = line.strip()

        if str(lines) != "":
            if "Gender:" in lines:
                lines = lines.replace("Male", "M")
                lines = lines.replace("Female", "F")
                lines = lines.replace("male", "M")
                lines = lines.replace("female", "F")
                lines = lines.replace("m", "M")
                lines = lines.replace("f", "F")
            cleanedText.append(lines)
    return cleanedText


def determineIndexOfBook(list):
    """
    :param list: @list --> Single profile list
    :return: @int --> index of the location of character "Books:"
    """
    return list.index("Books:")


def storingProfilesAsDict(bookIndex, cleanedTextList, currentProfileIndex):
    """
    :param bookIndex: @int
    :param cleanedTextList: @list --> text list of single profile
    :param currentProfileIndex: @int --> Unique id for each profile
    :return: @dictionary --> dictionary for single profile

    Return format:
    {
    "Name":@String, 'Gender': @String, 'Age': @String, 'Dislikes': @list, 'Acceptable_age_range': @String,
    'Acceptable_country': @String
    }

    """
    dictionary = {}
    bookList = []

    for indexToRead in xrange(0, bookIndex):
        data = str(cleanedTextList[indexToRead]).split(":")

        '''
        Data[0]: Key name
        Data[1]: Raw data
        
        '''
        if "," in data[1]:

            '''
            Splitting data further if data contains the character ","
            '''
            tempList = data[1].split(",")
            saveList = []

            for ix in tempList:
                if str(ix) != "":
                    saveList.append(str(ix).strip())

            '''
            Saving to Dictionary
            '''
            dictionary[data[0]] = saveList

            '''
            (Acceptable_country, Likes, Dislikes)
            
            For compatibility, if there exists only a single data in any of these field above, a list is created to 
            contain a single element aid compatibility '''

        elif str(data[0].lower()) == "Acceptable_country".lower():
            tempSaveList = [str(data[1]).strip()]
            dictionary[data[0]] = tempSaveList

        elif str(data[0].lower()) == "Likes".lower():
            tempSaveList = [str(data[1]).strip()]
            dictionary[data[0]] = tempSaveList

        elif str(data[0].lower()) == "Dislikes".lower():
            tempSaveList = [str(data[1]).strip()]
            dictionary[data[0]] = tempSaveList

        else:

            dictionary[data[0]] = str(data[1]).strip()

    '''
    Saving books data:
    Range starts from identified "Books:" character to the length of list
    '''
    for indexToRead in xrange(int(bookIndex) + 1, int(len(cleanedTextList))):
        bookList.append(cleanedTextList[indexToRead])

    dictionary["Books"] = bookList
    dictionary["id"] = int(currentProfileIndex)
    return dictionary


def convertFileListToProfileList(folder_path, fileList):
    """

    :param folder_path: @String --> Path of folder
    :param fileList: [@String,@String] --> list of file names
    :return: list of dictionary
    """

    currentProfileIndex = 0
    profileList = []

    for filePath in fileList:
        file_data = readFileData(folder_path, filePath)

        '''
        Cleaning data
        '''
        cleanedTextList = cleaningData(file_data)

        bookIndex = determineIndexOfBook(cleanedTextList)
        # print bookIndex

        profileList.append(storingProfilesAsDict(bookIndex, cleanedTextList, currentProfileIndex))

        currentProfileIndex = int(currentProfileIndex) + 1

    return profileList


def run(folder_Path):
    """
    :param folder_Path: path of folder
    :return: list of dictionary


    Return format:
    @String --> String
    @list --> list
    @dictionary --> dictionary

    [
    {"Name":@String, 'Gender': @String, 'Age': @String, 'Dislikes': @list, 'Acceptable_age_range': @String,
    'Acceptable_country': @String},
    @dictionary,
    @dictionary, ......
    ]

    """

    files_in_folder = readFolder(folder_Path)
    list_of_dictionary_profiles_data = convertFileListToProfileList(folder_Path, files_in_folder)

    return list_of_dictionary_profiles_data
