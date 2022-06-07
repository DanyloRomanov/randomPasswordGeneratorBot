import random
import string


def generate_secure_password():
    r_n_1 = random.randint(100, 999)
    r_n_2 = random.randint(100, 999)
    r_upper_l_1 = random.choice(string.ascii_uppercase)
    r_lower_l_1 = random.choice(string.ascii_lowercase)
    r_l_1 = random.choice(string.ascii_letters)
    r_special_ch = random.choice(string.punctuation)

    return f'{r_l_1}{r_n_1}{r_special_ch}{r_lower_l_1}{r_n_2}{r_upper_l_1}'

