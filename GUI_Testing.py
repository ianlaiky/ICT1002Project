import sys
import wx
import os
from function2 import main as Func2
from function3 import main as Func3
from function4_testing import main as Func4
from function5 import main as Func5
from mainTest import mainTest


class OutputWindow(wx.TextCtrl):
    """
    Class used for creating the output window
    """
    def __init__(self):
        frame2 = wx.Frame(None,-1, "Application Name - Output", size=(500,500))
        frame2.Show()
        self.parent = frame2
        wx.TextCtrl.__init__(self,self.parent,size=(485,460), style=wx.TE_MULTILINE|wx.TE_READONLY| wx.HSCROLL)
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
        Func2 = wx.Button(panel, label="Matched Students", pos=(100, 60), size=(300, 40))
        Func3 = wx.Button(panel, label="Top 3 Best Matched (Likes/Dislikes)", pos=(100, 110), size=(300, 40))
        Func4 = wx.Button(panel, label="Top 3 Best Matched (Books)", pos=(100, 160), size=(300, 40))
        Func5 = wx.Button(panel, label="Top 3 Best Matched (Overall)", pos=(100, 210), size=(300, 40))
        Func6 = wx.Button(panel, label="Output Top 3 Matches to CSV", pos=(100, 260), size=(300, 40))

        ExitButton = wx.Button(panel, label="Exit", pos=(210, 400), size=(80, 30))

        '''Binding buttons to actions'''
        self.Bind(wx.EVT_BUTTON, self.Func1, Func1)
        self.Bind(wx.EVT_BUTTON, self.Func2, Func2)
        self.Bind(wx.EVT_BUTTON, self.Func3, Func3)
        self.Bind(wx.EVT_BUTTON, self.Func4, Func4)
        self.Bind(wx.EVT_BUTTON, self.Func5, Func5)
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

    def Func1(self, event):
        OutputWindow()
        mainTest(folder_path)

    def Func2(self, event):
        OutputWindow()
        Func2()

    def Func3(self, event):
        OutputWindow()
        Func3()

    def Func4(self, event):
        OutputWindow()
        Func4()                 #Error occurrs cos of 1st error test case

    def Func5(self, event):
        OutputWindow()
        Func5()

    #def Func6(self,event):
        #OutputWindow()
        #Func6()

if __name__ == "__main__":
    app = wx.App(False)         # <--- Set to False to output to console, True to output to popup window
    frame = MainFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
    sys.stdout = sys.__stdout__
