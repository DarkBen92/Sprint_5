from conftest import driver, url_registration, url_main_page, url_forgot_password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements_to_find import Locators
from credentials_generators.personal_credentials_generators import generator_login_email, generator_password


class TestLoginInAccount:
    def test_sign_main_page_by_button_log_account(self, driver, url_registration, url_main_page):
        """Вход по кнопке «Войти в аккаунт» на главной странице."""
        driver.get(url_registration)

        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Тестовый пользователь")
        email = generator_login_email()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        password = generator_password()
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        driver.get(url_main_page)

        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_PLACE_AN_ORDER[1])))

        url = driver.current_url
        assert url == url_main_page

    def test_sign_main_page_personal_account(self, driver, url_registration, url_main_page):
        """Вход через кнопку «Личный кабинет»."""
        driver.get(url_registration)

        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Тестовый пользователь")
        email = generator_login_email()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        password = generator_password()
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        driver.get(url_main_page)

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_PLACE_AN_ORDER[1])))

        url = driver.current_url
        assert url == url_main_page

    def test_sign_registration_page(self, driver, url_registration, url_main_page):
        """Вход через кнопку в форме регистрации."""
        driver.get(url_registration)

        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Тестовый пользователь")
        email = generator_login_email()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        password = generator_password()
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        driver.get(url_registration)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_REGISTRATION_PAGE[1])))
        driver.find_element(*Locators.BUTTON_INPUT_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_PLACE_AN_ORDER[1])))

        url = driver.current_url
        assert url == url_main_page

    def test_sign_forgot_password_page(self, driver, url_registration, url_main_page, url_forgot_password):
        """Вход через кнопку в странице восстановления пароля."""
        driver.get(url_registration)

        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Тестовый пользователь")
        email = generator_login_email()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        password = generator_password()
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        driver.get(url_forgot_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_PASSWORD_RECOVERY_PAGE[1])))
        driver.find_element(*Locators.BUTTON_INPUT_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_PLACE_AN_ORDER[1])))

        url = driver.current_url
        assert url == url_main_page
