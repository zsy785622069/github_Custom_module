#!/usr/bin/env python3
import logging

# 1. log 日志 配置
#   1). 配置 日志打印的格式
LOG_FILE_FORMAT = '%(asctime)s - %(levelname)s - 进程ID: %(process)d - %(message)s'

#   2). 配置日志文件的路径
LOG_FILE_PATH = "rili_pro_log.log"

#   3). 日志项目名
LOG_PROJECT_NAME = None

#   4). 日志单个文件的大小, 单位 Bytes ( 1KB = 1B )
LOG_MAX_BYTES = 31457280  # 30兆  1024*1024*10

#   5). 日志备份文件的个数
LOG_BACKUP_COUNT = 5

#   6). 日志字符集
LOG_ENCODING = 'utf-8'

#   7). 定义 logging 日志记录级别
LOG_LEVEL = logging.INFO

#   8). log 启动的模式
HANDLERS_LIST = [
    'mylog.log_handlers.file_handler',  # 写入文件
    'mylog.log_handlers.console_handler',  # 打印在屏幕上
]

