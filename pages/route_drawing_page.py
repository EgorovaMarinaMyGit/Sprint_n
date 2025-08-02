import allure
from pages.base_page import BasePage
from locators.route_drawing_page_locators import RouteDrawingPageLocators


class RouteDrawingPage(BasePage):

    @allure.step("Ввод разных адресов")
    def add_addresses(self):
        self.add_different_addresses(RouteDrawingPageLocators.FROM, RouteDrawingPageLocators.TO)


    @allure.step("Проверка отображения двух точек после ввода разных адресов")
    def check_visibility_labels(self):
        self.find_element_with_wait(RouteDrawingPageLocators.A_LABEL)
        a_visible = self.check_displaying_of_element(RouteDrawingPageLocators.A_LABEL)
        b_visible = self.check_displaying_of_element(RouteDrawingPageLocators.B_LABEL)
    
        if not a_visible:
            raise AssertionError("Элемент 'A' не отображается")
        if not b_visible:
            raise AssertionError("Элемент 'B' не отображается")
        return a_visible and b_visible