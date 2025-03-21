from tkinter import ttk
import tkinter as tk
from proto import simple_server_pb2

class ReqRepFrame(ttk.Frame):
    """
    ReqRep Frame

    Frame for all the gRPC Request-Response Example
    """
    def __init__(self, parent, logger, stub):
        super().__init__(parent, style="ReqRep.TFrame")

        # Create a Canvas widget to hold the scrollable content
        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # Create a vertical scrollbar linked to the canvas
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # Link the scrollbar to the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas for adding widgets
        self.frame = ttk.Frame(self.canvas)

        # Create a window in the canvas to hold the frame
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # Update the scroll region whenever the frame's size changes
        self.frame.bind("<Configure>", self.on_frame_configure)

        # Assign gRPC Stub
        self.stub = stub

        # Button 2
        self.button2 = ttk.Button(self.frame, text="Send Request", command=self.send_request)
        self.button2.grid(row=0, column=0, sticky="nw", padx=10)

        self.label = ttk.Label(self.frame, text="Response:", width=250, wraplength=1)
        self.label.grid(row=0, column=1, padx=10)

        # Configure row/column to expand with window resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

    def send_request(self):
        response = self.stub.GetText(simple_server_pb2.SimpleMessage(message="Hello World!"))

        print("Sending gRPC request...")
        print(f"Response: {response.message}")

        self.label.config(text=f"Response: {response.message}")

        return response.message

    def on_frame_configure(self, event):
        # Update the scrollable region of the canvas
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
