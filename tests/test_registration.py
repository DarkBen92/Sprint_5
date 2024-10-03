from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements_to_find import Locators
from credentials_generators.personal_credentials_generators import generator_login_email, generator_password
from data import Url


class TestRegistration:
    def test_successful_registration(self, driver):
        """Успешная регистрация."""
        driver.get(Url.URL_REGISTRATION)

        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Тестовый пользователь")
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(generator_login_email())
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(generator_password())
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))

        url = driver.current_url
        assert url == Url.URL_LOGIN

    def test_invalid_password(self, driver):
        """Проверка ошибки для некорректного пароля"""
        driver.get(Url.URL_REGISTRATION)

        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Тестовый пользователь")
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(generator_login_email())
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys("12345")
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.ERROR_TEXT_INVALID_PASSWORD[1])))

        error_text = driver.find_element(*Locators.ERROR_TEXT_INVALID_PASSWORD)
        assert error_text.text == "Некорректный пароль"
