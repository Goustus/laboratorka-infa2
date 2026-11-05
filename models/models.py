from dataclasses import dataclass

@dataclass
class Room:
    room_id: int
    number: str
    type: str
    price_per_day: float
    status: str

@dataclass
class Guest:
    guest_id: int
    first_name: str
    last_name: str
    phone: str

@dataclass
class Role:
    role_id: int
    role_name: str

@dataclass
class User:
    user_id: int
    role_id: int
    login: str
    password_hash: str
    # Служебное/вычисляемое поле (если потребуется выводить название роли текстом)
    role_name: str | None = None

@dataclass
class Booking:
    booking_id: int
    guest_id: int
    room_id: int
    check_in_date: str
    check_out_date: str
    total_price: float
    status: str
    # Вычисляемые поля для удобства отображения в интерфейсе
    guest_full_name: str | None = None
    room_number: str | None = None