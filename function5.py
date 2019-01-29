"""
Python File: function4.py
Author: Lee Jonathan
Created: 29/01/2019
Last Modified: 29/01/2019
Requires: In-built libraries from Function 2,3,4 and main
"""

from main import run as getData
from function2 import list_matched_country
from function3 import func3
from function4 import func4, best3, id_to_names


def func5(user_name, input_list):
    """
    Get user name and return overall suitability based on acceptable_country, books, interest
    :param user_name: @string -> username given by user
    :param input_list: @list -> list of profiles
    :return: list_of_names: @string -> list of names best matching given user
    """

    """Get data from different functions"""
    ids_match_country = list_matched_country(user_name, input_list, 1) #get list of ids which best matches based on id
    interest_based_data = func3(user_name, input_list, 1)#get id and scores which matches user based on interests
    books_based_data = func4(user_name, input_list, 1) #get id and scores which matches user based on books
    gender_of_user = "" #stores gender of user locally to be used later
    score_dict = {} #scores assigned to id

    """
    TODO: Remove when Jun Yan is done sleeping
    Currently placed here for Jun Yan to do on his part
    To get the gender of the user
    """
    for profile in input_list:
        if profile["Name"] == user_name: #if user name matches name in list
            gender_of_user = profile["Gender"] #set it as local var
            break
    """
    Given the gender of the user, iterate through list of ids which matches country
    Only leave opposite gender in list
    """
    for profile in input_list:
        if profile["id"] in ids_match_country and gender_of_user == profile["gender"]: #if id is in matched_country_list and matches gender of user
            ids_match_country.remove(profile["id"]) #remove it from the list

    """
    Iterate through the datasets and add up the score based on user_id
    """
    for interest_key, interest_value in interest_based_data.iteritems(): #interest key = id of user; interest_value = score for interest
        score_for_user = 0 #set score of individual locally
        if books_based_data.has_key(interest_key): #if the id is found in datasets of book scores
            score_for_user = interest_value + books_based_data[interest_key] #add the scores for interest and books together
        if interest_key in ids_match_country: #if id is in the list of acceptable country
            score_for_user += 150 #add 150 points to the score
        score_dict[interest_key] = score_for_user

    """Return top 3 scorer ids for this dictionary"""
    score_dict = best3(score_dict)

    """Translate ids for top 3 scorers to names"""
    list_of_names = id_to_names(score_dict, input_list)
    return list_of_names


def main():
    # Get data dynamically based on the profiles listed from filepath
    sample_list = getData('./profiles/')
    print func5("Michael Jackson", sample_list)


if __name__ == '__main__':
    main()

