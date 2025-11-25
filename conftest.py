import pytest
from selenium import webdriver
import requests
from faker import Faker
from url import Url
from pages.base_page import BasePage


def pytest_addoption(parser):
    """Добавляет параметр --browser для выбора браузера (по умолчанию: chrome)."""
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def browser(request):
    """Фикстура для запуска браузера (Chrome или Firefox)."""
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def created_user():
    """Создаёт тестового пользователя через API и возвращает его данные."""
    fake = Faker(locale='ru_RU')
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    requests.post(f'{Url.create_user}', json=user_data)
    return user_data


@pytest.fixture
def logged_in_browser(browser, created_user):
    """Выполняет авторизацию пользователя через UI и возвращает сессию браузера."""
    browser.get(Url.url_page)
    base_page = BasePage(browser)
    base_page.login(created_user["email"], created_user["password"])
    yield browser