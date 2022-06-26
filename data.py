import random
import string


letters = string.ascii_letters


def get_registered_user():
    return {
        "name": ''.join(random.choice(letters) for i in range (5)),
        "address": "17802 Glenn {}\nSouth Luke, SD 51308".format(''.join(random.choice(letters) for i in range (5))),
        "created_at": f"{random.randint(1990, 2022)}"
    }


if __name__ == "__main__":
    print(get_registered_user())
