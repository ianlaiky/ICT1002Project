"""
Python File: function2.py
Author: Goh Jun Yan
"""
from main import run as getData

def list_matched_country(id, dataList):

    """
    List all the students that fall in to the acceptable country of B should be printed out
    Return: matched_users   (list)
    """

    # Selected user
    print "User : ", dataList[id]['Name']

    """ Initialization """
    user_acceptable_country_str = ''
    user_acceptable_country_list = []
    matched_users = []

    """" Flags """
    # To check later on if it is str(0) or list(1)
    strOrList = -1
    # Check the user's index in the list
    user_index = -1

    """
    Iterates through the dataList to get the user's acceptable country and get the user's index so we can
    ignore the index during loops
    """
    for user in dataList:
        if user['id'] == id:
            # Record index
            user_index = dataList.index(user)
            # Checks if the dict value is a str
            if isinstance(user['Acceptable_country'], str):
                user_acceptable_country_str = user['Acceptable_country']
                strOrList = 0
            # Checks if the dict value is a list
            elif isinstance(user['Acceptable_country'], list):
                user_acceptable_country_list = user['Acceptable_country']
                strOrList = 1
            break

    """
    Iterates through the dataList, ignores selected user's index and compares the other user's country to
    the user acceptable country (str/list). If matched, append the other user's Name(for now) to matched_users list        
    """
    if user_index == -1:
        print "Error: Unable to get user index"
    elif strOrList == -1:
        print "Error: String or List"
    elif strOrList == 0:
        for other_user in dataList:
            if dataList.index(other_user) == user_index:
                continue
            elif other_user['Country'] == user_acceptable_country_str:
                # Appending only names for now
                matched_users.append(other_user['Name'])
    elif strOrList == 1:
        for country in user_acceptable_country_list:
            for other_user in dataList:
                if dataList.index(other_user) == user_index:
                    continue
                elif other_user['Country'] == country:
                    # Appending only names for now
                    matched_users.append(other_user['Name'])

    return matched_users

def main():
    # Get data dynamically based on the profiles listed from filepath
    sample_list = getData('./profiles/')
    # This is printing (id=4)Kevin's
    print list_matched_country(4, sample_list)


if __name__ == '__main__':
    main()
