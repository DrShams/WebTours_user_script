#!/usr/bin/python3

import pandas as pd
import random
import os
#import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-rmall', type=str, default="n", help="remove all accounts")
parser.add_argument('-add', type=int, default=0, help="add user files")
parser.add_argument('-clear', type=str, default="n", help="clear all reservations")

args = parser.parse_args()

usersremove_status = args.rmall #-rmall [y/n]
users = args.add                #-add [num]
clear_status = args.clear       #-clear  [y/n]

#CONFIG
LINES_TO_KEEP = 5           #сколько строк оставим в аккаунте после чистки

#отредактировать путь
path_users = r"C:\Users\1\Desktop\Bell Integrator HighLoad_29_01\__Project WebTours\Web Tours 1.0\WebTours\cgi-bin\users"#путь к файлу с юзерами
#менять взависимости от кол-ва скриптов
#path_dat = r"C:\Users\1\Documents\VuGen\Scripts\Shamsiev_6_20210208\Users.dat"#путь к файлу LoadRunner
#prefixname = "Auser" #2 -> 5
#path_dat = r"C:\Users\1\Documents\VuGen\Scripts\Shamsiev_6_20210206_search\Users.dat"#путь к файлу LoadRunner
#prefixname = "Buser" # 4 -> 10
path_dat = r"C:\Users\1\Documents\VuGen\Scripts\Shamsiev_6_20210206_authonly\Users.dat"#путь к файлу LoadRunner
prefixname = "Cuser" # 14 -> 35

def usersremoveall():
    """Example of usage: py user.py -rmall [y]"""
    filelist = [f for f in os.listdir(path_users)]
    x = 0
    for f in filelist:
        if f != "jojo":#all but jojo ))
            x += 1
            path_user = os.path.join(path_users, f)
            os.remove(path_user)
    print(str(x) + " users has been deleted")

#Clear all users from directory
def usergen(lp):
    """Example of usage: py user.py -add [number_of_users]"""

    chars_numbers = '1234567890'#комбинация паролей
    chars_login = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'#комбинация логинов
    #lp = int(sys.argv[1])
    #lp = int(input('Кол-во логинов и паролей?'+ "\n"))#генерируем кол-во логин-паролей

    login_list = list()
    pass_list = list()
    fname_list = list()
    lname_list = list()
    address_list = list()
    zipcode_list = list()
    expdate_list = list()#add !!"""
    cc_list = list()
    for x,n in enumerate(range(lp)):
        #PWD-ZIPCODE-CC
        password ='pwd'   #по дефолту
        zipcode = '0'
        cc = '42760600'
        for i in range(8):  #длина логина или пароля + 8
            password += random.choice(chars_numbers)
            zipcode += random.choice(chars_numbers)
            cc += random.choice(chars_numbers)
        pass_list.append(password)
        zipcode_list.append(zipcode)
        cc_list.append(cc)
        #LOGIN-FIRSTNAME-LASTNAME-ADDRESS
        login = prefixname + str(x) #LOGIN
        firstname = "Agent" + str(x)
        lastname = "Smith" + str(x)
        address = "Address " + str(x)
        fname_list.append(firstname)
        lname_list.append(lastname)
        address_list.append(address)
        login_list.append(login)
        #
        expdate_list.append("08/21")
        """собираем тело файла для каждого юзера: save and close"""
        #print(login,password)
        block = password+"\n"+firstname+";"+lastname+"\n"+address+"\n"+zipcode+"\n;"
        file = open(path_users + "\\" + login, 'w', encoding='utf-8')#\ - and \ !!!
        file.write(block)
        file.close()

    #Создаем таблицу
    data = {
    "LOGIN": login_list,
    "PWD": pass_list,
    "FIRSTNAME": fname_list,
    "LASTNAME": lname_list,
    "ADDRESS": address_list,
    "ZIPCODE": zipcode_list,
    "CC": cc_list,
    "EXPDATE": expdate_list}
    df = pd.DataFrame(data)
    print(df)
    df.to_csv(path_dat,index=False)#синхронизация в .dat file

def userclear():
    """Example of usage: py user.py -clear [y/n]"""
    filelist = [f for f in os.listdir(path_users)]
    x = 0
    for f in filelist:
        if f != "jojo":#all but jojo ))
            x += 1
            path_user = os.path.join(path_users, f)
            with open(path_user, "r+") as file:
                numlines = [file.readline() for _ in range(LINES_TO_KEEP)]
                file.seek(0)
                file.truncate()
                file.writelines(numlines)
    print(str(x) + " accounts has been reset")

def main():
    if users == 0 and clear_status != "y" and usersremove_status != "y":
        print("Usage:\n\
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
