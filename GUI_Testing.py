import sys
import wx
import os
from function1 import main as List_All_Details
from function2 import main as Country_Matches
from function3 import main as Likes_Matches
from function4 import main as Books_Matches
from function5 import main as Overall_Matches


class OutputWindow(wx.TextCtrl):
    """
    Class used for creating the output window
    """
    def __init__(self):
        frame2 = wx.Frame(None, -1, "Application Name - Output", size=(500, 500))
        frame2.Show()
        self.parent = frame2
        wx.TextCtrl.__init__(self, self.parent, size=(485, 460), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        sys.stdout = self
        print("=== Ready for output! ===\n")


class AppPanel(wx.Panel):
    """
    Class used for creating panels
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent


class MainFrame(wx.Frame):
    """
    Class used for creating the main frame
    """
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="Application Name", size=(500, 500))
        panel = AppPanel(self)

        self.folder_prompt()

        '''Creating Buttons'''
        Func1 = wx.Button(panel, label="Print all Details", pos=(100, 10), size=(300, 40))
        Func2 = wx.Button(panel, label="Match based on Country", pos=(100, 60), size=(300, 40))
        Func3 = wx.Button(panel, label="Match based on Likes/Dislikes", pos=(100, 110), size=(300, 40))
        Func4 = wx.Button(panel, label="Match based on Books", pos=(100, 160), size=(300, 40))
        Func5 = wx.Button(panel, label="Match based on Overall Profile", pos=(100, 210), size=(300, 40))
        Func6 = wx.Button(panel, label="Output Top 3 Matches to CSV", pos=(100, 260), size=(300, 40))

        ExitButton = wx.Button(panel, label="Exit", pos=(210, 400), size=(80, 30))

        '''Binding buttons to actions'''
        self.Bind(wx.EVT_BUTTON, self.List_All_Details, Func1)
        self.Bind(wx.EVT_BUTTON, self.Country_Matches, Func2)
        self.Bind(wx.EVT_BUTTON, self.Likes_Matches, Func3)
        self.Bind(wx.EVT_BUTTON, self.Books_Matches, Func4)
        self.Bind(wx.EVT_BUTTON, self.Overall_Matches, Func5)
        #self.Bind(wx.EVT_BUTTON, self.Func6, Func6)
        #self.Bind(wx.EVT_BUTTON,self.Func7, Func7)
        self.Bind(wx.EVT_BUTTON, self.exitButton, ExitButton)
        self.Bind(wx.EVT_CLOSE, self.exitWindow)

    '''Prompts user to enter folder path'''
    def folder_prompt(self):
        while True:
            self.folderPrompt = wx.TextEntryDialog(None, message="Enter folder path:", caption="Application Name",
                                                   value="./profiles/")
            '''Checks if its a directory'''
            if self.folderPrompt.ShowModal() == wx.ID_OK:
                global folder_path
                folder_path = self.folderPrompt.GetValue()  # Gets string input by user and assign it to folder_path

                if os.path.isdir(folder_path):
                    wx.MessageBox("Directory Verified", "Info", wx.OK | wx.ICON_INFORMATION)
                    break
                else:
                    wx.MessageBox("Error: Not a Directory", "Error", wx.OK | wx.ICON_ERROR)
            else:
                sys.exit()

    '''Defines what the Exit Button do'''
    def exitButton(self, event):
        self.Close(True)

    '''Defines what clicks the X button or Exit button do'''
    def exitWindow(self, event):
        dlg = wx.MessageDialog(self, "Confirm to Exit?", "Exit", wx.YES_NO | wx.ICON_WARNING)
        if dlg.ShowModal() == wx.ID_YES:
            self.Destroy()
            sys.exit()
        dlg.Destroy()

    def List_All_Details(self, event):
        OutputWindow()
        List_All_Details(folder_path)

    def Country_Matches(self, event):
        self.name_prompt = wx.TextEntryDialog(None, message="Enter your name:", caption="Application Name", value="")
        if self.name_prompt.ShowModal() == wx.ID_OK:
            global name
            name = self.name_prompt.GetValue()  # Gets string input by user and assign it to folder_path
            OutputWindow()
            Country_Matches(folder_path, name)

    def Likes_Matches(self, event):
        self.name_prompt = wx.TextEntryDialog(None, message="Enter your name:", caption="Application Name", value="")
        if self.name_prompt.ShowModal() == wx.ID_OK:
            global name
            name = self.name_prompt.GetValue()  # Gets string input by user and assign it to folder_path
            OutputWindow()
            Likes_Matches(folder_path, name)

    def Books_Matches(self, event):
        self.name_prompt = wx.TextEntryDialog(None, message="Enter your name:", caption="Application Name", value="")
        if self.name_prompt.ShowModal() == wx.ID_OK:
            global name
            name = self.name_prompt.GetValue()  # Gets string input by user and assign it to folder_path
            OutputWindow()
            Books_Matches(folder_path, name)

    def Overall_Matches(self, event):
        self.name_prompt = wx.TextEntryDialog(None, message="Enter your name:", caption="Application Name", value="")
        if self.name_prompt.ShowModal() == wx.ID_OK:
            global name
            name = self.name_prompt.GetValue()  # Gets string input by user and assign it to folder_path
            OutputWindow()
            Overall_Matches(folder_path, name)

    #def Func6(self,event):
        #OutputWindow()
        #Func6()

if __name__ == "__main__":
    app = wx.App(False)         # <--- Set to False to output to console, True to output to popup window
    frame = MainFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
    sys.stdout = sys.__stdout__
