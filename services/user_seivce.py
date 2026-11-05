from repositories import user_repository, role_repository
from models.models import User

def authenticate(login: str, password_hash: str):
    #логин
    user = user_repository.get_by_login(login)
    if not user:
        raise Exception("Пользователь с таким логином не найден!")
    #пароль
    if user.password_hash != password_hash:
        raise Exception("Неверный пароль!")
    return user