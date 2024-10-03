# Unit Testing Report

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/NickBland/2810ICT-milestone-2.git

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. 
Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.


## 1. **Test Summary**
list all tested functions related to the five required features and the corresponding test functions designed to test 
those functions, for example:

## 1. **Test Summary**

| **Tested Functions**           | **Test Functions**                               |
|-------------------------------|--------------------------------------------------|
| `initDatabase(filePath)`       | `test_initDatabase_with_valid_csv()`             |
|                               | `test_initDatabase_with_empty_csv()`             |
|                               | `test_initDatabase_with_invalid_file_path()`     |
|                               | `test_initDatabase_with_empty_file_path()`       |
|                               | `test_initDatabase_with_nonexistent_file()`      |
| `searchDatabase(filters, db)`  | `test_searchDatabase_with_keyword()`             |
|                               | `test_searchDatabase_with_nutrient_range()`      |
|                               | `test_searchDatabase_with_nutrient_level()`      |
|                               | `test_searchDatabase_with_invalid_minmax()`      |
|                               | `test_searchDatabase_with_all_filters()`         |
|                               | `test_searchDatabase_with_low_protein()`         |
|                               | `test_searchDatabase_with_mid_protein()`         |
|                               | `test_searchDatabase_with_high_protein()`        |
|                               | `test_searchDatabase_with_no_filters()`          |
| `displayResults(results, grid)`| `test_displayResults()`                          |

---

## 2. **Test Case Details**

### Test Case 1: testing valid CSV
- **Test Function/Module**
  - `test_initDatabase_with_valid_csv()`
- **Tested Function/Module**
  - `initDatabase(filePath)`
- **Description**
  - This function loads a CSV file into the database. The purpose of the test is to check whether the database is correctly loaded when given a valid CSV file.
- **1) Valid Input and Expected Output** 

| **Valid Input**               | **Expected Output**               |
|-------------------------------|-----------------------------------|
| `filePath = "test_valid.csv`  | `returns result as Database, error as None` |


- **1) Code for the Test Function**
```python
def test_initDatabase_with_valid_csv(setup_files):
    valid_csv_path, _, _ = setup_files
    result, error = initDatabase(valid_csv_path)
    assert result is not None
    assert error is None
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**              | **Expected Output** |
|--------------------------------|---------------------|
| `filePath = "test_invalid.csv` | `Returns None and raises `ValueError("File path is not a CSV file")``  |

- **2) Code for the Test Function**
```python
def test_initDatabase_with_invalid_file_path(setup_files):
    _, _, invalid_file_path = setup_files
    result, error = initDatabase(invalid_file_path)
    assert result is None
    assert isinstance(error, ValueError)
    assert str(error) == "File path is not a CSV file"
```
### Test Case 2: Testing Empty CSV 
- **Test Function/Module**
  - `test_initDatabase_with_empty_csv()`
- **Tested Function/Module**
  - `initDatabase(filePath)`
  
- **Description**
  - This function tests the `initDatabase` function to ensure that it handles an empty CSV file correctly by returning an error.
- **1) Valid Input and Expected Output**  

| **Invalid Input**              | **Expected Output** |
|--------------------------------|---------------------|
| `filePath = "test_invalid.csv` | `Returns None and raises `ValueError("File path is not a CSV file")``  |

- **1) Code for the Test Function**
```python
def test_initDatabase_with_empty_csv(setup_files):
    _, empty_csv_path, _ = setup_files
    result, error = initDatabase(empty_csv_path)
    assert result is None
    assert isinstance(error, ValueError)
    assert str(error) == "File is empty"
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `filePath = "test_empty.csv"` | `Returns None and raises `ValueError("File is empty")``|


- **2) Code for the Test Function**
```python
def test_initDatabase_with_empty_csv(setup_files):
    _, empty_csv_path, _ = setup_files
    result, error = initDatabase(empty_csv_path)
    assert result is None
    assert isinstance(error, ValueError)
    assert str(error) == "File is empty"
```

### Test Case 3: Test Case for Search Function with Keyword
- **Test Function/Module**
  - `test_searchDatabase_with_keyword()`
- **Tested Function/Module**
  - `searchDatabase(filters, db)`
- **Description**
  - This function searches the database for items based on the keyword filter. This test verifies that the correct entries are returned when filtering by a keyword.
- **1) Valid Input and Expected Output**  

| **Valid Input**                  | **Expected Output**                            |
|----------------------------------|------------------------------------------------|
| `filters = {"keyword": "banana"}` | `Returns DataFrame containing "banana" entries` |

- **1) Code for the Test Function**
```python
def test_searchDatabase_with_keyword(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {"keyword": "banana"}
    result = searchDatabase(filters, df)
    assert len(result) == 6
    assert result.iloc[0]["food"] == "banana cream pie"
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                   | **Expected Output**                               |
|-----------------------------------------------------|---------------------------------------------------|
| `filters = {"keyword": ""}`                         | Returns an empty DataFrame (no search results)    |
| `filters = {"keyword": None}`                       | Returns an empty DataFrame (no search results)    |
| `filters = {"keyword": 123}`                        | Returns an empty DataFrame (invalid search term)  |
| `filters = {"keyword": "nonexistentfooditem"}`      | Returns an empty DataFrame (no matches found)     |


- **2) Code for the Test Function**
```python
def test_searchDatabase_with_invalid_keyword(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)

```

### Test Case 4: Test case for search with Nutrient Range
- **Test Function/Module**
  - `test_searchDatabase_with_nutrient_range()`
- **Tested Function/Module**
  - `searchDatabase(filters, db)`
- **Description**
  - This function filters food items based on a specified nutrient range (e.g., protein). The test ensures that the function handles invalid range inputs, such as non-numeric values or nonsensical ranges, correctly.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `filters = {"nutrient": "Protein", "min": 0.5, "max": 1.0}`| `Returns DataFrame containing foods within the protein range 0.5 to 1.0`                 |


- **1) Code for the Test Function**
```python
def test_searchDatabase_with_nutrient_range(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {"nutrient": "Protein", "min": "0.5", "max": "1.0"}
    result = searchDatabase(filters, df)
    assert len(result) == 206
    assert result.iloc[0]["food"] == "cream cheese"

```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                         | **Expected Output**                             |
|-----------------------------------------------------------|-------------------------------------------------|
| `filters = {"nutrient": "Protein", "min": "abc", "max": 1.0}` | Returns an empty DataFrame (invalid min value)   |
| `filters = {"nutrient": "Protein", "min": 0.5, "max": "xyz"}` | Returns an empty DataFrame (invalid max value)   |
| `filters = {"nutrient": "Protein", "min": 2.0, "max": 1.0}`   | Returns an empty DataFrame (`min` > `max`)       |
| `filters = {"nutrient": "NonexistentNutrient", "min": 0, "max": 10}` | Returns an empty DataFrame (invalid nutrient)    |

- **2) Code for the Test Function**
```python
def test_searchDatabase_with_invalid_nutrient_range(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)

```



### Test Case 5: testing searchDatabase with nutrient level
- **Test Function/Module**
  - `test_searchDatabase_with_nutrient_level()`
- **Tested Function/Module**
  - `searchDatabase(filters, db)`
- **Description**
  - This function filters food items by a specific nutrient level (low, mid, high). The purpose of the test is to ensure the function correctly filters items based on valid nutrient levels and handles invalid levels appropriately.
  
- **1) Valid Input and Expected Output**  

| **Valid Input**                            | **Expected Output**                                 |
|--------------------------------------------|---------------------------------------------------|
| `filters = {"level-protein": 3}`           | Returns DataFrame filtered by high-protein items   |

- **1) Code for the Test Function**
```python
def test_searchDatabase_with_nutrient_level(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {"level-protein": 3}
    result = searchDatabase(filters, df)
    assert len(result) == 5
    assert result.iloc[0]["food"] == "pork top loin roasts raw"

```

### Test Case 6: testing searchDatabase with invalid `min` and `max` values
- **Test Function/Module**
  - `test_searchDatabase_with_invalid_minmax()`
- **Tested Function/Module**
  - `searchDatabase(filters, db)`
- **Description**
  - This function filters food items by a specified nutrient range using `min` and `max` values. The purpose of the test is to ensure the function handles invalid or non-numeric `min` and `max` values correctly.

- **1) Valid Input and Expected Output**  

| **Valid Input**                            | **Expected Output**                                     |
|--------------------------------------------|--------------------------------------------------------|
| `filters = {"nutrient": "Protein", "min": 0.5, "max": 1.0}` | Returns DataFrame with items that fall in this protein range |

- **1) Code for the Test Function**
```python
def test_searchDatabase_with_nutrient_range(fetch_real_data):
    data = fetch_real_data
    df = pd.DataFrame(data)
    filters = {"nutrient": "Protein", "min": 0.5, "max": 1.0}
    result = searchDatabase(filters, df)
    assert len(result) == 206
    assert result.iloc[0]["food"] == "cream cheese"
```

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
