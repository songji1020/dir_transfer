# coding:utf-8

import os 
import sys
import time
import grpc
from pb import file_pb2, file_pb2_grpc
from concurrent import futures
import json
import ast

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(lines)
        return lines

def write_file(file_name, context_line_list):
    with open(file_name, "w") as wfile:
        for line in context_line_list:
            wfile.write(line)


class fileServer(file_pb2_grpc.WiriteFileServicer):
    def __init__(self, root_path):
        ''' root_path 是目标目录 '''
        self.root_path = root_path

    def write_file(self, file_name, context):
        print("准备存文件:", file_name)
        self.check_path(file_name)
        string = str(context, encoding="utf-8")
        # lines = json.loads(string)
        lines = ast.literal_eval(string)     # 字符串格式的list 转成list
        with open('xxxxx.txt', "wb") as w_file:
            for line in lines:
                w_file.write(line)

    def check_path(self, path:str, root_path):
        ''' 检查路径是否存在 '''
        dir_list = path.split('\\')
        print(dir_list)
        if path[0] == '\\':
            dir_list.pop(0)
        dir_list.pop()
        print(dir_list)

        if len(dir_list):
            # 检查文件夹是否存在
            pass
        pass

    # def dir_exist_or_create(self,):

    # #### 真正重要的-输出函数 #### #
    def SendFile(self, request, context):
        file_path = request.file_path
        file_name = request.file_name
        content = request.content

        print("file_path:", file_path)
        print("file_name:", file_name)
        print("type of file_name:", type(file_name))
        print("content:", content)

        print("sys.path[0]=%s" % (sys.path[0]))

        current_path = sys.path[0] + '\\tmp'
        print(current_path)
        self.write_file(file_name, content)

        result = sys.path[0]
        return file_pb2.FileResponse(ret_code='0', info='ok', content='成功接收：' + result)

_HOST = 'localhost'
_PORT = '9090'
_ONE_DAY_IN_SECONDS = 1
_ROOT_PATH = '.'

def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_pb2_grpc.add_WiriteFileServicer_to_server(fileServer(_ROOT_PATH), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    print("haha")
    # content = read_file("test.txt")
    # write_file('test111.txt', content)
    serve()
