from repositories import user_repository, role_repository
from models.models import User

def register_user(role_id: int, login: str, password_hash: str):
    role = role_repository.get_by_id(role_id)
    if not role:
        raise Exception("Указанная роль не существует!")
    existing_user = user_repository.get_by_login(login)
    if existing_user:
        raise Exception("Пользователь с таким логином уже существует!")
    user_repository.create(role_id, login, password_hash)
    
def authenticate_user(login: str, password_hash: str) -> User:
    user = user_repository.get_by_login(login)
    if not user or user.password_hash != password_hash:
        raise Exception("Неверный логин или пароль")
    return user

def get_all_users() -> list[User]:
    return user_repository.get_all()