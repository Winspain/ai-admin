import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logging():
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file = os.path.join(log_directory, "app.log")

    # 创建日志器
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)  # 设置日志级别

    # 创建处理器，每个文件10MB，保留5个旧文件
    handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=1)
    handler.setLevel(logging.DEBUG)

    # 创建格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # 将处理器添加到日志器
    logger.addHandler(handler)

    return logger


# 可在应用中直接导入并使用 logger
logger = setup_logging()

