import wx

from gui import MyFrame3 as MyFrame
from error import ErrorDialog
from database import initDatabase, searchDatabase, displayResults

# Global variables
DATABASE = None  # Global database object - Pandas.DataFrame object


class MyFrame(MyFrame):
    def __init__(self):
        super().__init__(None)
        # Workaround to show the hint text in the input boxes, as this is not an option in the WXFormBuilder app
        self.search_keyword_input.SetHint("Enter keywords")

        # Initialise the database object
        global DATABASE  # Required to edit the global variable
        DATABASE, error = initDatabase(r"./Food_Nutrition_Dataset.csv")

        # Initialise the currently selected food to be none
        self.currently_selected_food = None

        self.Show()

        # If there is an error, show the dialog
        if error:
            ErrorDialog(self, str(error), True)
            #                             ^^^^ This is indicates the error is non-recoverable, so the app needs to be closed

        # Display display all database entries in the grid initially
        displayResults(DATABASE, self.search_results_grid)

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

        results = searchDatabase(search_filters, DATABASE)
        displayResults(results, self.search_results_grid)

    def selectFood(self, event):
        """
        Adjust the currently selected food item, depending on what user has double-clicked on
        """
        # Get the selected row
        selected_cell = self.search_results_grid.GetCellValue(
            self.search_results_grid.GetGridCursorRow(), 0
        )

        # If the selected cell is empty, or if the user double clicked on the header row, return
        if not selected_cell:
            return

        # Get the selected food item
        selected_food = DATABASE[DATABASE["food"] == selected_cell]

        # Update the currently selected food
        self.currently_selected_food = selected_food

        # Display the selected food item in the text box
        self.search_result_selected.SetLabel(selected_cell)

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
