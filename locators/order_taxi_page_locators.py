from selenium.webdriver.common.by import By


class OrderTaxiPageLocators: 

    FROM = (By.XPATH, "//input[@id='from']") # поле "Откуда"
    TO = (By.XPATH, "//input[@id='to']") # поле "Куда"
    WORKING = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Рабочий')]") # Рабочий
    SLEEPY = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Сонный')]") # Сонный
    VACATION = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Отпускной')]") # Отпускной
    TALKATIVE = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Разговорчивый')]") # Разговорчивый
    CONSOLATION = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Утешительный')]") # Утешительный
    GLOSSY = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Глянцевый')]") # Глянцевый
    CARD_LOCATOR = [By.XPATH, "//div[@class='tariff-cards']//div[contains(@class,'tcard')]"]
    CALL_TAXI = (By.XPATH, "//button[contains(text(),'Вызвать такси')]") # кнопка "Вызвать такси"
    TELEPHONE_FIELD = (By.XPATH, "//div[contains(text(),'Телефон')]") # поле "Телефон"
    PAYMENT_METHOD = (By.XPATH, "//div[contains(text(),'Способ оплаты')]") # поле "Способ оплаты"
    COMMENT_FOR_DRIVER = (By.XPATH, "//label[contains(text(),'Комментарий водителю...')]") # поле "Комментарий водителю..."
    ORDER_REQUIREMENTS = (By.XPATH, "//div[contains(text(),'Требования к заказу')]") # поле "Требования к заказу"
    ADD_NUMBER_AND_BOOK = (By.XPATH, "//span[contains(text(),'Ввести номер и заказать')]") # Ввести номер и заказать
    INFO_ROUTE = (By.XPATH, "//span[contains(text(),'Маршрут составит 3 км. и займёт 3 мин.')]") # Маршрут составит 3 км. и займёт 3 мин.
    I_LOCATOR = (By.XPATH, "//div[@class='tcard active']//button[@class='i-button tcard-i active']") # i на карточке тарифа
    TITLE_IN_MODAL_WINDOW = [By.XPATH, "//div[@class='tcard active']//div[@class='i-floating']//div[@class='i-dPrefix']"]

