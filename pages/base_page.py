from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from locators.base_locators import BaseLocators
import allure


class BasePage:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.locators = BaseLocators()

    @allure.step('Открыть страницу по URL')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Дождаться видимости элемента')
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Дождаться исчезновения элемента')
    def wait_for_element_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Дождаться кликабельности элемента')
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Выполнить клик по элементу')
    def click_on_element(self, locator):
        self.wait_for_element_clickable(locator).click()

    @allure.step('Проверить, что элемент отображается')
    def is_element_displayed(self, locator):
        return self.wait_for_element_visible(locator).is_displayed()

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_and_drop_ingredient(self, source_locator, target_locator):
        source = self.wait_for_element_visible(source_locator)
        target = self.wait_for_element_visible(target_locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()
        self.driver.execute_script("arguments[1].dispatchEvent(new Event('drop', { bubbles: true }));", source, target)

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator):
        return self.wait_for_element_visible(locator).text

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Проверить, что элемент скрыт или отсутствует')
    def is_element_hidden(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) == 0 or not elements[0].is_displayed()

    @allure.step('Заполнить поле текстом')
    def fill_field(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Выполнить авторизацию')
    def login(self, email, password):
        self.click_on_element(BaseLocators.BTN_LOGIN_ACC)
        self.fill_field(BaseLocators.FIELD_EMAIL, email)
        self.fill_field(BaseLocators.FIELD_PASSWORD, password)
        self.click_on_element(BaseLocators.BTN_LOGIN)

    @allure.step('Клик через JavaScript')
    def click_via_js(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Дождаться изменения счётчика')
    def wait_for_counter_change(self, counter_func, initial_value, timeout=15):
        return self.wait.until(
            lambda _: counter_func() != initial_value,
            message=f"Счётчик не изменился от {initial_value} за {timeout} сек"
        )

    @allure.step('Перейти в "Конструктор"')
    def go_to_constructor(self):
        self.click_on_element(self.locators.BTN_CONSTRR)
        self.wait_for_element_visible(self.locators.BUN)

    @allure.step('Перейти в "Ленту заказов"')
    def go_to_order_feed(self, use_js=False):
        click_func = self.click_via_js if use_js else self.click_on_element
        click_func(self.locators.BTN_ORDER_FEED)
        self.wait_for_element_visible(self.locators.FEED_TITLE)
