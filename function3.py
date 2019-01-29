"""
Python File: function4.py
Author: Chan Hon Siang and Lee Jonathan
Created: 29/01/2019
Last Modified: 29/01/2019
Requires: FuzzyWuzzy Lib, Levenshtein Libraries and in-built libraries from function 4 and main
"""
from fuzzywuzzy import fuzz
from function4 import best3, get_all_ids
from main import run as getData
import operator

def likes(id_list, likes_list):

    likes = {}
    for profile in likes_list:
        if not profile['id'] in id_list:  # if id does not match user ids to be ignored
            likes[profile['id']] = profile['Likes']  # match that user's id to likes they have

    return likes  # saved as dict so can map user to his/her likes when comparing

def dislikes(id_list, dislikes_list):

    dislikes = {}
    for profile in dislikes_list:
        if not profile['id'] in id_list:  # if id does not match user ids to be ignored
            dislikes[profile['id']] = profile['Dislikes']  # match that user's id to their dislikes

    return dislikes  # saved as dict so can map user to their dislikes when comparing

def cmp_likes(user_likes_list, cmp_likes_dict, user_dislikes_list, cmp_dislikes_dict):
    """
    Compares both the likes and dislikes of each user and compare them to the rest
    Returns list of tuples
    """

    """Initialize func var"""
    user_likeable_percentage_lst = []  # person's match percentage based on their likes
    total_likeable_percentage_dict = {} # total match percentages tagged to individual person
    user_dislikeable_percentage_lst = []  # same as above but for dislikes
    total_dislikeable_percentage_dict = {}  # same as above but for dislikes
    user_contradict_lst = []  # compares the likes and dislikes of user
    total_contradict_percentage_dict = {}  # compares the likes and dislikes for user and see if matches
    total_rating_dict = {} #rating of user based on likes and dislikes


    """Iterate through loop to calculate matchabiity"""
    for key, value in cmp_likes_dict.items(): ##cmp likes with likes
        for cmp_like in value:
            for user_like in user_likes_list:
                user_likeable_percentage_lst.append(fuzz.partial_token_set_ratio(user_like,
                                                                                 cmp_like))  # using Levenshtein Distance (partial_token_set_ratio) to calculate
        total_likeable_percentage_dict[key] = sum(user_likeable_percentage_lst) / len(
            user_likeable_percentage_lst)  # get average based on matched %
        del user_likeable_percentage_lst[:]  # clear list after each person is iterated through

    for key, value in cmp_dislikes_dict.items(): #cmp dislikes with dislikes
        for cmp_dislikes in value:
            for user_dislike in user_dislikes_list:
                user_dislikeable_percentage_lst.append(fuzz.partial_token_set_ratio(user_dislike,
                                                                                 cmp_dislikes))  # using Levenshtein Distance (partial_token_set_ratio) to calculate
        total_dislikeable_percentage_dict[key] = sum(user_dislikeable_percentage_lst) / len(
            user_dislikeable_percentage_lst)  # get average based on matched %
        del user_dislikeable_percentage_lst[:]  # clear list after each person is iterated through

    for key, value in cmp_dislikes_dict.items(): #cmp user likes with cmp_list dislikes
        for cmp_dislike in value:
            for user_like in user_likes_list:
                user_contradict_lst.append(fuzz.partial_token_set_ratio(user_like,
                                                                                 cmp_dislike))  # using Levenshtein Distance (partial_token_set_ratio) to calculate
        total_contradict_percentage_dict[key] = sum(user_contradict_lst) / len(user_contradict_lst)  # get average based on matched %
        del user_dislikeable_percentage_lst[:]  # clear list after each person is iterated through

    """
    Iterate through likeable and dislikeable percentage to calculate value of rating
    Stores as a dictionary
    """
    for like_key, like_value in total_likeable_percentage_dict.iteritems():
        if total_dislikeable_percentage_dict.has_key(like_key) and total_contradict_percentage_dict.has_key(like_key):
            rating = (2 * like_value) + (2*total_dislikeable_percentage_dict[like_key]) - (1.5 * total_contradict_percentage_dict[like_key])#rating calculated by 2 * cmp_like_rating + 2 * cmp_dislike_rating - 1.5 * contradict
            total_rating_dict[like_key] = rating

    """
    Sorts in descending order to get best matched to worst matched in order.
    Creates list of tuples
    """
    total_rating_dict = sorted(total_rating_dict.items(), key=operator.itemgetter(1),
                                            reverse=True)
    return total_rating_dict

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

def func3(name, inputlist):
    """
    Takes in list of profiles and name to match with
    Outputs list of top 3 names matched according to
    interests in likes and dislikes
    """

    try:

        """Initialize function var"""
        likes_of_user = []  # used to get likes from given user
        dislikes_of_user = [] # same as above but for dislikes
        list_of_ids = []  # stores list of ids inclu. id of given user and ids of same gender to avoid
        gender_of_user = ''  # store gender of user so can avoid those profiles


        for profile in inputlist:
            if name == profile['Name']:  # if matches username
                likes_of_user = profile['Likes'][:]  # get book list and store as func var
                dislikes_of_user = profile["Dislikes"][:]
                list_of_ids.append(profile['id'])  # store id into func var
                gender_of_user = profile['Gender']  # store gender as func var


        for profile in inputlist:
            if gender_of_user == profile['Gender']:  # if the gender matches that of user
                list_of_ids.append(profile['id'])  # add id to list to be ignored

        """
        Get both the likes and dislikes of users and store in a dict
        """
        likes_dict_to_cmp = likes(list_of_ids, inputlist)
        dislikes_dict_to_cmp = dislikes(list_of_ids, inputlist)
        """
        Get list of ids and ratings in desc order for user based on algorithm
        """
        best_matched_ids = cmp_likes(likes_of_user, likes_dict_to_cmp, dislikes_of_user, dislikes_dict_to_cmp)
        """
        Returns list of best 3 ids based on list of values
        """
        best_3_ids = best3(best_matched_ids)
        """
        Get list of names of best matched students
        Takes on best 3 ids given by cmp_likes function
        and list of profiles
        """
        list_of_profile_names = id_to_names(best_3_ids, inputlist)

        return list_of_profile_names

    except ValueError:
        print "No such user %s, please try again!" %name #if name does not exist, print this


def func3_returnallids(name, inputlist):
    """
    Takes in list of profiles and name to match with
    Outputs list of ALL ids matched according to
    interests in likes and dislikes
    """

    try:

        """Initialize function var"""
        likes_of_user = []  # used to get likes from given user
        dislikes_of_user = []  # same as above but for dislikes
        list_of_ids = []  # stores list of ids inclu. id of given user and ids of same gender to avoid
        gender_of_user = ''  # store gender of user so can avoid those profiles

        for profile in inputlist:
            if name == profile['Name']:  # if matches username
                likes_of_user = profile['Likes'][:]  # get book list and store as func var
                dislikes_of_user = profile["Dislikes"][:]
                list_of_ids.append(profile['id'])  # store id into func var
                gender_of_user = profile['Gender']  # store gender as func var

        for profile in inputlist:
            if gender_of_user == profile['Gender']:  # if the gender matches that of user
                list_of_ids.append(profile['id'])  # add id to list to be ignored

        """
        Get both the likes and dislikes of users and store in a dict
        """
        likes_dict_to_cmp = likes(list_of_ids, inputlist)
        dislikes_dict_to_cmp = dislikes(list_of_ids, inputlist)

        """
        Get list of ids and ratings in desc order for user based on algorithm
        """
        best_matched_ids = cmp_likes(likes_of_user, likes_dict_to_cmp, dislikes_of_user, dislikes_dict_to_cmp)

        """
        Take list of tuples and return list of all ids
        """
        best_matched_ids = get_all_ids(best_matched_ids)

        return best_matched_ids

    except ValueError:
        print "No such user %s, please try again!" %name #if name does not exist, print this


def main():
    # Get data dynamically based on the profiles listed from filepath
    sample_list = getData('./profiles/')
    print "For Michael:"
    print func3('Michael Jackson', sample_list)
    print "\nFor Carol:"
    print func3('Carol', sample_list)
    print "\nFor Kevin:"
    print func3('Kevin', sample_list)
    print "\nFor Rose:"
    print func3('Rose', sample_list)
    print "\nFor Shelley:"
    print func3('Shelley', sample_list)
    print "\nFor Joel:"
    print func3('Joel Jackson', sample_list)
    print "\nFor Jenny:"
    print func3('Jenny Wang', sample_list)
    print "\nFor Angela:"
    print func3('Angela Little', sample_list)
    print "\nFor Lisa:"
    print func3('Lisa Marie', sample_list)
    print "\nFor Teresa:"
    print func3('Teresa', sample_list)
    print func3_returnallids('Michael Jackson', sample_list)


if __name__ == '__main__':
    main()
