// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: float_exchange.proto

#ifndef PROTOBUF_INCLUDED_float_5fexchange_2eproto
#define PROTOBUF_INCLUDED_float_5fexchange_2eproto

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3006001
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3006001 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#define PROTOBUF_INTERNAL_EXPORT_protobuf_float_5fexchange_2eproto 

namespace protobuf_float_5fexchange_2eproto {
// Internal implementation detail -- do not use these members.
struct TableStruct {
  static const ::google::protobuf::internal::ParseTableField entries[];
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[];
  static const ::google::protobuf::internal::ParseTable schema[2];
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors();
}  // namespace protobuf_float_5fexchange_2eproto
namespace floatexchange {
class FloatRequest;
class FloatRequestDefaultTypeInternal;
extern FloatRequestDefaultTypeInternal _FloatRequest_default_instance_;
class FloatResponse;
class FloatResponseDefaultTypeInternal;
extern FloatResponseDefaultTypeInternal _FloatResponse_default_instance_;
}  // namespace floatexchange
namespace google {
namespace protobuf {
template<> ::floatexchange::FloatRequest* Arena::CreateMaybeMessage<::floatexchange::FloatRequest>(Arena*);
template<> ::floatexchange::FloatResponse* Arena::CreateMaybeMessage<::floatexchange::FloatResponse>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace floatexchange {

// ===================================================================

class FloatRequest : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:floatexchange.FloatRequest) */ {
 public:
  FloatRequest();
  virtual ~FloatRequest();

  FloatRequest(const FloatRequest& from);

  inline FloatRequest& operator=(const FloatRequest& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  FloatRequest(FloatRequest&& from) noexcept
    : FloatRequest() {
    *this = ::std::move(from);
  }

  inline FloatRequest& operator=(FloatRequest&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const FloatRequest& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const FloatRequest* internal_default_instance() {
    return reinterpret_cast<const FloatRequest*>(
               &_FloatRequest_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  void Swap(FloatRequest* other);
  friend void swap(FloatRequest& a, FloatRequest& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline FloatRequest* New() const final {
    return CreateMaybeMessage<FloatRequest>(NULL);
  }

  FloatRequest* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<FloatRequest>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const FloatRequest& from);
  void MergeFrom(const FloatRequest& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(FloatRequest* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // float num1 = 1;
  void clear_num1();
  static const int kNum1FieldNumber = 1;
  float num1() const;
  void set_num1(float value);

  // float num2 = 2;
  void clear_num2();
  static const int kNum2FieldNumber = 2;
  float num2() const;
  void set_num2(float value);

  // float num3 = 3;
  void clear_num3();
  static const int kNum3FieldNumber = 3;
  float num3() const;
  void set_num3(float value);

  // @@protoc_insertion_point(class_scope:floatexchange.FloatRequest)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  float num1_;
  float num2_;
  float num3_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::protobuf_float_5fexchange_2eproto::TableStruct;
};
// -------------------------------------------------------------------

class FloatResponse : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:floatexchange.FloatResponse) */ {
 public:
  FloatResponse();
  virtual ~FloatResponse();

  FloatResponse(const FloatResponse& from);

  inline FloatResponse& operator=(const FloatResponse& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  FloatResponse(FloatResponse&& from) noexcept
    : FloatResponse() {
    *this = ::std::move(from);
  }

  inline FloatResponse& operator=(FloatResponse&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor();
  static const FloatResponse& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const FloatResponse* internal_default_instance() {
    return reinterpret_cast<const FloatResponse*>(
               &_FloatResponse_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  void Swap(FloatResponse* other);
  friend void swap(FloatResponse& a, FloatResponse& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline FloatResponse* New() const final {
    return CreateMaybeMessage<FloatResponse>(NULL);
  }

  FloatResponse* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<FloatResponse>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const FloatResponse& from);
  void MergeFrom(const FloatResponse& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(FloatResponse* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // float result1 = 1;
  void clear_result1();
  static const int kResult1FieldNumber = 1;
  float result1() const;
  void set_result1(float value);

  // float result2 = 2;
  void clear_result2();
  static const int kResult2FieldNumber = 2;
  float result2() const;
  void set_result2(float value);

  // float result3 = 3;
  void clear_result3();
  static const int kResult3FieldNumber = 3;
  float result3() const;
  void set_result3(float value);

  // @@protoc_insertion_point(class_scope:floatexchange.FloatResponse)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  float result1_;
  float result2_;
  float result3_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::protobuf_float_5fexchange_2eproto::TableStruct;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// FloatRequest

// float num1 = 1;
inline void FloatRequest::clear_num1() {
  num1_ = 0;
}
inline float FloatRequest::num1() const {
  // @@protoc_insertion_point(field_get:floatexchange.FloatRequest.num1)
  return num1_;
}
inline void FloatRequest::set_num1(float value) {
  
  num1_ = value;
  // @@protoc_insertion_point(field_set:floatexchange.FloatRequest.num1)
}

// float num2 = 2;
inline void FloatRequest::clear_num2() {
  num2_ = 0;
}
inline float FloatRequest::num2() const {
  // @@protoc_insertion_point(field_get:floatexchange.FloatRequest.num2)
  return num2_;
}
inline void FloatRequest::set_num2(float value) {
  
  num2_ = value;
  // @@protoc_insertion_point(field_set:floatexchange.FloatRequest.num2)
}

// float num3 = 3;
inline void FloatRequest::clear_num3() {
  num3_ = 0;
}
inline float FloatRequest::num3() const {
  // @@protoc_insertion_point(field_get:floatexchange.FloatRequest.num3)
  return num3_;
}
inline void FloatRequest::set_num3(float value) {
  
  num3_ = value;
  // @@protoc_insertion_point(field_set:floatexchange.FloatRequest.num3)
}

// -------------------------------------------------------------------

// FloatResponse

// float result1 = 1;
inline void FloatResponse::clear_result1() {
  result1_ = 0;
}
inline float FloatResponse::result1() const {
  // @@protoc_insertion_point(field_get:floatexchange.FloatResponse.result1)
  return result1_;
}
inline void FloatResponse::set_result1(float value) {
  
  result1_ = value;
  // @@protoc_insertion_point(field_set:floatexchange.FloatResponse.result1)
}

// float result2 = 2;
inline void FloatResponse::clear_result2() {
  result2_ = 0;
}
inline float FloatResponse::result2() const {
  // @@protoc_insertion_point(field_get:floatexchange.FloatResponse.result2)
  return result2_;
}
inline void FloatResponse::set_result2(float value) {
  
  result2_ = value;
  // @@protoc_insertion_point(field_set:floatexchange.FloatResponse.result2)
}

// float result3 = 3;
inline void FloatResponse::clear_result3() {
  result3_ = 0;
}
inline float FloatResponse::result3() const {
  // @@protoc_insertion_point(field_get:floatexchange.FloatResponse.result3)
  return result3_;
}
inline void FloatResponse::set_result3(float value) {
  
  result3_ = value;
  // @@protoc_insertion_point(field_set:floatexchange.FloatResponse.result3)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace floatexchange

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_INCLUDED_float_5fexchange_2eproto
