# Diploma-work
Дипломная работа. Архитектура фреймворка. Автоматизация тестирования проекта "Читай-город"

## Ссылка на финальный проект по тестированию
https://bony-order-0da.notion.site/16c679a75a794d558808f55975d0d489?pvs=4

## Описание проекта
Данный проект содержит набор автоматизированных тестов для интернет-магазина книг "Читай-город". Тесты охватывают как функциональность API, так и пользовательский интерфейс (UI), обеспечивая надежное тестирование различных операций, таких как добавление, обновление и удаление товаров из корзины, а также тестирование функциональности поиска.

## Структура проекта
./test - тесты
./api - работа с API
./ui - работа с ui

## Описание классов
Pages/: Папка, содержащая классы для работы с API и UI.

AddToCartAPI: Класс для работы с API добавления товара в корзину. Он реализует методы для добавления товаров и взаимодействия с API.
AddToCart: Класс для работы с UI добавления товара в корзину. Он автоматизирует действия пользователя в интерфейсе веб-приложения.
DeleteFromCartAPI: Класс для работы с API удаления товара из корзины. Он реализует методы для удаления товаров через API запросы.
DeleteFromCart: Класс, тестирующий функциональность удаления товара из корзины на сайте Читай-город.
SearchByAuthor: Класс для тестирования поля поиска по автору на сайте Читай-город. Он проверяет, корректно ли работает поиск по имени автора.
SearchByTitle: Класс для тестирования поля поиска по названию книги на сайте Читай-город. Он проверяет, корректно ли работает поиск по названию.
EmptyPostRequest: Класс, тестирующий отправку пустого запроса к API. Он проверяет, как API обрабатывает запросы без данных.
UpdateCartAPI: Класс, который тестирует функциональность обновления товаров в корзине на сайте Читай-город.
WrongRequestAPI: Класс для отправки неверного запроса к API, что позволяет проверить, как система обрабатывает ошибки.
test_api.py: Файл, в котором описаны тесты для API. Здесь тестируются функции, связанные с добавлением, удалением и обновлением товаров в корзине, а также обработка неверных запросов и пустых запросов.

test_ui.py: Файл, в котором описаны тесты для пользовательского интерфейса. Здесь тестируются сценарии, такие как добавление и удаление товаров из корзины через интерфейс, а также проверка функционирования полей поиска.

## Стек
selenium
requests
pytest
allure
webdriver
webdriver-manager

## Установка
Клонируйте репозиторий: git clone https://github.com/anton82skypro/Diploma-work.git

Перейдите в каталог проекта Chitai-gorod

Настройте переменные окружения. Перед запуском приложения убедитесь, что у вас установлены необходимые переменные окружения. Установите все зависимости из requirements.txt. Для этого введите команду pip install - r requirements.txt

## Получение токена авторизации и ID товара
Для работы с API вам понадобятся токен авторизации и ID товара:

Откройте инструменты разработчика в вашем браузере (обычно нажатием клавиши F12).
Перейдите на сайт Читай-город и выполните необходимые операции (например, добавление товара в корзину).
На вкладке Network (Сеть) найдите запросы, отправляемые при добавлении товара в корзину.
В заголовках запроса найдите поле Authorization. Скопируйте токен вместе со словом Bearer и вставьте его в файл constants.py -> bearer_token
Чтобы найти ID товара, проверьте параметры запроса или ответ сервера. Обычно это поле id объекта товара. Вставьте его значение в файл test_api.py, функцию test_edit_cart -> items_to_update = [{'id': "здесь найденный ID товара"}]
## Запуск тестов API
Чтобы запустить тесты API, используйте следующую команду: pytest -k test_api.py

## Запуск тестов UI
Чтобы запустить тесты пользовательского интерфейса, используйте следующую команду: pytest -k test_ui.py

## Запуск всех тестов
Чтобы запустить все тесты в проекте, используйте следующую команду: pytest

## Запуск тестов в Visual Studio Code
Для удобства запуска тестов вы также можете использовать интерфейс Visual Studio Code.

Откройте проект: Запустите Visual Studio Code и откройте папку Chitai-gorod с проектом.
Откройте тестовый файл: В панели проводника (Explorer) нажмите вкладку Testing слева и откройте сразу все тесты проекта или отдельно файлы test_api.py и test_ui.py.
Запуск тестов:
Найдите кнопку "Запустить тесты" (Run Tests) в правом верхнем углу редактора (обычно это зелёная кнопка с изображением треугольника или надписью "Run").
Нажмите на эту кнопку, чтобы запустить выбранные тесты.
Просмотр результатов: После завершения тестов результаты будут отображены в панели Терминал или Результаты тестов.

ВАЖНО : обновление токена и ID товара нужно произвести до запуска тестов!!!
