from src.core.abstractions.abstract_entity import AbstractEntity


class StoreHouseModel(AbstractEntity):
    __name: str = ""
    __location: str = ""
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value
        
    @property
    def location(self) -> str:
        return self.__location
    
    @location.setter
    def location(self, value: str):
        self.__location = value

    def set_compare_mode(self, other) -> bool:
        return super().set_compare_mode(other)
