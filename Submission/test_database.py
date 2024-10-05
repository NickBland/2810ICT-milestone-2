import pytest
import pandas as pd
import os

# Import DB functions
from database import initDatabase, searchDatabase, displayResults, addToComparison


def pytest_html_report_title(report):
    report.title = "Database Tests Report"


@pytest.fixture
def setup_files():
    tests_dir = os.path.dirname(__file__)
    valid_csv_path = os.path.join(tests_dir, "test_valid.csv")
    empty_csv_path = os.path.join(tests_dir, "test_empty.csv")
    invalid_file_path = os.path.join(tests_dir, "test_valid.csvERROR")

    # Write some data to the valid CSV file
    pd.DataFrame({"col1": [1, 2], "col2": [3, 4]}).to_csv(valid_csv_path, index=False)

    # Create an empty CSV file
    pd.DataFrame().to_csv(empty_csv_path, index=False)

    yield valid_csv_path, empty_csv_path, invalid_file_path

    # Remove the temporary files after tests
    if os.path.exists(valid_csv_path):
        os.remove(valid_csv_path)
    if os.path.exists(empty_csv_path):
        os.remove(empty_csv_path)


@pytest.fixture
def fetch_real_data():
    data = pd.read_csv(r"./Food_Nutrition_Dataset.csv")
    yield data


def test_initDatabase_with_valid_csv(setup_files):
    valid_csv_path, _, _ = setup_files
    result, error = initDatabase(valid_csv_path)
    assert result is not None
    assert error is None


def test_initDatabase_with_empty_csv(setup_files):
    _, empty_csv_path, _ = setup_files
    result, error = initDatabase(empty_csv_path)
    assert result is None
    assert isinstance(error, ValueError)
    assert str(error) == "File is empty"


def test_initDatabase_with_invalid_file_path(setup_files):
    _, _, invalid_file_path = setup_files
    result, error = initDatabase(invalid_file_path)
    assert result is None
    assert isinstance(error, ValueError)
    assert str(error) == "File path is not a CSV file"


def test_initDatabase_with_empty_file_path():
    result, error = initDatabase("")
    assert result is None
    assert isinstance(error, FileNotFoundError)
    assert str(error) == "File path is empty"


def test_initDatabase_with_nonexistent_file():
    result, error = initDatabase("nonexistent.csv")
    assert result is None
    assert isinstance(error, FileNotFoundError)


def test_searchDatabase_with_keyword(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {"keyword": "banana"}
    result = searchDatabase(filters, df)
    assert len(result) == 6
    assert result.iloc[0]["food"] == "banana cream pie"


def test_searchDatabase_with_nutrient_range(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {"nutrient": "Protein", "min": "0.5", "max": "1.0"}
    result = searchDatabase(filters, df)
    assert len(result) == 206
    assert result.iloc[0]["food"] == "cream cheese"


def test_searchDatabase_with_nutrient_level(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {"level-protein": 3}
    result = searchDatabase(filters, df)
    assert len(result) == 5
    assert result.iloc[0]["food"] == "pork top loin roasts raw"


def test_searchDatabase_with_invalid_minmax(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {"nutrient": "Protein", "min": "abd", "max": "def"}
    assert len(searchDatabase(filters, df)) == 2395


def test_searchDatabase_with_all_filters(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {
        "keyword": "",
        "nutrient": "",
        "min": "",
        "max": "",
        "level-protein": 1,
        "level-sugar": 1,
        "level-carb": 2,
        "level-fat": 1,
        "level-nutri": 1,
    }
    result = searchDatabase(filters, df)
    assert len(result) == 3
    assert result.iloc[0]["food"] == "tapioca pearls"


def test_searchDatabase_with_low_protein(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {
        "level-protein": 1,
    }
    result = searchDatabase(filters, df)
    assert len(result) == 2383
    assert result.iloc[0]["food"] == "cream cheese"


def test_searchDatabase_with_mid_protein(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {
        "level-protein": 2,
    }
    result = searchDatabase(filters, df)
    assert len(result) == 7
    assert result.iloc[0]["food"] == "pork backribs raw"


def test_searchDatabase_with_high_protein(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {
        "level-protein": 3,
    }
    result = searchDatabase(filters, df)
    assert len(result) == 5
    assert result.iloc[0]["food"] == "pork top loin roasts raw"


def test_searchDatabase_with_no_filters(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {}
    result = searchDatabase(filters, df)
    assert len(result) == 2396
    assert result.iloc[0]["food"] == "cream cheese"

def test_addComparisonNone(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    comparison_list = []

    # Empty selected food
    selected_food = None
    currently_selected_food = selected_food
    addToComparison(currently_selected_food, comparison_list)

def test_addComparisonAddOne(fetch_real_data):

    data = fetch_real_data
    df = pd.DataFrame(data)
    comparison_list = []

    # Select Food
    selected_food = df[df["food"] == "cream Cheese"]
    currently_selected_food = selected_food
    addToComparison(currently_selected_food, comparison_list)

def test_addComparisonAddTwo(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    comparison_list = []
    
    # add two different foods
    selected_food = df[df["food"] == "cream cheese"]
    currently_selected_food = selected_food
    comparison_list = addToComparison(currently_selected_food, comparison_list)

    selected_food = df[df["food"] == "gruyere cheese"]
    currently_selected_food = selected_food
    addToComparison(currently_selected_food, comparison_list)

def test_addComparisonAddSame(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    comparison_list = []

    # Add two of the same food
    selected_food = df[df["food"] == "cream cheese"]
    currently_selected_food = selected_food
    comparison_list = addToComparison(currently_selected_food, comparison_list)

    selected_food = df[df["food"] == "cream cheese"]
    currently_selected_food = selected_food
    addToComparison(currently_selected_food, comparison_list)


def test_displayResults(fetch_real_data, mocker):
    data = fetch_real_data
    df = pd.DataFrame(data)

    # Create a mock grid
    # grid = SimpleMock()
    grid = mocker.MagicMock()

    # Call the displayResults function
    displayResults(df, grid)

    # Assertions to check if the grid methods were called correctly
    grid.ClearGrid.assert_called_once()
    grid.SetTable.assert_called_once()
    grid.AutoSizeColumns.assert_called_once()
    grid.HideRowLabels.assert_called_once()
