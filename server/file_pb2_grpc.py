# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import file_pb2 as file__pb2


class WiriteFileStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendFile = channel.unary_unary(
        '/filerebuild.WiriteFile/SendFile',
        request_serializer=file__pb2.FileInfoRequest.SerializeToString,
        response_deserializer=file__pb2.FileResponse.FromString,
        )


class WiriteFileServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SendFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WiriteFileServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendFile': grpc.unary_unary_rpc_method_handler(
          servicer.SendFile,
          request_deserializer=file__pb2.FileInfoRequest.FromString,
          response_serializer=file__pb2.FileResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'filerebuild.WiriteFile', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
