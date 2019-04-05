#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: JYRoooy
import os, threading

myFileList = []
global counter_lock
counter_lock = threading.Lock()
def fileWalk(source_file_path, destination_file_path):
    for cur_dir, dirs, files in os.walk(source_file_path):
        for file in files:
            my_cur_path = cur_dir + "/" + file
            myFileList.append(my_cur_path)

class myThread(threading.Thread):
    def __init__(self, tid, source_file_path, destination_file_path):
        threading.Thread.__init__(self)
        self.tid = tid
        self.source_file_path = source_file_path
        self.destination_file_path = destination_file_path
        self.new_dir = ''
        self.cur_file_name = ''
        self.sub_path = ''
        self.new_dir = ''
        self.my_file_des = ''
        self.my_file_cur = ''
    def run(self):
        while 1:

            if myFileList!=[]:
                counter_lock.acquire()
                cur_file = myFileList.pop(-1)
                counter_lock.release()
                try:
                    my_destination_file_path = self.destination_file_path
                    os.makedirs(my_destination_file_path)
                except:
                    pass

                self.cur_file_name = cur_file.lstrip(self.source_file_path)
                self.sub_path = os.path.split(self.cur_file_name)[0]
                self.new_dir = self.destination_file_path + self.sub_path
                try:
                    os.makedirs(self.new_dir)
                except:
                    pass
                self.new_file = self.new_dir + "/"+ os.path.split(self.cur_file_name)[1]
                self.my_file_cur = open(cur_file, 'rb')
                self.my_file_des = open(self.new_file, 'wb')
                print(self.tid, self.cur_file_name)
                while True:
                    content = self.my_file_cur.read(1024)
                    if len(content) == 0:
                        break
                    else:
                        self.my_file_des.write(content)
                self.my_file_des.close()
                self.my_file_cur.close()
            else:
                break




# class myThread(threading.Thread):
#     def __init__(self, tid, source_file_path, destination_file_path):
#         threading.Thread.__init__(self)
#         self.tid = tid
#         self.source_file_path = source_file_path
#         self.destination_file_path = destination_file_path
#     def run(self):
#         try:
#             my_destination_file_path = self.destination_file_path
#             os.makedirs(my_destination_file_path)
#         except:
#             print("该源目录已经存在")
#             pass
#
#         for cur_dir, dirs, files in os.walk(self.source_file_path):
#                 for file in files:
#                     if cur_dir == self.source_file_path:
#                         try:
#                             my_file_cur_path = cur_dir + "\\" + file
#                             my_file_des_path = my_destination_file_path + "\\" + file
#                             my_file_cur = open(my_file_cur_path, 'rb')
#                             my_file_des = open(my_file_des_path, 'wb')
#                             print(self.tid, my_file_des_path)
#                             while True:
#                                 content = my_file_cur.read(1024)
#                                 if len(content) == 0:
#                                     break
#                                 else:
#                                     my_file_des.write(content)
#                             my_file_des.close()
#                             my_file_cur.close()
#                         except:
#                             pass
#                     else:
#                         try:
#                             my_cur_dir = self.destination_file_path + cur_dir.split(self.source_file_path)[1]
#                             os.makedirs(my_cur_dir)
#                             my_file_cur_path = cur_dir + "\\" + file
#                             my_file_des_path = my_cur_dir + "\\" + file
#                             my_file_cur = open(my_file_cur_path, 'rb')
#                             my_file_des = open(my_file_des_path, 'wb')
#                             print(self.tid, my_file_des_path)
#                             while True:
#                                 try:
#                                     content = my_file_cur.read(1024)
#                                 except:
#                                     pass
#                                 if len(content) == 0:
#                                     break
#                                 else:
#                                     my_file_des.write(content)
#                                 my_file_des.close()
#                                 my_file_cur.close()
#                         except:
#                             pass


if __name__ == '__main__':
    '''
    用户输入
    '''
    threads = []

    my_source_file_path = input('请输入源文件夹全路径')
    destination_file_path = input('请输入目标文件夹全路径')
    fileWalk(my_source_file_path, destination_file_path)
    for i in range(5):
        thread1 = myThread(i,my_source_file_path,destination_file_path)
        threads.append(thread1)
    for t in threads:
        t.start();
    '''
    控制台
    '''
    # if len(sys.argv) <= 4:
    #     exit(0)
    # elif '-cd' in sys.argv and len(sys.argv) == 5:
    #     copyDirectory(sys.argv[sys.argv.index('-cd')+1], sys.argv[sys.argv.index('-dd')+1])
    #     exit(0)