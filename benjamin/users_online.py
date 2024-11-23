from enum import Enum


class Status(Enum):
    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'


def get_number_of_online_users(input_dict):
    users_online = 0
    for key, value in input_dict.items():
        if str(value).upper() == Status.ONLINE.value:
            users_online += 1

    return users_online


def get_number_of_online_users2(input_dict2):
    users_online = {key: value
                    for key, value in input_dict2.items() if str(value).upper() == Status.ONLINE.value}
    return len(users_online.values())


if __name__ == "__main__":
    input_dict_data = {
        "Ananda": "online",
        "Chethana": "online",
        "Atharv": "offline",
        "Aarav": "offline"
    }

    users_online_out = get_number_of_online_users(input_dict_data)

    print(f"user online:{users_online_out}")
    users_online_out2 = get_number_of_online_users2(input_dict_data)

    print(f"user online:{users_online_out2}")
