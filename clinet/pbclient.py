# coding:utf-8

import os 
import sys
import grpc
from pb import file_pb2, file_pb2_grpc

def read_file(file_name):
    # print("file_name:", file_name)
    file_size = os.path.getsize(file_name)
    print ("文件大小:", file_size)
    with open(file_name, 'rb') as file:
        content = file.read(-1)  # bytes
        return content

def write_file(file_name, context_line_list):
    with open(file_name, "w") as wfile:
        for line in context_line_list:
            wfile.write(line)


_HOST = 'localhost'
# _HOST = '192.168.15.122'
_PORT = '9090'

_Total_Files = 0
_Total_Fault = 0
_Fault_List = []

def file_send(root_path, file_name):
    ''' file_name 是 root_path后的相对路径+文件名 '''
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = file_pb2_grpc.WiriteFileStub(channel=conn)

    content = read_file(root_path + file_name)
    try:
        response = client.SendFile(file_pb2.FileInfoRequest(file_path = root_path,file_name = file_name,content = content))
        # print("ret_code: " + response.ret_code)
        # print("info: " + response.info)
        # print("content: " + response.content)
        return 0
    except Exception as e:
        print("出错:",e)
        _Fault_List.append(root_path + file_name + "  ->" + str(e))
        return 1


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
    Total_Files = total
    _Total_Fault = 0
    for file in file_list:
        i = i + 1
        full_path = root_path + file
        # print (full_path)
        print('\n准备发送%d/%d：%s' % (i, total, full_path))
        ret = file_send(root_path, file)
        _Total_Fault = _Total_Fault + ret

    print("\n出错统计文件列表")
    for fault_info in _Fault_List:
        print(fault_info)
    print("\n出错统计：%s/%s" % (_Total_Fault, Total_Files))

if __name__ == '__main__':
    print("haha")

    # files_send('F:\\3Debug\python\\rebuildfile')
    files_send('F:\\3Debug\\python\\github\\src_folder')