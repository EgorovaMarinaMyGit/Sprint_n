import allure
import pytest
from data import URL


class TestBeforeOrderPage:


    @allure.title("Проверка, что при переключении между видами маршрута \
    \ 'Быстрый' и 'Оптимальный' происходит смена активного таба")
    def test_changing_active_tab_after_swich_fast_to_optimal(self, before_order_page):
        before_order_page.go_to_url(URL)
        before_order_page.add_addresses()
        taxi_active_on_fast = before_order_page.check_active_taxi_on_fast()  
        car_no_active_on_fast = before_order_page.check_no_active_car_on_fast()
        before_order_page.switch_on_optimal()
        taxi_no_active_on_optimal = before_order_page.check_no_active_taxi_on_optimal()
        car_active_on_optimal = before_order_page.check_active_car_on_optimal()

        assert taxi_active_on_fast == True and car_no_active_on_fast == True \
            and taxi_no_active_on_optimal == True and car_active_on_optimal == True

    @pytest.mark.xfail(reason="При переключении тарифов время не меняется")
    @allure.title("Проверка, что при переключении между видами маршрута \
    \ 'Быстрый' и 'Оптимальный' происходит пересчет времени и стоимости маршрута")
    def test_changing_price_and_duration_after_swich_fast_to_optimal(self, before_order_page):
        before_order_page.go_to_url(URL)
        before_order_page.add_addresses()
        price_fast, duration_fast = before_order_page.get_price_and_time()
        before_order_page.switch_on_optimal()
        price_optimal, duration_optimal = before_order_page.get_price_and_time()

        assert price_fast != price_optimal and duration_fast != duration_optimal


    @pytest.mark.xfail(reason="При переходе на 'Свой' смена активного таба не происходит")
    @allure.title("Проверка, что при переключении между видами маршрута \
    \ 'Быстрый' и 'Свой' происходит смена активного таба")
    def test_changing_active_tab_after_swich_fast_to_own(self, before_order_page):
        before_order_page.go_to_url(URL)
        before_order_page.add_addresses()
        taxi_active_on_fast = before_order_page.check_active_taxi_on_fast()
        bike_no_active_on_fast = before_order_page.check_no_active_bike_on_fast()
        before_order_page.switch_on_own()
        taxi_no_active_on_own = before_order_page.check_no_active_taxi_on_own()
        bike_active_on_own = before_order_page.check_active_bike_on_own()

        assert taxi_active_on_fast == True and bike_no_active_on_fast == True \
            and taxi_no_active_on_own == True and bike_active_on_own == True
        

    @allure.title("Проверка, что при переключении между видами маршрута \
    \ 'Быстрый' и 'Свой' становятся активны типы передвижения Машина, Пешком, \
    \ Такси, Велосипед, Самокат, Драйв")
    # изменяется артрибут: был - type disabled, стал - просто type
    def test_all_tabs_active_after_swich_fast_to_own(self, before_order_page):
        before_order_page.go_to_url(URL)
        before_order_page.add_addresses()
        disabled_tabs = before_order_page.get_attribute_of_tab()
        before_order_page.switch_on_own()
        active_tabs = before_order_page.get_attribute_of_tab()

        assert disabled_tabs != active_tabs
        
        
    @allure.title("Проверка, что при выборе вида маршрута 'Быстрый' активна \
    \ кнопка 'Вызвать такси'")
    def test_check_activity_call_taxi_button_on_fast(self, before_order_page):
        before_order_page.go_to_url(URL)
        before_order_page.add_addresses()

        assert before_order_page.check_activity_call_taxi_button()


    @allure.title("Проверка, что при выборе вида маршрута 'Свой', типа передвижения \
    \ 'Драйв' активна кнопка 'Забронировать'")
    def test_check_activity_booking_button_on_own(self, before_order_page):
        before_order_page.go_to_url(URL)
        before_order_page.add_addresses()
        before_order_page.switch_on_own()
        before_order_page.switch_to_drive()

        assert before_order_page.check_activity_booking_button()