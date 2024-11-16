from connexion import FlaskApp

from src.api.routes.nomenclature import nomenclature_blueprint
from src.api.routes.reports import reports_blueprint
from src.api.routes.prototype import prototype_blueprint
from src.api.routes.settings import settings_blueprint
from src.api.routes.store import store_blueprint
from src.di.manager import recipe_manager
from src.di.observer_manager import observer_manager

app = FlaskApp(__name__)

app.add_api('swagger.yaml')
app.app.register_blueprint(reports_blueprint)
app.app.register_blueprint(prototype_blueprint)
app.app.register_blueprint(store_blueprint)
app.app.register_blueprint(settings_blueprint)
app.app.register_blueprint(nomenclature_blueprint)


observer_manager.add(recipe_manager)
