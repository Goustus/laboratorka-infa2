from database import get_connection
from models.models import Booking

def _map(s) -> Booking:
    return Booking(booking_id=s[0],guest_id=s[1],room_id=s[2],check_in_date=s[3],check_out_date=s[4],total_price=s[5],status=s[6])

def create(guest_id: int, room_id: int, check_in_date: str, check_out_date: str, total_price: float, status: str):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        insert into booking (guest_id, room_id, check_in_date, check_out_date, total_price, status)
        values (?, ?, ?, ?, ?, ?)
    """, (guest_id, room_id, check_in_date, check_out_date, total_price, status))
    conn.commit()
    conn.close()

def get_by_id(booking_id: int) -> Booking | None:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select booking_id, guest_id, room_id, check_in_date, check_out_date, total_price, status
        from booking
        where booking_id = ?
    """, (booking_id,))
    s=c.fetchone()
    conn.close()
    return _map(s) if s else None

def get_all() -> list[Booking]:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select booking_id, guest_id, room_id, check_in_date, check_out_date, total_price, status
        from booking
    """)
    rows=c.fetchall()
    conn.close()
    return [_map(r) for r in rows]

def update_status(booking_id: int, status: str):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        update booking
        set status = ?
        where booking_id = ?
    """, (status, booking_id))
    conn.commit()
    conn.close()

def delete(booking_id: int):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        delete from booking
        where booking_id = ?
    """, (booking_id,))
    conn.commit()
    conn.close()