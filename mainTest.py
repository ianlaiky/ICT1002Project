from main import run as main


def mainTest():
    list_of_dictionary_profiles_data = main("./profiles/")  #Replace parameter with GUI's folder_path

    for i in list_of_dictionary_profiles_data:
        print "Unique Id: ", i["id"]

        print "Name: ", i["Name"]

        print "Gender: ", i["Gender"]

        print "Country: ", i["Country"]

        print "Acceptable_country: ", i["Acceptable_country"]

        print "Age: ", i["Age"]

        print "Acceptable_age_range: ", i["Acceptable_age_range"]

        print "Likes: ", i["Likes"]

        print "Dislikes: ", i["Dislikes"]

        print "Books:", i["Books"]

        print "\n"
        print "----------------------------------------------------------------------------------------------------------------------------"
