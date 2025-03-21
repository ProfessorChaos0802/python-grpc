from tkinter import ttk

class TitleLabel(ttk.Label):
    """
    Tile label for client app
    """
    def __init__(self, parent, text):
        super().__init__(parent, text=text, style="Title.TLabel")