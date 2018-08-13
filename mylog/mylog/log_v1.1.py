#!/usr/bin/env python3
from logging import handlers
from mylog.settings import (
    LOG_PROJECT_NAME,
    LOG_FILE_PATH,
    LOG_MAX_BYTES,
    LOG_BACKUP_COUNT,
    LOG_ENCODING,
    LOG_FILE_FORMAT,
    LOG_LEVEL
)

import logging


def myLog():
    logger = logging.getLogger(LOG_PROJECT_NAME)

    # 1.设置统一的日志级别, 全局 日志级别
    logger.setLevel(LOG_LEVEL)

    # 2. 设置输出文件中
    fh = handlers.RotatingFileHandler(LOG_FILE_PATH,
                                      maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT,
                                      encoding=LOG_ENCODING)

    # 4. 将 handler 绑定到 logger 对象中
    logger.addHandler(fh)  # 绑定 fh

    # 5. 生成 formatter 对象, 并把 formatter 对象绑定到 handler 对象
    #   5.2. 生成 输出到文件 的模式
    file_formatter = logging.Formatter(LOG_FILE_FORMAT)

    # 6. 给 handler 一个格式
    fh.setFormatter(file_formatter)

    return logger


