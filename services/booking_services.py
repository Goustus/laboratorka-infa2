from repositories import booking_repository, room_repository, guest_repository
from models.models import Booking
from datetime import datetime

def create_booking(guest_id: int, room_id: int, check_in: str, check_out: str):

    guest=guest_repository.get_by_id(guest_id)
    if not guest:
        raise Exception("Гость с таким ID не найден!")


    room=room_repository.get_by_id(room_id)
    if not room:
        raise Exception("Комната не найдена!")
    if room.status != "Свободен":
        raise Exception(f"Комната №{room.number} в данный момент недоступна для бронирования.")
    #время
    try:
        check_in=datetime.strptime(check_in, "%Y-%m-%d")
        check_out=datetime.strptime(check_out, "%Y-%m-%d")
    except Exception:
        raise Exception("Неверный формат даты! Используйте формат ГГГГ-ММ-ДД.")
    if check_in>=check_out:
        raise Exception("Дата выезда должна быть строго позже даты заезда!")
    if check_in.date() < datetime.now().date():
        raise Exception("Нельзя забронировать номер на прошедшую дату!")
    #стоимость
    days=(check_out - check_in).days
    total_price=days*room.price_per_day
    booking_repository.create(guest_id=guest_id,room_id=room_id,check_in_date=check_in.strftime("%Y-%m-%d"),check_out_date=check_out.strftime("%Y-%m-%d"),total_price=total_price,status="Забронировано")
    room_repository.update(room_id=room_id, status="Занято", price_per_day=room.price_per_day)

def get_all_bookings()->list[Booking]:
    return booking_repository.get_all()

def cancel_booking(booking_id: int):
    booking = booking_repository.get_by_id(booking_id)
    if not booking:
        raise Exception("Бронирование не найдено!")
    if booking.status == "Отменено":
        raise Exception("Это бронирование уже отменено.")
    booking_repository.update_status(booking_id, "Отменено")
    #освободить комнату
    room = room_repository.get_by_id(booking.room_id)
    if room:
        room_repository.update(room.room_id, "Свободен", room.price_per_day)