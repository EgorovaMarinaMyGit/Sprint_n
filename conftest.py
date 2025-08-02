import pytest
from selenium import webdriver
from pages.route_drawing_page import RouteDrawingPage
from pages.route_data_page import RouteDataPage



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