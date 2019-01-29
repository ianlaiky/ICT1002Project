"""
Python File: function4.py
Author: Lee Jonathan
Created: 29/01/2019
Last Modified: 29/01/2019
Requires: In-built libraries from Function 2,3,4 and main
"""

from main import run as getData
from function2 import list_matched_country
from function3 import func3_returnalldata
from function4 import func4_returnalldata, best3, id_to_names


def func5(user_name, input_list):
    """
    Get user name and return overall suitability based on acceptable_country, books, interest
    :param user_name:
    :param input_list:
    :return: list_of_names:
    """

    ids_match_country = list_matched_country(user_name, input_list, 1)
    interest_based_data = func3_returnalldata(user_name, input_list)
    books_based_data = func4_returnalldata(user_name, input_list)
    gender_of_user = ""
    score_dict = {}

    for profile in input_list:
        if profile["Name"] == user_name:
            gender_of_user = profile["Gender"]
            break

    for profile in input_list:
        if profile["id"] in ids_match_country and gender_of_user == profile["gender"]:
            ids_match_country.remove(profile["id"])


    for interest_key, interest_value in interest_based_data.iteritems():
        score_for_user = 0
        if books_based_data.has_key(interest_key):
            score_for_user = interest_value + books_based_data[interest_key]
        if interest_key in ids_match_country:
            score_for_user +=100
        score_dict[interest_key] = score_for_user

    score_dict = best3(score_dict)
    list_of_names = id_to_names(score_dict, input_list)
    return list_of_names


def main():
    # Get data dynamically based on the profiles listed from filepath
    sample_list = getData('./profiles/')
    print func5("Michael Jackson", sample_list)


if __name__ == '__main__':
    main()

