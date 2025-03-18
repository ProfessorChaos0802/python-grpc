from concurrent import futures
import logging
import random

import grpc
from proto import simple_server_pb2_grpc
import tkinter as tk
from frames import MainFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("gRPC Powered UI")
        self.geometry("800x600")
        self.resizable(True, True)

        # Create the gRPC channel
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = simple_server_pb2_grpc.SimpleServerStub(self.channel)

        # Create the main frame
        self.main_frame = MainFrame(self, self.stub)
        self.main_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App();
    app.mainloop();