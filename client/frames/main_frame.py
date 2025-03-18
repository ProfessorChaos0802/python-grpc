import tkinter as tk
from .buttons_frame import ButtonsFrame

class MainFrame(tk.Frame):
    def __init__(self, parent, stub):
        super().__init__(parent)

        # Label at the top
        self.label = tk.Label(self, text="Welcome to gRPC Client UI", font=("Arial", 14))
        self.label.pack(pady=10)

        # Assign gRPC Stub
        self.stub = stub

        # Add the buttons frame
        self.buttons_frame = ButtonsFrame(self, self.stub)
        self.buttons_frame.pack(pady=20)
