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
            size=wx.Size(1102, 503),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.search_panel = wx.Panel(
            self.m_notebook1,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        search_bSizer = wx.BoxSizer(wx.HORIZONTAL)

        search_left_panel = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(
            self.search_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        search_left_panel.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel5 = wx.Panel(
            self.search_panel,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        search_left_panel.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        search_bSizer.Add(search_left_panel, 1, wx.EXPAND, 5)

        self.search_results_grid = wx.grid.Grid(
            self.search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0
        )

        # Grid
        self.search_results_grid.CreateGrid(5, 5)
        self.search_results_grid.EnableEditing(True)
        self.search_results_grid.EnableGridLines(True)
        self.search_results_grid.EnableDragGridSize(False)
        self.search_results_grid.SetMargins(0, 0)

        # Columns
        self.search_results_grid.EnableDragColMove(False)
        self.search_results_grid.EnableDragColSize(True)
        self.search_results_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.search_results_grid.EnableDragRowSize(True)
        self.search_results_grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.search_results_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        search_bSizer.Add(self.search_results_grid, 0, wx.ALL | wx.EXPAND, 5)

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

        search_bSizer.Add(search_right_panel, 1, wx.EXPAND, 5)

        self.search_panel.SetSizer(search_bSizer)
        self.search_panel.Layout()
        search_bSizer.Fit(self.search_panel)
        self.m_notebook1.AddPage(self.search_panel, _("Search"), False)
        self.food_panel = wx.Panel(
            self.m_notebook1,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        self.m_notebook1.AddPage(self.food_panel, _("Food"), False)
        self.comparison_panel = wx.Panel(
            self.m_notebook1,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TAB_TRAVERSAL,
        )
        self.m_notebook1.AddPage(self.comparison_panel, _("Comparison"), False)

        bSizer3.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
