import random

def generate_user_payload():
    # Генерируем случайный email, чтобы каждый раз был уникальный юзер
    random_email = f"test_{random.randint(1000, 9999)}@yandex.ru"
    payload = {
        "email": random_email,
        "password": "password",
        "name": "Username"
    }
    return payload