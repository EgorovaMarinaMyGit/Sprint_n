from selenium.webdriver.common.by import By


class RouteDataPageLocators:

    FROM = (By.XPATH, "//input[@id='from']") # поле "Откуда"
    TO = (By.XPATH, "//input[@id='to']") # поле "Куда"
    A_LABEL = (By.XPATH, "//ymaps[@class='ymaps-2-1-79-route-pin__label-a']") # точка А
    B_LABEL = (By.XPATH, "//ymaps[@class='ymaps-2-1-79-route-pin__label-b']") # точка B
    OPTIMAL = (By.XPATH, "//div[contains(text(),'Оптимальный')]") # Оптимальный
    FAST = (By.XPATH, "//div[contains(text(),'Быстрый')]") # Быстрый
    OWN = (By.XPATH, "//div[contains(text(),'Свой')]") # Свой
    CAR_ICON = (By.XPATH, "//img[@src='/static/media/car.8a2b1ff5.svg']") # иконка машина
    MAN_ICON = (By.XPATH, "//img[@src='/static/media/walk.d33bf83c.svg']") # иконка человек
    TAXI_ICON_ACTIVE = (By.XPATH, "//img[@src='/static/media/taxi-active.b0be3054.svg']") # иконка такси когда выбрана
    BIKE_ICON = (By.XPATH, "//img[@src='/static/media/bike.fb41c762.svg']") # иконка велосипед
    SCOOTER_ICON = (By.XPATH, "//img[@src='/static/media/scooter.cf9bb57e.svg']") # иконка самокат
    DRIVE_ICON = (By.XPATH, "//img[@src='/static/media/drive.fa5137d7.svg']") # иконка драйв
    PRICE_TAXI = (By.XPATH, "//div[contains(text(),'Такси ~ 188 руб.')]") # Такси ~ 188 руб.
    DURATION = (By.XPATH, "//div[contains(text(),'В пути 3 мин.')]") # В пути 3 мин.
    CALL_TAXI = (By.XPATH, "//button[contains(text(),'Вызвать такси')]") # кнопка "Вызвать такси"
    BOOKING = (By.XPATH, "//button[contains(text(),'Забронировать')]") # кнопка "Забронировать"
    FREE_AVTO = (By.XPATH, "//div[contains(text(),'Авто Бесплатно')]") # Авто Бесплатно
    ZERO_MINUTE = (By.XPATH, "//div[contains(text(),'В пути 0 мин.')]") # В пути 0 мин.


