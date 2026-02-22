import logging
import os


class CoreLogger:

    LOG_DIR = "logs"
    LOG_FILE = "logs/system.log"

    @staticmethod
    def _ensure_log_dir():
        if not os.path.exists(CoreLogger.LOG_DIR):
            os.makedirs(CoreLogger.LOG_DIR)

    @staticmethod
    def get_logger():
        CoreLogger._ensure_log_dir()

        logger = logging.getLogger("KAMELEON_CORE")

        if not logger.handlers:
            logger.setLevel(logging.INFO)

            file_handler = logging.FileHandler(CoreLogger.LOG_FILE)
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger
