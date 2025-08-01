import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.route_drawing_page_locators import RouteDrawingPageLocators
from data import from_address, to_address


class RouteDrawingPage(BasePage):


    @allure.step("Ввод разных адресов")
    def add_different_addresses(self):
        self.add_text_to_element(RouteDrawingPageLocators.FROM, from_address)
        self.add_text_to_element(RouteDrawingPageLocators.TO, to_address)


    @allure.step("Проверка отображения двух точек")
    def check_visibility_labels(self):
        self.find_element_with_wait(RouteDrawingPageLocators.A_LABEL)
        return self.check_displaying_of_element(RouteDrawingPageLocators.A_LABEL), self.check_displaying_of_element(RouteDrawingPageLocators.B_LABEL)