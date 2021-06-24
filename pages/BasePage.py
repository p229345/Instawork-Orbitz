from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Can't find element by locator: {locator}")

    def element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _verify_elements_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Can't find element by locator: {locator}")

    def get_elements(self, locator: tuple):
        return self._verify_elements_presence(locator)

    def go_to_page(self, url: str):
        self.driver.get(url)
        return self

    def click_element(self, locator: tuple):
        element = self.element(locator)
        element.click()

    def do_send_keys(self, locator, text):
        element = self.element(locator)
        element.send_keys(text)

    def text_from_element(self, locator):
        element = BasePage.element(self, locator)
        return element.text

    def get_names_open_windows(self):
        return self.driver.window_handles

    def switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)
