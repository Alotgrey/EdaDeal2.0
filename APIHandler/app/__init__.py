from fastapi import FastAPI

from APIHandler.app.configuration.server import Server


def create_app(_=None) -> FastAPI:
    app = FastAPI()

    return Server(app).get_app()
