import grpc
from concurrent import futures
import float_exchange_pb2
import float_exchange_pb2_grpc
import random



class FloatExchangeServicer(float_exchange_pb2_grpc.FloatExchangeServicer):
    def SendFloats(self, request, context):
        print(f"Received: {request.num1}, {request.num2}, {request.num3}")
        return float_exchange_pb2.FloatResponse(
            result1=request.num1,
            result2=request.num2,
            result3=request.num3
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    float_exchange_pb2_grpc.add_FloatExchangeServicer_to_server(FloatExchangeServicer(), server)
    
    port = 30000
    server_address = f'172.17.0.9:{port}'
    server.add_insecure_port(server_address)
    print(f"Server starting on {server_address}")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

