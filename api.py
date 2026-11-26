import requests
import allure
from data import BASE_URL
import endpoints

# --- ПОЛЬЗОВАТЕЛИ ---

@allure.step("Регистрация пользователя")
def register_user(payload):
    return requests.post(f'{BASE_URL}{endpoints.REGISTER}', json=payload)

@allure.step("Авторизация пользователя")
def login_user(payload):
    return requests.post(f'{BASE_URL}{endpoints.LOGIN}', json=payload)

@allure.step("Удаление пользователя")
def delete_user(access_token):
    headers = {"Authorization": access_token}
    return requests.delete(f'{BASE_URL}{endpoints.USER}', headers=headers)


# --- ЗАКАЗЫ ---

@allure.step("Получение списка ингредиентов")
def get_ingredients():
    return requests.get(f'{BASE_URL}{endpoints.INGREDIENTS}')

@allure.step("Создание заказа (авторизованный)")
def create_order_auth(payload, access_token):
    headers = {"Authorization": access_token}
    return requests.post(f'{BASE_URL}{endpoints.ORDERS}', json=payload, headers=headers)

@allure.step("Создание заказа (неавторизованный)")
def create_order_unauth(payload):
    return requests.post(f'{BASE_URL}{endpoints.ORDERS}', json=payload)

@allure.step("Получение заказов пользователя")
def get_user_orders(access_token):
    headers = {"Authorization": access_token}
    return requests.get(f'{BASE_URL}{endpoints.ORDERS}', headers=headers)

@allure.step("Получение всех заказов")
def get_all_orders():
    return requests.get(f'{BASE_URL}{endpoints.ORDERS_ALL}')