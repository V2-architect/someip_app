import grpc
from concurrent import futures
import float_exchange_pb2
import float_exchange_pb2_grpc
import threading
import time
import random

# 전역변수 설정
float_var1 = 0.0
float_var2 = 0.0
float_var3 = 0.0

# 락 설정 (동시성 제어)
lock = threading.Lock()

# 서비스 구현
class FloatExchangeServicer(float_exchange_pb2_grpc.FloatExchangeServicer):
    def SendFloats(self, request, context):
        global float_var1, float_var2, float_var3
        print(f"Received: {request.num1}, {request.num2}, {request.num3}")

        # 새로운 스레드에서 전역 변수에 쓰기 작업
        def update_floats():
            global float_var1, float_var2, float_var3
            with lock:
                float_var1 = request.num1
                float_var2 = request.num2
                float_var3 = request.num3
            print("Updated global float variables.")
        
        # 스레드 생성하여 값 갱신
        threading.Thread(target=update_floats).start()

        return float_exchange_pb2.FloatResponse(
            result1=request.num1,
            result2=request.num2,
            result3=request.num3
        )

# 1초에 한번 전역변수 출력하는 스레드
def print_floats():
    global float_var1, float_var2, float_var3
    while True:
        with lock:
            print(f"Current float values: {float_var1}, {float_var2}, {float_var3}")
        time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    float_exchange_pb2_grpc.add_FloatExchangeServicer_to_server(FloatExchangeServicer(), server)
    
    # 랜덤 포트 사용
    port = 30000
    server_address = f'172.17.0.9:{port}'
    server.add_insecure_port(server_address)
    print(f"Server starting on {server_address}")
    
    # 스레드 생성: 전역변수 출력하는 스레드
    print_thread = threading.Thread(target=print_floats)
    print_thread.daemon = True  # 데몬 스레드로 설정
    print_thread.start()
    
    # 서버 시작
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
