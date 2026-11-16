from database import get_connection
from models.models import Room

def _map(s) -> Room:
    return Room(room_id=s[0],number=s[1],type=s[2],price_per_day=s[3],status=s[4])


def create(number: str, type: str, price_per_day: float, status: str):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        insert into room (number, type, price_per_day, status)
        values (?, ?, ?, ?)
    """, (number, type, price_per_day, status))
    conn.commit()
    conn.close()


def get_by_id(room_id: int) -> Room | None:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select room_id, number, type, price_per_day, status
        from room
        where room_id = ?
    """, (room_id,))
    s=c.fetchone()
    conn.close()
    return _map(s) if s else None


def get_all() -> list[Room]:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select room_id, number, type, price_per_day, status
        from room
    """)
    k=c.fetchall()
    conn.close()
    return [_map(s) for s in k]
def update(room_id: int, status: str, price_per_day: float):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        update room
        set status = ?, price_per_day = ?
        where room_id = ?
    """, (status, price_per_day, room_id))
    conn.commit()
    conn.close()

def delete(room_id: int):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        delete from room
        where room_id = ?
    """, (room_id,))
    conn.commit()
    conn.close()