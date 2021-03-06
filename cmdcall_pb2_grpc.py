# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cmdcall_pb2 as cmdcall__pb2


class CmdCallStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Call = channel.unary_unary(
        '/cmdcall.CmdCall/Call',
        request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
        response_deserializer=cmdcall__pb2.CallResponse.FromString,
        )


class CmdCallServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Call(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CmdCallServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Call': grpc.unary_unary_rpc_method_handler(
          servicer.Call,
          request_deserializer=cmdcall__pb2.CallRequest.FromString,
          response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cmdcall.CmdCall', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
