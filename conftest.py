import pytest
from selenium import webdriver
from pages.route_drawing_page import RouteDrawingPage
from pages.route_data_page import RouteDataPage
from pages.before_order_page import BeforeOrderPage
from pages.order_taxi_page import OrderTaxiPage
from pages.scenario_page import ScenarioPage



# для браузера + выход
@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    yield chrome
    chrome.quit()

# фикстура для страницы отрисовки маршрута
@pytest.fixture
def route_drawing_page(driver):
    page_route_drawing = RouteDrawingPage(driver)
    return page_route_drawing

# фикстура для страницы отображения блока с выбором маршрута
@pytest.fixture
def route_data_page(driver):
    page_route_data = RouteDataPage(driver)
    return page_route_data


# фикстура для страницы с блоком данных перед заказом
@pytest.fixture
def before_order_page(driver):
    page_before_order = BeforeOrderPage(driver)
    return page_before_order


# фикстура для страницы с заказом такси
@pytest.fixture
def order_taxi_page(driver):
    page_order_taxi = OrderTaxiPage(driver)
    return page_order_taxi


# фикстура для страницы сценариев
@pytest.fixture
def scenario_page(driver):
    page_scenario = ScenarioPage(driver)
    return page_scenario