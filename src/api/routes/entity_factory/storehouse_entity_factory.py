from src.api.routes.entity_factory.abstractions.report_entity_factory import ReportEntityFactory
from src.core.models.storehouse_model import StoreHouseModel
from src.infrastructure.repositories.storehouse_repository import StoreHouseRepository


class StoreHouseEntityFactory(ReportEntityFactory[list[StoreHouseModel]]):
    
    __repository: StoreHouseRepository = StoreHouseRepository()
    
    def get_path_name(self) -> str:
        return 'storehouse'

    def get_entity(self):
        return self.__repository.get_all()