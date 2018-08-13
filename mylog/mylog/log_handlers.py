#!/usr/bin/env python3
import logging
from logging import handlers

from mylog.settings import (
    LOG_FILE_PATH,
    LOG_MAX_BYTES,
    LOG_BACKUP_COUNT,
    LOG_ENCODING,
    LOG_FILE_FORMAT,
)


def file_handler(logger):
    """
    在 logger 添加 向 文件中追加日志
    :param logger: 日志
    :return:
    """
    # 设置输出文件中
    fh = handlers.RotatingFileHandler(
        LOG_FILE_PATH, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT, encoding=LOG_ENCODING)

    # 将 handler 绑定到 logger 对象中
    logger.addHandler(fh)

    # 生成 formatter 对象, 并把 formatter 对象绑定到 handler 对象, 输出的内容写入文件
    file_formatter = logging.Formatter(LOG_FILE_FORMAT)

    # 给 handler 一个格式
    fh.setFormatter(file_formatter)


def console_handler(logger):
    ch = logging.StreamHandler()  # 输出在屏幕上
    logger.addHandler(ch)  # 绑定 ch
    console_formatter = logging.Formatter(LOG_FILE_FORMAT)
    ch.setFormatter(console_formatter)







