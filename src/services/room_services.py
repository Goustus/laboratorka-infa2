from repositories import room_repository
from models.models import Room

def create_room(number: str, type: str, price_per_day: float, status: str):
    if price_per_day <= 0:
        raise Exception("Цена за день должна быть больше нуля!")
    all_rooms = room_repository.get_all()
    for r in all_rooms:
        if r.number == number:
            raise Exception(f"Комната с номером {number} уже существует!") 
    room_repository.create(number, type, price_per_day, status)

def get_all_rooms() -> list[Room]:
    return room_repository.get_all()

def update_room_info(room_id: int, status: str, price_per_day: float):
    room = room_repository.get_by_id(room_id)
    if not room:
        raise Exception("Комната не найдена!")
    if price_per_day <= 0:
        raise Exception("Цена не может быть отрицательной!")
    room_repository.update(room_id, status, price_per_day)