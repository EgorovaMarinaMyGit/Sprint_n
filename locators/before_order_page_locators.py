from selenium.webdriver.common.by import By


class BeforeOrderPageLocators:

    FROM = (By.XPATH, "//input[@id='from']") # поле "Откуда"
    TO = (By.XPATH, "//input[@id='to']") # поле "Куда"
    OPTIMAL = (By.XPATH, "//div[contains(text(),'Оптимальный')]") # Оптимальный
    FAST = (By.XPATH, "//div[contains(text(),'Быстрый')]") # Быстрый
    OWN = (By.XPATH, "//div[contains(text(),'Свой')]") # Свой
    ICON_MOVEMENTS = [By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')]"]
    CAR_ICON = (By.XPATH, "//img[@src='/static/media/car.8a2b1ff5.svg']") # иконка машина
    CAR_ICON_ACTIVE = (By.XPATH, "//img[@src='/static/media/car-active.a27e745e.svg']") # иконка машина когда выбрана
    MAN_ICON = (By.XPATH, "//img[@src='/static/media/walk.d33bf83c.svg']") # иконка человек
    TAXI_ICON_ACTIVE = (By.XPATH, "//img[@src='/static/media/taxi-active.b0be3054.svg']") # иконка такси когда выбрана
    TAXI_ICON = (By.XPATH, "//img[@src='/static/media/taxi.9a02abc6.svg']") # иконка такси
    BIKE_ICON = (By.XPATH, "//img[@src='/static/media/bike.fb41c762.svg']") # иконка велосипед
    BIKE_ICON_ACTIVE = (By.XPATH, "//img[@src='/static/media/bike-active.b0d16d8b.svg']в") # иконка велосипед когда выбрана
    SCOOTER_ICON = (By.XPATH, "//img[@src='/static/media/scooter.cf9bb57e.svg']") # иконка самокат
    DRIVE_ICON = (By.XPATH, "//img[@src='/static/media/drive.fa5137d7.svg']") # иконка драйв
    PRICE = (By.XPATH, "//div[@class='text']") # стоимость
    DURATION = (By.XPATH, "//div[@class='duration']") # время
    CALL_TAXI = (By.XPATH, "//button[contains(text(),'Вызвать такси')]") # кнопка "Вызвать такси"
    BOOKING = (By.XPATH, "//button[contains(text(),'Забронировать')]") # кнопка "Забронировать"