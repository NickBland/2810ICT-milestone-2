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


# Function for searching the dataframe.
def searchDatabase(filters: dict, database: pd.DataFrame):
    print(filters)
    print(database)

    # Grab all the data we need to search and filter the dataframe.
    # Search:
    keyword = filters.get("keyword", "")
    # Nutrients:
    nutrient = filters.get("nutrient", "")
    # Nutrient Range:
    min_value = filters.get("min", "")
    max_value = filters.get("max", "")
    # Nutrient Level:
    level_protein = filters.get("level-protein", 0)
    level_sugar = filters.get("level-sugar", 0)
    level_carb = filters.get("level-carb", 0)
    level_fat = filters.get("level-fat", 0)
    level_nutri = filters.get("level-nutri", 0)
    # Other (Checkboxes):
    high_protein = filters.get("high-protein", False)
    low_sugar = filters.get("low-sugar", False)

    # Filter the dataframe based on the keyword entered in the search bar.
    if keyword:
        filtered_db = database[
            database["food"].str.contains(keyword, regex=False, case=False, na=False)
        ]
    else:
        filtered_db = database

    filtered_db.loc["Nutrition Density"] = pd.to_numeric(
        filtered_db["Nutrition Density"], errors="coerce"
    )

    # Nutrient Range filter, filter the dataframe based on min and max values.
    if nutrient and min_value and max_value:
        filtered_db[nutrient] = pd.to_numeric(filtered_db[nutrient], errors="coerce")

        try:
            min_value = float(min_value)
            max_value = float(max_value)
        except ValueError:
            print("Invalid min or max, using default")
            min_value = float("-inf")
            max_value = float("inf")

        filtered_db = filtered_db[
            (filtered_db[nutrient] >= min_value) & (filtered_db[nutrient] <= max_value)
        ]

    # resist the auto-filter!

    # Checks and filters table depending on what is selected.
    # Filters, dropdown boxes (Nutritional Level)
    if level_protein:
        filtered_db = checkFilters(filtered_db, level_protein, "Protein")
    if level_carb:
        filtered_db = checkFilters(filtered_db, level_carb, "Carbohydrates")
    if level_fat:
        filtered_db = checkFilters(filtered_db, level_fat, "Fat")
    if level_sugar:
        filtered_db = checkFilters(filtered_db, level_sugar, "Sugars")
    if level_nutri:
        filtered_db = checkFilters(filtered_db, level_nutri, "Nutrition Density")

    # Filters, Checkboxes (Other)
    if high_protein:
        filtered_db = filterHigh(filtered_db, "Protein")
    if low_sugar:
        filtered_db = filterLow(filtered_db, "Sugars")
    return filtered_db


# Check which filter we are using
def checkFilters(database: pd.DataFrame, filters: int, nutrient: str):
    if filters == 1:
        database = filterLow(database, nutrient)
    elif filters == 2:
        database = filterMid(database, nutrient)
    elif filters == 3:
        database = filterHigh(database, nutrient)

    return database


# (Low) Filter the nutrient based on if it is < 33% of the max value.
def filterLow(database: pd.DataFrame, nutrient: str):
    max_value = database[nutrient].max()
    max_value = 0.33 * max_value
    database = database[database[nutrient] < max_value]
    return database


# (Mid) Filter the nutrient based on if it is >= 33% and < 66% of the max value.
def filterMid(database: pd.DataFrame, nutrient: str):
    max_value = database[nutrient].max()
    min_value = 0.33 * max_value
    max_value = 0.66 * max_value
    database = database[
        (database[nutrient] >= min_value) & (database[nutrient] < max_value)
    ]
    return database


# (High) Filter the nutrient based on if it is > 66% of the max value.
def filterHigh(database: pd.DataFrame, nutrient: str):
    max_value = database[nutrient].max()
    max_value = 0.66 * max_value
    database = database[database[nutrient] > max_value]
    return database


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
