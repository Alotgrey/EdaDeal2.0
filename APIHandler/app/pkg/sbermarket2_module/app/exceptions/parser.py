from dataclasses import dataclass

from APIHandler.app.pkg.sbermarket2_module.app.exceptions.base import (
    ApplicationException,
)


@dataclass(eq=False)
class FetcherNotFound(ApplicationException):
    @property
    def message(self):
        return f'Не найден обработчик для этой версии/запроса. Передайте его явно fetcher=[...]"'