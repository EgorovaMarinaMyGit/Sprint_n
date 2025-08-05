import allure
from data import URL


class TestRouteDataPage:

    @allure.title("Проверка отображения тарифов Оптимальный, Быстрый, Свой после \
    \ ввода двух разных адресов")
    def test_check_visibility_rates_different_addresses(self, route_data_page):
        route_data_page.go_to_url(URL)
        route_data_page.add_addresses()

        assert route_data_page.check_visibility_rates()


    @allure.title("Проверка отображения типов передвижения: Машина, Пешком, Такси, \
    \ Велосипед, Самокат, Драйв после ввода двух разных адресов")
    def test_check_visibility_movement_types_different_addresses(self, route_data_page):
        route_data_page.go_to_url(URL)
        route_data_page.add_addresses()

        assert route_data_page.check_visibility_movements_icons()


    @allure.title("Проверка отображения стоимости поездки после ввода двух разных адресов")
    def test_check_visibility_price_different_addresses(self, route_data_page):
        route_data_page.go_to_url(URL)
        route_data_page.add_addresses()

        assert route_data_page.check_visibility_price()


    @allure.title("Проверка отображения длительности поездки после ввода двух разных адресов")
    def test_check_visibility_duration_different_addresses(self, route_data_page):
        route_data_page.go_to_url(URL)
        route_data_page.add_addresses()

        assert route_data_page.check_visibility_duration()


    @allure.title("Проверка отображения кнопки 'Вызать такси' после ввода двух разных адресов")
    def test_check_visibility_call_taxi_button_different_addresses(self, route_data_page):
        route_data_page.go_to_url(URL)
        route_data_page.add_addresses()

        assert route_data_page.check_visibility_call_taxi_button()


    @allure.title("Проверка отображения кнопки 'Забронировать' для типа Драйв после ввода \
    \ двух разных адресов")
    def test_check_visibility_booking_button_different_addresses(self, route_data_page):
        route_data_page.go_to_url(URL)
        route_data_page.add_addresses()

        assert route_data_page.check_visibility_booking_button()


    @allure.title("Проверка отображения 'Авто Бесплатно' после ввода двух одинаковых адресов")
    def test_check_visibility_free_avto_equal_addresses(self, route_data_page):
        route_data_page.go_to_url(URL)
        route_data_page.add_addresses_equal()

        assert route_data_page.check_visibility_avto_free()


    @allure.title("Проверка отображения 'В пути 0 мин.' после ввода двух одинаковых адресов")
    def test_check_visibility_zero_minute_equal_addresses(self, route_data_page):
        route_data_page.go_to_url(URL)
        route_data_page.add_addresses_equal()

        assert route_data_page.check_visibility_zero_minute()