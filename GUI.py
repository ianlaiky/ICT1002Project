"""
Python File: GUI.py
Author: Toh Wei Hao Nicholas
"""

import sys
import wx
import os
from function1 import main as List_All_Details
from function1 import run as Check
from function2 import main as Country_Matches
from function3 import main as Likes_Matches
from function4 import main as Books_Matches
from function5 import main as Overall_Matches
from function6Main import run as OutputCSV
from CreateNew import main as Create_New_Profile


class OutputWindow(wx.TextCtrl):
    """
    Class used for creating the output window
    """
    def __init__(self):
        frame2 = wx.Frame(None, -1, "Dabao - Output", size=(500, 500))
        frame2.Show()
        self.parent = frame2
        wx.TextCtrl.__init__(self, self.parent, size=(485, 460), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        sys.stdout = self


class AppPanel(wx.Panel):
    """
    Class used for creating panels
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent


class MainWindow(wx.Frame):
    """
    Class used for creating the main frame
    """
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="DaBao", size=(500, 500))
        panel = AppPanel(self)

        self.folder_prompt()

        wx.StaticText(panel, wx.ID_ANY,
                      label="Welcome! If you have not created a profile before, please create a new profile first",
                      pos=(30, 10), size=wx.DefaultSize)

        ''' Creating Buttons '''
        Func7 = wx.Button(panel, label="Create New Profile", pos=(100, 50), size=(300, 40))
        Func1 = wx.Button(panel, label="Print all Details", pos=(100, 100), size=(300, 40))
        Func2 = wx.Button(panel, label="Match based on Country", pos=(100, 150), size=(300, 40))
        Func3 = wx.Button(panel, label="Match based on Likes/Dislikes", pos=(100, 200), size=(300, 40))
        Func4 = wx.Button(panel, label="Match based on Books", pos=(100, 250), size=(300, 40))
        Func5 = wx.Button(panel, label="Match based on Overall Profile", pos=(100, 300), size=(300, 40))
        Func6 = wx.Button(panel, label="Output Top 3 Matches to CSV", pos=(100, 350), size=(300, 40))

        ExitButton = wx.Button(panel, label="Exit", pos=(210, 400), size=(80, 30))

        ''' Binding buttons to actions '''
        self.Bind(wx.EVT_BUTTON, self.List_All_Profiles, Func1)
        self.Bind(wx.EVT_BUTTON, self.Country_Matches, Func2)
        self.Bind(wx.EVT_BUTTON, self.Likes_Matches, Func3)
        self.Bind(wx.EVT_BUTTON, self.Books_Matches, Func4)
        self.Bind(wx.EVT_BUTTON, self.Overall_Matches, Func5)
        self.Bind(wx.EVT_BUTTON, self.OutputCSV, Func6)
        self.Bind(wx.EVT_BUTTON, self.CreateNewProfile, Func7)
        self.Bind(wx.EVT_BUTTON, self.exitButton, ExitButton)
        self.Bind(wx.EVT_CLOSE, self.exitWindow)

    ''' Prompts user to enter folder path '''
    def folder_prompt(self):
        while True:
            folderPrompt = wx.TextEntryDialog(None, message="Enter folder path:", caption="DaBao",
                                              value="./profiles/")

            if folderPrompt.ShowModal() == wx.ID_OK:
                global folder_path
                folder_path = folderPrompt.GetValue()  # Gets string input by user and assign it to folder_path

                '''Checks if its a directory and if profiles can be parsed'''
                if os.path.isdir(folder_path):
                    try:
                        Check(folder_path)
                        wx.MessageBox("Directory Verified", "Info", wx.OK | wx.ICON_INFORMATION)
                        break
                    except IndexError:
                        wx.MessageBox("Error: Error parsing files from folder\n"
                                      "Please check your folder path", "Error", wx.OK | wx.ICON_ERROR)
                    except Exception:
                        wx.MessageBox("Error: An unknown error has occurred,\n"
                                      "Please check your folder path", "Error", wx.OK | wx.ICON_ERROR)
                else:
                    wx.MessageBox("Error: Not a Directory.\nPlease check your folder path", "Error", wx.OK | wx.ICON_ERROR)
            else:
                sys.exit()

    ''' Defines what the Exit Button do '''
    def exitButton(self, event):
        self.Close(True)

    ''' Defines what clicks the X button or Exit button do '''
    def exitWindow(self, event):
        dlg = wx.MessageDialog(self, "Confirm to Exit?", "Exit", wx.YES_NO | wx.ICON_WARNING)
        if dlg.ShowModal() == wx.ID_YES:
            self.Destroy()
            sys.exit()
        dlg.Destroy()

    ''' List all Profiles '''
    def List_All_Profiles(self, event):
        OutputWindow()
        List_All_Details(folder_path)

    ''' Lists all matches based on Acceptable Countries '''
    def Country_Matches(self, event):
        while True:
            name_prompt = wx.TextEntryDialog(None, message="Enter your name:", caption="DaBao", value="")
            if name_prompt.ShowModal() == wx.ID_OK:
                global name
                name = name_prompt.GetValue()
                if len(name) == 0:
                    dlg = wx.MessageBox("Error: Please enter your name!", "Error", wx.OK | wx.ICON_ERROR)
                else:
                    try:
                        OutputWindow()
                        Country_Matches(folder_path, name)
                    except IndexError:
                        dlg = wx.MessageBox("Error: Name not found in System.\nTry creating a profile first", "Error",
                                            wx.OK | wx.ICON_ERROR)
                    except Exception:
                        dlg = wx.MessageBox("Error: An unknown error has occurred.\nPlease try again later", "Error",
                                            wx.OK | wx.ICON_ERROR)
                    break
            else:
                break

    ''' Lists Top 3 matches based on Likes '''
    def Likes_Matches(self, event):
        while True:
            name_prompt = wx.TextEntryDialog(None, message="Enter your name:", caption="DaBao", value="")
            if name_prompt.ShowModal() == wx.ID_OK:
                global name
                name = name_prompt.GetValue()
                if len(name) == 0:
                    dlg = wx.MessageBox("Error: Please enter your name!", "Error", wx.OK | wx.ICON_ERROR)
                else:
                    OutputWindow()
                    Likes_Matches(folder_path, name)
                    break
            else:
                break

    ''' Lists Top 3 matches based on Books '''
    def Books_Matches(self, event):
        while True:
            name_prompt = wx.TextEntryDialog(None, message="Enter your name:", caption="DaBao", value="")
            if name_prompt.ShowModal() == wx.ID_OK:
                global name
                name = name_prompt.GetValue()
                if len(name) == 0:
                    dlg = wx.MessageBox("Error: Please enter your name!", "Error", wx.OK | wx.ICON_ERROR)
                else:
                    OutputWindow()
                    Books_Matches(folder_path, name)
                    break
            else:
                break

    ''' Lists Top 3 matches based on Overall Profile '''
    def Overall_Matches(self, event):
        while True:
            name_prompt = wx.TextEntryDialog(None, message="Enter your name:", caption="DaBao", value="")
            if name_prompt.ShowModal() == wx.ID_OK:
                global name
                name = name_prompt.GetValue()
                if len(name) == 0:
                    dlg = wx.MessageBox("Error: Please enter your name!", "Error", wx.OK | wx.ICON_ERROR)
                else:
                    try:
                        OutputWindow()
                        Overall_Matches(folder_path, name)
                        break
                    except IndexError:
                        dlg = wx.MessageBox("Error: Name not found in System.\nTry creating a profile first", "Error",
                                            wx.OK | wx.ICON_ERROR)
                    except Exception:
                        dlg = wx.MessageBox("Error: An unknown error has occurred.\nPlease try again later", "Error",
                                            wx.OK | wx.ICON_ERROR)
                    break
            else:
                break

    ''' Outputs Top 3 matches of each profile to a CSV file '''
    def OutputCSV(self, event):
        try:
            OutputWindow()
            OutputCSV(folder_path)
        except (Exception):
            dlg = wx.MessageBox("Error: An Unexpected Error occurred. \n"
                                "Please try again later.", "Error", wx.OK | wx.ICON_ERROR)
            if dlg == wx.OK:
                return

    ''' Creates a New Profile '''
    def CreateNewProfile(self, event):
        try:
            Create_New_Profile(folder_path)
        except (Exception):
            dlg = wx.MessageBox("Error: An Unexpected Error occurred. \n"
                                "Please try again later.", "Error", wx.OK | wx.ICON_ERROR)
            if dlg == wx.OK:
                return


if __name__ == "__main__":
    MainApp = wx.App(False)
    MainWindow = MainWindow(parent=None, id=-1)
    MainWindow.Show()
    MainApp.MainLoop()
    sys.stdout = sys.__stdout__
