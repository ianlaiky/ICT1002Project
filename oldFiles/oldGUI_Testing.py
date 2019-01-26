import wx
from os import walk
from main import *
from mainTest import *


class AppFrame(wx.Frame):
    """
    Setting up Window & its parameters
    """
    def __init__(self):
        wx.Frame.__init__(self, None,
                          title="Application Name",
                          pos=wx.DefaultPosition,
                          size=wx.Size(700, 500),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        panel = wx.Panel(self)
        lbl = wx.StaticText(panel,
                            label="Hello there! Please enter the folder path: ")

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_sizer.Add(lbl, 0, wx.ALL, 5)

        """
        Setting up Exit Button and Exit Window
        """
        exit_button = wx.Button(panel, label="Exit", pos=(300, 400), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.exitButton, exit_button)
        self.Bind(wx.EVT_CLOSE, self.exitWindow)

        """
        Setting up TextBox
        """
        self.txt = wx.TextCtrl(panel,
                               value="./profiles/",
                               style=wx.TE_PROCESS_ENTER,
                               size=(600, 30))
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def exitButton(self, event):
        self.Close(True)

    def exitWindow(self, event):
        self.Destroy()

    def onEnter(self, event):
        folder_path = self.txt.GetValue()   # Gets string input by user and assign it to folder_path
        folder_path.lower()                 # change folder_path to lowercase to avoid collisions
        run(folder_path)
        mainTest()
        #list_of_dictionary_profiles_data = run("./profiles/")
        #print(list_of_dictionary_profiles_data)
    # main.py code goes somewhere here


if __name__ == "__main__":
    app = wx.App(True)
    frame = AppFrame()
    app.MainLoop()
