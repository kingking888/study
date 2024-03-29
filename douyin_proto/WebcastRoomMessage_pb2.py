# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WebcastRoomMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WebcastRoomMessage.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18WebcastRoomMessage.proto\"J\n\x12WebcastRoomMessage\x12!\n\x0bmessageInfo\x18\x01 \x01(\x0b\x32\x0c.MessageInfo\x12\x11\n\tmsgDetail\x18\x02 \x01(\t\"S\n\x0bMessageInfo\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x11\n\tmessageId\x18\x02 \x01(\x03\x12\x0e\n\x06roomId\x18\x03 \x01(\x03\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x62\x06proto3'
)




_WEBCASTROOMMESSAGE = _descriptor.Descriptor(
  name='WebcastRoomMessage',
  full_name='WebcastRoomMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messageInfo', full_name='WebcastRoomMessage.messageInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msgDetail', full_name='WebcastRoomMessage.msgDetail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=28,
  serialized_end=102,
)


_MESSAGEINFO = _descriptor.Descriptor(
  name='MessageInfo',
  full_name='MessageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='MessageInfo.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messageId', full_name='MessageInfo.messageId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roomId', full_name='MessageInfo.roomId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='MessageInfo.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=104,
  serialized_end=187,
)

_WEBCASTROOMMESSAGE.fields_by_name['messageInfo'].message_type = _MESSAGEINFO
DESCRIPTOR.message_types_by_name['WebcastRoomMessage'] = _WEBCASTROOMMESSAGE
DESCRIPTOR.message_types_by_name['MessageInfo'] = _MESSAGEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebcastRoomMessage = _reflection.GeneratedProtocolMessageType('WebcastRoomMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTROOMMESSAGE,
  '__module__' : 'WebcastRoomMessage_pb2'
  # @@protoc_insertion_point(class_scope:WebcastRoomMessage)
  })
_sym_db.RegisterMessage(WebcastRoomMessage)

MessageInfo = _reflection.GeneratedProtocolMessageType('MessageInfo', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEINFO,
  '__module__' : 'WebcastRoomMessage_pb2'
  # @@protoc_insertion_point(class_scope:MessageInfo)
  })
_sym_db.RegisterMessage(MessageInfo)


# @@protoc_insertion_point(module_scope)
