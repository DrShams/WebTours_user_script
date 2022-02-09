##Скрипт для наполнения пользователей в файловой системе приложения WebTours 1.0
#Данный скрипт
        py user.py -rmall [y] - (all users will be deleted) \n\
        py user.py -add [number_of_users] - (previous users will be deleted) \n\
        py user.py -clear [y] - to clear all reservations")
    if usersremove_status == "y":
        usersremoveall()
    if users > 0:
        usergen(users)
    if clear_status == "y":
        userclear()

if __name__ == "__main__":
    main()
