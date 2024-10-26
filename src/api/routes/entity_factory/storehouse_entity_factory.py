from src.infrastructure.repositories.storehouse_repository import StoreHouseRepository


class StoreHouseEntityFactory():
    
    __repository: StoreHouseRepository = StoreHouseRepository()
    
    def get_path_name(self) -> str:
        return 'storehouse'

    def get_entity(self):
        return self.__repository.get_all()