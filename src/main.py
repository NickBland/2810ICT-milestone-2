import wx

from gui import MyFrame3 as MyFrame

from error import ErrorDialog

from database import initDatabase, searchDatabase

# Global variables
global DATABASE  # Global database object - Pandas.DataFrame object


class MyFrame(MyFrame):
    def __init__(self):
        super().__init__(None)

        # Initialize the database object
        DATABASE, error = initDatabase(r"./src/Food_Nutrition_Dataset.csv")

        # Workaround to show the hint text in the input boxes, as this is not an option in the WXFormBuilder app
        self.search_keyword_input.SetHint("Enter keywords")

        self.Show()

        # If there is an error, show the dialog
        if error:
            ErrorDialog(self, str(error), True)
            #                             ^^^^ This is an non-recoverable error

    def exitApp(self, event):
        """
        Exit the application
        """
        self.Close()


# Run the WX application
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
