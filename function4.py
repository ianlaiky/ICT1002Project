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
    Get all the books read by each student excluding those from id to be ignored
    :param id_list: @list -> list of ids to ignore
    :param input_list: @list -> list of profiles
    :return: all_books_read_dict: @dictionary -> list of books tagged by user id as a dictionary
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
    Compares all books read by user and books read by the rest
    :param user_book_list: @list -> list of books read by user
    :param cmp_book_dict: @list > list of books to compare with
    :return: @total_likeable_percentage_dict: @dictionary -> score attached to user id in a dictionary
    """

    """Initialize func var"""
    user_likeable_percentage_lst = []  # person's match percentage based on books read
    total_likeable_percentage_dict = {}  # total match percentages tagged to individual person

    """Iterate through loop to calculate matchabiity"""
    for key, value in cmp_book_dict.items():
        for cmp_book in value:
            for user_book in user_book_list:
                user_likeable_percentage_lst.append(fuzz.partial_token_set_ratio(user_book,
                                                                                 cmp_book))  # using Levenshtein Distance (partial_token_set_ratio) to calculate
        total_likeable_percentage_dict[key] = sum(user_likeable_percentage_lst) / len(
            user_likeable_percentage_lst)  # get average based on matched %
        del user_likeable_percentage_lst[:]  # clear list after each person is iterated through

    return total_likeable_percentage_dict


def best3(input_dict):
    """
    Sort and takes the first 3 ids and puts them in a list
    :param input_dict: @dictionary -> dictionary of values tagged to id
    :return: list_to_be_returned: @list -> list of top 3 ids to be returned
    """

    """
    Sorts in descending order to get best matched to worst matched in order.
    Creates list of tuples"""
    input_dict = sorted(input_dict.items(), key=operator.itemgetter(1), reverse=True)
    list_to_be_returned = []
    for x in xrange(3):
        list_to_be_returned.append(input_dict[x][0])

    return list_to_be_returned

def id_to_names(id_list, input_list):
    """
    Convert ids to names
    :param id_list: @list -> list of ids
    :param input_list: @list -> list of profiles
    :return: name_list: @list -> list of converted names
    """

    """Initialization of func var"""
    name_list = []

    """Iterate through list of profile to get names"""
    for x in xrange(len(id_list)):  # for each element in asc index
        for profile in input_list:
            if profile['id'] == id_list[x]:  # if id matches that in list of specific index
                name_list.append(profile['Name'])  # put this into list to be returned

    return name_list

def profile_elimination(gender_of_user, youngest_age, oldest_age, input_list):
    """
    Eliminates profiles based on user's acceptable age range and gender
    :param gender_of_user: @str -> gender of user
    :param youngest_age: @int -> youngest acceptable age by user
    :param oldest_age: @int -> oldest acceptable age by user
    :param input_list: @list -> list of profiles
    :return: id_list_to_ignore: @list -> list of ids that suit acceptable age range and opp gender
    """

    id_list_to_ignore = [] #puts the value of user ids into the list of ids to be ignored

    for profile in input_list:
        if profile['Gender'] == gender_of_user:
            id_list_to_ignore.append(profile['id'])
            hi = int(profile['Age'])
        elif not int(profile['Age']) in xrange(youngest_age, oldest_age+1):
            id_list_to_ignore.append(profile['id'])

    return id_list_to_ignore


def func4(name, input_list, OUTPUT_FLAG=0):
    """
    Based on user's general interests and disinterests, give out 3 most suited candidates for matching or return whole dataset
    :param name: @string -> username given by user
    :param input_list: @id -> list of profiles
    :param OUTPUT_FLAG: @int -> if =0 return top 3 ids based on book pref elif =1 return dataset of full scores
    :return:
    """
    """
    Takes in list of profiles and name to match with
    Outputs list of names matched according to
    interests in books
    """

    try:
        """Initialize function var"""
        books_of_user = []  # used to get books from given user
        gender_of_user = ''  # store gender of user so can avoid those profiles
        id_of_user = '' #store id of user as a func var
        youngest_acceptable_age = 0 #youngest age that can be accepted by given user
        oldest_acceptable_age = 0 #oldest age that can be accepted by given user

        """
        Iterate through profiles to get
        list of books and id from given user
        """
        for profile in input_list:
            if name == profile['Name']:  # if matches username
                books_of_user = profile['Books'][:]  # get book list and store as func var
                id_of_user = profile['id'] #gets id of user to ignore
                acceptable_age_list = list(profile['Acceptable_age_range'].split('-')) #gets age range and store as range of numbers
                youngest_acceptable_age  = int(acceptable_age_list[0])#gets the youngest age
                oldest_acceptable_age = int(acceptable_age_list[1])  #gets the oldest age
                gender_of_user = profile['Gender']  # store gender as func var

        """Error Checking for names, to see if name exist"""
        if id_of_user == '': #if there is no match of ids to the ids in the dataset
            raise ValueError

        list_of_ids = profile_elimination(gender_of_user, youngest_acceptable_age, oldest_acceptable_age, input_list)

        """
        Get all the books except those belonging to user
        Takes in ids to be ignored incl. user and list of profiles
        """
        books_dict_to_cmp = all_books(list_of_ids, input_list)

        """
        Get data in dict based on liked books
        Takes in the list of books from users
        and dictionary of other books to compare with
        """
        best_matched_ids = cmp_books(books_of_user, books_dict_to_cmp)

        if OUTPUT_FLAG == 1:
            return best_matched_ids
        elif OUTPUT_FLAG == 0:
            """
            Sorts and Gets the top 3 ids based on liked books
            Takes in data in dict
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


def main(folder_path,name):
    # Get data dynamically based on the profiles listed from filepath
    sample_list = getData(folder_path)
    output_list = func4(name, sample_list)
    print("You matched with the following based on your favourite books: ")
    print("\n".join(output_list))


if __name__ == '__main__':
    main()
