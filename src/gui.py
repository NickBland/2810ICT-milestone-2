# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
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

class MyFrame3 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1111,558 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_panel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        search_bSizer = wx.BoxSizer( wx.HORIZONTAL )

        search_left_panel = wx.BoxSizer( wx.VERTICAL )

        self.nutrient_panel_top = wx.Panel( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        search_left_panel.Add( self.nutrient_panel_top, 1, wx.EXPAND |wx.ALL, 5 )

        self.nutrient_panel_bot = wx.Panel( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        search_left_panel.Add( self.nutrient_panel_bot, 1, wx.EXPAND |wx.ALL, 5 )


        search_bSizer.Add( search_left_panel, 1, wx.EXPAND, 5 )

        self.search_results_grid = wx.grid.Grid( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.search_results_grid.CreateGrid( 2, 1 )
        self.search_results_grid.EnableEditing( False )
        self.search_results_grid.EnableGridLines( True )
        self.search_results_grid.EnableDragGridSize( False )
        self.search_results_grid.SetMargins( 0, 0 )

        # Columns
        self.search_results_grid.SetColSize( 0, 160 )
        self.search_results_grid.EnableDragColMove( False )
        self.search_results_grid.EnableDragColSize( False )
        self.search_results_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.search_results_grid.AutoSizeRows()
        self.search_results_grid.EnableDragRowSize( False )
        self.search_results_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.search_results_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        search_bSizer.Add( self.search_results_grid, 1, wx.ALL|wx.EXPAND, 5 )

        search_right_panel = wx.BoxSizer( wx.VERTICAL )

        self.search_title = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_title.Wrap( -1 )

        self.search_title.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        search_right_panel.Add( self.search_title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.search_keyword_input = wx.TextCtrl( self.search_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        search_right_panel.Add( self.search_keyword_input, 0, wx.ALL|wx.EXPAND, 5 )

        self.search_filters_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Filters"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_filters_label.Wrap( -1 )

        self.search_filters_label.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        search_right_panel.Add( self.search_filters_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.search_filter_nutrients_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Nutrients:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_filter_nutrients_label.Wrap( -1 )

        search_right_panel.Add( self.search_filter_nutrients_label, 0, wx.ALL, 5 )

        search_filter_nutrient_selectionChoices = []
        self.search_filter_nutrient_selection = wx.Choice( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), search_filter_nutrient_selectionChoices, 0 )
        self.search_filter_nutrient_selection.SetSelection( 0 )
        search_right_panel.Add( self.search_filter_nutrient_selection, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.search_filter_range_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Nutrient Range:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_filter_range_label.Wrap( -1 )

        search_right_panel.Add( self.search_filter_range_label, 0, wx.ALL, 5 )

        search_filter_range_box = wx.BoxSizer( wx.HORIZONTAL )

        self.search_filter_range_min_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Min"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.search_filter_range_min_label.Wrap( -1 )

        search_filter_range_box.Add( self.search_filter_range_min_label, 1, wx.ALL, 5 )

        self.search_filter_range_min = wx.TextCtrl( self.search_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        search_filter_range_box.Add( self.search_filter_range_min, 0, wx.ALL, 5 )

        self.search_filter_range_mid_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_filter_range_mid_label.Wrap( -1 )

        search_filter_range_box.Add( self.search_filter_range_mid_label, 0, wx.ALL, 5 )

        self.search_filter_range_max = wx.TextCtrl( self.search_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        search_filter_range_box.Add( self.search_filter_range_max, 0, wx.ALL, 5 )

        self.search_filter_range_max_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Max"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_filter_range_max_label.Wrap( -1 )

        search_filter_range_box.Add( self.search_filter_range_max_label, 1, wx.ALL, 5 )


        search_right_panel.Add( search_filter_range_box, 0, wx.ALIGN_TOP|wx.ALL|wx.SHAPED|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.search_filter_nutritional_level_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Nutritional Level:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_filter_nutritional_level_label.Wrap( -1 )

        search_right_panel.Add( self.search_filter_nutritional_level_label, 0, wx.ALL, 5 )

        search_filter_level_selectionChoices = []
        self.search_filter_level_selection = wx.Choice( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, search_filter_level_selectionChoices, 0 )
        self.search_filter_level_selection.SetSelection( 0 )
        search_right_panel.Add( self.search_filter_level_selection, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.search_filter_other_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Other:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_filter_other_label.Wrap( -1 )

        search_right_panel.Add( self.search_filter_other_label, 0, wx.ALL, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.search_filter_highProtein = wx.CheckBox( self.search_panel, wx.ID_ANY, _(u"High Protein"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.search_filter_highProtein, 0, wx.ALL, 5 )

        self.search_filter_lowSugar = wx.CheckBox( self.search_panel, wx.ID_ANY, _(u"Low Sugar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.search_filter_lowSugar, 0, wx.ALL, 5 )


        search_right_panel.Add( bSizer9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticline1 = wx.StaticLine( self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        search_right_panel.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.search_result_label = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"Currently Selected:"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.search_result_label.Wrap( -1 )

        self.search_result_label.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        search_right_panel.Add( self.search_result_label, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.search_result_selected = wx.StaticText( self.search_panel, wx.ID_ANY, _(u"No Food Selected"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_result_selected.Wrap( -1 )

        search_right_panel.Add( self.search_result_selected, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button13 = wx.Button( self.search_panel, wx.ID_ANY, _(u"View Data"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button13, 1, wx.ALL, 5 )

        self.m_button14 = wx.Button( self.search_panel, wx.ID_ANY, _(u"Reset"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button14, 1, wx.ALL, 5 )


        search_right_panel.Add( bSizer10, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button15 = wx.Button( self.search_panel, wx.ID_ANY, _(u"Add/Remove from Comparison"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button15, 1, wx.ALL, 5 )

        self.m_button16 = wx.Button( self.search_panel, wx.ID_ANY, _(u"Exit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button16, 1, wx.ALL, 5 )


        search_right_panel.Add( bSizer11, 1, wx.EXPAND, 5 )


        search_bSizer.Add( search_right_panel, 1, wx.EXPAND, 5 )


        self.search_panel.SetSizer( search_bSizer )
        self.search_panel.Layout()
        search_bSizer.Fit( self.search_panel )
        self.m_notebook1.AddPage( self.search_panel, _(u"Search"), False )
        self.food_panel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook1.AddPage( self.food_panel, _(u"Food"), False )
        self.comparison_panel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook1.AddPage( self.comparison_panel, _(u"Comparison"), False )

        bSizer3.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.search_results_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.selectFood )
        self.search_keyword_input.Bind( wx.EVT_TEXT, self.search )
        self.m_button13.Bind( wx.EVT_BUTTON, self.search )
        self.m_button14.Bind( wx.EVT_BUTTON, self.resetApp )
        self.m_button15.Bind( wx.EVT_BUTTON, self.addComparison )
        self.m_button16.Bind( wx.EVT_BUTTON, self.exitApp )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def selectFood( self, event ):
        event.Skip()

    def search( self, event ):
        event.Skip()


    def resetApp( self, event ):
        event.Skip()

    def addComparison( self, event ):
        event.Skip()

    def exitApp( self, event ):
        event.Skip()


