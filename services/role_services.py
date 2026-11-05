from repositories import role_repository
from models.models import Role

def create_role(role_name: str):
    if not role_name.strip():
        raise Exception("Название роли не может быть пустым!")
    role_repository.create(role_name)

def get_all_roles() -> list[Role]:
    return role_repository.get_all()