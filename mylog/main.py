#!/usr/bin/env python3
from mylog.log import myLog

logger = myLog()
for i in range(10):
    logger.error("test log %s" % i)



