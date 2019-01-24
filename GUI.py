#THIS IS NOT FINAL, I JUST PUSH UP AS REFERENCE

import wx
from os import walk

class MyFrame(wx.Frame):
    #Setting up Window
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(450,100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="Application Name")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
                            label="Hello there! Please enter the folder path: ")
        my_sizer.Add(lbl,0,wx.ALL,5)
        self.txt = wx.TextCtrl(panel,
                               style=wx.TE_PROCESS_ENTER,
                               size=(400,30))
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.onEnter)
        my_sizer.Add(self.txt,0,wx.ALL,5)
        panel.SetSizer(my_sizer)
        self.Show()

    #Main Program Code
    def onEnter(self,event):
        folder_path = self.txt.GetValue()       #Gets string input by user and assign it to folder_path
        folder_path.lower()                     #change folder_path to lowercase to avoid collisions

        #Main program code goes somewhere here

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
