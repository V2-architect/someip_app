#include <grpcpp/grpcpp.h>
#include <float_exchange.grpc.pb.h>
#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>

// 전역변수
float float_var1 = 0.0;
float float_var2 = 0.0;
float float_var3 = 0.0;

// 락 설정 (동시성 제어)
std::mutex mtx;

// 서비스 구현
class FloatExchangeServiceImpl final : public floatexchange::FloatExchange::Service {
public:
    grpc::Status SendFloats(grpc::ServerContext* context, const floatexchange::FloatRequest* request, floatexchange::FloatResponse* response) override {
        std::cout << "Received: " << request->num1() << ", " << request->num2() << ", " << request->num3() << std::endl;

        // 전역 변수 업데이트 작업을 스레드로 처리
        std::thread update_thread([request]() {
            std::lock_guard<std::mutex> lock(mtx);
            float_var1 = request->num1();
            float_var2 = request->num2();
            float_var3 = request->num3();
            std::cout << "Updated global float variables." << std::endl;
        });
        update_thread.detach();

        response->set_result1(request->num1());
        response->set_result2(request->num2());
        response->set_result3(request->num3());
        return grpc::Status::OK;
    }
};

// 1초마다 전역변수 출력하는 스레드
void PrintFloats() {
    while (true) {
        std::this_thread::sleep_for(std::chrono::seconds(1));
        std::lock_guard<std::mutex> lock(mtx);
        std::cout << "Current float values: " << float_var1 << ", " << float_var2 << ", " << float_var3 << std::endl;
    }
}

int main(int argc, char** argv) {
    std::string server_address("0.0.0.0:50051");
    FloatExchangeServiceImpl service;

    grpc::ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr<grpc::Server> server(builder.BuildAndStart());

    std::cout << "Server listening on " << server_address << std::endl;

    // 스레드 생성: 전역변수 출력하는 스레드
    std::thread print_thread(PrintFloats);
    print_thread.detach();

    server->Wait();
    return 0;
}
