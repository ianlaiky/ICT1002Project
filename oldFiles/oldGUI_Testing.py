import wx


class OtherFrame(wx.Frame):
    """
    Class used for creating frames other than the main one
    """

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.Show()


class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        btn = wx.Button(self, label='Create New Frame')
        Func1 = wx.Button(self, label="Print all Details", pos=(100, 10), size=(300, 40))
        Func2 = wx.Button(self, label="Matched Students", pos=(100, 60), size=(300, 40))
        Func3 = wx.Button(self, label="[WIP] Top 3 Best Matched (Likes/Dislikes)", pos=(100, 110), size=(300, 40))
        Func4 = wx.Button(self, label="Top 3 Best Matched (Books)", pos=(100, 160), size=(300, 40))

        btn.Bind(wx.EVT_BUTTON, self.on_new_frame)
        self.Bind(wx.EVT_BUTTON,self.)
        self.frame_number = 1
        self.parent = parent

    def on_new_frame(self, event):
        title = 'SubFrame {}'.format(self.frame_number)
        frame = OtherFrame(title=title,parent=self.parent)
        self.frame_number += 1


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Main Frame', size=(800, 600))
        panel = MyPanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()