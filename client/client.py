import grpc
import tkinter as tk

from frames import MainFrame
from config import Logger
from proto import simple_server_pb2_grpc
from config.get_config import get_config
from lib.log_config import log_config
from lib.styles import set_styles


class App(tk.Tk):
    """
    Main Application
    """
    def __init__(self, config, logger):
        super().__init__()
        self.title(config['general']['title'])
        self.geometry(f"{int(config['general']['window_width'])}x{int(config['general']['window_height'])}")
        self.resizable(True, True)

        # Set styles
        set_styles(config)

        # Create the gRPC channel
        logger.info("Creating gRPC channel...")
        self.channel = grpc.insecure_channel(f"{config['general']['grpc_host']}:{config['general']['grpc_port']}")
        self.stub = simple_server_pb2_grpc.SimpleServerStub(self.channel)
        logger.info(f"Created gRPC channel to {config['general']['grpc_host']}:{config['general']['grpc_port']}")

        # Create the main frame
        self.main_frame = MainFrame(self, logger, self.stub)
        self.main_frame.pack(fill="both", expand=True, padx=0, pady=0)

if __name__ == "__main__":
    # Setup Configuration and Logging
    client_config = get_config()

    client_logger = Logger(client_config)
    log_config(client_logger, client_config)

    # Start App
    app = App(client_config, client_logger)
    app.mainloop()