import allure
import pytest
from data import URL, taxi_rates, expected_rates_names_and_descriptions


class TestOrderTaxiPage:

    @allure.title("Проверка, что после введения адресов, выбора тарифа 'Быстрый' и нажатия \
    \ кнопки 'Заказать такси' открывается форма заказа со всеми 6 тарифами")
    def test_check_visibility_taxi_rates(self, order_taxi_page):
        order_taxi_page.go_to_url(URL)
        order_taxi_page.add_addresses()
        order_taxi_page.click_call_taxi_button()
        current_rates = order_taxi_page.check_visibility_taxi_rates()

        assert set(current_rates) == set(taxi_rates)

    
    @allure.title("Проверка, что после введения адресов, выбора тарифа 'Быстрый' и нажатия \
    \ кнопки 'Заказать такси' один из отображающихся тарифов активый")
    def test_check_activity_taxi_rate(self, order_taxi_page):
        order_taxi_page.go_to_url(URL)
        order_taxi_page.add_addresses()
        order_taxi_page.click_call_taxi_button()
        active_rate = order_taxi_page.get_attribute_of_rate_card()
    
        assert len(active_rate) == 1


    @pytest.mark.xfail(reason="У тарифов 'Сонный' и 'Разговорчивый' в ПО не такое описание, \
    \ как в ПО")
    @allure.title("Проверка, что после введения адресов, выбора тарифа 'Быстрый' и нажатия \
    \ кнопки 'Заказать такси' при наведении на иконку i в правом верхнем углу каждого тарифа \
    \ отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ")
    def test_check_description_in_modal_window(self, order_taxi_page):
        order_taxi_page.go_to_url(URL)
        order_taxi_page.add_addresses()
        order_taxi_page.click_call_taxi_button()
        names_and_description_of_rates = order_taxi_page.get_list_with_rates_and_descriptions()
        assert names_and_description_of_rates == expected_rates_names_and_descriptions


    @allure.title("Проверка, что после введения адресов, выбора тарифа 'Быстрый' и нажатия \
    \ кнопки 'Заказать такси' под тарифами отображается блок с полями Телефон, Способ \
    \ оплаты, Комментарий водителю, Требования к заказ, Заказ тарифа Такси")
    def test_check_visibility_info_under_rates(self, order_taxi_page):
        order_taxi_page.go_to_url(URL)
        order_taxi_page.add_addresses()
        order_taxi_page.click_call_taxi_button()

        assert order_taxi_page.check_visibility_info_under_rates()