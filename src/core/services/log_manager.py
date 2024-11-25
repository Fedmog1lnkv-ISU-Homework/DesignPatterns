from src.core.abstractions.abstract_manager import AbstractManager
from src.core.enums.event_type import EventType
from src.utils.logger.logger import Logger
from src.utils.observer.event import Event


class LogManager(AbstractManager):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LogManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()

    def log_http(self, event: Event):
        method = None
        url = None
        body = None

        if 'method' in event.data.keys():
            method = event.data['method']

        if 'url' in event.data.keys():
            url = event.data['url']

        if 'body' in event.data.keys():
            body = event.data['body']

        message = "http request got"

        if method is not None:
            message += f'", method: "{method}"'

        if url is not None:
            message += f', url: "{url}"'

        if body is not None:
            message += f', body: "{body}"'

        Logger.info(message)

    def handle_event(self, event: Event):
        super().handle_event(event)

        if event.type == EventType.DUMP_DATA:
            Logger.info("dump data")

        if event.type == EventType.CHANGE_NOMENCLATURE:
            Logger.info(f"change nomenclature, with unique_code: {event.data.unique_code}")

        if event.type == EventType.HTTP_REQUEST_GOT:
            self.log_http(event)