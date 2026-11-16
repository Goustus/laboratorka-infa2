from database import get_connection
from models.models import User

def _map(s) -> User:
    return User(user_id=s[0],role_id=s[1],login=s[2],password_hash=s[3])

def create(role_id: int, login: str, password_hash: str):
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        insert into user (role_id, login, password_hash)
        values (?, ?, ?)
    """, (role_id, login, password_hash))
    conn.commit()
    conn.close()

def get_by_id(user_id: int) -> User | None:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select user_id, role_id, login, password_hash
        from user
        where user_id = ?
    """, (user_id,))
    s=c.fetchone()
    conn.close()
    return _map(s) if s else None

def get_by_login(login: str) -> User | None:
    conn=get_connection()
    c=conn.cursor()
    c.execute("""
        select user_id, role_id, login, password_hash
        from user
        where login = ?
    """, (login,))
    s=c.fetchone()
    conn.close()
    return _map(s) if s else None

def get_all() -> list[User]:
    conn = get_connection()
    c=conn.cursor()
    c.execute("""
        select user_id, role_id, login, password_hash
        from user
    """)
    rows=c.fetchall()
    conn.close()
    return [_map(r) for r in rows]