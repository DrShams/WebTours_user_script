# Скрипт для наполнения/удаления/очистки пользователей в файловой системе приложения WebTours 1.0

### Перед использованием установите все необходимые библиотеки (файл requirements.txt прилагается)

## Примеры использования
создать определенное количество пользователей:
> py user.py -add [number_of_users]

очистить данные все бронирования текущих пользователей
> py user.py -clear [y]

удалит всех пользователей в системе
> py user.py -rmall [y]


    if usersremove_status == "y":
        usersremoveall()
    if users > 0:
        usergen(users)
    if clear_status == "y":
        userclear()

if __name__ == "__main__":
    main()
