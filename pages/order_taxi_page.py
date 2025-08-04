import allure
import pytest
from pages.base_page import BasePage
from locators.order_taxi_page_locators import OrderTaxiPageLocators
from data import taxi_rates


class OrderTaxiPage(BasePage):

    @allure.step("Ввод разных адресов")
    def add_addresses(self):
        self.add_different_addresses(OrderTaxiPageLocators.FROM, OrderTaxiPageLocators.TO)


    @allure.step("Нажать на кнопку 'Вызвать такси'")
    def click_call_taxi_button(self):
        self.find_element_with_wait(OrderTaxiPageLocators.CALL_TAXI)
        self.click_to_element(OrderTaxiPageLocators.CALL_TAXI)
        

    @allure.step("Проверка отображения тарифов такси")
    def check_visibility_taxi_rates(self):
        displaying_rates = []
        for rate in taxi_rates:
            self.find_element_with_wait(rate)
            self.check_displaying_of_element(rate)
            displaying_rates.append(rate)
        return displaying_rates


    @allure.step("Получение атрибута карточки тарифа")
    def get_attribute_of_rate_card(self):
        rates = self.wait_for_elements(OrderTaxiPageLocators.CARD_LOCATOR)
        active_rate = []
        for attribute in rates:
            class_attr = attribute.get_attribute("class")
            if "active" in class_attr:
                active_rate.append(attribute)
        return active_rate


    @allure.step("Получить список названий тарифов")
    def get_rates_names_list(self): 
        rates_names_list = []
        for names in taxi_rates:
            self.find_element_with_wait(names)
            text = self.get_text_from_element(names)
            rates_names_list.append(text)
        return rates_names_list
    

    @allure.step("Получить список описаний тарифов")
    def get_rates_description_list(self):
        rates_description_list = []
        for names in taxi_rates:
            self.find_element_with_wait(names)
            self.click_to_element(names)
            self.hover_to_element(OrderTaxiPageLocators.I_LOCATOR)
            self.find_element_with_wait(OrderTaxiPageLocators.TITLE_IN_MODAL_WINDOW)
            descr = self.get_text_from_element(OrderTaxiPageLocators.TITLE_IN_MODAL_WINDOW)
            rates_description_list.append(descr)
        return rates_description_list
    

    @allure.step("Получение данных - название тарифа и его описание")
    def get_list_with_rates_and_descriptions(self):
        keys = self.get_rates_names_list()
        values = self.get_rates_description_list()
        rates_dict = {}
        for i in range(len(keys)):
            rates_dict[keys[i]] = values[i]
        return rates_dict
    

    @allure.step("Проверка отображения информации под тарифами")
    def check_visibility_info_under_rates(self):
        telephon = self.check_displaying_of_element(OrderTaxiPageLocators.TELEPHONE_FIELD)
        payment = self.check_displaying_of_element(OrderTaxiPageLocators.PAYMENT_METHOD)
        comment = self.check_displaying_of_element(OrderTaxiPageLocators.COMMENT_FOR_DRIVER)
        requirements = self.check_displaying_of_element(OrderTaxiPageLocators.ORDER_REQUIREMENTS)
        book = self.check_displaying_of_element(OrderTaxiPageLocators.ADD_NUMBER_AND_BOOK)
        info = self.check_displaying_of_element(OrderTaxiPageLocators.INFO_ROUTE)
        return telephon, payment, comment, requirements, book, info

