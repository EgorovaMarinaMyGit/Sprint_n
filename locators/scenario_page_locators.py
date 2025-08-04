from selenium.webdriver.common.by import By


class ScenarioPageLocators:

    FROM = (By.XPATH, "//input[@id='from']") # поле "Откуда"
    TO = (By.XPATH, "//input[@id='to']") # поле "Куда"
    CALL_TAXI = (By.XPATH, "//button[contains(text(),'Вызвать такси')]") # кнопка "Вызвать такси"
    ORDER_REQUIREMENTS = (By.XPATH, "//div[contains(text(),'Требования к заказу')]") # поле "Требования к заказу"
    TABLE_FOR_LAPTOP = (By.XPATH, "//span[@class='slider round']") # чек-бокс "Столик для ноутбука"
    ADD_NUMBER_AND_BOOK_BUTTON = (By.XPATH, "//button[@class='smart-button']") # Ввести номер и заказать
    FIND_CAR = (By.XPATH, "//div[contains(text(),'Поиск машины')]") # Поиск машины
    TIMER = (By.XPATH, "//div[@class='order-header-time']") # таймер
    CANCEL_BUTTON = (By.XPATH, "//button[@class='order-button']//img[@src='/static/media/plus.d25b8941.svg']") # кнопка "Отменить"
    DETAILS_BUTTON = (By.XPATH, "//button[@class='order-button']//img[@src='/static/media/burger.7f0605c2.svg']") # кнопка "Детали"
    TITLE_WINDOW_ORDER = (By.XPATH, "//div[@class='order-header-title']") # заголовок в окне (где время)
    CAR_NUMBER = (By.XPATH, "//div[@class='order-number']//div[@class='number']") # номер машины
    IMAGE_CAR = (By.XPATH, "//div[@class='order-number']//img[@src='/static/media/economy.61e4a774.svg']") # картинка машины
    DRIVER_NAME = (By.XPATH, "//div[@class='order-btn-group']//div[2]") # имя водителя
    DRIVER_AVATAR = (By.XPATH, "//img[@src='/static/media/bender.e90e5089.svg']") # аватарка водителя
    DRIVER_RATING = (By.XPATH, "//div[@class='order-button']//div[1]") # рейтинг водителя
    

