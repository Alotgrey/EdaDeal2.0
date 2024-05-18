**Базовые Зависимости**
- Python >= 3.12
   - poetry

**Установка основных зависимостей**

Зайдите в корневую директорию проекта и запустите следующую команду:  ```poetry install```

**Запуск FastAPI приложения**
1. Запустить FastAPI из корневой директории можно командой

   ```poetry run uvicorn APIHandler.app:create_app```

2. Перейдите по http://localhost:8000/docs и используйте API Endpoint'ы.
