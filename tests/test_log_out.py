from conftest import driver, setup_user
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements_to_find import Locators
from data import Url


class TestLogOut:
    def test_log_out_by_button_exit(self, driver, setup_user):
        """Выход из аккаунта по кнопке «Выйти»."""
        email, password = setup_user
        driver.get(Url.URL_LOGIN)

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_PLACE_AN_ORDER[1])))

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_PAGE_PERSONAL_ACCOUNT[1])))

        driver.find_element(*Locators.BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TITLE_LOGIN_PAGE[1])))

        url = driver.current_url
        assert url == Url.URL_LOGIN
