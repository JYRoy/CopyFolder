#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: JYRoooy
import os

import sys


def walkFile(filePath):
    for cur_dir, dirs, files in os.walk(filePath):
        for file in files:
            wholePath = cur_dir+'\\'+file
            myFile = os.stat(path=wholePath)
            if myFile.st_size > 20*1024:
                print("文件名称为：",file,"路径为：",wholePath)

if __name__ == '__main__':
    '''
    用户输入
    '''
    # myFilePath = input('请输入文件夹全路径')
    # walkFile(myFilePath)

    '''
    参数给定
    '''
    if len(sys.argv) <= 1:
        exit(0)
    elif '-d' in sys.argv and len(sys.argv) == 3:
        walkFile(sys.argv[sys.argv.index('-d')+1])
        exit(0)