#!/usr/bin/env python3
# log   V 1.2
from logging import handlers
from mylog.settings import (
    HANDLERS_LIST,
    LOG_PROJECT_NAME,
    LOG_LEVEL
)

import logging
import importlib


def model_run():
    for path in HANDLERS_LIST:
        module_path, func_name = path.rsplit('.', 1)

        # 2. 利用 importlib 导致指定路径的模块文件
        modle = importlib.import_module(module_path)  # 导入 module_path 路径的文件
        cls = getattr(modle, func_name)
        yield cls


def myLog():
    logger = logging.getLogger(LOG_PROJECT_NAME)
    logger.setLevel(LOG_LEVEL)

    for func_model in model_run():
        func_model(logger)

    return logger









