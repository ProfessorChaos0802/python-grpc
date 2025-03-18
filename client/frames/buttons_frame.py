import tkinter as tk
from proto import simple_server_pb2

class ButtonsFrame(tk.Frame):
    def __init__(self, parent, stub):
        super().__init__(parent)

        # gRPC stub
        self.stub = stub

        # Button 1
        self.button1 = tk.Button(self, text="Connect", command=self.connect)
        self.button1.pack(side="left", padx=10)

        # Button 2
        self.button2 = tk.Button(self, text="Send Request", command=self.send_request)
        self.button2.pack(side="left", padx=10)

    def connect(self):
        print("Connecting to gRPC server...")

    def send_request(self):
        response = self.stub.GetText(simple_server_pb2.SimpleMessage(message="Hello World!"))

        print("Sending gRPC request...")
        print(f"Response: {response.message}")