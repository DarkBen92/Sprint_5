"""Генератор логина и пароля."""

import random
import string
from faker import Faker

random_fake = Faker("ru-Ru")


def generator_login_email():
    """Генерация email."""
    random_int = ''.join(random.sample(string.digits, 3))
    first_name = random_fake.first_name_male().lower()
    last_name = random_fake.last_name_male().lower()
    cohort_number = 14
    email = f"{first_name}{last_name}{cohort_number}{random_int}@yandex.ru"
    return email


def generator_password():
    """Генерация пароля."""
    symbols = string.ascii_letters + string.digits
    password = ''.join(random.sample(symbols, 10))
    return password
