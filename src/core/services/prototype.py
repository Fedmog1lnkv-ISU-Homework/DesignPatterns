from src.core.abstractions.abstract_manager import AbstractManager
from src.infrastructure.prototype.abstract.abstract import AbstractPrototype
from src.infrastructure.factory.prototype_factory import PrototypeFactory
from src.infrastructure.filter.item.item import FilterItem
from src.utils.observer.event import Event


class PrototypeService(AbstractManager):
    __prototype_factory: PrototypeFactory
    
    def __init__(self):
        self.__prototype_factory = PrototypeFactory()
        
    def get_by_filters(self, data: list, filters: list[FilterItem]) -> list:
        prototype = self.__prototype_factory.create(data)
        
        return prototype.create(filters)

    def handle_event(self, event: Event):
         super().handle_event(event)
    