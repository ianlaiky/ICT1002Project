import wx
import os
from function2 import main as Func2
from function4_testing import main as Func4
from mainTest import mainTest

class AppFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="Application Name", size=(500, 500))
        panel = wx.Panel(self)

        self.folderPrompt = wx.TextEntryDialog(None, message="Enter folder path:", caption="Application Name",
                                               value="./profiles/")

        if self.folderPrompt.ShowModal() == wx.ID_OK:
            self.checkFileExists(self)      #Replace this w a check if file can open function

        Func1 = wx.Button(panel, label="Func1", pos=(50, 10), size=(150, 40))
        Func2 = wx.Button(panel, label="Matched Students", pos=(250, 10), size=(150, 40))
        Func3 = wx.Button(panel, label="Top 3 Best Matched (Likes/Dislikes)", pos=(50, 100), size=(150, 40))
        Func4 = wx.Button(panel, label="Top 3 Best Matched (Books)", pos=(250, 100), size=(150, 40))

        ExitButton = wx.Button(panel, label="Exit", pos=(250, 400), size=(80, 30))

        self.Bind(wx.EVT_BUTTON, self.onEnter, Func1)
        self.Bind(wx.EVT_BUTTON, self.Func2, Func2)
        self.Bind(wx.EVT_BUTTON, self.Func4, Func4)
        #Insert Func3, 5-7 Bind events here when ready
        self.Bind(wx.EVT_BUTTON, self.exitButton, ExitButton)
        self.Bind(wx.EVT_CLOSE, self.exitWindow)

    def exitButton(self, event):
        self.Close(True)

    def exitWindow(self, event):
        self.Destroy()

    def checkFileExists(self, event):
        global folder_path
        folder_path = self.folderPrompt.GetValue()  # Gets string input by user and assign it to folder_path
        if os.path.isdir(folder_path):
            self.onEnter(self)                      #This currently will still continue if fail, but Func1 will not work

    def onEnter(self, event):
        mainTest(folder_path)

    def Func2(self, event):
        Func2()

    def Func4(self,event):
        Func4()

if __name__ == "__main__":
    app = wx.App(False)         # <--- Set to False to output to console, True to output to popup window
    frame = AppFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
