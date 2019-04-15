import random
import string


def password(length = 10, special = 3):
    passwd_chars = []
    normal_chars = string.ascii_letters + string.digits
    special_chars = string.punctuation
    for i in range(0, length-special):
        passwd_chars.append(random.choice(normal_chars))
    for i in range(0,special):
        passwd_chars.append(random.choice(special_chars))
    random.shuffle(passwd_chars)
    return "".join(passwd_chars)
