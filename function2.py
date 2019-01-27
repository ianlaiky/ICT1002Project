"""
Python File: function2.py
Author: Goh Jun Yan
"""

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
    # This is printing (id=4)Kevin's
    print list_matched_country(4, sample_list)


if __name__ == '__main__':
    main()
