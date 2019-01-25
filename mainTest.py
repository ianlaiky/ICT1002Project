from main import run as main

list_of_dictionary_profiles_data = main("./profiles/")

for i in list_of_dictionary_profiles_data:
    print "Unique Id"
    print i["id"]

    print "Name "
    print i["Name"]

    print "Gender "
    print i["Gender"]

    print "Country "
    print i["Country"]

    print "Acceptable_country "
    print i["Acceptable_country"]

    print "Age "
    print i["Age"]

    print "Acceptable_age_range "
    print i["Acceptable_age_range"]

    print "Likes "
    print i["Likes"]

    print "Dislikes "
    print i["Dislikes"]

    print "Books"
    print i["Books"]

    print "\n"
    print "----------------------------------------------------------------------------------------------------------------------------"
