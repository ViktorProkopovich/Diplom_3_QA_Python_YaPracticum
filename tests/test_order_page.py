from pages.order_page import OrderPage
import allure


class TestOrder:
    def _create_order(self, page):
        page.add_ingredients()
        page.place_order()
        number = '0' + page.get_order_number()
        page.close_order_modal()
        return number

    @allure.title('Номер заказа отображается в "В работе"')
    def test_order_appears_in_progress(self, logged_in_browser):
        page = OrderPage(logged_in_browser)
        order_num = self._create_order(page)
        page.go_to_feed_js()
        in_feed = page.get_orders_in_progress()
        assert order_num == in_feed

    @allure.title('Счётчик "Всего" увеличивается')
    def test_total_counter_increases(self, logged_in_browser):
        page = OrderPage(logged_in_browser)
        page.go_to_feed()
        initial = int(page.get_total_count())
        page.go_to_constructor()
        self._create_order(page)
        page.go_to_feed_js()
        updated = int(page.get_total_count())
        assert updated == initial + 1

    @allure.title('Счётчик "Сегодня" увеличивается')
    def test_today_counter_increases(self, logged_in_browser):
        page = OrderPage(logged_in_browser)
        page.go_to_feed()
        initial = int(page.get_today_count())
        page.go_to_constructor()
        self._create_order(page)
        page.go_to_feed_js()
        updated = int(page.get_today_count())
        assert updated == initial + 1
