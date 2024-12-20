from datetime import datetime, timedelta
import random

from src.core.enums.trsndsction_type import TransactionType
from src.core.models.store_transaction import StoreTransaction
from src.infrastructure.generators.start_nomenclature_generator import StartNomenclatureGenerator
from src.infrastructure.generators.start_storehouse_generator import StartStoreHouseGenerator


class StoreTransactionGenerator:

    _instance = None
    __nomenclature_generatore: StartNomenclatureGenerator = StartNomenclatureGenerator()
    __storehouse_generator: StartStoreHouseGenerator = StartStoreHouseGenerator()

    def __init__(self):
        self.__transactions = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StoreTransactionGenerator, cls).__new__(cls)
        return cls._instance
    
    def __generate_transactions_egs(self):
        
        tr_income = StoreTransaction()

        tr_income.date = datetime(2024, 10, 25, 17, 0, 0)

        tr_income.nomenclature = self.__nomenclature_generatore.get_sugar()
        tr_income.storehouse = self.__storehouse_generator.get_first_storehouse()
        tr_income.measure_unit = tr_income.nomenclature.units
        tr_income.type = TransactionType.INCOME
        tr_income.count = 100.0
        
        self.__egs_income = tr_income

        tr_expense = StoreTransaction()

        tr_expense.date = datetime(2024, 10, 25, 19, 0, 0)

        tr_expense.nomenclature = self.__nomenclature_generatore.get_sugar()
        tr_expense.storehouse = self.__storehouse_generator.get_first_storehouse()
        tr_expense.measure_unit = tr_income.nomenclature.units
        tr_expense.type = TransactionType.EXPENSE
        tr_expense.count = 40.0

        self.__egs_expense = tr_expense

    def __generate_transactions_chicken_fillet(self):

        tr_income = StoreTransaction()

        tr_income.date = datetime(2024, 10, 25, 17, 30, 0)

        tr_income.nomenclature = self.__nomenclature_generatore.get_chicken_fillet()
        tr_income.storehouse = self.__storehouse_generator.get_third_storehouse()
        tr_income.measure_unit = tr_income.nomenclature.units
        tr_income.type = TransactionType.INCOME
        tr_income.count = 100.0

        self.__chicken_income = tr_income

        tr_expense = StoreTransaction()

        tr_expense.date = datetime(2024, 10, 25, 19, 50, 0)

        tr_expense.nomenclature = self.__nomenclature_generatore.get_chicken_fillet()
        tr_expense.storehouse = self.__storehouse_generator.get_third_storehouse()
        tr_expense.measure_unit = tr_income.nomenclature.units
        tr_expense.type = TransactionType.EXPENSE
        tr_expense.count = 40.0

        self.__chicken_expense = tr_expense

    def __generate_transactions_butter(self):

        tr_income = StoreTransaction()

        tr_income.date = datetime(2024, 10, 25, 11, 0, 0)

        tr_income.nomenclature = self.__nomenclature_generatore.get_butter()
        tr_income.storehouse = self.__storehouse_generator.get_third_storehouse()
        tr_income.measure_unit = tr_income.nomenclature.units
        tr_income.type = TransactionType.INCOME
        tr_income.count = 10.0

        self.__butter_income = tr_income

        tr_expense = StoreTransaction()

        tr_expense.date = datetime(2024, 10, 25, 13, 0, 0)

        tr_expense.nomenclature = self.__nomenclature_generatore.get_butter()
        tr_expense.storehouse = self.__storehouse_generator.get_third_storehouse()
        tr_expense.measure_unit = tr_income.nomenclature.units
        tr_expense.type = TransactionType.EXPENSE
        tr_expense.count = 7.0

        self.__butter_expense = tr_expense

    def __generate_transactions_water(self):

        tr_income = StoreTransaction()

        tr_income.date = datetime(2024, 10, 25, 14, 0, 0)

        tr_income.nomenclature = self.__nomenclature_generatore.get_water()
        tr_income.storehouse = self.__storehouse_generator.get_second_storehouse()
        tr_income.measure_unit = tr_income.nomenclature.units
        tr_income.type = TransactionType.INCOME
        tr_income.count = 2000.0

        self.__water_income = tr_income

        tr_expense = StoreTransaction()

        tr_expense.date = datetime(2024, 10, 25, 15, 0, 0)

        tr_expense.nomenclature = self.__nomenclature_generatore.get_water()
        tr_expense.storehouse = self.__storehouse_generator.get_second_storehouse()
        tr_expense.measure_unit = tr_income.nomenclature.units
        tr_expense.type = TransactionType.EXPENSE
        tr_expense.count = 1200.0

        self.__water_expense = tr_expense

    def generate_store_transactions(self):

        dates = [
            datetime(2024, 10, 25, 0, 0, 0),
            datetime(2024, 10, 26, 0, 0, 0),
            datetime(2024, 10, 27, 0, 0, 0),
            datetime(2024, 10, 28, 0, 0, 0),
            datetime(2024, 10, 29, 0, 0, 0),
            datetime(2024, 10, 30, 0, 0, 0),
        ]

        time_deltas = [
            timedelta(hours=1),
            timedelta(hours=2),
            timedelta(hours=3),
            timedelta(hours=4),
            timedelta(hours=5),
            timedelta(hours=6),
        ]

        nomenclatures = self.__nomenclature_generatore.get_nomenclatures()

        storehouses = self.__storehouse_generator.get_storehouses()

        transactions = []

        for date in dates:
            for time_delta in time_deltas:
                for nomenclature in nomenclatures:
                    for storehouse in storehouses:
                        tr = StoreTransaction()

                        tr.date = date + time_delta

                        tr.nomenclature = nomenclature
                        tr.storehouse = storehouse
                        tr.measure_unit = tr.nomenclature.units
                        if random.randint(0, 1) == 1:
                            tr.type = TransactionType.INCOME
                        else:
                            tr.type = TransactionType.EXPENSE

                        tr.count = float(random.randint(1, 10))
                        # tr.count = 5.0

                        transactions.append(tr)

        self.__transactions = transactions

    def generate(self):
        self.__generate_transactions_egs()
        self.__generate_transactions_chicken_fillet()
        self.__generate_transactions_butter()
        self.__generate_transactions_water()
        self.generate_store_transactions()

    def get_store_transactions(self):
        self.generate()
        return self.__transactions
        
    