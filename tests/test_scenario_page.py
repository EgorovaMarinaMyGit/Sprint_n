import allure
import pytest
from data import URL


class TestScenarioPage:

# Сценарий. Ввести два разных предустановленных адреса в поля "Откуда" и "Куда", 
# выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси


#Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку 
# Ввести номер и заказать
    @allure.title("Проверка окна ожидания машины")
    def test_check_window_waiting_car(self, scenario_page):
        scenario_page.go_to_url(URL)
        scenario_page.add_addresses()
        scenario_page.click_call_taxi_button()
        scenario_page.switch_to_working_rate()
        scenario_page.select_table_for_laptop()
        scenario_page.click_to_order_car()
        
        assert scenario_page.check_elements_in_window_waiting_car()


# Дождаться окончания таймера поиска машины
    @allure.title("Проверка окна созданного заказа")
    def test_check_window_created_order(self, scenario_page):
        scenario_page.go_to_url(URL)
        scenario_page.add_addresses()
        scenario_page.click_call_taxi_button()
        scenario_page.switch_to_working_rate()
        scenario_page.click_to_order_car()
        
        assert scenario_page.check_elements_in_window_created_order()


# Нажать кнопку 'Детали' в блоке 'Ещё' про поездку'
    @allure.title("Проверка, что стоимость, которая была при выборе тарифа, равна стоимости \
    \ после нажатия кнопки 'Детали'")
    def test_check_price_in_details_the_same_before_order(self, scenario_page):
        scenario_page.go_to_url(URL)
        scenario_page.add_addresses()
        scenario_page.click_call_taxi_button()
        scenario_page.switch_to_working_rate()
        price_in_rate_card = scenario_page.get_price_before_order()
        scenario_page.click_to_order_car()
        price_in_details = scenario_page.get_price_after_order_in_details()

        assert price_in_rate_card == price_in_details

    
# Нажать кнопку 'Отмена'
    @pytest.mark.xfail(reason="Кнопка 'Отменить' не нажимается")
    @allure.title("Проверка, что после нажатия на кнопку 'Отмена' окно закрывается")
    def test_check_close_window_after_click_cancel(self, scenario_page):
        scenario_page.go_to_url(URL)
        scenario_page.add_addresses()
        scenario_page.click_call_taxi_button()
        scenario_page.switch_to_working_rate()
        scenario_page.click_to_order_car()
        scenario_page.click_to_cancel_button()

        assert scenario_page.window_waiting_visibility() == False

