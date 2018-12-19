# coding:utf-8

import os 
import sys


def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(lines)


if __name__ == '__main__':
    print("haha")
    read_file("test.txt")