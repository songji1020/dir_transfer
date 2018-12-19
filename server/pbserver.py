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

    def write_file(self, folder, file_name, context):
        ''' context 是bytes格式 '''
        print("准备存文件:", folder + file_name)
        path = self.check_path(file_name, folder)
        with open(path, "wb") as w_file:
            w_file.write(context)

    def check_path(self, filename:str, folder):
        ''' 检查路径是否存在 不存在则创建'''
        path = folder + filename
        folder_t = os.path.dirname(path)
        if not os.path.exists(folder_t):
            print("创建：", folder_t)
            os.makedirs(folder_t, 0o777)
        return path


    # #### 真正重要的-输出函数 #### #
    def SendFile(self, request, context):
        file_path = request.file_path
        file_name = request.file_name
        content = request.content

        current_path = sys.path[0] + '\\tmp'
        self.write_file(current_path, file_name, content)
        result = sys.path[0]
        return file_pb2.FileResponse(ret_code='0', info='ok', content='成功接收：' + result)

_HOST = 'localhost'
_PORT = '9090'
_ONE_DAY_IN_SECONDS = 1
_ROOT_PATH = '.'
# MAX_MESSAGE_LENGTH = 30 * 1024 *1024
MAX_MESSAGE_LENGTH = 1 * 1024 *1024

def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10), \
                             options = [('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), \
                                        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])
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
