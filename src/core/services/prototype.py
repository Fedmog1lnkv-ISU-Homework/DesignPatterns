from src.infrastructure.prototype.abstract.abstract import AbstractPrototype
from src.infrastructure.factory.prototype_factory import PrototypeFactory
from src.infrastructure.filter.item.item import FilterItem


class PrototypeService:
    __prototype_factory: PrototypeFactory
    
    def __init__(self):
        self.__prototype_factory = PrototypeFactory()
        
    def get_by_filters(self, data: list, filters: list[FilterItem]) -> list:
        prototype = self.__prototype_factory.create(data)
        
        return prototype.create(filters)
    