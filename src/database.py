import pandas as pd

# import wx.grid
from datatable import DataTable


def initDatabase(filePath: str):
    """
    Initialize the database object with the given file path
    """
    result = None

    # First determine if the path actually exists
    if not filePath:
        return result, FileNotFoundError("File path is empty")

    # Determine if the file provided is a CSV file
    if not filePath.endswith(".csv"):
        return result, ValueError("File path is not a CSV file")

    # Read the CSV file
    try:
        result = pd.read_csv(filePath)
    except Exception as e:
        if str(e) == "No columns to parse from file":
            return None, ValueError("File is empty")
        else:
            return result, e

    # Return the result
    return result, None


def searchDatabase(filters: dict, database: pd.DataFrame):
    print(filters)
    print(database)
    return


def displayResults(database: pd.DataFrame, grid):
    # Clear the grid
    grid.ClearGrid()

    # Display just the names of the items (col 1)
    df = database.food
    data = DataTable(df.to_frame())
    grid.SetTable(data, True)
    grid.AutoSizeColumns(True)
    grid.HideRowLabels()  # Hide the row numbers (they take up too much space)
    return
