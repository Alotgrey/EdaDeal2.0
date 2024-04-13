from APIHandler.app.configuration.routes.routes import Routes
from APIHandler.app.internal.routes import parser_v2

__routes__ = Routes(routers=(parser_v2.router, ))
