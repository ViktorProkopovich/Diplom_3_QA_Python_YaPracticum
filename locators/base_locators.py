from selenium.webdriver.common.by import By


class BaseLocators:
    # Навигация
    BTN_CONSTRR = (By.XPATH, "//p[text()='Конструктор']")                          # Кнопка "Конструктор"
    BTN_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")                    # Кнопка "Лента заказов"

    # Ингредиенты
    FLUOR_BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')            # Булка
    BUN = (By.XPATH, "//img[contains(@alt, 'Флюоресцентная булка R2-D3')]")       # Булка как ингредиент
    SOUCE = (By.XPATH, "//img[contains(@alt, 'Соус Spicy-X')]")                   # Соус как ингредиент
    BURGER_CONSTR = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")  # Контейнер конструктора

    # Лента заказов
    FEED_TITLE = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5' and text()='Лента заказов']")  # Заголовок ленты

    # Модальные окна
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")                  # Модальное окно
    BTN_MODAL_CLOSE = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')  # Крестик закрытия
    COUNT_SPICY_X = (By.XPATH, "//p[text()='Соус Spicy-X']/ancestor::a//p[contains(@class, 'counter_counter__num')]")  # Счётчик соуса

    # Авторизация
    BTN_LOGIN_ACC = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]")        # Кнопка входа на главной
    FIELD_EMAIL = (By.XPATH, "//input[@type='text']")                             # Поле email
    FIELD_PASSWORD = (By.XPATH, "//input[@type='password']")                      # Поле пароля
    BTN_LOGIN = (By.XPATH, "//button[contains(., 'Войти')]")                      # Кнопка "Войти"