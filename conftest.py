import pytest
from selenium import webdriver
from credentials_generators.personal_credentials_generators import generator_login_email, generator_password
from data import Url
from elements_to_find import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def setup_user(driver):
    driver.get(Url.URL_REGISTRATION)
    driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Тестовый пользователь")
    email = generator_login_email()
    driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
    password = generator_password()
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
    driver.find_element(*Locators.BUTTON_REGISTRATION).click()
    yield email, password
