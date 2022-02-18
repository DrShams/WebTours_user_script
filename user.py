import argparse
import csv
import random
import os
from string import ascii_letters


LINES_TO_KEEP_NUM = 4
USERS_DIR_PATH = "users"
DAT_DIR_PATH = "data"
PREFIX_NAME = "Cuser"
CSV_FILENAME = "dat"
# path_users = r"C:\Users\1\Desktop\Bell Integrator HighLoad_29_01\__Project WebTours\Web Tours 1.0\WebTours\cgi-bin\users"  # путь к файлу с юзерами
# path_dat = r"C:\Users\1\Documents\VuGen\Scripts\Shamsiev_6_20210206_authonly\Users.dat"  # путь к файлу LoadRunner


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--create", type=int, help="Number of users profiles to create")
    parser.add_argument("--remove", default="n", help="Remove all user profiles")
    parser.add_argument("--clear", default="n", help="Clear all user reservations")

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


def dump_to_csv(user: dict) -> None:
    csv_filename = os.path.join(DAT_DIR_PATH, CSV_FILENAME)
    with open(csv_filename, "a") as csvfile:
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
    os.makedirs(USERS_DIR_PATH, exist_ok=True)
    os.makedirs(DAT_DIR_PATH, exist_ok=True)

    args = parse_args()
    to_remove = args.remove
    to_clear = args.clear
    to_create = args.create

    files_removed = remove_files(USERS_DIR_PATH)
    print(f"{files_removed} files deleted")
    for _ in range(10):
        user = generate_user_profile()
        write_user_profile(user, USERS_DIR_PATH)
        dump_to_csv(user)
    clear_user_profiles(USERS_DIR_PATH)


if __name__ == "__main__":
    main()
