import requests
import json
import allure
from constants import API1_url, API2_url, bearer_token


@allure.description("Тест добавления товара в корзину на сайте Читай-город.")
class UpdateCartAPI:
    """
        Класс для работы с API обновления корзины на сайте Читай-город.
        Атрибуты:
            url (str): URL для работы с корзиной.
            headers (dict): Заголовки запроса, включая авторизацию.
    """
    url = API1_url  # URL для работы с корзиной
    url_2 = API2_url  # URL для обновления корзины

    def __init__(self, url):
        """
            Инициализация класса UpdateCartAPI.
            :param url: URL, используемый для работы с корзиной.
        """
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': bearer_token
        }

    @allure.step("Обновление содержимого корзины")
    def update_cart(self, items: dict):
        """Отправляет PUT-запрос для редактирования корзины.
            :param items: Словарь с товарами для обновления корзины
                Пример формата:
            {
                "items": [{"id": 1, "quantity": 2}, {"id": 2, "quantity": 1}]
            }
                :return: содержит статус-код ответа (int) и текст ответа (str)
        """
        # Отправляем PUT-запрос для редактирования корзины
        response = requests.put(
            self.url_2, headers=self.headers, data=json.dumps(items))
        # Возвращаем статус-код и текст ответа от сервера
        return response.status_code, response.text
