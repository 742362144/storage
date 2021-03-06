# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmdcall.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cmdcall.proto',
  package='cmdcall',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rcmdcall.proto\x12\x07\x63mdcall\"\x1a\n\x0b\x43\x61llRequest\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\"\x1e\n\x0c\x43\x61llResponse\x12\x0e\n\x06output\x18\x01 \x01(\t2@\n\x07\x43mdCall\x12\x35\n\x04\x43\x61ll\x12\x14.cmdcall.CallRequest\x1a\x15.cmdcall.CallResponse\"\x00\x62\x06proto3')
)




_CALLREQUEST = _descriptor.Descriptor(
  name='CallRequest',
  full_name='cmdcall.CallRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='cmdcall.CallRequest.cmd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=52,
)


_CALLRESPONSE = _descriptor.Descriptor(
  name='CallResponse',
  full_name='cmdcall.CallResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='cmdcall.CallResponse.output', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['CallRequest'] = _CALLREQUEST
DESCRIPTOR.message_types_by_name['CallResponse'] = _CALLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CallRequest = _reflection.GeneratedProtocolMessageType('CallRequest', (_message.Message,), {
  'DESCRIPTOR' : _CALLREQUEST,
  '__module__' : 'cmdcall_pb2'
  # @@protoc_insertion_point(class_scope:cmdcall.CallRequest)
  })
_sym_db.RegisterMessage(CallRequest)

CallResponse = _reflection.GeneratedProtocolMessageType('CallResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALLRESPONSE,
  '__module__' : 'cmdcall_pb2'
  # @@protoc_insertion_point(class_scope:cmdcall.CallResponse)
  })
_sym_db.RegisterMessage(CallResponse)



_CMDCALL = _descriptor.ServiceDescriptor(
  name='CmdCall',
  full_name='cmdcall.CmdCall',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=86,
  serialized_end=150,
  methods=[
  _descriptor.MethodDescriptor(
    name='Call',
    full_name='cmdcall.CmdCall.Call',
    index=0,
    containing_service=None,
    input_type=_CALLREQUEST,
    output_type=_CALLRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CMDCALL)

DESCRIPTOR.services_by_name['CmdCall'] = _CMDCALL

# @@protoc_insertion_point(module_scope)
