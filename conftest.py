import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def url_registration():
    url = "https://stellarburgers.nomoreparties.site/register"
    return url


@pytest.fixture
def url_main_page():
    url = "https://stellarburgers.nomoreparties.site/"
    return url


@pytest.fixture
def url_forgot_password():
    url = "https://stellarburgers.nomoreparties.site/forgot-password"
    return url


@pytest.fixture
def url_account_profile():
    url = "https://stellarburgers.nomoreparties.site/account/profile"
    return url


@pytest.fixture
def url_login():
    url = "https://stellarburgers.nomoreparties.site/login"
    return url
