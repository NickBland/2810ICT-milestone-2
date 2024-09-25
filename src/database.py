import pandas as pd


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
        return result, e

    # Check if the file is empty
    if result.empty:
        return result, ValueError("File is empty")

    # Return the result
    return result, None


def searchDatabase():
    pass
