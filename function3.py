"""
Python File: function4.py
Author: Chan Hon Siang and Lee Jonathan
Created: 29/01/2019
Last Modified: 29/01/2019
Requires: FuzzyWuzzy Lib, Levenshtein Libraries and in-built libraries from function 4 and main
"""
from fuzzywuzzy import fuzz
from function4 import best3, id_to_names, profile_elimination
from main import run as getData


def likes(id_list, input_list):
    """
    Creates list of likes to be compared with
    :param id_list: @list -> list of ids to ignore
    :param input_list: @list -> list of profiles
    :return: likes: @list -> return list of likes to compare with
    """
    likes = {}
    for profile in input_list:
        if not profile['id'] in id_list:  # if id does not match user ids to be ignored
            likes[profile['id']] = profile['Likes']  # match that user's id to likes they have

    return likes  # saved as dict so can map user to his/her likes when comparing

def dislikes(id_list, input_list):
    """
    Creates list of dislikes to be compared with
    :param id_list: @list -> list of ids to ignore
    :param input_list: @ist -> list of profiles
    :return: likes: @list -> return list of dislikes to compare with
    """
    dislikes = {}
    for profile in input_list:
        if not profile['id'] in id_list:  # if id does not match user ids to be ignored
            dislikes[profile['id']] = profile['Dislikes']  # match that user's id to their dislikes

    return dislikes  # saved as dict so can map user to their dislikes when comparing

def cmp_likes(user_likes_list, cmp_likes_dict, user_dislikes_list, cmp_dislikes_dict):
    """
    Compares both the likes, dislikes and return result based on algo
    :param user_likes_list: @list -> list of user's likes
    :param cmp_likes_dict: @list -> list of likes to compare with
    :param user_dislikes_list: @list -> list of user's dislikes
    :param cmp_dislikes_dict: @list -> list of dislikes to compare with
    :return: total_rating_dict: @dict -> dictionary of ids tagged to score
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
    for key, value in cmp_likes_dict.items(): #cmp likes with likes
        for cmp_like in value:
            for user_like in user_likes_list:
                user_likeable_percentage_lst.append(fuzz.partial_token_set_ratio(user_like, cmp_like))  # using Levenshtein Distance (partial_token_set_ratio) to calculate
        total_likeable_percentage_dict[key] = sum(user_likeable_percentage_lst) / len(
            user_likeable_percentage_lst)  # get average based on matched %
        del user_likeable_percentage_lst[:]  # clear list after each person is iterated through

    for key, value in cmp_dislikes_dict.items(): #cmp dislikes with dislikes
        for cmp_dislikes in value:
            for user_dislike in user_dislikes_list:
                user_dislikeable_percentage_lst.append(fuzz.partial_token_set_ratio(user_dislike, cmp_dislikes))  # using Levenshtein Distance (partial_token_set_ratio) to calculate
        total_dislikeable_percentage_dict[key] = sum(user_dislikeable_percentage_lst) / len(user_dislikeable_percentage_lst)  # get average based on matched %
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
    for like_key, like_value in total_likeable_percentage_dict.iteritems(): #for every id and like percentage value
        if total_dislikeable_percentage_dict.has_key(like_key) and total_contradict_percentage_dict.has_key(like_key): #if the id exist in both other dict
            rating = (2 * like_value) + (2*total_dislikeable_percentage_dict[like_key]) - (1.5 * total_contradict_percentage_dict[like_key])#rating calculated by 2 * cmp_like_rating + 2 * cmp_dislike_rating - 1.5 * contradict
            total_rating_dict[like_key] = rating #store in dict

    return total_rating_dict


def func3(name, inputlist, OUTPUT_FLAG=0):
    """
    Based on user's book interest, give out 3 most suited candidates for matching or return whole dataset
    :param name: @string -> name of user
    :param inputlist: @list -> list of profiles
    :param OUTPUT_FLAG: @int -> if =0 return top 3 ids based on book pref elif =1 return dataset of full scores
    :return:
    """
    try:
        """Initialize function var"""
        likes_of_user = []  # used to get likes from given user
        dislikes_of_user = [] # same as above but for dislikes
        id_of_user = ''  # store id of user as a func var
        youngest_acceptable_age = 0  # youngest age that can be accepted by given user
        oldest_acceptable_age = 0  # oldest age that can be accepted by given user


        for profile in inputlist:
            if name == profile['Name']:  # if matches username
                likes_of_user = profile['Likes'][:]  # get likes and store as func var
                dislikes_of_user = profile["Dislikes"][:] #get dislikes and store as func var
                id_of_user = profile['id']  # gets id of user to ignore
                acceptable_age_list = list(profile['Acceptable_age_range'].split('-'))  # gets age range and store as range of numbers
                youngest_acceptable_age = int(acceptable_age_list[0])  # gets the youngest age
                oldest_acceptable_age = int(acceptable_age_list[1])  # gets the oldest age
                gender_of_user = profile['Gender']  # store gender as func var

        """Error Checking for names, to see if name exist"""
        if id_of_user == '':  # if there is no match of ids to the ids in the dataset
            raise ValueError

        list_of_ids = profile_elimination(gender_of_user, youngest_acceptable_age, oldest_acceptable_age, inputlist)

        """
        Get both the likes and dislikes of users and store in a dict
        """
        likes_dict_to_cmp = likes(list_of_ids, inputlist)
        dislikes_dict_to_cmp = dislikes(list_of_ids, inputlist)

        """
        Get dict of data in desc order for user based on algorithm
        """
        best_matched_ids = cmp_likes(likes_of_user, likes_dict_to_cmp, dislikes_of_user, dislikes_dict_to_cmp)

        if OUTPUT_FLAG == 1:
            return best_matched_ids
        elif OUTPUT_FLAG == 0:
            """
            Sorts and Gets list of best 3 ids based on list of values
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
    print func3('Michael Jackson', sample_list, 1)


if __name__ == '__main__':
    main()
