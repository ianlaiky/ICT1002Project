import function6
import main
import function5


def get_all_userProfile(folder_path):
    return main.run(folder_path)


def append_data(data):
    function6.write_file(data)


'''
Main code
'''


def run(folder_path):
    """

    :param folder_path: @String --> Folder path
    """
    function6.clear_file()
    profileList = get_all_userProfile(folder_path)
    append_data(["Name", "Match with"])
    for i in profileList:
        print i["Name"]
        print function5.func5(i["Name"], profileList)

        append_data([i["Name"], ', '.join(function5.func5(i["Name"], profileList)).replace(",", " |")])
