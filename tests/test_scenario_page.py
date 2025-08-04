import allure
import pytest
from data import URL


class TestScenarioPage:

    @allure.title("Проверка окна ожидания машины")
    def test_check_window_waiting_car(self, scenario_page):
        scenario_page.go_to_url(URL)
        scenario_page.add_addresses()
        scenario_page.click_call_taxi_button()
        scenario_page.select_table_for_laptop()
        scenario_page.click_to_order_car()
        
        assert scenario_page.check_elements_in_window_waiting_car()


    @allure.title("Проверка окна созданного заказа")
    def test_check_window_created_order(self, scenario_page):
        scenario_page.go_to_url(URL)
        scenario_page.add_addresses()
        scenario_page.click_call_taxi_button()
        scenario_page.select_table_for_laptop()
        scenario_page.click_to_order_car()
        
        assert scenario_page.check_elements_in_window_created_order()