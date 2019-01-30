import wx

class MyFrame(wx.Frame):
    #Setting up Window & its parameters
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(700, 500),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="Application Name")

        panel = wx.Panel(self)
        lbl = wx.StaticText(panel,
                            label="Hello there! Please enter the folder path: ")

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_sizer.Add(lbl, 0, wx.ALL, 5)

        #Setting up Exit Button and Exit Window
        ExitButton = wx.Button(panel, label="Exit", pos=(300, 400), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.exitButton, ExitButton)
        self.Bind(wx.EVT_CLOSE, self.exitWindow)

        #Setting up TextBox
        self.txt = wx.TextCtrl(panel,
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
        folder_path = self.txt.GetValue()       #Gets string input by user and assign it to folder_path
        folder_path.lower()                     #change folder_path to lowercase to avoid collisions

    #function1.py code goes somewhere here

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
