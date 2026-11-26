import pytest
import allure
from api import create_order_auth, create_order_unauth
from data import VALID_INGREDIENTS, INVALID_INGREDIENTS


class TestOrderCreation:

    @allure.title("Создание заказа с авторизацией и с ингредиентами")
    def test_create_order_auth_with_ingredients(self, auth_token):

        payload = {"ingredients": VALID_INGREDIENTS}
        
        response = create_order_auth(payload, auth_token)
        
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без авторизации")
    @pytest.mark.xfail(reason="Баг API: заказ создается без авторизации (ожидается 401, по факту 200)")
    def test_create_order_unauthorized(self):
        payload = {"ingredients": VALID_INGREDIENTS}
        
        response = create_order_unauth(payload)
        
        assert response.status_code == 401  # <- Мы оставляем ПРАВИЛЬНЫЙ ассерт!

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, auth_token):
        payload = {"ingredients": []}
        
        response = create_order_auth(payload, auth_token)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(self, auth_token):
        payload = {"ingredients": INVALID_INGREDIENTS}
        
        response = create_order_auth(payload, auth_token)

        assert response.status_code == 500