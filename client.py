import json
import os
import traceback
import grpc

import cmdcall_pb2
import cmdcall_pb2_grpc

from util import *

DEFAULT_PORT = '19350'
HOST = '133.133.135.22'
def rpcCall(cmd, host=HOST, port=DEFAULT_PORT):
    print(host)
    print(port)
    try:
        channel = grpc.insecure_channel("{0}:{1}".format(host, port))
        client = cmdcall_pb2_grpc.CmdCallStub(channel)
        # ideally, you should have try catch block here too
        response = client.Call(cmdcall_pb2.CallRequest(cmd=cmd))
        return response.output
    except grpc.RpcError as e:
        traceback.print_exc()
        # ouch!
        # lets print the gRPC error message
        # which is "Length of `Name` cannot be more than 10 characters"

        # print(e.details())
        # lets access the error code, which is `INVALID_ARGUMENT`
        # `type` of `status_code` is `grpc.StatusCode`
        # status_code = e.code()
        # should print `INVALID_ARGUMENT`
        # logger.debug(status_code.name)
        # should print `(3, 'invalid argument')`
        # logger.debug(status_code.value)
        # want to do some specific action based on the error?
        # if grpc.StatusCode.INVALID_ARGUMENT == status_code:
        #     # do your stuff here
        #     pass
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    print(rpcCall('ls /', host='133.133.135.22', port='19350'))