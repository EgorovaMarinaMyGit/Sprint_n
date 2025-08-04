from locators.order_taxi_page_locators import OrderTaxiPageLocators
from locators.scenario_page_locators import ScenarioPageLocators


URL = 'https://ez-route.stand.praktikum-services.ru/'

from_address = 'Хамовнический вал, 34'
to_address = 'Зубовский бульвар, 37'


taxi_rates = [
    OrderTaxiPageLocators.WORKING, 
    OrderTaxiPageLocators.SLEEPY, 
    OrderTaxiPageLocators.VACATION, 
    OrderTaxiPageLocators.TALKATIVE, 
    OrderTaxiPageLocators.CONSOLATION, 
    OrderTaxiPageLocators.GLOSSY 
]


expected_rates_names_and_descriptions = {
    "Рабочий": "Для деловых особ, которых отвлекают",
    "Сонный": "Если мысли не выходят из головы",
    "Отпускной": "Если пришла пора отдохнуть",
    "Разговорчивый": "Для тех, кто не выспался", 
    "Утешительный":"Если хочется свернуться калачиком",
    "Глянцевый": "Если нужно блистать"
}


elements_in_waiting_window = [
    ScenarioPageLocators.FIND_CAR,
    ScenarioPageLocators.TIMER,
    ScenarioPageLocators.CANCEL_BUTTON,
    ScenarioPageLocators.DETAILS_BUTTON
]


elements_in_window_created_order = [
    ScenarioPageLocators.IMAGE_CAR,
    ScenarioPageLocators.DRIVER_NAME,
    ScenarioPageLocators.DRIVER_AVATAR,
    ScenarioPageLocators.DRIVER_RATING
]