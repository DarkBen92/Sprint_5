from conftest import driver, setup_user
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements_to_find import Locators
from data import Url


class TestPassageFromPersonalAccount:
    def test_passage_by_click_constructor(self, driver, setup_user):
        """Переход по клику на Конструктор."""
        email, password = setup_user
        driver.get(Url.URL_LOGIN)

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

        driver.find_element(*Locators.CONSTRUCTOR_HEADER).click()

        url = driver.current_url
        assert url == Url.URL_MAIN_PAGE

    def test_passage_by_click_logo(self, driver, setup_user):
        """Переход по клику на логотип Stellar Burgers."""
        email, password = setup_user
        driver.get(Url.URL_LOGIN)

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

        driver.find_element(*Locators.LOGO_HEADER).click()

        url = driver.current_url
        assert url == Url.URL_MAIN_PAGE
