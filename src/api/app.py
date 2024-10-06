from connexion import FlaskApp

from src.api.routes.reports import reports_blueprint

app = FlaskApp(__name__)

app.app.register_blueprint(reports_blueprint)
