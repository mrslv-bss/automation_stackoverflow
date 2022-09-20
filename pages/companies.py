from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys, open_public_page
from pages.default import search_specific_public_page_request

search_company_by_name_input = (By.XPATH, "//div[contains(@class, 'js-keyword-search')]"
                                    "/div/input[contains(@class, 's-input__search')]")
search_company_by_location_input = (By.XPATH, "//div[contains(@class, 'js-location-search')]"
                                        "/div/input[contains(@class, 's-input__md')]")
search_companies_button = (By.XPATH, "//button[contains(@class, 'js-search-btn')]")
companies_search_result_number_text = (By.XPATH, "//div[contains(@class, 'js-search-title')]/span")
companies_result_grid_element = (By.XPATH, "//div[@class='company-list']/div")


def open_companies_page_and_search_by_name(get_driver, text):
    open_public_page(get_driver, "Companies")
    return search_specific_public_page_request(get_driver, companies_search_result_number_text,
                                               search_company_by_name_input, companies_result_grid_element, text)


def open_companies_page_and_search_by_location(get_driver, text):
    open_public_page(get_driver, "Companies")
    return search_specific_public_page_request(get_driver, companies_search_result_number_text,
                                               search_company_by_location_input, companies_result_grid_element, text)
