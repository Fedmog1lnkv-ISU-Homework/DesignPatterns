from flasgger import Swagger

from src.api.app import app
from src.core.services.start_manager import StartManager
from src.core.services.store_service import StoreManager

test_dict = {
    "inn": "123456789012",  # 12 символов
    "account": "40702810123",  # 11 символов
    "correspondent_account": "38104000000",  # 11 символов
    "bic": "044525225",  # 9 символов
    "name": "Hello world",  # n символов
    "type_of_ownership": "hello"  # 5 символов
}

if __name__ == "__main__":
    StartManager()

    store_manager = StoreManager()

    store_manager.init_store_turnovers_by_date_block()

    Swagger(app.app, template_file="swagger.yaml")

    app.run(port=8080)