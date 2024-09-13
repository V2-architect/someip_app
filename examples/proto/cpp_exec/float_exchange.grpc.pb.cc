// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: float_exchange.proto

#include "float_exchange.pb.h"
#include "float_exchange.grpc.pb.h"

#include <functional>
#include <grpcpp/impl/codegen/async_stream.h>
#include <grpcpp/impl/codegen/async_unary_call.h>
#include <grpcpp/impl/codegen/channel_interface.h>
#include <grpcpp/impl/codegen/client_unary_call.h>
#include <grpcpp/impl/codegen/client_callback.h>
#include <grpcpp/impl/codegen/method_handler_impl.h>
#include <grpcpp/impl/codegen/rpc_service_method.h>
#include <grpcpp/impl/codegen/service_type.h>
#include <grpcpp/impl/codegen/sync_stream.h>
namespace floatexchange {

static const char* FloatExchange_method_names[] = {
  "/floatexchange.FloatExchange/SendFloats",
};

std::unique_ptr< FloatExchange::Stub> FloatExchange::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  (void)options;
  std::unique_ptr< FloatExchange::Stub> stub(new FloatExchange::Stub(channel));
  return stub;
}

FloatExchange::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel)
  : channel_(channel), rpcmethod_SendFloats_(FloatExchange_method_names[0], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status FloatExchange::Stub::SendFloats(::grpc::ClientContext* context, const ::floatexchange::FloatRequest& request, ::floatexchange::FloatResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_SendFloats_, context, request, response);
}

void FloatExchange::Stub::experimental_async::SendFloats(::grpc::ClientContext* context, const ::floatexchange::FloatRequest* request, ::floatexchange::FloatResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_SendFloats_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::floatexchange::FloatResponse>* FloatExchange::Stub::AsyncSendFloatsRaw(::grpc::ClientContext* context, const ::floatexchange::FloatRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::floatexchange::FloatResponse>::Create(channel_.get(), cq, rpcmethod_SendFloats_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::floatexchange::FloatResponse>* FloatExchange::Stub::PrepareAsyncSendFloatsRaw(::grpc::ClientContext* context, const ::floatexchange::FloatRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::floatexchange::FloatResponse>::Create(channel_.get(), cq, rpcmethod_SendFloats_, context, request, false);
}

FloatExchange::Service::Service() {
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      FloatExchange_method_names[0],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< FloatExchange::Service, ::floatexchange::FloatRequest, ::floatexchange::FloatResponse>(
          std::mem_fn(&FloatExchange::Service::SendFloats), this)));
}

FloatExchange::Service::~Service() {
}

::grpc::Status FloatExchange::Service::SendFloats(::grpc::ServerContext* context, const ::floatexchange::FloatRequest* request, ::floatexchange::FloatResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace floatexchange
