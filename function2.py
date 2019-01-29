"""
Python File: function2.py
Author: Goh Jun Yan
"""
from main import run as getData


def list_matched_country(value, data_list, id_or_name=1):

    """
    List all the students that fall in to the acceptable country of B should be printed out
    Param:
        value -> Name (str)
        data_list -> Data input (list)
        id_or_name -> 1 (e.g)(0 for id, 1 for Name)
    Return: matched_users   (list)
    """

    """ Initialization """
    user_acceptable_country_str = ''
    user_acceptable_country_list = []
    matched_users = []
    # To choose output type, 0 -> id, 1 -> Name
    if id_or_name == 0:
        output_type = "id"
    elif id_or_name == 1:
        output_type = "Name"

    """" Flags """
    # To check later on if it is str(0) or list(1)
    str_or_list = -1
    # Check the user's index in the list
    user_index = -1

    """
    Iterates through the data_list to get the user's acceptable country and get the user's index so we can
    ignore the index during loops
    """
    for user in data_list:
        # If searching the data_list using id
        if user['Name'] == value:
            # Record index
            user_index = data_list.index(user)
            # Checks if the dict value is a str
            if isinstance(user['Acceptable_country'], str):
                user_acceptable_country_str = user['Acceptable_country']
                str_or_list = 0
            # Checks if the dict value is a list
            elif isinstance(user['Acceptable_country'], list):
                user_acceptable_country_list = user['Acceptable_country']
                str_or_list = 1
            break

    """
    Iterates through the data_list, ignores selected user's index and compares the other user's country to
    the user acceptable country (str/list). If matched, append the other user's Name(for now) to matched_users list        
    """
    if user_index == -1:
        print "Error: Unable to get user index"
    elif str_or_list == -1:
        print "Error: String or List"
    elif str_or_list == 0:
        for other_user in data_list:
            if data_list.index(other_user) == user_index:
                continue
            elif other_user['Country'] == user_acceptable_country_str:
                # Appending only names for now
                matched_users.append(other_user[output_type])
    elif str_or_list == 1:
        for country in user_acceptable_country_list:
            for other_user in data_list:
                if data_list.index(other_user) == user_index:
                    continue
                elif other_user['Country'] == country:
                    # Appending only names for now
                    matched_users.append(other_user[output_type])

#    print "Selected user : ", user['Name']
    return matched_users


def main():
    # Get data dynamically based on the profiles listed from filepath
    sample_list = getData('./profiles/')
    # list_matched_country(Name(str), data input(list), id or name output type(0->id, 1->Name)(default value->1))
    print list_matched_country("Kevin", sample_list)


if __name__ == '__main__':
    main()
