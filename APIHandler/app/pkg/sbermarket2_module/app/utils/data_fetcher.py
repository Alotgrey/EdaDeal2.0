import json
import logging
import re
import time

import undetected_chromedriver as uc  # type: ignore

from APIHandler.app.pkg.sbermarket2_module.app.utils.constants import UTILS_PATH


class DataFetcher:
    def __init__(self, browser_path=None) -> None:
        self.browser_path = browser_path
        self.__validate_browser_path()

    def get_cookies(
        self,
    ) -> dict:
        cookies = self.__get_cookies_from_file()

        if cookies is None:
            all_data = self.__get_all_data()
            cookies = all_data["cookies"]
        return cookies

    def get_user_agent(
        self,
    ) -> str:
        user_agent = self.__get_user_agent_from_file()

        if user_agent is None:
            all_data = self.__get_all_data()
            user_agent = all_data["user_agent"]
        return user_agent

    def get_token(
        self,
    ) -> str:
        token = self.__get_token_from_file()

        if token is None:
            all_data = self.__get_all_data()
            token = all_data["token"]
        return token

    def get_driver(self, headless_mode: bool = False):
        if self.browser_path is None:
            driver = uc.Chrome(headless=headless_mode)
        else:
            driver = uc.Chrome(
                headless=headless_mode,
                browser_executable_path=self.browser_path,
            )
        logging.debug("Создали экземпляр WebDriver")
        return driver

    # ? Сделать этот метод - staticmethod и не создавать driver если его не передали?? 🤔
    def get_page_source_code(self, url, driver=None, headless_mode: bool = False, is_driver_quit=True) -> str:
        if driver is None:
            driver = self.get_driver(headless_mode=headless_mode)

        driver.get(url)
        page_data = driver.page_source
        # ? А нужно ли выходить из драйвера?
        if is_driver_quit:
            driver.quit()
        return page_data

    def __validate_browser_path(self):
        logging.debug("Ищем путь до Chrome WebDriver")
        try:
            driver = self.get_driver(headless_mode=True)
            driver.quit()
        except (FileNotFoundError, TypeError):
            if self.browser_path is None:
                error_text = f"Не найден путь к браузеру Chrome: {self.browser_path}. Укажите browser_path в аргументах"
                # logging.error(error_text)
                raise FileNotFoundError(error_text)
            error_text = f"Некорректный путь к браузеру Chrome: {self.browser_path}"
            # logging.error(error_text)
            raise FileNotFoundError(error_text)

    def __get_all_data(self) -> dict:
        logging.info("Открываю браузер хром для получения токена")
        driver = self.get_driver(headless_mode=True)

        driver.get("https://sbermarket.ru/")
        user_agent = driver.execute_script("return navigator.userAgent;")
        time.sleep(5)
        token = re.findall('STOREFRONT_API_V3_CLIENT_TOKEN: "([^"]+)"', driver.page_source)[0]
        cookies = driver.get_cookies()

        cookies_dict = {}
        for cookie in cookies:
            cookies_dict[cookie["name"]] = cookie["value"]

        logging.info(f"Токен получен: {token}")

        self.__save_token_in_file(token=token)
        self.__save_cookies_in_file(cookies=cookies_dict)
        self.__save_user_agent_in_file(user_agent=user_agent)

        driver.quit()

        return {"token": token, "cookies": cookies, "user_agent": user_agent}

    def __save_cookies_in_file(self, cookies: dict):
        """Сохраняет токен в файл"""
        with open(rf"{UTILS_PATH}\cookies.json", "w", encoding="utf-8") as f:
            json.dump(cookies, f)
        logging.info("Куки сохранены в файл")

    def __save_user_agent_in_file(self, user_agent: str):
        """Сохраняет user-agent в файл"""
        with open(rf"{UTILS_PATH}\user_agent.txt", "w", encoding="utf-8") as f:
            f.write(user_agent)
        logging.info("User_agent сохранен в файл")

    def __save_token_in_file(self, token: str):
        """Сохраняет токен в файл"""
        with open(rf"{UTILS_PATH}\token.txt", "w", encoding="utf-8") as f:
            f.write(token)
        logging.info("Токен сохранен в файл")

    def __get_cookies_from_file(self) -> dict | None:
        """Получить куки из файла"""
        try:
            with open(rf"{UTILS_PATH}\cookies.json", "r", encoding="utf-8") as f:
                cookies = json.load(f)
            logging.debug("Получены куки из файла")
        except FileNotFoundError:
            logging.error("Файл с куки не найден")
            return None

        return cookies

    def __get_user_agent_from_file(self) -> str | None:
        """Получить user_agent из файла"""
        try:
            with open(rf"{UTILS_PATH}\user_agent.txt", "r", encoding="utf-8") as f:
                user_agent = f.read()
            logging.debug("Получен user_agent из файла")
        except FileNotFoundError:
            logging.error("Файл с user_agent не найден")
            return None

        return user_agent

    def __get_token_from_file(self) -> str | None:
        """Получить токен из файла"""
        try:
            with open(rf"{UTILS_PATH}\token.txt", "r", encoding="utf-8") as f:
                token = f.read()
            logging.debug("Получен токен из файла")
        except FileNotFoundError:
            logging.error("Файл с токеном не найден")
            return None

        return token


# if __name__ == "__main__":
#     from sbermarket2_module.app.utils.constants import CHROME_PATH

#     test = DataFetcher(CHROME_PATH)
#     cookies = test.get_cookies()
#     token = test.get_token()

#     print(cookies, token)
