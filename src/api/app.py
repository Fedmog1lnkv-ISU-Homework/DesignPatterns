from connexion import FlaskApp

from src.api.midllware.log import LoggingMiddleware
from src.api.routes.nomenclature import nomenclature_blueprint
from src.api.routes.osv import osv_blueprint
from src.api.routes.reports import reports_blueprint
from src.api.routes.prototype import prototype_blueprint
from src.api.routes.settings import settings_blueprint
from src.api.routes.store import store_blueprint
from src.di.manager import recipe_manager, store_service, settings_manager, start_manager, log_manager
from src.di.observer_manager import observer_manager

app = FlaskApp(__name__)

app.add_api('swagger.yaml')
app.app.register_blueprint(reports_blueprint)
app.app.register_blueprint(prototype_blueprint)
app.app.register_blueprint(store_blueprint)
app.app.register_blueprint(settings_blueprint)
app.app.register_blueprint(nomenclature_blueprint)
app.app.register_blueprint(osv_blueprint)

app.add_wsgi_middleware(LoggingMiddleware)

observer_manager.add(settings_manager)
observer_manager.add(recipe_manager)
observer_manager.add(store_service)
observer_manager.add(start_manager)
observer_manager.add(log_manager)

