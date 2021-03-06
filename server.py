# coding=utf-8
import os
import socket
import subprocess
import sys
import threading
import time
import traceback
from concurrent import futures
from json import dumps
from threading import Thread

import grpc

from util import runCmd, get_IP

sys.path.append('%s/' % os.path.dirname(os.path.realpath(__file__)))

import cmdcall_pb2, cmdcall_pb2_grpc  # 刚刚生产的两个文件

DEFAULT_PORT = '19999'


class Operation(object):
    def __init__(self, cmd, params, with_result=False, xml_to_json=False, kv_to_json=False):
        if cmd is None or cmd == "":
            raise Exception("plz give me right cmd.")
        if not isinstance(params, dict):
            raise Exception("plz give me right parameters.")

        self.params = params
        self.cmd = cmd
        self.params = params
        self.with_result = with_result
        self.xml_to_json = xml_to_json
        self.kv_to_json = kv_to_json

    def get_cmd(self):
        cmd = self.cmd
        for key in self.params.keys():
            cmd = "%s --%s %s " % (cmd, key, self.params[key])
        return cmd

    def execute(self):
        cmd = self.get_cmd()
        return runCmd(cmd)


class CmdCallServicer(cmdcall_pb2_grpc.CmdCallServicer):

    def Call(self, request, ctx):
        try:
            cmd = str(request.cmd)
            print(cmd)
            op = Operation(cmd, {})
            lines = op.execute()
            if lines:
                return cmdcall_pb2.CallResponse(output=dumps(lines))
            else:
                return cmdcall_pb2.CallResponse(output="[]")
        except Exception:
            traceback.print_exc()
            return cmdcall_pb2.CallResponse(output=traceback.format_exc())

def run_server():
    # 多线程服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 实例化 计算len的类
    servicer = CmdCallServicer()
    # 注册本地服务,方法CmdCallServicer只有这个是变的
    cmdcall_pb2_grpc.add_CmdCallServicer_to_server(servicer, server)
    # 监听端口
    print("%s:%s" % (get_IP(), DEFAULT_PORT))
    server.add_insecure_port("%s:%s" % (get_IP(), DEFAULT_PORT))
    # 开始接收请求进行服务
    server.start()
    return server
    # 使用 ctrl+c 可以退出服务
    # try:
    #     print("rpc server running...")
    #     time.sleep(1000)
    # except KeyboardInterrupt:
    #     print("rpc server stopping...")
    #     server.stop(0)


def keep_alive():
    server = run_server()
    while True:
        time.sleep(5)
    # while True:
    #     output = None
    #     try:
    #         output = runCmdAndGetOutput('netstat -anp|grep %s:%s' % (get_docker0_IP(), DEFAULT_PORT))
    #     except ExecuteException:
    #         logger.debug(traceback.format_exc())
    #     if output is not None and output.find('%s:%s' % (get_docker0_IP(), DEFAULT_PORT)) >= 0:
    #         # logger.debug("port 19999 is alive")
    #         pass
    #     else:
    #         # try stop server
    #         try:
    #             server.stop(0)
    #         except Exception:
    #             logger.debug(traceback.format_exc())
    #         # restart server
    #         server = run_server()
    #         logger.debug("restart port %s..." % DEFAULT_PORT)
    #     time.sleep(1)



if __name__ == '__main__':
    keep_alive()
