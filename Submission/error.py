from error_gui import errorDialog as errorDialog


class ErrorDialog(errorDialog):
    def __init__(self, parent, message, exitable=False):
        super().__init__(parent)
        self.error_label_message.SetLabel(message)
        self.exitable = exitable
        self.ShowModal()

    def exitError(self, event):
        """
        If the error is non-recovarable, close the application
        Otherwise, close just the error dialog
        """
        if self.exitable:
            self.GetParent().Close()
        self.Destroy()
