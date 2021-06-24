from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchResultNew(BasePage):
    SEARCH_PAGE_NEW = (By.ID, 'flight-search-page')
    FLYING_FROM_AFTER_SEARCH = (By.CSS_SELECTOR, 'button[aria-label*="Flying from"]')
    FLYING_TO_AFTER_SEARCH = (By.CSS_SELECTOR, 'button[aria-label*="Flying to"]')
    DEPARTING_AFTER_SEARCH = (By.ID, 'start-date-ROUND_TRIP-0-btn')
    RETURNING_AFTER_SEARCH = (By.ID, 'end-date-ROUND_TRIP-0-btn')
    NONSTOP = (By.XPATH, '//div[@data-test-id="stops-0-label" and contains(text(), "Nonstop")]')
    SORT_BY_DROPDOWN = (By.CSS_SELECTOR, 'select[data-test-id="sortDropdown"]')
    PRICE_HIGHEST = (By.CSS_SELECTOR, 'option[data-opt-id*="PRICE_DECREASING"]')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'button[class="uitk-card-link"]')
    CONTINUE_AFTER_SELECT = (By.CSS_SELECTOR, 'button[data-test-id="select-button"]')
