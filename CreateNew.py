# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title=u"Application Name", pos=wx.DefaultPosition, size=wx.Size(500, 500),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        Sizer = wx.FlexGridSizer(0, 2, 0, 0)
        Sizer.SetFlexibleDirection(wx.BOTH)
        Sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.NameLabel = wx.StaticText(self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0, u"Name:")
        self.NameLabel.Wrap(-1)

        Sizer.Add(self.NameLabel, 0, wx.ALL, 5)

        self.NameField = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        Sizer.Add(self.NameField, 0, wx.ALL, 5)

        self.GenderLabel = wx.StaticText(self, wx.ID_ANY, u"Gender:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.GenderLabel.Wrap(-1)

        Sizer.Add(self.GenderLabel, 0, wx.ALL, 5)

        GenderFieldChoices = [u"Male", u"Female"]
        self.GenderField = wx.RadioBox(self, wx.ID_ANY, u"wxRadioBox", wx.Point(150, -1), wx.Size(150, -1),
                                       GenderFieldChoices, 1, wx.RA_SPECIFY_ROWS)
        self.GenderField.SetSelection(0)
        Sizer.Add(self.GenderField, 0, wx.ALL, 5)

        self.CountryLabel = wx.StaticText(self, wx.ID_ANY, u"Your Country:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.CountryLabel.Wrap(-1)

        Sizer.Add(self.CountryLabel, 0, wx.ALL, 5)

        CountryFieldChoices = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla",
                               "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria",
                               "Azerbaijan",
                               "The Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
                               "Benin",
                               "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
                               "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde",
                               "Cayman Islands", "Central African Republic", "Chad", "Chile",
                               "People 's Republic of China",
                               "Republic of China", "Christmas Island", "Cocos(Keeling) Islands", "Colombia", "Comoros",
                               "Congo", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus",
                               "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
                               "Egypt",
                               "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands",
                               "Faroe Islands", "Fiji", "Finland", "France", "French Polynesia", "Gabon", "The Gambia",
                               "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada",
                               "Guadeloupe",
                               "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea - Bissau", "Guyana", "Haiti",
                               "Honduras",
                               "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
                               "Israel",
                               "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
                               "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
                               "Lebanon",
                               "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau",
                               "Macedonia",
                               "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
                               "Martinique",
                               "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco",
                               "Mongolia",
                               "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Nagorno - Karabakh",
                               "Namibia",
                               "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand",
                               "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island",
                               "Turkish Republic of Northern Cyprus",
                               "Northern Mariana", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama",
                               "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn Islands", "Poland",
                               "Portugal",
                               "Puerto Rico", "Qatar", "Romania", "Russia", "Rwanda", "Saint Barthelemy",
                               "Saint Helena",
                               "Saint Kitts and Nevis", "Saint Lucia", "Saint Martin", "Saint Pierre and Miquelon",
                               "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
                               "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
                               "Slovakia",
                               "Slovenia", "Solomon Islands", "Somalia", "Somaliland", "South Africa", "South Ossetia",
                               "Spain", "Sri Lanka", "Sudan", "Suriname", "Svalbard", "Swaziland", "Sweden",
                               "Switzerland",
                               "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor - Leste", "Togo",
                               "Tokelau",
                               "Tonga", "Transnistria Pridnestrovie", "Trinidad and Tobago", "Tristan da Cunha",
                               "Tunisia",
                               "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine",
                               "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan",
                               "Vanuatu",
                               "Vatican City", "Venezuela", "Vietnam", "British Virgin Islands", "Isle of Man",
                               "US Virgin Islands", "Wallis and Futuna", "Western Sahara", "Yemen", "Zambia",
                               "Zimbabwe"]

        self.CountryField = wx.ComboBox(self, wx.ID_ANY, u"Select Country", wx.DefaultPosition, wx.Size(200, -1),
                                        CountryFieldChoices, wx.CB_DROPDOWN)
        Sizer.Add(self.CountryField, 0, wx.ALL, 5)

        self.AcceptableCountryLabel = wx.StaticText(self, wx.ID_ANY, u"Acceptable Countries:", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.AcceptableCountryLabel.Wrap(-1)

        Sizer.Add(self.AcceptableCountryLabel, 0, wx.ALL, 5)

        self.AcceptableCountryField = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, 100),
                                                 CountryFieldChoices,
                                                 wx.LB_ALWAYS_SB | wx.LB_HSCROLL | wx.LB_MULTIPLE | wx.LB_SORT)
        Sizer.Add(self.AcceptableCountryField, 0, wx.ALL, 5)

        self.AgeLabel = wx.StaticText(self, wx.ID_ANY, u"Age:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.AgeLabel.Wrap(-1)

        Sizer.Add(self.AgeLabel, 0, wx.ALL, 5)

        self.AgeField = wx.TextCtrl(self, wx.ID_ANY, u"00", wx.DefaultPosition, wx.Size(30, -1), 0)
        self.AgeField.SetMaxLength(2)
        Sizer.Add(self.AgeField, 0, wx.ALL, 5)

        self.AcceptabelAgeRangeLabel = wx.StaticText(self, wx.ID_ANY, u"Acceptable Age Range:", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.AcceptabelAgeRangeLabel.Wrap(-1)

        Sizer.Add(self.AcceptabelAgeRangeLabel, 0, wx.ALL, 5)

        self.AcceptableAgeRangeField = wx.TextCtrl(self, wx.ID_ANY, u"18-99", wx.DefaultPosition, wx.DefaultSize, 0)
        self.AcceptableAgeRangeField.SetMaxLength(5)
        Sizer.Add(self.AcceptableAgeRangeField, 0, wx.ALL, 5)

        self.LikesLabel = wx.StaticText(self, wx.ID_ANY, u"Likes:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LikesLabel.Wrap(-1)

        Sizer.Add(self.LikesLabel, 0, wx.ALL, 5)

        self.LikesField = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1),
                                      wx.TE_BESTWRAP)
        Sizer.Add(self.LikesField, 0, wx.ALL, 5)

        self.DislikesLabel = wx.StaticText(self, wx.ID_ANY, u"Dislikes", wx.DefaultPosition, wx.DefaultSize, 0)
        self.DislikesLabel.Wrap(-1)

        Sizer.Add(self.DislikesLabel, 0, wx.ALL, 5)

        self.DislikesField = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1),
                                         wx.TE_BESTWRAP)
        Sizer.Add(self.DislikesField, 0, wx.ALL, 5)

        self.BooksLabel = wx.StaticText(self, wx.ID_ANY, u"Books:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.BooksLabel.Wrap(-1)

        Sizer.Add(self.BooksLabel, 0, wx.ALL, 5)

        self.BooksField = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1),
                                      wx.TE_BESTWRAP)
        Sizer.Add(self.BooksField, 0, wx.ALL, 5)

        Sizer.Add((0, 0), 1, wx.EXPAND, 5)

        self.SaveButton = wx.Button(self, wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0)

        self.SaveButton.SetBitmapPosition(wx.BOTTOM)
        Sizer.Add(self.SaveButton, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER, 5)

        self.SetSizer(Sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.SaveButton.Bind(wx.EVT_BUTTON, self.SaveData)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def SaveData(self, event):
        name = self.NameField.GetValue()
        gender = self.GenderField.GetSelection()
        country = self.CountryField.GetValue()
        acceptable_country = self.AcceptableCountryField.GetSelections()
        age = self.AgeField.GetValue()
        acceptable_age_range = self.AcceptableAgeRangeField.GetValue()
        likes = self.LikesField.GetValue()
        dislikes = self.DislikesField.GetValue()
        books = self.BooksField.GetValue()
        print(name)
        print(gender)
        print(country)
        print(acceptable_country)
        print(age)
        print(acceptable_age_range)
        print(likes)
        print(dislikes)
        print(books)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(parent=None)
    frame.Show()
    app.MainLoop()
    # sys.stdout = sys.__stdout__
