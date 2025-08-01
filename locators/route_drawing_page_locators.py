from selenium.webdriver.common.by import By


class RouteDrawingPageLocators:

    FROM = (By.XPATH, "//input[@id='from']") # поле "Откуда"
    TO = (By.XPATH, "//input[@id='to']") # поле "Куда"
    A_LABEL = (By.XPATH, "//ymaps[@class='ymaps-2-1-79-route-pin__label-a']") # точка А
    B_LABEL = (By.XPATH, "//ymaps[@class='ymaps-2-1-79-route-pin__label-b']") # точка B

