
from src.core.abstractions.abstract_manager import AbstractManager
from src.utils.observer.event import Event


class ObserverManager:
    __observers: list = []
    
    def add(self, manager: AbstractManager):
        if isinstance(manager, AbstractManager):
            if manager not in self.__observers:
                self.__observers.append(manager)
                print(f"Observer added: {manager.__class__.__name__}")
                
    def notify(self, event: Event):
        for observer in self.__observers:
            observer.handle_event(event)