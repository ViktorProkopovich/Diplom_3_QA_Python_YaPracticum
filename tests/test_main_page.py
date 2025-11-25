from pages.main_page import MainPage
import allure
from url import Url


class TestMain:

    @allure.title('Переход в "Конструктор"')
    def test_go_to_constructor(self, browser):
        page = MainPage(browser)
        page.go_to_constructor()
        assert page.get_current_url() == Url.url_page

    @allure.title('Переход в "Ленту заказов"')
    def test_go_to_feed(self, browser):
        page = MainPage(browser)
        page.go_to_feed()
        assert page.get_current_url() == Url.url_feed

    @allure.title('Открытие модального окна ингредиента')
    def test_open_ingredient_modal(self, browser):
        page = MainPage(browser)
        page.open_ingredient_modal()
        assert page.is_modal_open()

    @allure.title('Закрытие модального окна по крестику')
    def test_close_ingredient_modal(self, browser):
        page = MainPage(browser)
        page.open_ingredient_modal()
        page.close_ingredient_modal()
        assert page.is_modal_closed()

    @allure.title('Счётчик ингредиента увеличивается')
    def test_ingredient_counter(self, browser):
        page = MainPage(browser)
        page.open_page(Url.url_page)
        initial = int(page.get_sauce_counter() or 0)
        page.add_bun()
        page.add_sauce()
        final = int(page.get_sauce_counter() or 0)
        assert final > initial
