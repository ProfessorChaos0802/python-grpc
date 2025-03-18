from concurrent import futures
import logging
import random

import grpc
from proto import simple_server_pb2
from proto import simple_server_pb2_grpc

class SimpleServerServicer(simple_server_pb2_grpc.SimpleServerServicer):

    def __init__(self):
        pass

    def GetText(self, request, context):
        return simple_server_pb2.SimpleMessage(message=f"Hello World! Here is a random number {random.randint(1,50)}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simple_server_pb2_grpc.add_SimpleServerServicer_to_server(SimpleServerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()