# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-d6b9800)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext

_ = gettext.gettext

###########################################################################
## Class MyFrame3
###########################################################################


class MyFrame3(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=wx.EmptyString,
            pos=wx.DefaultPosition,
            size=wx.Size(1111, 558),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.notebook = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.search_panel = wx.Panel(
            self.notebook,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        search_bSizer = wx.BoxSizer(wx.HORIZONTAL)

        search_left_panel = wx.BoxSizer(wx.VERTICAL)

        self.nutrient_panel_top = wx.Panel(
            self.search_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        search_left_panel.Add(self.nutrient_panel_top, 1, wx.EXPAND | wx.ALL, 5)

        self.nutrient_panel_bot = wx.Panel(
            self.search_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        search_left_panel.Add(self.nutrient_panel_bot, 1, wx.EXPAND | wx.ALL, 5)

        search_bSizer.Add(search_left_panel, 1, wx.EXPAND, 5)

        self.search_results_grid = wx.grid.Grid(
            self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0
        )

        # Grid
        self.search_results_grid.CreateGrid(2, 1)
        self.search_results_grid.EnableEditing(False)
        self.search_results_grid.EnableGridLines(True)
        self.search_results_grid.EnableDragGridSize(False)
        self.search_results_grid.SetMargins(0, 0)

        # Columns
        self.search_results_grid.SetColSize(0, 160)
        self.search_results_grid.EnableDragColMove(False)
        self.search_results_grid.EnableDragColSize(False)
        self.search_results_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.search_results_grid.AutoSizeRows()
        self.search_results_grid.EnableDragRowSize(False)
        self.search_results_grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.search_results_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        search_bSizer.Add(self.search_results_grid, 1, wx.ALL | wx.EXPAND, 5)

        search_right_panel = wx.BoxSizer(wx.VERTICAL)

        self.search_title = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Search"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.search_title.Wrap(-1)

        self.search_title.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        search_right_panel.Add(
            self.search_title, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5
        )

        self.search_keyword_input = wx.TextCtrl(
            self.search_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        search_right_panel.Add(self.search_keyword_input, 0, wx.ALL | wx.EXPAND, 5)

        self.search_filters_label = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Filters"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.search_filters_label.Wrap(-1)

        self.search_filters_label.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        search_right_panel.Add(
            self.search_filters_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5
        )

        self.search_filter_nutrients_label = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Nutrients:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.search_filter_nutrients_label.Wrap(-1)

        search_right_panel.Add(self.search_filter_nutrients_label, 0, wx.ALL, 5)

        search_filter_nutrient_selectionChoices = [
            _("Caloric Value"),
            _("Fat"),
            _("Saturated Fats"),
            _("Monounsaturated Fats"),
            _("Polyunsaturated Fats"),
            _("Carbohydrates"),
            _("Sugars"),
            _("Protein"),
            _("Dietary Fiber"),
            _("Cholesterol"),
            _("Sodium"),
            _("Water"),
            _("Vitamin A"),
            _("Vitamin B1"),
            _("Vitamin B11"),
            _("Vitamin B12"),
            _("Vitamin B2"),
            _("Vitamin B3"),
            _("Vitamin B5"),
            _("Vitamin B6"),
            _("Vitamin C"),
            _("Vitamin D"),
            _("Vitamin E"),
            _("Vitamin K"),
            _("Calcium"),
            _("Copper"),
            _("Iron"),
            _("Magnesium"),
            _("Manganese"),
            _("Phosphorus"),
            _("Potassium"),
            _("Selenium"),
            _("Zinc"),
            _("Nutrition Density"),
        ]
        self.search_filter_nutrient_selection = wx.Choice(
            self.search_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.Size(200, -1),
            search_filter_nutrient_selectionChoices,
            0,
        )
        self.search_filter_nutrient_selection.SetSelection(0)
        search_right_panel.Add(
            self.search_filter_nutrient_selection,
            0,
            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL,
            5,
        )

        self.search_filter_range_label = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Nutrient Range:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.search_filter_range_label.Wrap(-1)

        search_right_panel.Add(self.search_filter_range_label, 0, wx.ALL, 5)

        search_filter_range_box = wx.BoxSizer(wx.HORIZONTAL)

        self.search_filter_range_min_label = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Min"),
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.ALIGN_RIGHT,
        )
        self.search_filter_range_min_label.Wrap(-1)

        search_filter_range_box.Add(self.search_filter_range_min_label, 1, wx.ALL, 5)

        self.search_filter_range_min = wx.TextCtrl(
            self.search_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(50, -1),
            0,
        )
        search_filter_range_box.Add(self.search_filter_range_min, 0, wx.ALL, 5)

        self.search_filter_range_mid_label = wx.StaticText(
            self.search_panel, wx.ID_ANY, _("-"), wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.search_filter_range_mid_label.Wrap(-1)

        search_filter_range_box.Add(self.search_filter_range_mid_label, 0, wx.ALL, 5)

        self.search_filter_range_max = wx.TextCtrl(
            self.search_panel,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.Size(50, -1),
            0,
        )
        search_filter_range_box.Add(self.search_filter_range_max, 0, wx.ALL, 5)

        self.search_filter_range_max_label = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Max"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.search_filter_range_max_label.Wrap(-1)

        search_filter_range_box.Add(self.search_filter_range_max_label, 1, wx.ALL, 5)

        search_right_panel.Add(
            search_filter_range_box,
            0,
            wx.ALIGN_TOP | wx.ALL | wx.SHAPED | wx.ALIGN_CENTER_HORIZONTAL,
            5,
        )

        self.search_filter_nutritional_level_label = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Nutritional Level:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.search_filter_nutritional_level_label.Wrap(-1)

        search_right_panel.Add(self.search_filter_nutritional_level_label, 0, wx.ALL, 5)

        bSizer111 = wx.BoxSizer(wx.HORIZONTAL)

        nutrition_level_filter_panel = wx.BoxSizer( wx.VERTICAL )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        nutrition_filter_protein_box = wx.BoxSizer( wx.VERTICAL )

        self.n_level_title_protein = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Protein"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.n_level_title_protein.Wrap( -1 )

        nutrition_filter_protein_box.Add( self.n_level_title_protein, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        search_filter_level_proteinChoices = [ _(u"N/A"), _(u"Low"), _(u"Mid"), _(u"High") ]
        self.search_filter_level_protein = wx.Choice( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, search_filter_level_proteinChoices, 0 )
        self.search_filter_level_protein.SetSelection( 0 )
        nutrition_filter_protein_box.Add( self.search_filter_level_protein, 0, wx.ALL, 5 )

        self.m_staticText18 = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Sugar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        nutrition_filter_protein_box.Add( self.m_staticText18, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        search_filter_level_sugarChoices = [ _(u"N/A"), _(u"Low"), _(u"Mid"), _(u"High") ]
        self.search_filter_level_sugar = wx.Choice( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, search_filter_level_sugarChoices, 0 )
        self.search_filter_level_sugar.SetSelection( 0 )
        nutrition_filter_protein_box.Add( self.search_filter_level_sugar, 0, wx.ALL, 5 )


        bSizer15.Add( nutrition_filter_protein_box, 0, wx.ALIGN_CENTER, 5 )

        nutrition_level_carb_box = wx.BoxSizer( wx.VERTICAL )

        self.n_level_title_carb = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Carbohydrates"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.n_level_title_carb.Wrap( -1 )

        nutrition_level_carb_box.Add( self.n_level_title_carb, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        search_filter_level_carbChoices = [ _(u"N/A"), _(u"Low"), _(u"Mid"), _(u"High") ]
        self.search_filter_level_carb = wx.Choice( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, search_filter_level_carbChoices, 0 )
        self.search_filter_level_carb.SetSelection( 0 )
        nutrition_level_carb_box.Add( self.search_filter_level_carb, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.n_level_title_nutri1 = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Nutritional density"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.n_level_title_nutri1.Wrap( -1 )

        nutrition_level_carb_box.Add( self.n_level_title_nutri1, 0, wx.ALL, 5 )

        search_filter_level_nutriChoices = [ _(u"N/A"), _(u"Low"), _(u"Mid"), _(u"High") ]
        self.search_filter_level_nutri = wx.Choice( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, search_filter_level_nutriChoices, 0 )
        self.search_filter_level_nutri.SetSelection( 0 )
        nutrition_level_carb_box.Add( self.search_filter_level_nutri, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer15.Add( nutrition_level_carb_box, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        nutrition_level_fat_box = wx.BoxSizer( wx.VERTICAL )

        self.n_level_title_fat = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Fat"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.n_level_title_fat.Wrap( -1 )

        nutrition_level_fat_box.Add( self.n_level_title_fat, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        search_filter_level_fatChoices = [ _(u"N/A"), _(u"Low"), _(u"Mid"), _(u"High") ]
        self.search_filter_level_fat = wx.Choice( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, search_filter_level_fatChoices, 0 )
        self.search_filter_level_fat.SetSelection( 0 )
        nutrition_level_fat_box.Add( self.search_filter_level_fat, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer15.Add( nutrition_level_fat_box, 1, 0, 5 )


        nutrition_level_filter_panel.Add( bSizer15, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        search_right_panel.Add( nutrition_level_filter_panel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.search_filter_other_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Other:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_filter_other_label.Wrap( -1 )

        self.n_level_title_fat = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Fat"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.n_level_title_fat.Wrap(-1)

        bSizer111.Add(self.n_level_title_fat, 0, wx.ALL, 5)

        self.n_level_title_carb = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Carbohydrates"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.n_level_title_carb.Wrap(-1)

        bSizer111.Add(self.n_level_title_carb, 0, wx.ALL, 5)

        search_right_panel.Add(bSizer111, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer101 = wx.BoxSizer(wx.VERTICAL)

        search_filter_level_selectionChoices = [_("Low"), _("Mid"), _("High")]
        self.search_filter_level_selection = wx.Choice(
            self.search_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            search_filter_level_selectionChoices,
            0,
        )
        self.search_filter_level_selection.SetSelection(0)
        bSizer101.Add(
            self.search_filter_level_selection,
            0,
            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL,
            5,
        )

        search_right_panel.Add(bSizer101, 1, wx.EXPAND, 5)

        self.search_filter_other_label = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Other:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.search_filter_other_label.Wrap(-1)

        search_right_panel.Add(self.search_filter_other_label, 0, wx.ALL, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.search_filter_highProtein = wx.CheckBox(
            self.search_panel,
            wx.ID_ANY,
            _("High Protein"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizer9.Add(self.search_filter_highProtein, 0, wx.ALL, 5)

        self.search_filter_lowSugar = wx.CheckBox(
            self.search_panel,
            wx.ID_ANY,
            _("Low Sugar"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizer9.Add(self.search_filter_lowSugar, 0, wx.ALL, 5)

        search_right_panel.Add(bSizer9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticline1 = wx.StaticLine(
            self.search_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.LI_HORIZONTAL,
        )
        search_right_panel.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.search_result_label = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("Currently Selected:"),
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.ALIGN_CENTER_HORIZONTAL,
        )
        self.search_result_label.Wrap(-1)

        self.search_result_label.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        search_right_panel.Add(
            self.search_result_label, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5
        )

        self.search_result_selected = wx.StaticText(
            self.search_panel,
            wx.ID_ANY,
            _("No Food Selected"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.search_result_selected.Wrap(-1)

        search_right_panel.Add(
            self.search_result_selected, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5
        )

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button13 = wx.Button(
            self.search_panel,
            wx.ID_ANY,
            _("View Data"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizer10.Add(self.m_button13, 1, wx.ALL, 5)

        self.m_button14 = wx.Button(
            self.search_panel,
            wx.ID_ANY,
            _("Reset"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizer10.Add(self.m_button14, 1, wx.ALL, 5)

        search_right_panel.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button15 = wx.Button(
            self.search_panel,
            wx.ID_ANY,
            _("Add/Remove from Comparison"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizer11.Add(self.m_button15, 1, wx.ALL, 5)

        self.m_button16 = wx.Button(
            self.search_panel,
            wx.ID_ANY,
            _("Exit"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        bSizer11.Add(self.m_button16, 1, wx.ALL, 5)

        search_right_panel.Add(bSizer11, 1, wx.EXPAND, 5)

        search_bSizer.Add(search_right_panel, 1, wx.EXPAND, 5)

        self.search_panel.SetSizer(search_bSizer)
        self.search_panel.Layout()
        search_bSizer.Fit(self.search_panel)
        self.notebook.AddPage(self.search_panel, _("Search"), True)
        self.food_page = wx.Panel(
            self.notebook,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        food_information_sizer = wx.BoxSizer(wx.VERTICAL)

        self.food_selected_label = wx.StaticText(
            self.food_page,
            wx.ID_ANY,
            _("No Food Selected"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.food_selected_label.Wrap(-1)

        self.food_selected_label.SetFont(
            wx.Font(
                20,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        food_information_sizer.Add(
            self.food_selected_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5
        )

        self.food_none_warning = wx.StaticText(
            self.food_page,
            wx.ID_ANY,
            _("Please double click an item under 'Search' to view more information"),
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.ALIGN_CENTER_HORIZONTAL,
        )
        self.food_none_warning.Wrap(-1)

        self.food_none_warning.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_TELETYPE,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )
        # Connect Events
        self.search_results_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.selectFood )
        self.search_keyword_input.Bind( wx.EVT_TEXT, self.search )
        self.search_filter_nutrient_selection.Bind( wx.EVT_CHOICE, self.search )
        self.search_filter_range_min.Bind( wx.EVT_TEXT, self.search )
        self.search_filter_range_max.Bind( wx.EVT_TEXT, self.search )
        self.search_filter_level_protein.Bind( wx.EVT_CHOICE, self.search )
        self.search_filter_level_sugar.Bind( wx.EVT_CHOICE, self.search )
        self.search_filter_level_carb.Bind( wx.EVT_CHOICE, self.search )
        self.search_filter_level_nutri.Bind( wx.EVT_CHOICE, self.search )
        self.search_filter_level_fat.Bind( wx.EVT_CHOICE, self.search )
        self.search_filter_highProtein.Bind( wx.EVT_CHECKBOX, self.search )
        self.search_filter_lowSugar.Bind( wx.EVT_CHECKBOX, self.search )
        self.m_button13.Bind( wx.EVT_BUTTON, self.search )
        self.m_button14.Bind( wx.EVT_BUTTON, self.resetApp )
        self.m_button15.Bind( wx.EVT_BUTTON, self.addComparison )
        self.m_button16.Bind( wx.EVT_BUTTON, self.exitApp )

        food_information_sizer.Add(
            self.food_none_warning, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5
        )

        gSizer1 = wx.GridSizer(0, 3, 0, 0)

        self.food_micro_pie = wx.Panel(
            self.food_page,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        gSizer1.Add(self.food_micro_pie, 1, wx.EXPAND | wx.ALL, 5)

        self.food_macro_graph = wx.Panel(
            self.food_page,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        gSizer1.Add(self.food_macro_graph, 1, wx.EXPAND | wx.ALL, 5)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.food_information_grid_label = wx.StaticText(
            self.food_page,
            wx.ID_ANY,
            _("Food Nutrients (per 100g)"),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.food_information_grid_label.Wrap(-1)

        self.food_information_grid_label.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        bSizer13.Add(
            self.food_information_grid_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5
        )

        self.food_information_grid = wx.grid.Grid(
            self.food_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0
        )

        # Grid
        self.food_information_grid.CreateGrid(17, 2)
        self.food_information_grid.EnableEditing(False)
        self.food_information_grid.EnableGridLines(True)
        self.food_information_grid.EnableDragGridSize(False)
        self.food_information_grid.SetMargins(0, 0)

        # Columns
        self.food_information_grid.EnableDragColMove(False)
        self.food_information_grid.EnableDragColSize(True)
        self.food_information_grid.SetColLabelAlignment(
            wx.ALIGN_CENTER, wx.ALIGN_CENTER
        )

        # Rows
        self.food_information_grid.EnableDragRowSize(True)
        self.food_information_grid.SetRowLabelAlignment(
            wx.ALIGN_CENTER, wx.ALIGN_CENTER
        )

        # Label Appearance

        # Cell Defaults
        self.food_information_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer13.Add(
            self.food_information_grid, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5
        )

        gSizer1.Add(bSizer13, 1, wx.EXPAND, 5)

        food_information_sizer.Add(gSizer1, 1, wx.EXPAND, 5)

        food_information_sizer.Add((0, 15), 0, wx.EXPAND, 5)

        self.food_page.SetSizer(food_information_sizer)
        self.food_page.Layout()
        food_information_sizer.Fit(self.food_page)
        self.notebook.AddPage(self.food_page, _("Food"), False)
        self.comparison_page = wx.Panel(
            self.notebook,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        self.notebook.AddPage(self.comparison_page, _("Comparison"), False)

        bSizer3.Add(self.notebook, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.updatePage)
        self.search_results_grid.Bind(
            wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.selectFood
        )
        self.search_keyword_input.Bind(wx.EVT_TEXT, self.search)
        self.search_filter_nutrient_selection.Bind(wx.EVT_CHOICE, self.search)
        self.search_filter_range_min.Bind(wx.EVT_TEXT, self.search)
        self.search_filter_range_max.Bind(wx.EVT_TEXT, self.search)
        self.search_filter_level_selection.Bind(wx.EVT_CHOICE, self.search)
        self.search_filter_highProtein.Bind(wx.EVT_CHECKBOX, self.search)
        self.search_filter_lowSugar.Bind(wx.EVT_CHECKBOX, self.search)
        self.m_button13.Bind(wx.EVT_BUTTON, self.search)
        self.m_button14.Bind(wx.EVT_BUTTON, self.resetApp)
        self.m_button15.Bind(wx.EVT_BUTTON, self.addComparison)
        self.m_button16.Bind(wx.EVT_BUTTON, self.exitApp)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def updatePage(self, event):
        event.Skip()

    def selectFood(self, event):
        event.Skip()

    def search(self, event):
        event.Skip()

    def resetApp(self, event):
        event.Skip()

    def addComparison(self, event):
        event.Skip()

    def exitApp(self, event):
        event.Skip()
