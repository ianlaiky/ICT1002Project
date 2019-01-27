from function4 import func4

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


def main():
    print "For Michael:"
    print func4('Michael Jackso', sample_list) #first use case to test for wrong input
    print "\nFor Michael:"
    print func4('Michael Jackson', sample_list)
    print "\nFor Carol:"
    print func4('Carol', sample_list)
    print "\nFor Kevin:"
    print func4('Kevin', sample_list)
    print "\nFor Rose:"
    print func4('Rose', sample_list)
    print "\nFor Shelley:"
    print func4('Shelley', sample_list)
    print "\nFor Joel:"
    print func4('Joel Jackson', sample_list)
    print "\nFor Jenny:"
    print func4('Jenny Wang', sample_list)
    print "\nFor Angela:"
    print func4('Angela Little', sample_list)
    print "\nFor Lisa:"
    print func4('Lisa Marie', sample_list)
    print "\nFor Teresa:"
    print func4('Teresa', sample_list)


if __name__ == '__main__':
    main()
