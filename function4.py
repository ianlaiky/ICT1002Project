"""
Python File: function4.py
Author: Lee Jonathan
Created: 23/01/2019
Last Modified: 29/01/2019
Requires: FuzzyWuzzy Lib, Levenshtein Libraries and functions from main
"""

from main import run as getData
from fuzzywuzzy import fuzz
import operator

def all_books(id_list, input_list):
    """
    Gets all the books read by each student
    Takes in list of ids to be ignored and list of all profiles
    Returns a dictionary of list of books read tagged to user id
    """

    """Initialize func var"""
    all_books_read_dict = {}

    """
    Iterate through list of profiles
    to find all other books other than
    the ones from the user himself
    """
    for profile in input_list:
        if not profile['id'] in id_list:  # if id does not match user ids to be ignored
            all_books_read_dict[profile['id']] = profile['Books']  # match that user's id to the books he/she read

    return all_books_read_dict  # saved as dict so can map user to his/her books when comparing


def cmp_books(user_book_list, cmp_book_dict):
    """
    Compares all the books read by user and books read by the rest
    Takes in list of books user reads and dictionary of books the rest reads
    Returns a list of ids of best matched people
    """

    """Initialize func var"""
    user_likeable_percentage_lst = []  # person's match percentage based on books read
    total_likeable_percentage_dict = {}  # total match percentages tagged to individual person
    top_3_id_lst = []  # list to be returned

    """Iterate through loop to calculate matchabiity"""
    for key, value in cmp_book_dict.items():
        for cmp_book in value:
            for user_book in user_book_list:
                user_likeable_percentage_lst.append(fuzz.partial_token_set_ratio(user_book,
                                                                                 cmp_book))  # using Levenshtein Distance (partial_token_set_ratio) to calculate
        total_likeable_percentage_dict[key] = sum(user_likeable_percentage_lst) / len(
            user_likeable_percentage_lst)  # get average based on matched %
        del user_likeable_percentage_lst[:]  # clear list after each person is iterated through

    """
    Sorts in descending order to get best matched to worst matched in order.
    Creates list of tuples"""
    total_likeable_percentage_dict = sorted(total_likeable_percentage_dict.items(), key=operator.itemgetter(1),
                                            reverse=True)

    return total_likeable_percentage_dict


def best3(list_of_tuples):
    """
    Takes the first 3 ids and puts them in a list
    :param list_of_tuples:
    :return: list_to_be_returned
    """

    list_to_be_returned = []
    for x in xrange(3):
        list_to_be_returned.append(list_of_tuples[x][0])

    return list_to_be_returned


def get_all_ids(list_of_tuples):
    """
    Takes in list of tuples and convert to list of ids
    :param list_of_tuples:
    :return: list_of_ids
    """

    list_of_ids = []
    for tuple in list_of_tuples:
        list_of_ids.append(tuple[0])

    return list_of_ids


def id_to_names(id_list, input_list):
    """
    Convert ids to names
    Takes in list of ids and dictionary of profiles
    Returns list of names
    """

    """Initialization of func var"""
    name_list = []

    """Iterate through list of profile to get names"""
    for x in xrange(len(id_list)):  # for each element in asc index
        for profile in input_list:
            if profile['id'] == id_list[x]:  # if id matches that in list of specific index
                name_list.append(profile['Name'])  # put this into list to be returned

    return name_list


def func4(name, input_list):
    """
    Takes in list of profiles and name to match with
    Outputs list of names matched according to
    interests in books
    """

    try:
        """Initialize function var"""
        books_of_user = []  # used to get books from given user
        list_of_ids = []  # stores list of ids inclu. id of given user and ids of same gender to avoid
        gender_of_user = ''  # store gender of user so can avoid those profiles

        """
        Iterate through profiles to get
        list of books and id from given user
        """
        for profile in input_list:
            if name == profile['Name']:  # if matches username
                books_of_user = profile['Books'][:]  # get book list and store as func var
                list_of_ids.append(profile['id'])  # store id into func var
                gender_of_user = profile['Gender']  # store gender as func var

        """Error Checking for names, to see if name exist"""
        if len(list_of_ids) != 1: #if there is no match of ids to the ids in the dataset
            raise ValueError

        """
        Wow this might be pretty inefficient
        Re-iterate through profiles to get 
        all ids of same gender as given user
        """
        for profile in input_list:
            if gender_of_user == profile['Gender']:  # if the gender matches that of user
                list_of_ids.append(profile['id'])  # add id to list to be ignored

        """
        Get all the books except those belonging to user
        Takes in ids to be ignored incl. user and list of profiles
        """
        books_dict_to_cmp = all_books(list_of_ids, input_list)

        """
        Get ids in desc order based on liked books
        Takes in the list of books from users
        and dictionary of other books to compare with
        """
        best_matched_ids = cmp_books(books_of_user, books_dict_to_cmp)

        """
        Gets the top 3 ids based on liked books
        Takes in id list of tuples
        Returns top3 ids to match with as a list
        """
        best_3_ids = best3(best_matched_ids)

        """
        Get list of names of best matched students
        Takes on best 3 ids given by cmp_book function
        and list of profiles
        """
        list_of_profile_names = id_to_names(best_3_ids, input_list)

        return list_of_profile_names

    except ValueError:
        print "No such user %s, please try again!" %name #if name does not exist, print this


def func4_returnallids(name, input_list):
    """
    Takes in list of profiles and name to match with
    Outputs list of ids for ALL matched according to
    interests in books
    """

    try:

        """Initialize function var"""
        books_of_user = []  #used to get books from given user
        list_of_ids = []  #stores list of ids inclu. id of given user and ids of same gender to avoid
        gender_of_user = '' #store gender of user so can avoid those profiles

        """
        Iterate through profiles to get
        list of books and id from given user
        """
        for profile in input_list:
            if name == profile['Name']:  #if matches username
                books_of_user = profile['Books'][:]  #get book list and store as func var
                list_of_ids.append(profile['id'])  #store id into func var
                gender_of_user = profile['Gender'] #store gender as func var

        """
        Wow this might be pretty inefficient
        Re-iterate through profiles to get 
        all ids of same gender as given user
        """
        for profile in input_list:
            if gender_of_user == profile['Gender']: # if the gender matches that of user
                list_of_ids.append(profile['id']) # add id to list to be ignored


        """
        Get all the books except those belonging to user
        Takes in ids to be ignored incl. user and list of profiles
        """
        books_dict_to_cmp = all_books(list_of_ids, input_list)

        """
        Get list of tuples of ids and values in desc order based on liked books
        Takes in the list of books from users
        and dictionary of other books to compare with
        """
        best_matched_ids = cmp_books(books_of_user, books_dict_to_cmp)

        """
        Take list of tuples and return list of all ids
        """
        best_matched_ids = get_all_ids(best_matched_ids)

        return best_matched_ids

    except ValueError:
        print "No such user %s, please try again!" %name #if name does not exist, print this


def main(folder_path):
    # Get data dynamically based on the profiles listed from filepath
    sample_list = getData(folder_path)
    func4_returnallids("Joel Jackson", sample_list)


if __name__ == '__main__':
    main()
