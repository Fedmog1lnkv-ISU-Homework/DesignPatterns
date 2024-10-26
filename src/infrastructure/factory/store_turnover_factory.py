from src.core.enums.trsndsction_type import TransactionType
from src.core.models.store_transaction import StoreTransaction
from src.core.models.store_turnover import StoreTurnover


class TransactionKey:
    nomenclature_key: str = ""
    store_key: str = ""
    unit_key: str = ""
    
    def __init__(self, nomenclature_key: str, store_key: str, unit_key: str):
        self.nomenclature_key = nomenclature_key
        self.store_key = store_key
        self.unit_key = unit_key
    
    def key(self):
        return f"{self.nomenclature_key}.{self.store_key}.{self.unit_key}" 

class StoreTurnoverFactory:
    
    def create(self, data: list[StoreTransaction]) -> list[StoreTurnover]:
        
        transactions = {}
        result = []
        
        for transaction in data:
            key = TransactionKey(transaction.nomenclature.unique_code, transaction.storehouse.unique_code, transaction.measure_unit.unique_code)
            
            if key.key() not in transactions.keys():
                transactions[key.key()] = []
                
            transactions[key.key()].append(transaction)
            
        for key in transactions.keys():
            result.append(self.__calculate_turnover(transactions[key]))
            
        return result
            
    def __calculate_amount(self, transaction: StoreTransaction) -> float:
        res = 0.0
        
        type_to_delta = {
            TransactionType.INCOME: 1.0,
            TransactionType.EXPENSE: -1.0,
        }
        
        if transaction.type in type_to_delta.keys():
            res = type_to_delta[transaction.type] * transaction.count
        
        return res
        
    def __calculate_turnover(self, data: list[StoreTransaction]) -> StoreTurnover:
        result = StoreTurnover()
        
        amount = 0.0
        
        for transaction in data:
            result.nomenclature = transaction.nomenclature
            result.storehouse = transaction.storehouse
            result.unit = transaction.measure_unit
            
            amount += self.__calculate_amount(transaction)

        result.amount = amount
        
        return result 