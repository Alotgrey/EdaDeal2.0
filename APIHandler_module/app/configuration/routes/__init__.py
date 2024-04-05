from APIHandler_module.app.configuration.routes.routes import Routes
from APIHandler_module.app.internal.routes import parser2

__routes__ = Routes(routers=(parser2.router, ))