from datatable import DataTable
import pandas as pd
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

matplotlib.use("WXAgg")


def updateFood(food, comparison_list, UI):
    """
    Update the Food Page to display the selected food item
    """

    # Close all matplotlib figures to prevent memory leaks
    plt.close("all")

    # First check that the user has switched to the food_page (Page 1)
    if UI.notebook.GetSelection() == 1:
        if food is None:
            UI.food_selected_label.SetLabel("No Food Selected")
            UI.food_none_warning.Show()
            UI.food_information_grid.Hide()
            UI.food_information_grid_label.Hide()
            UI.food_micro_pie.Hide()
            UI.food_macro_graph.Hide()
        else:
            UI.food_none_warning.Hide()
            UI.food_information_grid_label.Show()
            UI.food_selected_label.SetLabel(food["food"].values[0])
            updateGrid(food, UI.food_information_grid)
            drawPieChart(food, UI.food_micro_pie)
            drawBarChart(food, UI.food_macro_graph)
    elif UI.notebook.GetSelection() == 2:
        if len(comparison_list) == 0:
            UI.comparison_foodA_name.SetLabel("No Food Selected")
            UI.comparison_foodB_name.SetLabel("No Food Selected")
            UI.comparison_foodA_grid.Hide()
            UI.comparison_foodA_micro.Hide()
            UI.comparison_foodA_macro.Hide()
            UI.comparison_foodB_grid.Hide()
            UI.comparison_foodB_micro.Hide()
            UI.comparison_foodB_macro.Hide()
        elif len(comparison_list) == 1:
            UI.comparison_foodA_name.SetLabel(comparison_list["food"].values[0])
            UI.comparison_foodB_name.SetLabel("No Food Selected")
            updateGrid(comparison_list.iloc[:1], UI.comparison_foodA_grid)
            drawPieChart(comparison_list.iloc[:1], UI.comparison_foodA_micro)
            drawBarChart(comparison_list.iloc[:1], UI.comparison_foodA_macro)
            UI.comparison_foodB_grid.Hide()
            UI.comparison_foodB_micro.Hide()
            UI.comparison_foodB_macro.Hide()
        else:
            UI.comparison_foodA_name.SetLabel(comparison_list["food"].values[0])
            UI.comparison_foodB_name.SetLabel(comparison_list["food"].values[1])
            updateGrid(comparison_list.iloc[:1], UI.comparison_foodA_grid)
            updateGrid(comparison_list.iloc[1:2], UI.comparison_foodB_grid)
            drawPieChart(comparison_list.iloc[:1], UI.comparison_foodA_micro)
            drawPieChart(comparison_list.iloc[1:2], UI.comparison_foodB_micro)
            drawBarChart(comparison_list.iloc[:1], UI.comparison_foodA_macro)
            drawBarChart(comparison_list.iloc[1:2], UI.comparison_foodB_macro)

            # Make sure everything is shown
            UI.comparison_foodA_grid.Show()
            UI.comparison_foodA_micro.Show()
            UI.comparison_foodA_macro.Show()
            UI.comparison_foodB_grid.Show()
            UI.comparison_foodB_micro.Show()
            UI.comparison_foodB_macro.Show()

    UI.Layout()  # Update the layout of the page after everything has been rendered
    return


def updateGrid(food, component):
    # If the nutrient_percentage column is present, remove it
    if "nutrient_percentage" in food.columns:
        food = food.drop(columns=["nutrient_percentage"])

    # Display the food information as a table
    # Convert the names of the columns to a row each, and then the value as the second column
    # Skip the first row, as it contains the food name
    df = food.T.reset_index().iloc[1:]

    df.columns = ["Nutrient Name", "Value"]

    # Add the unit to a third column. This will have to be manual unfortunately
    df["Unit"] = [
        "kcal",
        "g",
        "g",
        "g",
        "g",
        "g",
        "g",
        "g",
        "g",
        "mg",
        "g",
        "g",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "mg",
        "N/A",
    ]

    food_information = DataTable(pd.DataFrame(df))

    grid = component
    grid.SetTable(food_information, True)
    grid.AutoSizeColumns()
    grid.HideRowLabels()

    grid.Show()


def drawPieChart(food, panel_component):
    """
    Draw a pie chart of the vitamin breakdown of the selected food item
    """

    print(food)

    # Get the micro nutrient values
    vitaminA = food["Vitamin A"].values[0]
    vitaminB1 = food["Vitamin B1"].values[0]
    vitaminB11 = food["Vitamin B11"].values[0]
    vitaminB12 = food["Vitamin B12"].values[0]
    vitaminB2 = food["Vitamin B2"].values[0]
    vitaminB3 = food["Vitamin B3"].values[0]
    vitaminB5 = food["Vitamin B5"].values[0]
    vitaminB6 = food["Vitamin B6"].values[0]
    vitaminC = food["Vitamin C"].values[0]
    vitaminD = food["Vitamin D"].values[0]
    vitaminE = food["Vitamin E"].values[0]
    vitaminK = food["Vitamin K"].values[0]

    values = [
        vitaminA,
        vitaminB1,
        vitaminB11,
        vitaminB12,
        vitaminB2,
        vitaminB3,
        vitaminB5,
        vitaminB6,
        vitaminC,
        vitaminD,
        vitaminE,
        vitaminK,
    ]

    types = [
        "A",
        "B1",
        "B11",
        "B12",
        "B2",
        "B3",
        "B5",
        "B6",
        "C",
        "D",
        "E",
        "K",
    ]

    # Remove any vitamins that are 0
    values, types = zip(*[(v, t) for v, t in zip(values, types) if v != 0])

    # Function to format the percentage labels depending on the size of the slice (tiny ones will overlap otherwise)
    def autopct_func(pct):
        return ("%1.1f%%" % pct) if pct > 1 else ""

    # Create the pie chart figure
    fig, ax = plt.subplots()
    ax.pie(
        values,
        labels=types,
        autopct=autopct_func,
        startangle=90,
        shadow=False,
        labeldistance=1.1,
        pctdistance=0.85,
    )
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle
    ax.set_title("Vitamin Breakdown")

    # Resize chart so it looks nicer
    h, w = panel_component.GetSize()
    fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())

    fig.tight_layout()

    canvas = FigureCanvasWxAgg(panel_component, -1, fig)
    canvas.SetSize(panel_component.GetSize())

    # Display the pie chart
    panel_component.Show()
    return


def drawBarChart(food, panel_component):
    """
    Draw a bar chart of the macronutrient breakdown of the selected food item
    """

    values = [
        food["Protein"].values[0],
        food["Carbohydrates"].values[0],
        food["Fat"].values[0],
        food["Sugars"].values[0],
    ]

    labels = ["Protein", "Carbs", "Fat", "Sugars"]

    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel("Amount (g per 100g)")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=90)

    ax.set_title("Macronutrient Breakdown")

    # Resize chart so it looks nicer
    h, w = panel_component.GetSize()
    fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())

    fig.tight_layout()

    canvas = FigureCanvasWxAgg(panel_component, -1, fig)
    canvas.SetSize(panel_component.GetSize())

    # Display the bar chart
    panel_component.Show()
    return
