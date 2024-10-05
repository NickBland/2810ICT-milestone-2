# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-d6b9800)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext

_ = gettext.gettext

###########################################################################
## Class errorDialog
###########################################################################


class errorDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=_("Error"),
            pos=wx.DefaultPosition,
            size=wx.Size(296, 244),
            style=wx.CAPTION,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.error_label_title = wx.StaticText(
            self, wx.ID_ANY, _("Error"), wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.error_label_title.Wrap(-1)

        self.error_label_title.SetFont(
            wx.Font(
                16,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                False,
                wx.EmptyString,
            )
        )

        bSizer9.Add(self.error_label_title, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticline2 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL
        )
        bSizer9.Add(self.m_staticline2, 0, wx.ALL | wx.EXPAND, 5)

        self.error_label_message = wx.StaticText(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.ALIGN_CENTER_HORIZONTAL,
        )
        self.error_label_message.Wrap(-1)

        self.error_label_message.SetFont(
            wx.Font(
                wx.NORMAL_FONT.GetPointSize(),
                wx.FONTFAMILY_TELETYPE,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                False,
                wx.EmptyString,
            )
        )

        bSizer9.Add(self.error_label_message, 1, wx.ALL | wx.EXPAND, 5)

        self.error_button_exit = wx.Button(
            self, wx.ID_ANY, _("Confirm"), wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer9.Add(self.error_button_exit, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.VERTICAL)

        # Connect Events
        self.error_button_exit.Bind(wx.EVT_BUTTON, self.exitError)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def exitError(self, event):
        event.Skip()
