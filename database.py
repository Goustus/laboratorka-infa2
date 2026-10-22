import sqlite3
db=sqlite3.connect('hotel.db')
c=db.cursor()
c.execute("PRAGMA foreign_keys = ON;")

c.execute("""CREATE TABLE Room (
    room_id integer primary key autoincrement,
    number text not null,
    type text not null,
    price_per_day real not null,
    status text not null
)""")

c.execute("""CREATE TABLE Client (
    client_id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    phone text not null
)""")

c.execute("""CREATE TABLE Booking (
    booking_id integer primary key autoincrement,
    client_id integer not null,
    room_id integer not null,
    check_in_date text not null,
    check_out_date text not null,
    total_price REAL not null,
    foreign key (client_id) references Client (client_id),
    foreign key (room_id) references Room (room_id)
)""")

c.execute("INSERT INTO Room (number, type, price_per_day, status) VALUES ('101', 'Одноместный', 2500.0, 'Свободен')")
c.execute("INSERT INTO Room (number, type, price_per_day, status) VALUES ('102', 'Двухместный', 4000.0, 'Занят')")
c.execute("INSERT INTO Client (first_name, last_name, phone) VALUES ('Иван', 'Иванов', '+79524732988')")
c.execute("INSERT INTO Client (first_name, last_name, phone) VALUES ('Пётр', 'Петров', '+78005553535')")
c.execute("INSERT INTO Booking (client_id, room_id, check_in_date, check_out_date, total_price) VALUES (1, 2, '2026-11-01', '2026-11-05', 16000.0)")

db.commit()
db.close()