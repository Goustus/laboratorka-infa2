from services import user_service

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

        choice = input("Выберите действие: ")

        if choice == "0":
            break
        elif choice == "6":
            login = input("Логин нового админа: ")
            password = input("Пароль: ")
            try:
                user_service.register_user(role_id=1, login=login, password=password)
                print("Администратор успешно добавлен!")
            except Exception as e:
                print(f"Ошибка: {e}")
        else:
            print("В разработке...")

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
        
        if choice == "1":
            print("\n--- РЕГИСТРАЦИЯ КЛИЕНТА ---")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            try:
                user_service.register_user(role_id=2, login=login, password=password)
                print("Успех! Теперь вы можете войти.")
            except Exception as e:
                print(f"Ошибка регистрации: {e}")
                
        elif choice == "2":
            print("\n--- АВТОРИЗАЦИЯ ---")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            try:
                logged_user = user_service.authenticate_user(login, password)
                print(f"Добро пожаловать, {logged_user.login}!")
                if logged_user.role_id == 1:
                    admin_menu(logged_user)
                else:
                    client_menu(logged_user)
            except Exception as e:
                print(f"Ошибка входа: {e}")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()