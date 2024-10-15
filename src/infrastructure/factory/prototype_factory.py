from src.infrastructure.prototype.abstract.abstract import AbstractPrototype
from src.infrastructure.filter.operation_mapper.operation_mapper import FilterOperationTypeMapper

class PrototypeFactory:
    
    @staticmethod
    def create(data: list):
        return AbstractPrototype(data, FilterOperationTypeMapper())
        