from selenium.webdriver.common.by import By


class Locators:
    NAME_INPUT_FIELD = By.XPATH, "//label[text()='Имя']/parent::div/input"  # Поле для имени
    EMAIL_INPUT_FIELD = By.XPATH, "//label[text()='Email']/parent::div/input"  # Поле для email
    PASSWORD_INPUT_FIELD = By.XPATH, "//label[text()='Пароль']/parent::div/input"  # Поле для пароля
    BUTTON_REGISTRATION = By.XPATH, ".//button[text()='Зарегистрироваться']"  # Кнопка "Зарегистрироваться"
    TITLE_LOGIN_PAGE = By.XPATH, "//h2[text()='Вход']"  # Заголовок страницы входа
    TITLE_REGISTRATION_PAGE = By.XPATH, "//h2[text()='Регистрация']"  # Заголовок страницы регистрации
    ERROR_TEXT_INVALID_PASSWORD = By.XPATH, "//p[text()='Некорректный пароль']"  # Текст ошибки о некорректном пароле
    BUTTON_LOG_IN_TO_YOUR_ACCOUNT = By.XPATH, ".//button[text()='Войти в аккаунт']/parent::div/button"  # Кнопка "Войти в аккаунт"
    BUTTON_INPUT = By.XPATH, ".//button[text()='Войти']"  # Кнопка "Войти"
    BUTTON_PLACE_AN_ORDER = By.XPATH, "//button[text()='Оформить заказ']/parent::div/button"  # Кнопка "Оформить заказ"
    PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']/parent::a"  # Личный кабинет
    BUTTON_INPUT_LOGIN = By.XPATH, "//a[text()='Войти']"  # Кнопка "Войти" для перехода на страницу входа
    TITLE_PASSWORD_RECOVERY_PAGE = By.XPATH, "//h2[text()='Восстановление пароля']"  # Заголовок страницы восстановление пароля
    TEXT_PAGE_PERSONAL_ACCOUNT = By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']"  # Текст страницы профиля
    CONSTRUCTOR_HEADER = By.XPATH, "//p[text()='Конструктор']/parent::a"  # Конструктор
    LOGO_HEADER = By.XPATH, "//div/a/*[name()='svg']"  # Логотип
    BUTTON_EXIT = By.XPATH, "//button[text()='Выход']"  # Кнопка "Выход"
    TEXT_BREAD = By.XPATH, "//h2[text()='Булки']"  # Текст "Булки"
    TEXT_SAUCE = By.XPATH, "//h2[text()='Соусы']"  # Текст "Соусы"
    TEXT_TOPPING = By.XPATH, "//h2[text()='Начинки']"  # Текст "Начинки"
    CURRENT_SECTION = By.XPATH, "//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"  # Выбранный раздела бургера
