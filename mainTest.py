"""
Python File: mainTest.py
Author: Ian Lai Kheng Yan
"""

from function1 import run as main


def mainTest(path):
    list_of_dictionary_profiles_data = main(path)

    for i in list_of_dictionary_profiles_data:
        print "Unique Id: ", i["id"]

        print "Name: ", i["Name"]

        print "Gender: ", i["Gender"]

        print "Country: ", i["Country"]

        print "Acceptable Countries: ", ", ".join(i["Acceptable_country"])

        print "Age: ", i["Age"]

        print "Acceptable Age Range: ", i["Acceptable_age_range"]

        print "Likes: ", ", ".join(i["Likes"])

        print "Dislikes: ", ", ".join(i["Dislikes"])

        print "Books: \n", "\n".join(i["Books"])

        print "\n"
        print "----------------------------------------------------------------------------------------------------------------------------"
