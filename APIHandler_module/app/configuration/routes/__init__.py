from app.configuration.routes.routes import Routes
from app.internal.routes import parser2

__routes__ = Routes(routers=(parser2.router, ))