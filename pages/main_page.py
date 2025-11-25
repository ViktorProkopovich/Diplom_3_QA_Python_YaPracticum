from pages.base_page import BasePage
import allure
from url import Url


class MainPage(BasePage):

    @allure.step('Перейти в "Конструктор"')
    def go_to_constructor(self):
        self.open_page(Url.url_feed)
        super().go_to_constructor()

    @allure.step('Перейти в "Ленту заказов"')
    def go_to_feed(self):
        self.open_page(Url.url_page)
        super().go_to_order_feed(use_js=False)

    @allure.step('Открыть модальное окно ингредиента')
    def open_ingredient_modal(self):
        self.open_page(Url.url_page)
        self.click_on_element(self.locators.FLUOR_BUN)
        self.wait_for_element_visible(self.locators.MODAL)

    @allure.step('Проверить, что модальное окно открыто')
    def is_modal_open(self):
        return self.is_element_displayed(self.locators.MODAL)

    @allure.step('Закрыть модальное окно по крестику')
    def close_ingredient_modal(self):
        self.click_on_element(self.locators.BTN_MODAL_CLOSE)
        self.wait_for_element_not_visible(self.locators.MODAL)

    @allure.step('Проверить, что модальное окно закрыто')
    def is_modal_closed(self):
        return self.is_element_hidden(self.locators.MODAL)

    @allure.step('Добавить булку в конструктор')
    def add_bun(self):
        self.drag_and_drop_ingredient(self.locators.BUN, self.locators.BURGER_CONSTR)

    @allure.step('Добавить соус в конструктор')
    def add_sauce(self):
        self.drag_and_drop_ingredient(self.locators.SOUCE, self.locators.BURGER_CONSTR)

    @allure.step('Получить счётчик соуса')
    def get_sauce_counter(self):
        return self.get_element_text(self.locators.COUNT_SPICY_X)