import allure
from api import login_user
from helpers import generate_user_payload

class TestUserLogin:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, registered_user):
        response = login_user(registered_user)
        
        assert response.status_code == 200
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()

    @allure.title("Вход с неверным логином и паролем")
    def test_login_wrong_credentials(self):
        invalid_payload = {
            "email": "wrong_email@yandex.ru",
            "password": "wrong_password"
        }
        
        response = login_user(invalid_payload)
        
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"