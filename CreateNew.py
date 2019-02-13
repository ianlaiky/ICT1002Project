"""
Python File: CreateNew.py
Author: Toh Wei Hao Nicholas
"""

import wx
import re
import time


class RegFrame(wx.Frame):

    def __init__(self, parent, path):
        wx.Frame.__init__(self, parent, title="DaBao", pos=wx.DefaultPosition, size=wx.Size(500, 500),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.parent = parent
        global folder_path
        folder_path = path
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        Sizer = wx.FlexGridSizer(0, 2, 0, 0)
        Sizer.SetFlexibleDirection(wx.BOTH)
        Sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        ''' Setting up New Profile Form '''
        self.NameLabel = wx.StaticText(self, wx.ID_ANY, label="Name:", pos=wx.DefaultPosition, size=wx.DefaultSize)
        self.NameLabel.Wrap(-1)
        Sizer.Add(self.NameLabel, 0, wx.ALL, 5)

        self.NameField = wx.TextCtrl(self, wx.ID_ANY, value="", pos=wx.DefaultPosition, size=wx.Size(300, -1))
        Sizer.Add(self.NameField, 0, wx.ALL, 5)

        self.GenderLabel = wx.StaticText(self, wx.ID_ANY, label="Gender:", pos=wx.DefaultPosition, size=wx.DefaultSize)
        self.GenderLabel.Wrap(-1)
        Sizer.Add(self.GenderLabel, 0, wx.ALL, 5)

        GenderFieldChoices = ["Male", "Female"]
        self.GenderField = wx.RadioBox(self, wx.ID_ANY, label="Gender", pos=wx.Point(150, -1), size=wx.Size(200, -1),
                                       choices=GenderFieldChoices, majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.GenderField.SetSelection(0)
        Sizer.Add(self.GenderField, 0, wx.ALL, 5)

        self.CountryLabel = wx.StaticText(self, wx.ID_ANY, label="Your Country:", pos=wx.DefaultPosition,
                                          size=wx.DefaultSize)
        self.CountryLabel.Wrap(-1)
        Sizer.Add(self.CountryLabel, 0, wx.ALL, 5)

        global CountryFieldChoices
        CountryFieldChoices = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla",
                               "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria",
                               "Azerbaijan", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
                               "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
                               "British Virgin Islands", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia",
                               "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad",
                               "Chile", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo",
                               "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus",
                               "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
                               "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia",
                               "Falkland Islands", "Faroe Islands", "Fiji", "Finland", "France", "French Polynesia",
                               "Gabon", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada",
                               "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea - Bissau", "Guyana",
                               "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran",
                               "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey",
                               "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos",
                               "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
                               "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives",
                               "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte",
                               "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat",
                               "Morocco", "Mozambique", "Myanmar", "Nagorno-Karabakh", "Namibia", "Nauru", "Nepal",
                               "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua",
                               "Niger", "Nigeria", "Niue", "Norfolk Island", "North Korea", "Northern Mariana",
                               "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea",
                               "Paraguay", "People's Republic of China", "Peru", "Philippines", "Pitcairn Islands",
                               "Poland", "Portugal", "Puerto Rico", "Qatar", "Republic of China", "Romania", "Russia",
                               "Rwanda", "Saint Barthelemy", "Saint Helena", "Saint Kitts and Nevis", "Saint Lucia",
                               "Saint Martin", "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "Samoa",
                               "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
                               "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
                               "Somaliland", "South Africa", "South Korea", "South Ossetia", "Spain", "Sri Lanka",
                               "Sudan", "Suriname", "Svalbard", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan",
                               "Tajikistan", "Tanzania", "Thailand", "The Bahamas", "The Gambia", "Timor-Leste", "Togo",
                               "Tokelau", "Tonga", "Transnistria Pridnestrovie", "Trinidad and Tobago",
                               "Tristan da Cunha", "Tunisia", "Turkey", "Turkish Republic of Northern Cyprus",
                               "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine",
                               "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay",
                               "US Virgin Islands", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
                               "Wallis and Futuna", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"]

        self.CountryField = wx.ComboBox(self, wx.ID_ANY, value="Select Country", pos=wx.DefaultPosition,
                                        size=wx.Size(300, -1), choices=CountryFieldChoices, style=wx.CB_DROPDOWN)
        Sizer.Add(self.CountryField, 0, wx.ALL, 5)

        self.AcceptableCountryLabel = wx.StaticText(self, wx.ID_ANY, label="Acceptable Countries:",
                                                    pos=wx.DefaultPosition, size=wx.DefaultSize)
        self.AcceptableCountryLabel.Wrap(-1)
        Sizer.Add(self.AcceptableCountryLabel, 0, wx.ALL, 5)

        self.AcceptableCountryField = wx.ListBox(self, wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(300, 100),
                                                 choices=CountryFieldChoices, style=wx.LB_ALWAYS_SB | wx.LB_HSCROLL |
                                                 wx.LB_MULTIPLE | wx.LB_SORT)
        self.AcceptableCountryField.SetToolTip("What country's men/women are you looking for?")
        Sizer.Add(self.AcceptableCountryField, 0, wx.ALL, 5)

        self.AgeLabel = wx.StaticText(self, wx.ID_ANY, label="Age:", pos=wx.DefaultPosition, size=wx.DefaultSize)
        self.AgeLabel.Wrap(-1)
        Sizer.Add(self.AgeLabel, 0, wx.ALL, 5)

        self.AgeField = wx.TextCtrl(self, wx.ID_ANY, value="18", pos=wx.DefaultPosition, size=wx.Size(30, -1))
        self.AgeField.SetMaxLength(2)
        self.AgeField.SetToolTip("Enter your age!")
        Sizer.Add(self.AgeField, 0, wx.ALL, 5)

        self.AcceptableAgeRangeLabel = wx.StaticText(self, wx.ID_ANY, label="Acceptable Age Range:",
                                                     pos=wx.DefaultPosition, size=wx.DefaultSize)
        self.AcceptableAgeRangeLabel.Wrap(-1)
        Sizer.Add(self.AcceptableAgeRangeLabel, 0, wx.ALL, 5)

        self.AcceptableAgeRangeField = wx.TextCtrl(self, wx.ID_ANY, value="18-26", pos=wx.DefaultPosition,
                                                   size=wx.DefaultSize)
        self.AcceptableAgeRangeField.SetMaxLength(5)
        self.AcceptableAgeRangeField.SetToolTip("What's the age range that you are looking for?")
        Sizer.Add(self.AcceptableAgeRangeField, 0, wx.ALL, 5)

        self.LikesLabel = wx.StaticText(self, wx.ID_ANY, label="Likes:", pos=wx.DefaultPosition, size=wx.DefaultSize)
        self.LikesLabel.Wrap(-1)
        Sizer.Add(self.LikesLabel, 0, wx.ALL, 5)

        self.LikesField = wx.TextCtrl(self, wx.ID_ANY, value="", pos=wx.DefaultPosition, size=wx.Size(300, -1),
                                      style=wx.TE_BESTWRAP)
        self.LikesField.SetToolTip("Let others know what do you like! Separate likes by a comma")
        Sizer.Add(self.LikesField, 0, wx.ALL, 5)

        self.DislikesLabel = wx.StaticText(self, wx.ID_ANY, label="Dislikes", pos=wx.DefaultPosition,
                                           size=wx.DefaultSize)
        Sizer.Add(self.DislikesLabel, 0, wx.ALL, 5)

        self.DislikesField = wx.TextCtrl(self, wx.ID_ANY, value="", pos=wx.DefaultPosition, size=wx.Size(300, -1),
                                         style=wx.TE_BESTWRAP)
        self.DislikesField.SetToolTip("Let others know what do you hate! Separate dislikes by a comma")
        Sizer.Add(self.DislikesField, 0, wx.ALL, 5)

        self.BooksLabel = wx.StaticText(self, wx.ID_ANY, label="Books:", pos=wx.DefaultPosition, size=wx.DefaultSize)
        self.BooksLabel.Wrap(-1)
        Sizer.Add(self.BooksLabel, 0, wx.ALL, 5)

        self.BooksField = wx.TextCtrl(self, wx.ID_ANY, value="", pos=wx.DefaultPosition, size=wx.Size(300, -1),
                                      style=wx.TE_BESTWRAP | wx.TE_MULTILINE)
        self.BooksField.SetToolTip("What's your favourite books? Separate books by a blank line")
        Sizer.Add(self.BooksField, 0, wx.ALL, 5)

        SaveButton = wx.Button(self, wx.ID_ANY, label="SAVE", pos=(200, 420), size=wx.DefaultSize)
        SaveButton.SetBitmapPosition(wx.BOTTOM)

        self.SetSizer(Sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        ''' Bind Button to Action '''
        self.Bind(wx.EVT_BUTTON, self.SaveData, SaveButton)

    ''' Capture user input'''
    def SaveData(self, event):
        global name, gender, country, acceptable_country, acceptable_age_range, age, likes, dislikes, books

        name = str(self.NameField.GetValue())
        while True:
            if name == "":
                dlg = wx.MessageBox("Error: Please enter your name!", "Error", wx.OK | wx.ICON_ERROR)
                if dlg == wx.OK:
                    return
            else:
                break

        gender = self.GenderField.GetSelection()
        if gender == 0:
            gender = "M"
        else:
            gender = "F"

        country = str(self.CountryField.GetValue())
        while True:
            if country == "Select Country":
                dlg = wx.MessageBox("Error: Please select your country", "Error", wx.OK | wx.ICON_ERROR)
                if dlg == wx.OK:
                    return
            else:
                break

        acceptable_country_index = self.AcceptableCountryField.GetSelections()
        acceptable_country = []
        for i in acceptable_country_index:
            x = CountryFieldChoices[i]
            acceptable_country.append(x)

        acceptable_country = ", ".join(acceptable_country)

        age = self.AgeField.GetValue()
        while True:
            if re.match("\d\d", age):
                int(age)
                break
            else:
                dlg = wx.MessageBox("Error: Invalid Age!", "Error", wx.OK | wx.ICON_ERROR)
                if dlg == wx.OK:
                    return

        acceptable_age_range = self.AcceptableAgeRangeField.GetValue()
        while True:
            if re.match("\d\d-\d\d", acceptable_age_range):
                break
            else:
                dlg = wx.MessageBox("Error: Invalid Age Range!", "Error", wx.OK | wx.ICON_ERROR)
                if dlg == wx.OK:
                    return

        likes = self.LikesField.GetValue()
        dislikes = self.DislikesField.GetValue()
        books = self.BooksField.GetValue()

        self.write_to_file()

    ''' Save to file '''
    def write_to_file(self):
        try:
            timestr = time.strftime("%Y%m%d-%H%M%S")                          # Generates the current datetime
            filename = folder_path + "NewProfile" + timestr + ".txt"          # Combines to form a unique filename

            f = open(filename, "w+")
            f.write("Name: " + name)
            f.write("\nGender: " + gender)
            f.write("\nCountry: " + country)
            f.write("\nAcceptable_country: " + acceptable_country)
            f.write("\nAge: " + age)
            f.write("\nAcceptable_age_range: " + acceptable_age_range)
            f.write("\nLikes: " + likes)
            f.write("\nDislikes: " + dislikes)
            f.write("\nBooks: \n" + books)
            f.close()

            dlg = wx.MessageBox("Profile successfully created!", "Info", wx.OK | wx.ICON_INFORMATION)
            if dlg == wx.OK:
                self.Destroy()

        except (Exception):
            dlg = wx.MessageBox("Error: An Unexpected Error occurred. \n"
                                "Please try again later.", "Error", wx.OK | wx.ICON_ERROR)
            if dlg == wx.OK:
                return


def main(folder_path):
    app = wx.App(False)
    frame = RegFrame(None, folder_path)
    frame.Show()
    app.MainLoop()


#main("./profiles/")
