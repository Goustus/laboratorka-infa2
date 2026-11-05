from services import user_services, room_services, booking_services, guest_services

def admin_menu(user):
    while True:
        print(f"\n===== МЕНЮ АДМИНИСТРАТОРА ({user.login}) =====")
        print("1. Показать все номера")
        print("2. Добавить номер")
        print("3. Показать все бронирования")
        print("4. Создать бронирование")
        print("5. Отменить бронирование")
        print("6. Добавить нового администратора")
        print("0. Выход")

        choice=input("Выберите действие: ")

        if choice=="1":
            rooms=room_services.get_all_rooms()
            print("\n--- Номера ---")
            for r in rooms:
                print(f"ID: {r.room_id} | №{r.number} | {r.type} | {r.price_per_day} руб. | {r.status}")
                
        elif choice == "2":
            try:
                number=input("Номер комнаты: ")
                r_type=input("Тип (Одноместный/Двухместный): ")
                price=float(input("Цена за сутки: "))
                room_services.create_room(number, r_type, price, "Свободен")
                print("Номер добавлен!")
            except Exception as e:
                print(f"Ошибка: {e}")
                
        elif choice=="3":
            bookings=booking_services.get_all_bookings()
            print("\n--- Бронирования ---")
            for b in bookings:
                print(f"ID: {b.booking_id} | Гость ID: {b.guest_id} | Номер ID: {b.room_id} | {b.check_in_date} - {b.check_out_date} | {b.total_price} руб. | {b.status}")
                
        elif choice=="4":
            try:
                guest_id=int(input("ID гостя: "))
                room_id=int(input("ID номера: "))
                check_in=input("Дата заезда (YYYY-MM-DD): ")
                check_out=input("Дата выезда (YYYY-MM-DD): ")
                booking_services.create_booking(guest_id, room_id, check_in, check_out)
                print("Бронирование успешно!")
            except Exception as e:
                print(f"Ошибка: {e}")
                
        elif choice=="5":
            try:
                b_id=int(input("ID бронирования для отмены: "))
                booking_services.cancel_booking(b_id)
                print("Бронирование отменено.")
            except Exception as e:
                print(f"Ошибка: {e}")
                
        elif choice=="6":
            login=input("Логин нового админа: ")
            password=input("Пароль: ")
            try:
                user_services.register_user(role_id=1, login=login, password=password)
                print("Администратор успешно добавлен!")
            except Exception as e:
                print(f"Ошибка: {e}")
                
        elif choice=="0":
            break

def client_menu(user):
    while True:
        print(f"\n===== МЕНЮ КЛИЕНТА ({user.login}) =====")
        print("1. Показать свободные номера")
        print("2. Забронировать номер")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        if choice == "0":
            break
        else:
            print("В разработке...")

def main():
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ОТЕЛЯ ===")
        print("1. Регистрация (как клиент)")
        print("2. Авторизация (Вход)")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice=="1":
            print("\n--- РЕГИСТРАЦИЯ КЛИЕНТА ---")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            try:
                user_services.register_user(role_id=2, login=login, password_hush=password)
                print("Успех! Теперь вы можете войти.")
            except Exception as e:
                print(f"Ошибка регистрации: {e}")
                
        elif choice=="2":
            print("\n--- АВТОРИЗАЦИЯ ---")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            try:
                logged_user = user_services.authenticate_user(login, password)
                print(f"Добро пожаловать, {logged_user.login}!")
                if logged_user.role_id == 1:
                    admin_menu(logged_user)
                else:
                    client_menu(logged_user)
            except Exception as e:
                print(f"Ошибка входа: {e}")
        elif choice=="0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__=="__main__":
    main()