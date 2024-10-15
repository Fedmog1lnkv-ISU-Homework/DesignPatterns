from connexion import FlaskApp

from src.api.routes.reports import reports_blueprint
from src.api.routes.prototype import prototype_blueprint

app = FlaskApp(__name__)

app.add_api('swagger.yaml')
app.app.register_blueprint(reports_blueprint)
app.app.register_blueprint(prototype_blueprint)
