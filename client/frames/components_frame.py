from tkinter import ttk
from .req_rep_frame import ReqRepFrame

class ComponentsFrame(ttk.Frame):
    """
    Components Frame

    Frame for all the UI components
    """
    def __init__(self, parent, logger, stub):
        super().__init__(parent, style="Components.TFrame")

        # Assign gRPC Stub
        self.stub = stub

        # ReqRep Frame
        self.f1 = ReqRepFrame(self, logger, self.stub)
        self.f1.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

        self.f2 = ReqRepFrame(self, logger, self.stub)
        self.f2.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

        self.f3 = ReqRepFrame(self, logger, self.stub)
        self.f3.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

        self.f4 = ReqRepFrame(self, logger, self.stub)
        self.f4.grid(row=1, column=1, sticky="nsew", pady=10, padx=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

