"""
Python File: function4.py
Author: Lee Jonathan
Created: 23/01/2019
Last Modified: 23/01/2019
Requires: FuzzyWuzzy Lib and Levenshtein Libraries
"""

from fuzzywuzzy import fuzz
import operator

sample_list = [{'Name': 'Michael Jackson', 'Gender': 'M', 'Age': '29', 'Dislikes': ['durain', 'garlic', 'swimming'],
                'Acceptable_age_range': '18-29', 'Acceptable_country': ['Singapore', 'China'],
                'Books': ['Mere Christianity', 'Knowing God', 'The problem of Pain', 'The God who is there',
                          'The reason for God: belief in an age of skepticism',
                          'Experiencing God: knowing and doing the will of God, work book'],
                'Likes': ['hotpot', 'chicken and chops', 'chilli', 'roses', 'movies'], 'Country': 'Singapore', 'id': 0},
               {'Name': 'Lisa Marie', 'Gender': 'F', 'Age': '22', 'Dislikes': ['garlic', 'durain', 'swimming'],
                'Acceptable_age_range': '18-30', 'Acceptable_country': ['Singapore', 'China'],
                'Books': ['Desiring God Meditations of a Christian Hedonist', 'God Knowing',
                          'God Favor: Breath of Heaven', 'The God is there',
                          'The reason for God: in an age of skepticism',
                          'Experiencing God: knowing the will of God, work book'],
                'Likes': ['hotpot', 'chilli', 'chicken and chops', 'roses', 'movies'], 'Country': 'Singapore', 'id': 1},
               {'Name': 'Teresa', 'Gender': 'F', 'Age': '22', 'Dislikes': ['garlic', 'durain', 'swimming'],
                'Acceptable_age_range': '18-30', 'Acceptable_country': ['Singapore', 'China'],
                'Books': ['Total Truth: Liberating Christianity from its Cultural Captivity',
                          'Reflections on the Psalms',
                          'Intercessory Prayer: How God Can Use Your Prayers to Move Heaven Earth',
                          "God 's Favor - Breath Of Heaven", 'Letters to Malcolm: Chiefly on Prayer'],
                'Likes': ['hotpot', 'chilli', 'chicken and chops', 'roses', 'movies'], 'Country': 'Singapore', 'id': 2},
               {'Name': 'Carol', 'Gender': 'F', 'Age': '23', 'Dislikes': ['football', 'hunting', 'swimming'],
                'Acceptable_age_range': '23-50', 'Acceptable_country': ['Singapore', 'China'],
                'Books': ['Christian reflections', 'The red tent', 'The God who is there',
                          'God in the Dock: Essays on Theology and Ethics',
                          'Total truth: liberating christianity from its cultural captivity', 'Redeeming love'],
                'Likes': ['Chicken rice', 'hotpot', 'Carrot cake', 'chilli crab', 'roses', 'movies'], 'Country': 'USA',
                'id': 3}, {'Name': 'Kevin', 'Gender': 'M', 'Age': '25', 'Dislikes': ['curry', 'garlic', 'basketball'],
                           'Acceptable_age_range': '10-33', 'Acceptable_country': 'Singapore',
                           'Books': ['Human Philosohy', 'Adventures in Human Being', 'Meditations on the Philosophy',
                                     'Essay Concerning Human topic', 'Principles of Human being'],
                           'Likes': ['fish', 'chiken', 'chocolate', 'roses', 'durain', 'movies'],
                           'Country': 'Singapore', 'id': 4},
               {'Name': 'Rose', 'Gender': 'F', 'Age': '25', 'Dislikes': ['chilli', 'garlic', 'basketball'],
                'Acceptable_age_range': '18-35', 'Acceptable_country': ['Singapore', 'China', 'UK'],
                'Books': ['Human Philosohy book', 'Adventures in Human Being', 'Towards the Philosophy',
                          'Essay Related Human Topics', 'Human Being Shall Know Philosohy'],
                'Likes': ['fish', 'honey', 'chocolate', 'roses', 'durain', 'running'], 'Country': 'Singapore', 'id': 5},
               {'Name': 'Shelley', 'Gender': 'F', 'Age': '24', 'Dislikes': ['chilli', 'garlic', 'basketball'],
                'Acceptable_age_range': '18-35', 'Acceptable_country': ['Singapore', 'China', 'USA'],
                'Books': ['Human Philosohy book', 'Adventures in Human Being', 'Towards the Philosophy',
                          'Essay Related Human Topics', 'Human Being Shall Know Philosohy'],
                'Likes': ['fish', 'honey', 'chocolate', 'roses', 'durain', 'running'], 'Country': 'China', 'id': 6},
               {'Name': 'Joel Jackson', 'Gender': 'M', 'Age': '29', 'Dislikes': ['durain', 'garlic', 'swimming'],
                'Acceptable_age_range': '18-33', 'Acceptable_country': ['Singapore', 'China', 'USA'],
                'Books': ['Human Philosohy', 'Nicomachean Ethics', 'Summa Theologiae',
                          'Meditations on First Philosophy', 'Essay Concerning Human Understanding',
                          'Principles of Human Knowledge', 'Enquiry Concerning Human Understanding', 'Social Contract',
                          'Phenomenology of Spirit'],
                'Likes': ['hotpot', 'chicken and chops', 'chilli', 'roses', 'movies'], 'Country': 'Singapore', 'id': 7},
               {'Name': 'Jenny Wang', 'Gender': 'F', 'Age': '25', 'Dislikes': ['durain', 'garlic', 'swimming'],
                'Acceptable_age_range': '23-60', 'Acceptable_country': ['China', 'USA', 'Singapore'],
                'Books': ['Mere Christianity', 'Knowing God',
                          'How should we then live? the rise and decline of western thought and culture',
                          'The problem of Pain', 'The God who is there',
                          'The reason for God: belief in an age of skepticism',
                          'Experiencing God: knowing and doing the will of God, work book'],
                'Likes': ['hotpot', 'chicken and chops', 'chilli', 'roses', 'movies'], 'Country': 'China', 'id': 8},
               {'Name': 'Angela Little', 'Gender': 'F', 'Age': '22',
                'Dislikes': ['hotpot', 'chilli', 'roses', 'movies'], 'Acceptable_age_range': '18-30',
                'Acceptable_country': ['Singapore', 'China'],
                'Books': ['Christian reflections', 'The red tent', 'The God who is there',
                          'God in the Dock: Essays on Theology and Ethics',
                          'Total truth: liberating christianity from its cultural captivity', 'Redeeming love'],
                'Likes': ['garlic', 'durain', 'swimming', 'chicken and chops'], 'Country': 'Singapore', 'id': 9}]


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
    print total_likeable_percentage_dict

    """Takes first 3 values of sorted struct and store in list to be returned"""
    for x in xrange(3):
        top_3_id_lst.append(total_likeable_percentage_dict[x][0])

    return top_3_id_lst


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
    Get top 3 ids based on liked books
    Takes in the list of books from users
    and dictionary of other books to compare with
    """
    best_3_ids = cmp_books(books_of_user, books_dict_to_cmp)

    """
    Get list of names of best matched students
    Takes on best 3 ids given by cmp_book function
    and list of profiles
    """
    list_of_profile_names = id_to_names(best_3_ids, input_list)

    return list_of_profile_names


def main():
    func4('Joel Jackson', sample_list)


if __name__ == '__main__':
    main()
