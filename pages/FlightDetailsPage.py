from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class FlightDetailsPage(BasePage):
    FLIGHT_DETAILS = (By.CSS_SELECTOR, 'div[data-test-id="flight-review-header"]')
