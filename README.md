## 1.添加自定义模块  mylog

* 模块解释

  ```python
  # 直接导入 mylog/mylog/log 中的 myLog 函数
  from mylog.log import myLog
  logger = myLog()
  logger.error("错误信息")
  ```

* 配置讲解

  ```python
  # 配置在 settings.py 中 有解释
  ```

  

* 添加了自己日志模块

  ```python 
  # 在 mylog/mylog/settings.py 中配置
  HANDLERS_LIST 配置项, 被注释的不会执行
  ```

