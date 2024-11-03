from src.core.models.storehouse_model import StoreHouseModel


class StartStoreHouseGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StartStoreHouseGenerator, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.__generate_storehouse_1()
        self.__generate_storehouse_2()
        self.__generate_storehouse_3()

    def __generate_storehouse_1(self):
        st = StoreHouseModel()

        st.name = "Main storehouse"
        st.location = "location 1"

        self.__main_store = st

    def __generate_storehouse_2(self):
        st = StoreHouseModel()

        st.name = "Second storehouse"
        st.location = "location 2"

        self.__second_store = st

    def __generate_storehouse_3(self):
        st = StoreHouseModel()

        st.name = "Third storehouse"
        st.location = "location 1"

        self.__third_store = st

    def get_first_storehouse(self) -> StoreHouseModel:
        return self.__main_store

    def get_second_storehouse(self) -> StoreHouseModel:
        return self.__second_store

    def get_third_storehouse(self) -> StoreHouseModel:
        return self.__third_store

    def get_storehouses(self) -> list[StoreHouseModel]:
        return [self.__main_store, self.__second_store, self.__third_store]
