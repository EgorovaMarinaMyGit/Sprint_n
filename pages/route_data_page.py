import allure
from pages.base_page import BasePage
from locators.route_data_page_locators import RouteDataPageLocators


class RouteDataPage(BasePage): 

    @allure.step("Ввод разных адресов")
    def add_addresses(self):
        self.add_different_addresses(RouteDataPageLocators.FROM, RouteDataPageLocators.TO)

    
    @allure.step("Ввод одинаковых адресов")
    def add_addresses_equal(self):
        self.add_equal_addresses(RouteDataPageLocators.FROM, RouteDataPageLocators.TO)

    
    @allure.step("Проверка отображения тарифов Оптимальный, Быстрый, Свой")
    def check_visibility_rates(self):
        self.find_element_with_wait(RouteDataPageLocators.OPTIMAL)
        optimal_visible = self.check_displaying_of_element(RouteDataPageLocators.OPTIMAL)
        fast_visible = self.check_displaying_of_element(RouteDataPageLocators.FAST)
        own_visible = self.check_displaying_of_element(RouteDataPageLocators.OWN)

        if not optimal_visible:
            raise AssertionError("Элемент 'Оптимальный' не отображается")
        if not fast_visible:
            raise AssertionError("Элемент 'Быстрый' не отображается")
        if not own_visible:
            raise AssertionError("Элемент 'Свой' не отображается")
        return optimal_visible and fast_visible and own_visible
    

    @allure.step("Проверка отображения иконок типов передвижения")
    def check_visibility_movements_icons(self):
        self.find_element_with_wait(RouteDataPageLocators.TAXI_ICON_ACTIVE)
        car_icon_visible = self.check_displaying_of_element(RouteDataPageLocators.CAR_ICON)
        man_icon_visible = self.check_displaying_of_element(RouteDataPageLocators.MAN_ICON)
        taxi_icon_visible = self.check_displaying_of_element(RouteDataPageLocators.TAXI_ICON_ACTIVE)
        bike_icon_visible = self.check_displaying_of_element(RouteDataPageLocators.BIKE_ICON)
        scooter_icon_visible = self.check_displaying_of_element(RouteDataPageLocators.SCOOTER_ICON)
        drive_icon_visible = self.check_displaying_of_element(RouteDataPageLocators.DRIVE_ICON)

        if not car_icon_visible:
            raise AssertionError("Иконка 'Машина' не отображается")
        if not man_icon_visible:
            raise AssertionError("Иконка 'Пешком' не отображается")
        if not taxi_icon_visible:
            raise AssertionError("Иконка 'Такси' не отображается")
        if not bike_icon_visible:
            raise AssertionError("Иконка 'Велосипед' не отображается")
        if not scooter_icon_visible:
            raise AssertionError("Иконка 'Самокат' не отображается")
        if not drive_icon_visible:
            raise AssertionError("Иконка 'Драйв' не отображается")
        return car_icon_visible and man_icon_visible and taxi_icon_visible and bike_icon_visible and scooter_icon_visible and drive_icon_visible
    

    @allure.step("Проверка отображения стоимости") 
    def check_visibility_price(self):
        self.find_element_with_wait(RouteDataPageLocators.PRICE)
        return self.check_displaying_of_element(RouteDataPageLocators.PRICE)
    

    @allure.step("Проверка отображения времени в пути")
    def check_visibility_duration(self):
        self.find_element_with_wait(RouteDataPageLocators.DURATION)
        return self.check_displaying_of_element(RouteDataPageLocators.DURATION)
    

    @allure.step("Проверка отображения кнопки 'Вызать такси'")
    def check_visibility_call_taxi_button(self):
        self.find_element_with_wait(RouteDataPageLocators.CALL_TAXI)
        return self.check_displaying_of_element(RouteDataPageLocators.CALL_TAXI)
    

    @allure.step("Проверка отображения кнопки 'Забронировать'")
    def check_visibility_booking_button(self):
        self.find_element_with_wait(RouteDataPageLocators.OWN)
        self.click_to_element(RouteDataPageLocators.OWN)
        self.find_element_with_wait(RouteDataPageLocators.DRIVE_ICON)
        self.click_to_element(RouteDataPageLocators.DRIVE_ICON)
        self.find_element_with_wait(RouteDataPageLocators.BOOKING)
        return self.check_displaying_of_element(RouteDataPageLocators.BOOKING)
    
    
    @allure.step("Проверка отображения 'Авто Бесплатно'")
    def check_visibility_avto_free(self):
        self.find_element_with_wait(RouteDataPageLocators.FREE_AVTO)
        return self.check_displaying_of_element(RouteDataPageLocators.FREE_AVTO)
    

    @allure.step("Проверка отображения 'В пути 0 мин.'")
    def check_visibility_zero_minute(self):
        self.find_element_with_wait(RouteDataPageLocators.ZERO_MINUTE)
        return self.check_displaying_of_element(RouteDataPageLocators.ZERO_MINUTE)