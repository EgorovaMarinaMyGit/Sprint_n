import allure
from pages.base_page import BasePage
from locators.before_order_page_locators import BeforeOrderPageLocators


class BeforeOrderPage(BasePage):

    @allure.step("Ввод разных адресов")
    def add_addresses(self):
        self.add_different_addresses(BeforeOrderPageLocators.FROM, BeforeOrderPageLocators.TO)


    @allure.step("Проверка отображения активного таба Такси на тарифе 'Быстрый'")
    def check_active_taxi_on_fast(self):
        self.find_element_with_wait(BeforeOrderPageLocators.TAXI_ICON_ACTIVE)
        taxi_active = self.check_displaying_of_element(BeforeOrderPageLocators.TAXI_ICON_ACTIVE)
        return taxi_active
    

    @allure.step("Проверка, что таб Машина не активен на тарифе 'Быстрый'")
    def check_no_active_car_on_fast(self):
        car_no_active = self.check_displaying_of_element(BeforeOrderPageLocators.CAR_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.MAN_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.BIKE_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.SCOOTER_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.DRIVE_ICON)
        return car_no_active


    @allure.step("Перейти на тариф 'Оптимальный'")
    def switch_on_optimal(self):
        self.find_element_with_wait(BeforeOrderPageLocators.OPTIMAL)
        self.click_to_element(BeforeOrderPageLocators.OPTIMAL)


    @allure.step("Проверка, что таб Такси не активен на тарифе 'Оптимальный'")
    def check_no_active_taxi_on_optimal(self):
        self.find_element_with_wait(BeforeOrderPageLocators.TAXI_ICON)
        taxi_no_active = self.check_displaying_of_element(BeforeOrderPageLocators.TAXI_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.MAN_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.BIKE_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.SCOOTER_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.DRIVE_ICON)
        return taxi_no_active


    @allure.step("Проверка отображения активного таба Машина на тарифе 'Оптимальный'")
    def check_active_car_on_optimal(self):
        self.find_element_with_wait(BeforeOrderPageLocators.CAR_ICON_ACTIVE)
        car_active = self.check_displaying_of_element(BeforeOrderPageLocators.CAR_ICON_ACTIVE)
        return car_active


    @allure.step("Получить значение стоимости и времени поездки")
    def get_price_and_time(self):
        self.find_element_with_wait(BeforeOrderPageLocators.PRICE)
        price = self.get_text_from_element(BeforeOrderPageLocators.PRICE)
        self.find_element_with_wait(BeforeOrderPageLocators.DURATION)
        duration = self.get_text_from_element(BeforeOrderPageLocators.DURATION)
        return price, duration

    
    @allure.step("Перейти на тариф 'Свой'")
    def switch_on_own(self):
        self.find_element_with_wait(BeforeOrderPageLocators.OWN)
        self.click_to_element(BeforeOrderPageLocators.OWN)


    @allure.step("Проверка, что таб Велосипед не активен на тарифе 'Быстрый'")
    def check_no_active_bike_on_fast(self):
        bike_no_active = self.check_displaying_of_element(BeforeOrderPageLocators.BIKE_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.CAR_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.MAN_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.SCOOTER_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.DRIVE_ICON)
        return bike_no_active


    @allure.step("Проверка, что что таб Такси не активен на тарифе 'Свой'")
    def check_no_active_taxi_on_own(self):
        taxi_no_active = self.check_displaying_of_element(BeforeOrderPageLocators.TAXI_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.MAN_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.BIKE_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.SCOOTER_ICON)
        self.check_displaying_of_element(BeforeOrderPageLocators.DRIVE_ICON)
        return taxi_no_active

    
    @allure.step("Проверка отображения активного таба Велосипед на тарифе 'Свой'")
    def check_active_bike_on_own(self):
        self.find_element_with_wait(BeforeOrderPageLocators.BIKE_ICON_ACTIVE)
        bike_active = self.check_displaying_of_element(BeforeOrderPageLocators.BIKE_ICON_ACTIVE)
        return bike_active
    

    @allure.step("Получение атрибута таба (иконки способа передвижения)")
    def get_attribute_of_tab(self):
        elements = self.wait_for_elements(BeforeOrderPageLocators.ICON_MOVEMENTS)
        return [element.get_attribute("class") for element in elements]

    
    @allure.step("Проверка активности кнопки 'Вызвать такси'")
    def check_activity_call_taxi_button(self):
        self.find_element_with_wait(BeforeOrderPageLocators.CALL_TAXI)
        return self.check_element_is_clickable(BeforeOrderPageLocators.CALL_TAXI)
    

    @allure.step("Перейти на 'Драйв'")
    def switch_to_drive(self):
        self.find_element_with_wait(BeforeOrderPageLocators.DRIVE_ICON)
        return self.click_to_element(BeforeOrderPageLocators.DRIVE_ICON)


    @allure.step("Проверка активности кнопки 'Забронировать'")
    def check_activity_booking_button(self):
        self.find_element_with_wait(BeforeOrderPageLocators.BOOKING)
        return self.check_element_is_clickable(BeforeOrderPageLocators.BOOKING)