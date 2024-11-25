

import sys
from datetime import datetime
from venv import logger

from src.core.models.settings import Settings
from src.utils.logger.item import LogLevel, LogItem


class Logger:
    __log_level = LogLevel.DEBUG
    __output = sys.stdout

    @staticmethod
    def setup_by_settings(settings: Settings):
        Logger.__log_level = settings.log_level
        filepath = settings.log_file_path

        if filepath is not None:
            Logger.__output = open(filepath, "a")

    @staticmethod
    def set_log_level(log_level: LogLevel):
        Logger.__log_level = log_level
        Logger.info(f"Log level set to {log_level.name}")

    @staticmethod
    def get_log_level() -> LogLevel:
        return Logger.__log_level

    @staticmethod
    def set_file_output(output):
        Logger.__output = output

    @staticmethod
    def __log(item: LogItem):
        if item.level.value < Logger.__log_level.value:
            return

        time = datetime.now().isoformat()

        message = f"{item.level.name}: [{time}]\t{item.message}"

        Logger.__output.write(f"{message}\n")
        Logger.__output.flush()

    @staticmethod
    def debug(message: str):
        item = LogItem(LogLevel.DEBUG, message)
        Logger.__log(item)

    @staticmethod
    def info(message: str):
        item = LogItem(LogLevel.INFO, message)
        Logger.__log(item)

    @staticmethod
    def error(message: str):
        item = LogItem(LogLevel.ERROR, message)
        Logger.__log(item)