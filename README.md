# API Handler for Sbermarket Paser
**Базовые Зависимости**
- Python >= 3.12
   - poetry

## Установка основных зависимостей
Зайдите в корневую директорию проекта и установить зависимости:
- ```pip install poetry```
- ```poetry install```

## Запуск FastAPI приложения
1. Запустить FastAPI из корневой директории можно командой

   ```poetry run uvicorn APIHandler.app:create_app```

2. Перейдите по http://localhost:8000/docs и используйте API Endpoint'ы.

## Sbermarket Store Parser for Edadeal2.0
Можно найти в другом [репозитории](https://github.com/MRossa157/EdaDeal2.0-StoreParser?tab=readme-ov-file)