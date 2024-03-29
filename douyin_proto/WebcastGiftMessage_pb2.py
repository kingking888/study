# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WebcastGiftMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WebcastGiftMessage.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18WebcastGiftMessage.proto\"\x80\x01\n\x12WebcastGiftMessage\x12\'\n\rgift_msg_desc\x18\x01 \x01(\x0b\x32\x10.GiftMessageDesc\x12\x0f\n\x07gift_id\x18\x02 \x01(\x05\x12\x11\n\tgift_nums\x18\x04 \x01(\x05\x12\x1d\n\x0egift_user_info\x18\x07 \x01(\x0b\x32\x05.User\"\xb4\x05\n\x0fGiftMessageDesc\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x11\n\tmessageId\x18\x02 \x01(\x03\x12\x0e\n\x06roomId\x18\x03 \x01(\x03\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\x12,\n\tgift_info\x18\x08 \x01(\x0b\x32\x19.GiftMessageDesc.GiftInfo\x1a\x9b\x04\n\x08GiftInfo\x12>\n\x0egift_user_info\x18\x04 \x03(\x0b\x32&.GiftMessageDesc.GiftInfo.GiftUserInfo\x1a\xce\x03\n\x0cGiftUserInfo\x12\x42\n\tuser_info\x18\x15 \x01(\x0b\x32/.GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo\x12\x42\n\tgift_info\x18\x16 \x01(\x0b\x32/.GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo\x1a\x93\x01\n\x08UserInfo\x12O\n\x0buser_detail\x18\x01 \x01(\x0b\x32:.GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo.UserDetail\x1a\x36\n\nUserDetail\x12\x0b\n\x03uid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x64y_id\x18& \x01(\t\x1a\x9f\x01\n\x08GiftInfo\x12\x0e\n\x06giftId\x18\x01 \x01(\x05\x12O\n\x0bgift_deatil\x18\x02 \x01(\x0b\x32:.GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo.GiftDetail\x1a\x32\n\nGiftDetail\x12\x11\n\tgift_desc\x18\x01 \x01(\t\x12\x11\n\tgift_name\x18\x02 \x01(\t\"\x95\x04\n\x04User\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x10\n\x08short_id\x18\x02 \x01(\x03\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\x0e\n\x06gender\x18\x04 \x01(\x05\x12!\n\thead_info\x18\t \x01(\x0b\x32\x0e.User.HeadInfo\x12\"\n\tlevelInfo\x18\x15 \x01(\x0b\x32\x0f.User.LevelInfo\x12 \n\x08userInfo\x18\x16 \x01(\x0b\x32\x0e.User.UserInfo\x12&\n\x0blevelDetail\x18\x17 \x01(\x0b\x32\x11.User.LevelDetail\x12\r\n\x05\x64y_id\x18& \x01(\t\x12\x0f\n\x07sec_uid\x18. \x01(\t\x1a\x1b\n\x08HeadInfo\x12\x0f\n\x07headImg\x18\x01 \x03(\t\x1a\x1d\n\tLevelInfo\x12\x10\n\x08levelImg\x18\x01 \x03(\t\x1a\x1f\n\x0bLevelDetail\x12\x10\n\x08levelNum\x18\x06 \x01(\x05\x1a\x8c\x01\n\x0c\x46\x61nsCardInfo\x12\x14\n\x0c\x66\x61nsLevelImg\x18\x01 \x03(\t\x12-\n\ncardFormat\x18\x08 \x01(\x0b\x32\x19.User.FansCardInfo.format\x1a\x37\n\x06\x66ormat\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x05\x1a/\n\x08UserInfo\x12\x12\n\nfollowNums\x18\x01 \x01(\x05\x12\x0f\n\x07\x66\x61nsNum\x18\x02 \x01(\x05\x62\x06proto3'
)




_WEBCASTGIFTMESSAGE = _descriptor.Descriptor(
  name='WebcastGiftMessage',
  full_name='WebcastGiftMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gift_msg_desc', full_name='WebcastGiftMessage.gift_msg_desc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='WebcastGiftMessage.gift_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gift_nums', full_name='WebcastGiftMessage.gift_nums', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gift_user_info', full_name='WebcastGiftMessage.gift_user_info', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=29,
  serialized_end=157,
)


_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO_USERDETAIL = _descriptor.Descriptor(
  name='UserDetail',
  full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo.UserDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo.UserDetail.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo.UserDetail.name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dy_id', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo.UserDetail.dy_id', index=2,
      number=38, type=9, cpp_type=9, label=1,
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
  serialized_start=636,
  serialized_end=690,
)

_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_detail', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo.user_detail', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO_USERDETAIL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=543,
  serialized_end=690,
)

_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO_GIFTDETAIL = _descriptor.Descriptor(
  name='GiftDetail',
  full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo.GiftDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gift_desc', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo.GiftDetail.gift_desc', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gift_name', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo.GiftDetail.gift_name', index=1,
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
  serialized_start=802,
  serialized_end=852,
)

_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO = _descriptor.Descriptor(
  name='GiftInfo',
  full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='giftId', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo.giftId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gift_deatil', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo.gift_deatil', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO_GIFTDETAIL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=852,
)

_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO = _descriptor.Descriptor(
  name='GiftUserInfo',
  full_name='GiftMessageDesc.GiftInfo.GiftUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.user_info', index=0,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gift_info', full_name='GiftMessageDesc.GiftInfo.GiftUserInfo.gift_info', index=1,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO, _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=852,
)

_GIFTMESSAGEDESC_GIFTINFO = _descriptor.Descriptor(
  name='GiftInfo',
  full_name='GiftMessageDesc.GiftInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gift_user_info', full_name='GiftMessageDesc.GiftInfo.gift_user_info', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=852,
)

_GIFTMESSAGEDESC = _descriptor.Descriptor(
  name='GiftMessageDesc',
  full_name='GiftMessageDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='GiftMessageDesc.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messageId', full_name='GiftMessageDesc.messageId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roomId', full_name='GiftMessageDesc.roomId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='GiftMessageDesc.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='GiftMessageDesc.content', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gift_info', full_name='GiftMessageDesc.gift_info', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GIFTMESSAGEDESC_GIFTINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=852,
)


_USER_HEADINFO = _descriptor.Descriptor(
  name='HeadInfo',
  full_name='User.HeadInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='headImg', full_name='User.HeadInfo.headImg', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1105,
  serialized_end=1132,
)

_USER_LEVELINFO = _descriptor.Descriptor(
  name='LevelInfo',
  full_name='User.LevelInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='levelImg', full_name='User.LevelInfo.levelImg', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1134,
  serialized_end=1163,
)

_USER_LEVELDETAIL = _descriptor.Descriptor(
  name='LevelDetail',
  full_name='User.LevelDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='levelNum', full_name='User.LevelDetail.levelNum', index=0,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=1165,
  serialized_end=1196,
)

_USER_FANSCARDINFO_FORMAT = _descriptor.Descriptor(
  name='format',
  full_name='User.FansCardInfo.format',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='User.FansCardInfo.format.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='User.FansCardInfo.format.color', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='User.FansCardInfo.format.level', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=1284,
  serialized_end=1339,
)

_USER_FANSCARDINFO = _descriptor.Descriptor(
  name='FansCardInfo',
  full_name='User.FansCardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fansLevelImg', full_name='User.FansCardInfo.fansLevelImg', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cardFormat', full_name='User.FansCardInfo.cardFormat', index=1,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_USER_FANSCARDINFO_FORMAT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1199,
  serialized_end=1339,
)

_USER_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='User.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='followNums', full_name='User.UserInfo.followNums', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fansNum', full_name='User.UserInfo.fansNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1341,
  serialized_end=1388,
)

_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='User.uid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='short_id', full_name='User.short_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='User.nickname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gender', full_name='User.gender', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='head_info', full_name='User.head_info', index=4,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='levelInfo', full_name='User.levelInfo', index=5,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='User.userInfo', index=6,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='levelDetail', full_name='User.levelDetail', index=7,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dy_id', full_name='User.dy_id', index=8,
      number=38, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sec_uid', full_name='User.sec_uid', index=9,
      number=46, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_USER_HEADINFO, _USER_LEVELINFO, _USER_LEVELDETAIL, _USER_FANSCARDINFO, _USER_USERINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=1388,
)

_WEBCASTGIFTMESSAGE.fields_by_name['gift_msg_desc'].message_type = _GIFTMESSAGEDESC
_WEBCASTGIFTMESSAGE.fields_by_name['gift_user_info'].message_type = _USER
_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO_USERDETAIL.containing_type = _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO
_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO.fields_by_name['user_detail'].message_type = _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO_USERDETAIL
_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO.containing_type = _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO
_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO_GIFTDETAIL.containing_type = _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO
_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO.fields_by_name['gift_deatil'].message_type = _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO_GIFTDETAIL
_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO.containing_type = _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO
_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO.fields_by_name['user_info'].message_type = _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO
_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO.fields_by_name['gift_info'].message_type = _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO
_GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO.containing_type = _GIFTMESSAGEDESC_GIFTINFO
_GIFTMESSAGEDESC_GIFTINFO.fields_by_name['gift_user_info'].message_type = _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO
_GIFTMESSAGEDESC_GIFTINFO.containing_type = _GIFTMESSAGEDESC
_GIFTMESSAGEDESC.fields_by_name['gift_info'].message_type = _GIFTMESSAGEDESC_GIFTINFO
_USER_HEADINFO.containing_type = _USER
_USER_LEVELINFO.containing_type = _USER
_USER_LEVELDETAIL.containing_type = _USER
_USER_FANSCARDINFO_FORMAT.containing_type = _USER_FANSCARDINFO
_USER_FANSCARDINFO.fields_by_name['cardFormat'].message_type = _USER_FANSCARDINFO_FORMAT
_USER_FANSCARDINFO.containing_type = _USER
_USER_USERINFO.containing_type = _USER
_USER.fields_by_name['head_info'].message_type = _USER_HEADINFO
_USER.fields_by_name['levelInfo'].message_type = _USER_LEVELINFO
_USER.fields_by_name['userInfo'].message_type = _USER_USERINFO
_USER.fields_by_name['levelDetail'].message_type = _USER_LEVELDETAIL
DESCRIPTOR.message_types_by_name['WebcastGiftMessage'] = _WEBCASTGIFTMESSAGE
DESCRIPTOR.message_types_by_name['GiftMessageDesc'] = _GIFTMESSAGEDESC
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebcastGiftMessage = _reflection.GeneratedProtocolMessageType('WebcastGiftMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTGIFTMESSAGE,
  '__module__' : 'WebcastGiftMessage_pb2'
  # @@protoc_insertion_point(class_scope:WebcastGiftMessage)
  })
_sym_db.RegisterMessage(WebcastGiftMessage)

GiftMessageDesc = _reflection.GeneratedProtocolMessageType('GiftMessageDesc', (_message.Message,), {

  'GiftInfo' : _reflection.GeneratedProtocolMessageType('GiftInfo', (_message.Message,), {

    'GiftUserInfo' : _reflection.GeneratedProtocolMessageType('GiftUserInfo', (_message.Message,), {

      'UserInfo' : _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {

        'UserDetail' : _reflection.GeneratedProtocolMessageType('UserDetail', (_message.Message,), {
          'DESCRIPTOR' : _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO_USERDETAIL,
          '__module__' : 'WebcastGiftMessage_pb2'
          # @@protoc_insertion_point(class_scope:GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo.UserDetail)
          })
        ,
        'DESCRIPTOR' : _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_USERINFO,
        '__module__' : 'WebcastGiftMessage_pb2'
        # @@protoc_insertion_point(class_scope:GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo)
        })
      ,

      'GiftInfo' : _reflection.GeneratedProtocolMessageType('GiftInfo', (_message.Message,), {

        'GiftDetail' : _reflection.GeneratedProtocolMessageType('GiftDetail', (_message.Message,), {
          'DESCRIPTOR' : _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO_GIFTDETAIL,
          '__module__' : 'WebcastGiftMessage_pb2'
          # @@protoc_insertion_point(class_scope:GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo.GiftDetail)
          })
        ,
        'DESCRIPTOR' : _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO_GIFTINFO,
        '__module__' : 'WebcastGiftMessage_pb2'
        # @@protoc_insertion_point(class_scope:GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo)
        })
      ,
      'DESCRIPTOR' : _GIFTMESSAGEDESC_GIFTINFO_GIFTUSERINFO,
      '__module__' : 'WebcastGiftMessage_pb2'
      # @@protoc_insertion_point(class_scope:GiftMessageDesc.GiftInfo.GiftUserInfo)
      })
    ,
    'DESCRIPTOR' : _GIFTMESSAGEDESC_GIFTINFO,
    '__module__' : 'WebcastGiftMessage_pb2'
    # @@protoc_insertion_point(class_scope:GiftMessageDesc.GiftInfo)
    })
  ,
  'DESCRIPTOR' : _GIFTMESSAGEDESC,
  '__module__' : 'WebcastGiftMessage_pb2'
  # @@protoc_insertion_point(class_scope:GiftMessageDesc)
  })
_sym_db.RegisterMessage(GiftMessageDesc)
_sym_db.RegisterMessage(GiftMessageDesc.GiftInfo)
_sym_db.RegisterMessage(GiftMessageDesc.GiftInfo.GiftUserInfo)
_sym_db.RegisterMessage(GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo)
_sym_db.RegisterMessage(GiftMessageDesc.GiftInfo.GiftUserInfo.UserInfo.UserDetail)
_sym_db.RegisterMessage(GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo)
_sym_db.RegisterMessage(GiftMessageDesc.GiftInfo.GiftUserInfo.GiftInfo.GiftDetail)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {

  'HeadInfo' : _reflection.GeneratedProtocolMessageType('HeadInfo', (_message.Message,), {
    'DESCRIPTOR' : _USER_HEADINFO,
    '__module__' : 'WebcastGiftMessage_pb2'
    # @@protoc_insertion_point(class_scope:User.HeadInfo)
    })
  ,

  'LevelInfo' : _reflection.GeneratedProtocolMessageType('LevelInfo', (_message.Message,), {
    'DESCRIPTOR' : _USER_LEVELINFO,
    '__module__' : 'WebcastGiftMessage_pb2'
    # @@protoc_insertion_point(class_scope:User.LevelInfo)
    })
  ,

  'LevelDetail' : _reflection.GeneratedProtocolMessageType('LevelDetail', (_message.Message,), {
    'DESCRIPTOR' : _USER_LEVELDETAIL,
    '__module__' : 'WebcastGiftMessage_pb2'
    # @@protoc_insertion_point(class_scope:User.LevelDetail)
    })
  ,

  'FansCardInfo' : _reflection.GeneratedProtocolMessageType('FansCardInfo', (_message.Message,), {

    'format' : _reflection.GeneratedProtocolMessageType('format', (_message.Message,), {
      'DESCRIPTOR' : _USER_FANSCARDINFO_FORMAT,
      '__module__' : 'WebcastGiftMessage_pb2'
      # @@protoc_insertion_point(class_scope:User.FansCardInfo.format)
      })
    ,
    'DESCRIPTOR' : _USER_FANSCARDINFO,
    '__module__' : 'WebcastGiftMessage_pb2'
    # @@protoc_insertion_point(class_scope:User.FansCardInfo)
    })
  ,

  'UserInfo' : _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
    'DESCRIPTOR' : _USER_USERINFO,
    '__module__' : 'WebcastGiftMessage_pb2'
    # @@protoc_insertion_point(class_scope:User.UserInfo)
    })
  ,
  'DESCRIPTOR' : _USER,
  '__module__' : 'WebcastGiftMessage_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)
_sym_db.RegisterMessage(User.HeadInfo)
_sym_db.RegisterMessage(User.LevelInfo)
_sym_db.RegisterMessage(User.LevelDetail)
_sym_db.RegisterMessage(User.FansCardInfo)
_sym_db.RegisterMessage(User.FansCardInfo.format)
_sym_db.RegisterMessage(User.UserInfo)


# @@protoc_insertion_point(module_scope)
