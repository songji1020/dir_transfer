# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='file.proto',
  package='filerebuild',
  syntax='proto3',
  serialized_pb=_b('\n\nfile.proto\x12\x0b\x66ilerebuild\"H\n\x0f\x46ileInfoRequest\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\"?\n\x0c\x46ileResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\t\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t2S\n\nWiriteFile\x12\x45\n\x08SendFile\x12\x1c.filerebuild.FileInfoRequest\x1a\x19.filerebuild.FileResponse\"\x00\x62\x06proto3')
)




_FILEINFOREQUEST = _descriptor.Descriptor(
  name='FileInfoRequest',
  full_name='filerebuild.FileInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_path', full_name='filerebuild.FileInfoRequest.file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='filerebuild.FileInfoRequest.file_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='filerebuild.FileInfoRequest.content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=99,
)


_FILERESPONSE = _descriptor.Descriptor(
  name='FileResponse',
  full_name='filerebuild.FileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='filerebuild.FileResponse.ret_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='filerebuild.FileResponse.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='filerebuild.FileResponse.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['FileInfoRequest'] = _FILEINFOREQUEST
DESCRIPTOR.message_types_by_name['FileResponse'] = _FILERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileInfoRequest = _reflection.GeneratedProtocolMessageType('FileInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _FILEINFOREQUEST,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:filerebuild.FileInfoRequest)
  ))
_sym_db.RegisterMessage(FileInfoRequest)

FileResponse = _reflection.GeneratedProtocolMessageType('FileResponse', (_message.Message,), dict(
  DESCRIPTOR = _FILERESPONSE,
  __module__ = 'file_pb2'
  # @@protoc_insertion_point(class_scope:filerebuild.FileResponse)
  ))
_sym_db.RegisterMessage(FileResponse)



_WIRITEFILE = _descriptor.ServiceDescriptor(
  name='WiriteFile',
  full_name='filerebuild.WiriteFile',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=166,
  serialized_end=249,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendFile',
    full_name='filerebuild.WiriteFile.SendFile',
    index=0,
    containing_service=None,
    input_type=_FILEINFOREQUEST,
    output_type=_FILERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WIRITEFILE)

DESCRIPTOR.services_by_name['WiriteFile'] = _WIRITEFILE

# @@protoc_insertion_point(module_scope)
