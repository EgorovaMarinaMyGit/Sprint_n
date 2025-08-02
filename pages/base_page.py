import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import from_address, to_address


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)


    @allure.step("Перейти по URL'у")
    def go_to_url(self, url):
        self.driver.get(url)


    @allure.step("Найти элемент")
    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator) 
    

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
    

    @allure.step("Кликнуть на элемент")
    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()


    @allure.step("Проверить, что элемент не отображается")
    def check_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))


    @allure.step("Проверить, что текст появился на элементе")
    def check_text_to_be_present_in_element(self, locator, number):
        return WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(locator, number))


    @allure.step("Добавить тест в элемент")
    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)


    @allure.step("Получить текст у элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    

    @allure.step("Отформатировать локатор")
    def formatted_locator(self, f_locator, num):
        method, locator = f_locator
        locator = locator.format(num)
        return method, locator
    

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
    

    @allure.step("Доскроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element) 


    @allure.step("Ввод разных адресов")
    def add_different_addresses(self, locator_from, locator_to):
        self.add_text_to_element(locator_from, from_address)
        self.add_text_to_element(locator_to, to_address)


    @allure.step("Ввод одинаковых адресов")
    def add_equal_addresses(self, locator_from, locator_to):
        self.add_text_to_element(locator_from, from_address)
        self.add_text_to_element(locator_to, from_address)