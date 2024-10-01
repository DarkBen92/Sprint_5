from conftest import driver, setup_user
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements_to_find import Locators
from data import Url


class TestLoginInAccount:
    def test_sign_main_page_by_button_log_account(self, driver, setup_user):
        """Вход по кнопке «Войти в аккаунт» на главной странице."""
        email, password = setup_user
        driver.get(Url.URL_MAIN_PAGE)

        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_PLACE_AN_ORDER[1])))

        url = driver.current_url
        assert url == Url.URL_MAIN_PAGE

    def test_sign_main_page_personal_account(self, driver, setup_user):
        """Вход через кнопку «Личный кабинет»."""
        email, password = setup_user
        driver.get(Url.URL_MAIN_PAGE)

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_PLACE_AN_ORDER[1])))

        url = driver.current_url
        assert url == Url.URL_MAIN_PAGE

    def test_sign_registration_page(self, driver, setup_user):
        """Вход через кнопку в форме регистрации."""
        email, password = setup_user
        driver.get(Url.URL_REGISTRATION)

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_REGISTRATION_PAGE[1])))
        driver.find_element(*Locators.BUTTON_INPUT_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_PLACE_AN_ORDER[1])))

        url = driver.current_url
        assert url == Url.URL_MAIN_PAGE

    def test_sign_forgot_password_page(self, driver, setup_user):
        """Вход через кнопку в странице восстановления пароля."""
        email, password = setup_user
        driver.get(Url.URL_FORGOT_PASSWORD)

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
        assert url == Url.URL_MAIN_PAGE
