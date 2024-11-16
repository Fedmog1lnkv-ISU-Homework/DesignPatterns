
from src.core.services.recipe_manager import RecipeManager
from src.core.services.settings_manager import SettingsManager
from src.core.services.start_manager import StartManager
from src.core.services.store_service import StoreManager
from src.di.observer_manager import observer_manager

settings_manager = SettingsManager()
recipe_manager = RecipeManager()
store_service = StoreManager()
start_manager = StartManager()

store_service.init_store_turnovers_by_date_block()

