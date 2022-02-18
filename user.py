import argparse
import random
import os
from string import ascii_letters

import pandas as pd

LINES_TO_KEEP_NUM = 4
USERS_DIR_PATH = "users"
DAT_DIR_PATH = "data"
PREFIX_NAME = "Cuser"
CSV_FILENAME = "dat"
# path_users = r"C:\Users\1\Desktop\Bell Integrator HighLoad_29_01\__Project WebTours\Web Tours 1.0\WebTours\cgi-bin\users"  # путь к файлу с юзерами
# path_dat = r"C:\Users\1\Documents\VuGen\Scripts\Shamsiev_6_20210206_authonly\Users.dat"  # путь к файлу LoadRunner


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-rmall", default="n", help="remove all accounts")
    parser.add_argument("-add", type=int, default=0, help="add user files")
    parser.add_argument("-clear", default="n", help="clear all reservations")

    return parser.parse_args()


def remove_files(dir_path: str) -> int:
    filenames = [filename for filename in os.listdir(dir_path) if filename != "jojo"]

    for filename in filenames:
        filepath = os.path.join(dir_path, filename)
        os.remove(filepath)

    return len(filenames)


def generate_user_profile() -> dict:
    return {
        "login": f"{PREFIX_NAME}{random.randint(1000, 9999)}",
        "first_name": f"Agent{random.randint(1, 9)}",
        "last_name": f"Smith{random.randint(1, 9)}",
        "address": f"Address {random.randint(10, 99)}",
        "password": f"pwd{''.join(random.sample(ascii_letters, k=8))}",
        "zip": f"0{random.randint(1, 9)}",
        "cc": f"42760600{random.randint(1, 9)}",
        "cc_expires": "08/21",
    }


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
    usersremove_status = args.rmall #-rmall [y/n]
    users = args.add                #-add [num]
    clear_status = args.clear       #-clear  [y/n]

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
