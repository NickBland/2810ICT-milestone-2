import wx

from gui import MyFrame3 as MyFrame


class MyFrame(MyFrame):
    def __init__(self):
        super().__init__(None)

        # Workaround to show the hint text in the input boxes, as this is not in the WXFormBuilder app
        self.search_keyword_input.SetHint("Enter keywords")

        self.Show()


# Run the WX application
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
