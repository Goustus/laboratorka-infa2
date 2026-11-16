from database import get_connection
from models.models import Guest

def _map(s) -> Guest:
    return Guest(guest_id=s[0],first_name=s[1],last_name=s[2],phone=s[3])

def create(first_name: str, last_name: str, phone: str):
    conn = get_connection()
    c=conn.cursor()
    c.execute("""
        insert into guest (first_name, last_name, phone)
        values (?, ?, ?)
    """, (first_name, last_name, phone))
    conn.commit()
    conn.close()

def get_by_id(guest_id: int) -> Guest | None:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select guest_id, first_name, last_name, phone
        from guest
        where guest_id = ?
    """, (guest_id,))
    s=c.fetchone()
    conn.close()
    return _map(s) if s else None

def get_all() -> list[Guest]:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select guest_id, first_name, last_name, phone
        from guest
    """)
    rows=c.fetchall()
    conn.close()
    return [_map(r) for r in rows]

def update(guest_id: int, first_name: str, last_name: str, phone: str):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        update guest
        set first_name = ?, last_name = ?, phone = ?
        where guest_id = ?
    """, (first_name, last_name, phone, guest_id))
    conn.commit()
    conn.close()

def delete(guest_id: int):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        delete from guest
        where guest_id = ?
    """, (guest_id,))
    conn.commit()
    conn.close()