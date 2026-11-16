from database import get_connection
from models.models import Role

def _map(s) -> Role:
    return Role(role_id=s[0],role_name=s[1])

def create(role_name: str):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        insert into role (role_name)
        values (?)
    """, (role_name,))
    conn.commit()
    conn.close()

def get_by_id(role_id: int) -> Role | None:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select role_id, role_name
        from role
        where role_id = ?
    """, (role_id,))
    s=c.fetchone()
    conn.close()
    return _map(s) if s else None

def get_all() -> list[Role]:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select role_id, role_name
        from role
    """)
    rows=c.fetchall()
    conn.close()
    return [_map(r) for r in rows]