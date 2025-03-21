from tkinter import ttk
from .components_frame import ComponentsFrame
from labels.title_label import TitleLabel

class MainFrame(ttk.Frame):
    """
    Main Frame
    """
    def __init__(self, parent, logger, stub):
        super().__init__(parent, style="Main.TFrame")

        # Title Label
        self.title_label = TitleLabel(self, text="Welcome to gRPC Client UI")
        self.title_label.pack(pady=5)

        # Assign gRPC Stub
        self.stub = stub

        # Frame for rest of the widgets
        self.components_frame = ComponentsFrame(self, logger, self.stub)
        self.components_frame.pack(fill="both", expand=True, pady=(5, 20), padx=20)

        # # Add the buttons frame
        # self.buttons_frame = ButtonsFrame(self, self.stub)
        # self.buttons_frame.pack(pady=20)
