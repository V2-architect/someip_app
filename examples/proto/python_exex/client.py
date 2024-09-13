import grpc
import float_exchange_pb2
import float_exchange_pb2_grpc
import random
import time

def run():
    # 컨테이너가 실행 중인 IP 주소 및 랜덤 포트 설정
    host_ip = '172.17.0.9'
    port = 30000
    target = f'{host_ip}:{port}'

    n1 = 1.123
    n2 = 2.123
    n3 = 3.123
    
    # gRPC 채널 생성
    with grpc.insecure_channel(target) as channel:
        while True:
            stub = float_exchange_pb2_grpc.FloatExchangeStub(channel)
            
            # 요청할 float 값 3개 설정
            request = float_exchange_pb2.FloatRequest(
                num1=n1, num2=n2, num3=n3)
            start_time = time.time()
            
            # 서버에 요청 보내기
            response = stub.SendFloats(request)
            end_time = time.time()
            rtt = end_time - start_time

            print(f"Response: {response.result1}, {response.result2}, {response.result3}")
            print(f"RTT: {rtt * 1000:.2f} ms")  # RTT를 밀리초 단위로 출력

            time.sleep(1)

            n1 += 1
            n2 += 1
            n3 += 1

if __name__ == '__main__':
    run()

