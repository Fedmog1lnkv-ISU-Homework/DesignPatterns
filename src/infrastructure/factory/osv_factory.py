import datetime

from src.core.models.nomenclature_model import Nomenclature
from src.core.models.osv_model import OsvModel
from src.core.models.store_turnover import StoreTurnover
from src.core.models.storehouse_model import StoreHouseModel


class CreateOsvFactoryDTO:
    start_date: datetime.datetime
    end_date: datetime.datetime

    start_turnovers: [StoreTurnover]
    end_turnovers: [StoreTurnover]

    nomenclatures: [Nomenclature]
    storehouses: [StoreHouseModel]

class OsvIndex:
    nomenclature_id: str
    storehouse_id: str

    def idx(self) -> str:
        return f"{self.nomenclature_id}_{self.storehouse_id}"

class OsvFactory:

    @staticmethod
    def create(dto: CreateOsvFactoryDTO) -> list[OsvModel]:
        result: list[OsvModel] = []

        start_turnovers_map: dict[str, [StoreTurnover]] = {}

        for turnover in dto.start_turnovers:
            idx = OsvIndex()
            idx.nomenclature_id = turnover.nomenclature.unique_code
            idx.storehouse_id = turnover.storehouse.unique_code

            if idx.idx() not in start_turnovers_map.keys():
                start_turnovers_map[idx.idx()] = []

            start_turnovers_map[idx.idx()].append(turnover)

        end_turnovers_map: dict[str, [StoreTurnover]] = {}

        for turnover in dto.end_turnovers:
            idx = OsvIndex()
            idx.nomenclature_id = turnover.nomenclature.unique_code
            idx.storehouse_id = turnover.storehouse.unique_code

            if idx.idx() not in end_turnovers_map.keys():
                end_turnovers_map[idx.idx()] = []

            end_turnovers_map[idx.idx()].append(turnover)

        for nomenclature in dto.nomenclatures:
            for storehouse in dto.storehouses:
                idx = OsvIndex()
                idx.nomenclature_id = nomenclature.unique_code
                idx.storehouse_id = storehouse.unique_code

                start_turnovers = start_turnovers_map.get(idx.idx(), [])
                end_turnovers = end_turnovers_map.get(idx.idx(), [])

                start_amount = 0.0
                end_amount = 0.0

                for start_turnover in start_turnovers:
                    start_amount += start_turnover.amount
                for end_turnover in end_turnovers:
                    end_amount += end_turnover.amount

                osv = OsvModel()

                osv.start_date = dto.start_date
                osv.end_date = dto.end_date
                osv.start_amount = start_amount
                osv.end_amount = end_amount
                osv.nomenclature = nomenclature
                osv.storehouse = storehouse

                result.append(osv)

        return result

