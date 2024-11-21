from io import BytesIO

from src.core.enums.event_type import EventType
from src.di.observer_manager import observer_manager
from src.utils.logger.logger import Logger
from src.utils.observer.event import Event


class LoggingMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        self.log_request(environ)
        return self.app(environ, start_response)

    def get_request_body(self, environ):
        content_length = environ.get('CONTENT_LENGTH', '0')
        content_length = int(content_length) if content_length else 0

        if content_length > 0:
            body = environ['wsgi.input'].read(content_length)
            environ['wsgi.input'] = BytesIO(body)
            return body.decode('utf-8').replace('\n', '')
        return None

    def log_request(self, environ):
        method = environ.get('REQUEST_METHOD')
        url = environ.get('PATH_INFO')
        body = self.get_request_body(environ)

        event = Event()
        event.type = EventType.HTTP_REQUEST_GOT
        event.data = {
            'method': method,
            'url': url,
            'body': body
        }

        observer_manager.notify(event)