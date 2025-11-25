from pages.base_page import BasePage
import allure
from locators.order_locators import OrderFeedLocators


class OrderPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout=20)
        self.locators = OrderFeedLocators()

    @allure.step('Добавить ингредиенты в конструктор')
    def add_ingredients(self):
        self.drag_and_drop_ingredient(self.locators.BUN, self.locators.BURGER_CONSTR)
        self.drag_and_drop_ingredient(self.locators.SOUCE, self.locators.BURGER_CONSTR)

    @allure.step('Оформить заказ')
    def place_order(self):
        self.wait_for_element_clickable(self.locators.BTN_ORDER)
        self.click_on_element(self.locators.BTN_ORDER)

    @allure.step('Закрыть модальное окно заказа')
    def close_order_modal(self):
        self.wait_for_element_clickable(self.locators.BTN_CLOSE_MODAL)
        self.click_via_js(self.locators.BTN_CLOSE_MODAL)
        self.wait_for_element_not_visible(self.locators.ORDER_OVERLAIN_MODAL)

    @allure.step('Перейти в "Ленту заказов" (JS)')
    def go_to_feed_js(self):
        super().go_to_order_feed(use_js=True)

    @allure.step('Перейти в "Конструктор"')
    def go_to_constructor(self):
        super().go_to_constructor()

    @allure.step('Перейти в "Ленту заказов"')
    def go_to_feed(self):
        self.wait_for_element_not_visible(self.locators.ORDER_OVERLAIN_MODAL)
        super().go_to_order_feed(use_js=False)

    @allure.step('Получить номер заказа из "В работе"')
    def get_orders_in_progress(self):
        self.wait_for_element_visible(self.locators.ORDERS_IN_PROGRESS)
        return self.get_element_text(self.locators.ORDERS_IN_PROGRESS)

    @allure.step('Получить счётчик "Всего"')
    def get_total_count(self):
        return self.get_element_text(self.locators.TOTAL_ORDERS_COUNT)

    @allure.step('Получить счётчик "Сегодня"')
    def get_today_count(self):
        return self.get_element_text(self.locators.TODAY_ORDERS_COUNT)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        initial = self.get_element_text(self.locators.ID_ORDER)
        self.wait_for_counter_change(
            counter_func=lambda: self.get_element_text(self.locators.ID_ORDER),
            initial_value=initial,
            timeout=15
        )
        return self.get_element_text(self.locators.ID_ORDER)