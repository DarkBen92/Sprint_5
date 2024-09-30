from conftest import driver, url_main_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from elements_to_find import Locators


class TestConstructor:
    def test_passage_section_bread(self, driver, url_main_page):
        """Переход к разделу «Булки»"""
        driver.get(url_main_page)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT[1])))

        element = driver.find_element(*Locators.TEXT_BREAD)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        num_ingredients = len(driver.find_elements(By.XPATH, "//section[1]/div[2]/ul[1]/a"))
        assert num_ingredients == 2

    def test_passage_section_sauce(self, driver, url_main_page):
        """Переход к разделу «Соусы»"""
        driver.get(url_main_page)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT[1])))

        element = driver.find_element(*Locators.TEXT_SAUCE)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        num_ingredients = len(driver.find_elements(By.XPATH, "//section[1]/div[2]/ul[2]/a"))
        assert num_ingredients == 4

    def test_passage_section_topping(self, driver, url_main_page):
        """Переход к разделу «Начинки»"""
        driver.get(url_main_page)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT[1])))

        element = driver.find_element(*Locators.TEXT_TOPPING)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        num_ingredients = len(driver.find_elements(By.XPATH, "//section[1]/div[2]/ul[3]/a"))
        assert num_ingredients == 9
