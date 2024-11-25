from src.core.services.log_manager import LogManager
from src.core.services.recipe_manager import RecipeManager
from src.core.services.settings_manager import SettingsManager
from src.core.services.start_manager import StartManager
from src.core.services.store_service import StoreManager
from src.di.observer_manager import observer_manager
from src.utils.logger.logger import Logger

settings_manager = SettingsManager()
recipe_manager = RecipeManager()
store_service = StoreManager()
start_manager = StartManager()
log_manager = LogManager()

store_service.init_store_turnovers_by_date_block()

Logger.setup_by_settings(settings_manager.settings)

