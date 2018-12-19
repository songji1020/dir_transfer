# coding:utf-8

import os 
import sys
import grpc
from pb import file_pb2, file_pb2_grpc

def read_file(file_name):
    print("file_name:", file_name)
    with open(file_name, 'rb') as file:
        lines = file.readlines()
        print(lines)
        return lines

def write_file(file_name, context_line_list):
    with open(file_name, "w") as wfile:
        for line in context_line_list:
            wfile.write(line)


_HOST = 'localhost'
_PORT = '9090'

def file_send(root_path, file_name):
    ''' file_name 是 root_path后的相对路径+文件名 '''
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = file_pb2_grpc.WiriteFileStub(channel=conn)

    lines = read_file(root_path + file_name)
    string = str(lines)
    b_buf = bytes(string, encoding="utf-8")


    response = client.SendFile(file_pb2.FileInfoRequest(file_path = root_path,file_name = file_name,content = b_buf))
    print("ret_code: " + response.ret_code)
    print("info: " + response.info)
    print("content: " + response.content)

def all_files(root_path):
    file_list = []
    i = 0
    for root, dirs, files in os.walk(root_path):
        for file in files:
            i = i + 1
            full_path = "%s\%s" % (root, file)
            path = full_path[len(root_path): len(full_path)]
            file_list.append(path)
    return file_list

def files_send(root_path):
    ''' root_path不要已"\"结尾 '''
    i = 0
    file_list = all_files(root_path)
    total = len(file_list)
    for file in file_list:
        i = i + 1
        full_path = root_path + file
        # print (full_path)
        print('准备发送%d/%d：%s' % (i, total, full_path))
        file_send(root_path, file)

if __name__ == '__main__':
    print("haha")
    # content = read_file("test.txt")
    # write_file('test111.txt', content)
    # file_send('F:\\3Debug\python\\rebuildfile\\test111.txt')
    files_send('F:\\3Debug\python\\rebuildfile')
    # print("sys.path[0]=%s" % (sys.path[0]))
    # print("sys.path=%s" % (sys.path))

