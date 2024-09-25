import pytest
import pandas as pd
import os

import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


# Import DB functions
from database import initDatabase


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
