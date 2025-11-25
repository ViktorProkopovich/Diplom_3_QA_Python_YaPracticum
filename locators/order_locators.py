from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class OrderFeedLocators(BaseLocators):
    # Счётчики
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")  # "Выполнено за всё время"
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")    # "Выполнено за сегодня"

    # Раздел "В работе"
    ORDERS_IN_PROGRESS = (By.XPATH, "(//li[@class='text text_type_digits-default mb-2'])")  # Номера заказов "В работе"

    # Модальное окно заказа
    ID_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m') and contains(@class, 'text_type_digits-large')]")  # Номер заказа
    BTN_CLOSE_MODAL = (By.XPATH, '//button[contains(@class, "Modal_modal__close__TnseK")]')  # Кнопка закрытия
    ORDER_OVERLAIN_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")  # Оверлей модалки

    # Кнопка заказа
    BTN_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Кнопка "Оформить заказ"