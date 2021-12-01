#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
from datetime import datetime
from pathlib import Path

print('log 刷新脚本')

ACCESS_FILE_NEW_PATH="./log/"+datetime.today().strftime('%Y-%m-%d')+"-access.log"
ACCESS_FILE_PATH = 'access.log'

def newLogFileIfNotExist():
    if Path(ACCESS_FILE_PATH).is_file():
        with open(ACCESS_FILE_PATH, 'w') as fp:
            fp.truncate(0)
            print('清空了access.log文件')        
    else:
        with open(ACCESS_FILE_PATH, 'w') as fp:
            print('创建了新的access.log文件')        



newLogFileIfNotExist()

print('文件路径：'+ ACCESS_FILE_NEW_PATH)


if not os.path.exists('log'):
    os.makedirs('log')


if os.path.isfile(ACCESS_FILE_NEW_PATH):
    print('access.log文件，今天已经存在')
else:
    # shutil.move(ACCESS_FILE_PATH, ACCESS_FILE_NEW_PATH)
    shutil.copy(ACCESS_FILE_PATH, ACCESS_FILE_NEW_PATH)
    newLogFileIfNotExist()


if not os.path.exists('log-err'):
    os.makedirs('log-err')

ACCESS_FILE_ERR_NEW_PATH="./log-err/"+datetime.today().strftime('%Y-%m-%d')+"-nginx_error.log"
ACCESS_FILE_ERR_PATH = 'nginx_error.log'

print('错误日志文件路径：'+ ACCESS_FILE_ERR_NEW_PATH)




def newErrorLogFileIfNotExist():
    if Path(ACCESS_FILE_ERR_PATH).is_file():
        with open(ACCESS_FILE_ERR_PATH, 'w') as fp:
            fp.truncate(0)
            print('清空了nginx_error文件')  
    else:
        with open(ACCESS_FILE_ERR_PATH, 'w') as fp:
            print('创建了新的nginx_error文件')  

newErrorLogFileIfNotExist()

if os.path.isfile(ACCESS_FILE_ERR_NEW_PATH):
    print('nginx_error.log文件，今天已经存在')
else:
    # shutil.move(ACCESS_FILE_ERR_PATH, ACCESS_FILE_ERR_NEW_PATH)
    shutil.copy(ACCESS_FILE_ERR_PATH, ACCESS_FILE_ERR_NEW_PATH)
    newErrorLogFileIfNotExist()