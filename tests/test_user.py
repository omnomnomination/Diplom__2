import allure
from api import register_user
from helpers import generate_user_payload

class TestUserCreation:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, user_cleanup):
        payload = generate_user_payload()
        
        response = user_cleanup(payload)
        
        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_duplicate_user(self, registered_user):
        response = register_user(registered_user)
        
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_missing_field(self):
        payload = generate_user_payload()
        del payload["password"]
        
        response = register_user(payload)
        
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"