import requests
import allure
from constants import API1_url
from constants import bearer_token


@allure.description("Тестирование отправки пустого запроса к API .")
class EmptyPostRequest:
    """Класс для работы с API интернет-магазина.
        Этот класс отправки запросов к API для добавления продуктов в корзину
    """

    url = API1_url

    def __init__(self, url):
        """
            Создает объект для работы с корзиной.
            :param url: URL для добавления товара в корзину.
        """
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': bearer_token  # Токен для авторизации
        }

    def add_product_to_cart_with_empty_body(self):
        """
            Отправляет POST-запрос с пустым телом для добавления продукта
            :return: Статус код ответа от сервера (int).
            Ожидается, что в случае пустого тела запроса сервер вернет код 422.
        """
        response = requests.post(
            self.url, json={}, headers=self.headers)  # Отправляем пустое тело
        return response.status_code
