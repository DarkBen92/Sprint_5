from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements_to_find import Locators
from data import Url


class TestConstructor:
    def test_passage_section_bread(self, driver):
        """Переход к разделу «Булки»"""
        driver.get(Url.URL_MAIN_PAGE)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT[1])))

        element = driver.find_element(*Locators.TEXT_BREAD)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CURRENT_SECTION[1])))

        ingredient = driver.find_element(*Locators.CURRENT_SECTION)
        assert ingredient.text == "Булки"

    def test_passage_section_sauce(self, driver):
        """Переход к разделу «Соусы»"""
        driver.get(Url.URL_MAIN_PAGE)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT[1])))

        element = driver.find_element(*Locators.TEXT_SAUCE)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CURRENT_SECTION[1])))

        ingredient = driver.find_element(*Locators.CURRENT_SECTION)
        assert ingredient.text == "Соусы"

    def test_passage_section_topping(self, driver):
        """Переход к разделу «Начинки»"""
        driver.get(Url.URL_MAIN_PAGE)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT[1])))

        element = driver.find_element(*Locators.TEXT_TOPPING)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CURRENT_SECTION[1])))

        ingredient = driver.find_element(*Locators.CURRENT_SECTION)
        assert ingredient.text == "Начинки"
