import pandas as pd

# import wx.grid
from datatable import DataTable

# Conversion to kcal from g
FAT_CONVERSION = 9
CARB_CONVERSION = 4
SUGAR_CONVERSION = 4
PROTEIN_CONVERSION = 4
NUTRI_CONVERSION = 0


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

    keyword = filters.get("keyword", "")
    nutrient = filters.get("nutrient", "")
    level_protein = filters.get("level-protein", 0)
    print("THIS IS THE LEVEL PROTEIN + " + str(level_protein))
    level_sugar = filters.get("level-sugar", 0)
    level_carb = filters.get("level-carb", 0)
    level_fat = filters.get("level-fat", 0)
    level_nutri = filters.get("level-nutri", 0)
    min_value = filters.get("min", "")
    max_value = filters.get("max", "")
    high_protein = filters.get("high-protein", False)
    low_sugar = filters.get("low-sugar", False)

    # debug
    # print(type(nutrient))
    # print(nutrient)

    # Keyword Filter
    if keyword:
        filtered_db = database[
            database["food"].str.contains(keyword, regex=False, case=False, na=False)
        ]
    else:
        filtered_db = database

    filtered_db.loc["Nutrition Density"] = pd.to_numeric(
        filtered_db["Nutrition Density"], errors="coerce"
    )

    # NutrientFilter
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

    if level_protein:
        filtered_db = checkFilters(
            filtered_db, level_protein, "Protein", PROTEIN_CONVERSION
        )
    if level_carb:
        filtered_db = checkFilters(
            filtered_db, level_carb, "Carbohydrates", CARB_CONVERSION
        )
    if level_fat:
        filtered_db = checkFilters(filtered_db, level_fat, "Fat", FAT_CONVERSION)
    if level_sugar:
        filtered_db = checkFilters(filtered_db, level_sugar, "Sugars", SUGAR_CONVERSION)
    if level_nutri:
        filtered_db = checkFilters(
            filtered_db, level_nutri, "Nutrition Density", NUTRI_CONVERSION
        )
    # if high_protein:
    #     filterHigh(filtered_db, 'Protein')
    # if low_sugar:
    #     filterLow(filtered_db, 'Sugars')

    return filtered_db


def checkFilters(
    database: pd.DataFrame, filters: int, nutrient: str, conversion_type: str = ""
):
    if filters == 1:
        database = filterLow(database, nutrient, conversion_type)
    elif filters == 2:
        database = filterMid(database, nutrient, conversion_type)
    elif filters == 3:
        database = filterHigh(database, nutrient, conversion_type)

    return database


def filterLow(database: pd.DataFrame, nutrient: str, conversion_type: str):
    if nutrient == "Nutrition Density":
        database["nutrient_percentage"] = (
            database["Nutrition Density"] / database["Caloric Value"]
        )
        database = database[database["nutrient_percentage"] < 0.33]
        return database
    else:
        database["converted_nutrient"] = database[nutrient] * conversion_type
        database["nutrient_percentage"] = (
            database["converted_nutrient"] / database["Caloric Value"]
        )
        database = database[database["nutrient_percentage"] < 0.33]
        return database


def filterMid(database: pd.DataFrame, nutrient: str, conversion_type: str):
    if nutrient == "Nutrition Density":
        database["nutrient_percentage"] = (
            database["Nutrition Density"] / database["Caloric Value"]
        )
        database = database[
            (database["nutrient_percentage"] >= 0.33)
            & (database["nutrient_percentage"] < 0.66)
        ]
        return database
    else:
        database["converted_nutrient"] = database[nutrient] * conversion_type
        database["nutrient_percentage"] = (
            database["converted_nutrient"] / database["Caloric Value"]
        )
        database = database[
            (database["nutrient_percentage"] >= 0.33)
            & (database["nutrient_percentage"] < 0.66)
        ]
        return database


def filterHigh(database: pd.DataFrame, nutrient: str, conversion_type: str):
    if nutrient == "Nutrition Density":
        database["nutrient_percentage"] = (
            database["Nutrition Density"] / database["Caloric Value"]
        )
        database = database[database["nutrient_percentage"] > 0.66]
        return database
    else:
        database["converted_nutrient"] = database[nutrient] * conversion_type
        database["nutrient_percentage"] = (
            database["converted_nutrient"] / database["Caloric Value"]
        )
        database = database[database["nutrient_percentage"] > 0.66]
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
