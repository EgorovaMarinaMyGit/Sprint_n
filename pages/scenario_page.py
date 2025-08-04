import allure
import pytest
from pages.base_page import BasePage
from locators.scenario_page_locators import ScenarioPageLocators
from data import elements_in_waiting_window, elements_in_window_created_order


class ScenarioPage(BasePage):

    @allure.step("Ввод разных адресов")
    def add_addresses(self):
        self.add_different_addresses(ScenarioPageLocators.FROM, ScenarioPageLocators.TO)


    @allure.step("Нажать на кнопку 'Вызвать такси'")
    def click_call_taxi_button(self):
        self.find_element_with_wait(ScenarioPageLocators.CALL_TAXI)
        self.click_to_element(ScenarioPageLocators.CALL_TAXI)


    @allure.step("Выбрать чек-бокс 'Столик для ноутбука'")
    def select_table_for_laptop(self):
        self.scroll_to_element(ScenarioPageLocators.ORDER_REQUIREMENTS)
        self.click_to_element(ScenarioPageLocators.ORDER_REQUIREMENTS)
        self.click_to_element(ScenarioPageLocators.TABLE_FOR_LAPTOP)


    @allure.step("Нажать на заказ машины")
    def click_to_order_car(self):
        self.click_to_element(ScenarioPageLocators.ADD_NUMBER_AND_BOOK_BUTTON)


    @allure.step("Проверка элементов в окне ожидания машины")
    def check_elements_in_window_waiting_car(self):
        displayed_elements = []
        for element in elements_in_waiting_window: 
            self.find_element_with_wait(element)
            element_displayed = self.check_displaying_of_element(element)
            displayed_elements.append(element_displayed)
        return displayed_elements

    
    @allure.step("Проверка элементов в окне созданного заказа")
    def check_elements_in_window_created_order(self):
        self.long_waiting_element(ScenarioPageLocators.DRIVER_AVATAR)
        displayed_elements = []
        for element in elements_in_window_created_order: 
            element_displayed = self.check_displaying_of_element(element)
            displayed_elements.append(element_displayed)
        return displayed_elements