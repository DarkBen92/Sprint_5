from conftest import driver, url_registration, url_account_profile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements_to_find import Locators
from credentials_generators.personal_credentials_generators import generator_login_email, generator_password


class TestPassageInPersonalAccount:
    def test_passage_in_personal_account_by_click(self, driver, url_registration, url_account_profile):
        """Перехода по клику на Личный Кабинет"""
        driver.get(url_registration)

        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Тестовый пользователь")
        email = generator_login_email()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        password = generator_password()
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_PLACE_AN_ORDER[1])))

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_PAGE_PERSONAL_ACCOUNT[1])))

        url = driver.current_url
        assert url == url_account_profile
