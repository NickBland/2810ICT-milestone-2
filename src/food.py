from datatable import DataTable
import pandas as pd
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

matplotlib.use("WXAgg")


def updateFood(food, UI):
    """
    Update the Food Page to display the selected food item
    """
    # First check that the user has switched to the food_page (Page 1)
    if UI.notebook.GetSelection() != 1:
        return

    updateGrid(food, UI)

    drawPieChart(food, UI)
    drawBarChart(food, UI)
    UI.Layout()  # Update the layout of the page after everything has been rendered
    return


def updateGrid(food, UI):
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

        grid = UI.food_information_grid
        grid.SetTable(food_information, True)
        grid.AutoSizeColumns()
        grid.HideRowLabels()

        grid.Show()


def drawPieChart(food, UI):
    """
    Draw a pie chart of the vitamin breakdown of the selected food item
    """
    # If the food is None, set the pie chart to its default state
    if food is None:
        UI.food_micro_pie.Hide()
        return

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
    h, w = UI.food_micro_pie.GetSize()
    fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())

    fig.tight_layout()

    canvas = FigureCanvasWxAgg(UI.food_micro_pie, -1, fig)
    canvas.SetSize(UI.food_micro_pie.GetSize())

    # Display the pie chart
    UI.food_micro_pie.Show()
    return


def drawBarChart(food, UI):
    """
    Draw a bar chart of the macronutrient breakdown of the selected food item
    """
    # If the food is None, set the bar chart to its default state
    if food is None:
        UI.food_macro_graph.Hide()
        return

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
    h, w = UI.food_macro_graph.GetSize()
    fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())

    fig.tight_layout()

    canvas = FigureCanvasWxAgg(UI.food_macro_graph, -1, fig)
    canvas.SetSize(UI.food_macro_graph.GetSize())

    # Display the bar chart
    UI.food_macro_graph.Show()
    return
