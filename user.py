import argparse
import csv
import random
import os
from string import ascii_letters

#CONFIG
LINES_TO_KEEP_NUM = 4
USERS_DIR_PATH = r"C:\Users\1\Desktop\Bell Integrator HighLoad_29_01\__Project WebTours\Web Tours 1.0\WebTours\cgi-bin\users"

#DAT_DIR_PATH = r"C:\Users\1\Documents\VuGen\Scripts\Shamsiev_6_20210206_authonly\\"
#DAT_DIR_PATH = r"C:\Users\1\Documents\VuGen\Scripts\Shamsiev_6_20210206_search\\"
#DAT_DIR_PATH = r"C:\Users\1\Documents\VuGen\Scripts\Shamsiev_6_20210208\\"
DAT_DIR_PATH = r"C:\Users\1\Desktop\Bell Integrator HighLoad_29_01\__Project WebTours\_scripts\_WebTours_JMeter\\"

PREFIX_NAME = "FJuser"

CSV_FILENAME = "Users.dat"
def create_csv_with_headers():
    csv_filename = os.path.join(DAT_DIR_PATH, CSV_FILENAME)
    with open(csv_filename, "w",newline='') as csvfile:
        headers_writer = csv.writer(csvfile, delimiter=",")
        headers = ['LOGIN', 'PWD', 'FIRSTNAME','LASTNAME','ADDRESS','ZIPCODE','CC','EXPDATE']
        headers_writer.writerow(headers)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="This script automates creation, removing and clearing user profiles."
    )
    parser.add_argument(
        "--create",
        type=int,
        help="Number of users profiles to create",
    )
    parser.add_argument(
        "--remove",
        action="store_true",
        help="Remove all user profiles",
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear all user reservations",
    )

    return parser.parse_args()


def remove_files(dir_path: str) -> int:
    filenames = [filename for filename in os.listdir(dir_path) if filename != "jojo"]
    os.remove(DAT_DIR_PATH + CSV_FILENAME)
    for filename in filenames:
        filepath = os.path.join(dir_path, filename)
        os.remove(filepath)
    return len(filenames)


def generate_user_profile(num) -> dict:
    return {
        "login": f"{PREFIX_NAME}{num}",
        "first_name": f"Agent{num}",
        "last_name": f"Smith{num}",
        "address": f"Address {num}",
        "password": f"pwd{''.join(random.sample(ascii_letters, k=8))}",
        "zip": f"0{random.randint(10000,99999)}",
        "cc": f"42760600{random.randint(10000000, 99999999)}",
        "cc_expires": "08/21",
    }


def write_user_profile(user: dict, dirpath: str) -> None:
    filepath = os.path.join(dirpath, user["login"])
    with open(filepath, "w") as file:
        user_fields = [
            user["password"],
            ";".join([user["first_name"], user["last_name"]]),
            user["address"],
            user["zip"],
            ";",
        ]
        file.write("\n".join(user_fields))


def clear_user_profiles(dir_path: str) -> None:
    filenames = [filename for filename in os.listdir(dir_path) if filename != "jojo"]
    for filename in filenames:
        filepath = os.path.join(dir_path, filename)

        with open(filepath, "r+") as file:
            lines_to_keep = [file.readline() for _ in range(LINES_TO_KEEP_NUM)]
            file.seek(0)
            file.truncate()
            file.writelines(lines_to_keep)
            file.writelines(";")

    return len(filenames)

def dump_to_csv(user: dict) -> None:
    csv_filename = os.path.join(DAT_DIR_PATH, CSV_FILENAME)
    with open(csv_filename, "a",newline='') as csvfile:#w
        user_writer = csv.writer(csvfile, delimiter=",")
        user_profile = [
            user["login"],
            user["password"],
            user["first_name"],
            user["last_name"],
            user["address"],
            user["zip"],
            user["cc"],
            user["cc_expires"],
        ]
        user_writer.writerow(user_profile)

def main():
    os.makedirs(USERS_DIR_PATH, exist_ok=True)#?????????????? ??????????
    os.makedirs(DAT_DIR_PATH, exist_ok=True)

    args = parse_args() #?????????? ?????????????????? ?? ???????????????? ???? ?????????????? ????????????
    to_remove: bool = args.remove
    to_clear: bool = args.clear
    users_to_create: int = args.create

    if to_remove:       #???????? py user.py --remove
        files_removed = remove_files(USERS_DIR_PATH)
        print(f"{files_removed} files deleted")

    if to_clear:
        profiles_cleared = clear_user_profiles(USERS_DIR_PATH)
        print(f"{profiles_cleared} profiles cleared")

    if users_to_create:
        create_csv_with_headers()#???????????????? ?????????????????? ?????? .dat ??????????
        for num in range(users_to_create):
            user = generate_user_profile(num)
            write_user_profile(user, USERS_DIR_PATH)
            dump_to_csv(user)
        print(f"{users_to_create} user profiles have been created.")


if __name__ == "__main__":
    main()
