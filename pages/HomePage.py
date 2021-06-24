from selenium.common.exceptions import TimeoutException
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.TestData import TestData as TD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    FLIGHTS = (By.XPATH, '//span[contains(text(), "Flights")]')
    ROUNDTRIP = (By.XPATH, '//span[contains(text(), "Roundtrip")]')
    LEAVING_FROM = (By.CSS_SELECTOR, 'button[aria-label="Leaving from"]')
    INPUT_LEAVING_FROM = (By.ID, 'location-field-leg1-origin')
    GOING_TO = (By.CSS_SELECTOR, 'button[aria-label="Going to"]')
    INPUT_GOING_TO = (By.ID, 'location-field-leg1-destination')
    DEPARTING = (By.ID, 'd1-btn')
    DEPARTING_DATE = (By.CSS_SELECTOR, f"button[aria-label*='{TD.DEPARTING_DATE_STRING}']")
    RETURNING_DATE = (By.CSS_SELECTOR, f"button[aria-label*='{TD.RETURNING_DATE_STRING}']")
    DONE = (By.XPATH, '//span[text()="Done"]')
    SEARCH = (By.CSS_SELECTOR, 'button[data-testid="submit-button"]')
    SEARCH_RESULT_FIRST = (By.CSS_SELECTOR, 'div[class="uitk-card-content-section uitk-card-content-section-padded"]')

    def wait_for_search_results_load(self, locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise Exception("Problem to load search results.")
