import wx

from gui import MyFrame3 as MyFrame

from error import ErrorDialog

from database import initDatabase, searchDatabase

# Global variables
DATABASE = None  # Global database object - Pandas.DataFrame object


class MyFrame(MyFrame):
    def __init__(self):
        super().__init__(None)

        # Initialize the database object
        global DATABASE  # Required to edit the global variable
        DATABASE, error = initDatabase(r"./Food_Nutrition_Dataset.csv")

        # Workaround to show the hint text in the input boxes, as this is not an option in the WXFormBuilder app
        self.search_keyword_input.SetHint("Enter keywords")

        self.Show()

        # If there is an error, show the dialog
        if error:
            ErrorDialog(self, str(error), True)
            #                             ^^^^ This is indicates the error is non-recoverable, so the app needs to be closed

    def search(self, event):
        # Get the search keyword
        search_keyword = self.search_keyword_input.GetValue()

        search_filters = {
            "keyword": search_keyword,
            "nutrient": self.search_filter_nutrient_selection.GetSelection(),
            "min": self.search_filter_range_min.GetValue(),
            "max": self.search_filter_range_max.GetValue(),
            "level": self.search_filter_level_selection.GetSelection(),
            "high-protein": self.search_filter_highProtein.GetValue(),
            "low-sugar": self.search_filter_lowSugar.GetValue(),
        }

        searchDatabase(search_filters, DATABASE)

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
