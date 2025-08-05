import allure
from data import URL


class TestRouteDrawingPage:

    @allure.title("Проверка отображения двух точек начала и конца маршрута ' \
    'после ввода разных адресов")
    def test_check_visibility_labels(self, route_drawing_page):
        route_drawing_page.go_to_url(URL)
        route_drawing_page.add_addresses()

        assert route_drawing_page.check_visibility_labels()