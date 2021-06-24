from config.TestData import TestData as TD
from pages.HomePage import HomePage
from pages.SearchResultPage import SearchResultNew
from pages.FlightDetailsPage import FlightDetailsPage
from selenium.webdriver.common.keys import Keys


class TestFlightBook:

    def test_flight_book(self):
        driver = HomePage(self.driver)
        driver.go_to_page(TD.BASE_URL)
        driver.click_element(HomePage.FLIGHTS)
        driver.click_element(HomePage.ROUNDTRIP)
        driver.click_element(HomePage.LEAVING_FROM)
        driver.do_send_keys(HomePage.INPUT_LEAVING_FROM, TD.LOCATION_FROM)
        driver.do_send_keys(HomePage.INPUT_LEAVING_FROM, Keys.RETURN)
        driver.do_send_keys(HomePage.GOING_TO, TD.LOCATION_TO)
        driver.do_send_keys(HomePage.INPUT_GOING_TO, Keys.RETURN)
        driver.click_element(HomePage.DEPARTING)
        driver.click_element(HomePage.DEPARTING_DATE)
        driver.click_element(HomePage.RETURNING_DATE)
        driver.click_element(HomePage.DONE)
        driver.click_element(HomePage.SEARCH)
        driver.wait_for_search_results_load(HomePage.SEARCH_RESULT_FIRST)
        assert TD.LOCATION_FROM in driver.text_from_element(SearchResultNew.FLYING_FROM_AFTER_SEARCH) and \
               TD.LOCATION_TO in driver.text_from_element(SearchResultNew.FLYING_TO_AFTER_SEARCH) and \
               TD.DEPARTING_DATE_STRING in driver.text_from_element(SearchResultNew.DEPARTING_AFTER_SEARCH) and \
               TD.RETURNING_DATE_STRING in driver.text_from_element(SearchResultNew.RETURNING_AFTER_SEARCH)
        driver.click_element(SearchResultNew.NONSTOP)
        driver.click_element(SearchResultNew.SORT_BY_DROPDOWN)
        driver.click_element(SearchResultNew.PRICE_HIGHEST)
        search_result = driver.get_elements(SearchResultNew.SEARCH_RESULT)
        search_result[0].click()
        driver.click_element(SearchResultNew.CONTINUE_AFTER_SELECT)
        driver.wait_for_search_results_load(HomePage.SEARCH_RESULT_FIRST)
        driver.click_element(SearchResultNew.NONSTOP)
        driver.click_element(SearchResultNew.SORT_BY_DROPDOWN)
        driver.click_element(SearchResultNew.PRICE_HIGHEST)
        search_result = driver.get_elements(SearchResultNew.SEARCH_RESULT)
        search_result[0].click()
        driver.click_element(SearchResultNew.CONTINUE_AFTER_SELECT)
        windows = driver.get_names_open_windows()
        driver.switch_to_window(windows[1])
        flight_details_elements = driver.get_elements(FlightDetailsPage.FLIGHT_DETAILS)
        assert TD.LOCATION_FROM in flight_details_elements[0].text and \
               TD.LOCATION_TO in flight_details_elements[1].text and \
               TD.DEPARTING_DATE_STRING in flight_details_elements[0].text and \
               TD.RETURNING_DATE_STRING in flight_details_elements[1].text
