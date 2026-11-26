# Пользователи и Авторизация
REGISTER = '/api/auth/register'        # POST: Регистрация
LOGIN = '/api/auth/login'              # POST: Авторизация
USER = '/api/auth/user'                # GET: Получить данные, PATCH: Обновить, DELETE: Удалить
LOGOUT = '/api/auth/logout'            # POST: Выход из системы
TOKEN = '/api/auth/token'              # POST: Обновление токена

# Заказы
ORDERS = '/api/orders'                 # POST: Создать заказ, GET: Получить заказы пользователя
ORDERS_ALL = '/api/orders/all'         # GET: Получить все заказы (лента)

# Ингредиенты
INGREDIENTS = '/api/ingredients'       # GET: Получить список ингредиентов

# Восстановление пароля
PASSWORD_RESET = '/api/password-reset' # POST: Запрос на сброс пароля
PASSWORD_RESET_RESET = '/api/password-reset/reset' # POST: Установка нового пароля