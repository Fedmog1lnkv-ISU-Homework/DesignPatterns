from abc import ABC, abstractmethod

from src.utils.observer.event import Event


class AbstractManager(ABC):
    pass

    @abstractmethod
    def handle_event(self, event: Event):
        if not isinstance(event, Event):
            raise TypeError('event must be of type Event')
        