import pytest
from selenium import webdriver
from pages.route_drawing_page import RouteDrawingPage



# для браузера + выход
@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    yield chrome
    chrome.quit()

# фикстура для главной страницы
@pytest.fixture
def route_drawing_page(driver):
    page_route_drawing = RouteDrawingPage(driver)
    return page_route_drawing

# фикстура для страницы заказа
#@pytest.fixture
#def order_page(driver):
    #page_order = OrderPage(driver)
    #return page_order