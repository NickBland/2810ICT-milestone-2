from datatable import DataTable
import pandas as pd


def updateTable(food, UI):
    """
    Update the Food Page to display the selected food item
    """
    # First check that the user has switched to the food_page (Page 1)
    if UI.notebook.GetSelection() != 1:
        return

    # If the food is None, set the text boxes to their default states
    if food is None:
        UI.food_selected_label.SetLabel("No Food Selected")
        UI.food_none_warning.Show()
        UI.food_information_grid.Hide()
    else:
        # Hide the warning label
        UI.food_none_warning.Hide()

        # Display the food name
        UI.food_selected_label.SetLabel(food["food"].values[0])

        # Display the food information as a table
        # Convert the names of the columns to a row each, and then the value as the second column
        df = food.T.reset_index().iloc[1:]
        df.columns = ["Nutrient Name", "Value"]
        food_information = DataTable(pd.DataFrame(df))

        grid = UI.food_information_grid
        grid.SetTable(food_information, True)
        grid.AutoSizeColumn(0)  # Only resize the first column
        grid.HideRowLabels()

        grid.Center()

        grid.Show()

    return
