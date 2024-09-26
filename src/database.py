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
    
    keyword = filters.get('keyword', '')
    nutrient = filters.get('nutrient', '')
    min_value = filters.get('min', '')
    max_value = filters.get('max', '')

    #debug
    # print(type(nutrient))
    # print(nutrient)
    
    # Keyword Filter
    if keyword:
        filtered_db = database[database['food'].str.contains(keyword, regex=False, case=False, na=False)]
    else:
        filtered_db = database

    # NutrientFilter
    if nutrient and min_value and max_value:

        filtered_db[nutrient] = pd.to_numeric(filtered_db[nutrient], errors='coerce')

        try:
            min_value = float(min_value)
            max_value = float(max_value)
        except ValueError:
            print("Invalid min or max, using default")
            min_value = float('-inf')
            max_value = float('inf')

        filtered_db = filtered_db[(filtered_db[nutrient] >= min_value) & (filtered_db[nutrient] <= max_value)]

    return filtered_db
        
def displayResults(database: pd .DataFrame, grid):
    # Clear the grid
    grid.ClearGrid()

    # Display just the names of the items (col 1)
    df = database.food
    data = DataTable(df.to_frame())
    grid.SetTable(data, True)
    grid.AutoSizeColumns(True)
    grid.HideRowLabels()  # Hide the row numbers (they take up too much space)
    return
