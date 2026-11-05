from repositories import guest_repository
from models.models import Guest

def register_guest(first_name: str, last_name: str, phone: str):
    if not first_name.strip() or not last_name.strip():
        raise Exception("Имя и фамилия не могут быть пустыми!")
    if not phone.strip():
        raise Exception("Номер телефона обязателен для заполнения!")
        
    guest_repository.create(first_name, last_name, phone)

def get_all_guests() -> list[Guest]:
    return guest_repository.get_all()

def update_guest(guest_id: int, first_name: str, last_name: str, phone: str):
    guest = guest_repository.get_by_id(guest_id)
    if not guest:
        raise Exception("Гость не найден!")
        
    guest_repository.update(guest_id, first_name, last_name, phone)