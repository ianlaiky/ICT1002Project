import wx
from function4_testing import *
from mainTest import mainTest

class AppFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="Application Name", size=(500, 500))
        panel = wx.Panel(self)

        self.folderPrompt = wx.TextEntryDialog(None, message="Enter folder path:", caption="Application Name",
                                               value="./profiles/")

        if self.folderPrompt.ShowModal() == wx.ID_OK:
            self.onEnter(self)              #Replace this w a check if file can open function

        Func1 = wx.Button(panel, label="Func1", pos=(100, 10), size=(80, 40))
        Func2 = wx.Button(panel, label="Top 3 Best Matched", pos=(200, 10), size=(200, 40))
        ExitButton = wx.Button(panel, label="Exit", pos=(250, 400), size=(80, 30))

        self.Bind(wx.EVT_BUTTON, self.onEnter, Func1)
        self.Bind(wx.EVT_BUTTON, self.Func4, Func2)
        self.Bind(wx.EVT_BUTTON, self.exitButton, ExitButton)
        self.Bind(wx.EVT_CLOSE, self.exitWindow)

    def exitButton(self, event):
        self.Close(True)

    def exitWindow(self, event):
        self.Destroy()

    #def menu(self):


    def onEnter(self,event):
        folder_path = self.folderPrompt.GetValue()   # Gets string input by user and assign it to folder_path
        folder_path.lower()                 # change folder_path to lowercase to avoid collisions
        mainTest(folder_path)

    def Func4(self,event):
        main()

if __name__ == "__main__":
    app = wx.App(False)         # <--- Set to False to output to console, True to output to popup window
    frame = AppFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
