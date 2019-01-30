"""
Python File: function2.py
Author: Goh Jun Yan
"""
from function1 import run as getData


def list_matched_country(value, data_list, id_or_name=1):

    """
    List all the students that fall in to the acceptable country of B should be printed out
    (After matching for opposite gender, acceptable age)
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
    user_gender = ""
    acceptable_age_list = []
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
    Iterates through the data_list to get the user's acceptable country, get the user's index so we can
    ignore the index during loops and get the gender of the user
    """
    for user in data_list:
        # If searching the data_list using id
        if user['Name'] == value:
            # Record index
            user_index = data_list.index(user)
            user_gender = user['Gender']
            acceptable_age_list = user['Acceptable_age_range'].split("-")
            acceptable_age_list = map(int, acceptable_age_list)
            # Checks if the dict value is a str
            if isinstance(user['Acceptable_country'], str):
                user_acceptable_country_str = user['Acceptable_country']
                str_or_list = 0
            # Checks if the dict value is a list
            elif isinstance(user['Acceptable_country'], list):
                user_acceptable_country_list = user['Acceptable_country']
                str_or_list = 1
            break

#    print acceptable_age_list
#    print "max = ", max(acceptable_age_list)
#    print "min = ", min(acceptable_age_list)

    """
    Iterates through the data_list, ignores selected user's index and compares the other user's country to
    the user acceptable country (str/list). If matched, append the other user's Name(for now) to matched_users list        
    """
    if user_index == -1:
        print "Error: (Function 2)Unable to get user index"
    elif user_gender == "":
        print "Error: (Function 2)Unable to retrieve gender of user"
    elif str_or_list == -1:
        print "Error: (Function 2)String or List"
    # If User_acceptable_country is stored as a string
    elif str_or_list == 0:
        for other_user in data_list:
            # Ignore the selected user
            if data_list.index(other_user) == user_index:
                continue
            # Ignore the same sex
            elif other_user['Gender'] == user_gender:
                continue
            # Match user's acceptable countries with other_user's country
            elif other_user['Country'] == user_acceptable_country_str:
                # If other_user's age falls in between the acceptable age range of the selected user
                if min(acceptable_age_list) <= int(other_user['Age']) <= max(acceptable_age_list):
                    # Appending matched other_user to the matched_users list
                    matched_users.append(other_user[output_type])
    # If User_acceptable_country is stored as a list
    elif str_or_list == 1:
        for country in user_acceptable_country_list:
            for other_user in data_list:
                # Ignore the selected user
                if data_list.index(other_user) == user_index:
                    continue
                # Ignore the same sex
                elif other_user['Gender'] == user_gender:
                    continue
                # Match user's acceptable countries with other_user's country
                elif other_user['Country'] == country:
                    # If other_user's age falls in between the acceptable age range of the selected user
                    if min(acceptable_age_list) <= int(other_user['Age']) <= max(acceptable_age_list):
                        # Appending matched other_user to the matched_users list
                        matched_users.append(other_user[output_type])

    return matched_users


def main(folder_path, name):
    # Get data dynamically based on the profiles listed from filepath
    sample_list = getData(folder_path)
    # list_matched_country(Name(str), data input(list), id or name output type(0->id, 1->Name)(default value->1))
    output_list = list_matched_country(name, sample_list)
    print("You matched with the following based on your countries: ")
    print("\n".join(output_list))

if __name__ == '__main__':
    main()
