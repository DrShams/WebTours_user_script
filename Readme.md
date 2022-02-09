# Скрипт для наполнения/удаления/очистки пользователей в файловой системе приложения WebTours 1.0

## Перед использованием
### Установите все необходимые библиотеки (файл requirements.txt прилагается)

## Примеры использования
> py user.py -add [number_of_users] 
(создаст определенное количество пользователей) \n\

> py user.py -clear [y]
очистить данные все бронирования текущих пользователей) \n\

> py user.py -rmall [y] 
удалит всех пользователей в системе) \n\


    if usersremove_status == "y":
        usersremoveall()
    if users > 0:
        usergen(users)
    if clear_status == "y":
        userclear()

if __name__ == "__main__":
    main()
