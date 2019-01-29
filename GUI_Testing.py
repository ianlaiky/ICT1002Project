import sys
import wx
import os
from function2 import main as Func2
from function3 import main as Func3
from function4_testing import main as Func4
from mainTest import mainTest


class OtherFrame(wx.Frame):
    """
    Class used for creating other frames other than the main frame
    """
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.Show()


class AppPanel(wx.Panel):
    """
    Class used for creating panels
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.frame_number = 1
        self.parent = parent

    """Not In Use Yet"""
    def on_new_frame(self, event):
        title = 'SubFrame {}'.format(self.frame_number)
        frame = OtherFrame(title=title, parent=self.parent)
        self.frame_number += 1


class MainFrame(wx.Frame):
    """
    Class used for creating the main frame
    """
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="Application Name", size=(500, 500))
        panel = AppPanel(self)

        '''Prompts User for folder Path'''
        while True:
            self.folderPrompt = wx.TextEntryDialog(None, message="Enter folder path:", caption="Application Name",
                                                   value="./profiles/")

            if self.folderPrompt.ShowModal() == wx.ID_OK:
                global folder_path
                folder_path = self.folderPrompt.GetValue()  # Gets string input by user and assign it to folder_path
                if os.path.isdir(folder_path):
                    print("Directory Verified")
                    break
                else:
                    print("Error: Not a Directory")
            else:
                sys.exit()
                break

        '''Creating Buttons'''
        Func1 = wx.Button(panel, label="Print all Details", pos=(100, 10), size=(300, 40))
        Func2 = wx.Button(panel, label="Matched Students", pos=(100, 60), size=(300, 40))
        Func3 = wx.Button(panel, label="Top 3 Best Matched (Likes/Dislikes)", pos=(100, 110), size=(300, 40))
        Func4 = wx.Button(panel, label="Top 3 Best Matched (Books)", pos=(100, 160), size=(300, 40))

        ExitButton = wx.Button(panel, label="Exit", pos=(250, 400), size=(80, 30))

        '''Binding buttons to actions'''
        self.Bind(wx.EVT_BUTTON, self.onEnter, Func1)
        self.Bind(wx.EVT_BUTTON, self.Func2, Func2)
        self.Bind(wx.EVT_BUTTON, self.Func3, Func3)
        self.Bind(wx.EVT_BUTTON, self.Func4, Func4)
        #Insert Func5-7 Bind events here when ready
        self.Bind(wx.EVT_BUTTON, self.exitButton, ExitButton)
        self.Bind(wx.EVT_CLOSE, self.exitWindow)

    def exitButton(self, event):
        self.Close(True)
        sys.exit()

    def exitWindow(self, event):
        self.Destroy()
        sys.exit()

    def checkFileExists(self, event):
        global folder_path
        folder_path = self.folderPrompt.GetValue()  # Gets string input by user and assign it to folder_path
        if os.path.isdir(folder_path):
            print("Directory Verified")

        else:
            print("Error: Not a Directory")

    def onEnter(self, event):
        mainTest(folder_path)

    def Func2(self, event):
        Func2(folder_path)

    def Func3(self,event):
        Func3(folder_path)

    def Func4(self,event):
        Func4(folder_path)

if __name__ == "__main__":
    app = wx.App(True)         # <--- Set to False to output to console, True to output to popup window
    frame = MainFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
