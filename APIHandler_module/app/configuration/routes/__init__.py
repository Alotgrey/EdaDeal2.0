from APIHandler_module.app.configuration.routes.routes import Routes
from APIHandler_module.app.internal.routes import parser_v1, parser_v2

__routes__ = Routes(routers=(parser_v1.router, parser_v2.router))
