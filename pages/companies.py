from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys, open_public_page
from pages.default import search_specific_public_page_request, click_on_grid_element
from testdata.options import click_on_grid_element_companies

search_company_by_name_input = (By.XPATH, "//div[contains(@class, 'js-keyword-search')]"
                                    "/div/input[contains(@class, 's-input__search')]")
search_company_by_location_input = (By.XPATH, "//div[contains(@class, 'js-location-search')]"
                                        "/div/input[contains(@class, 's-input__md')]")
search_companies_button = (By.XPATH, "//button[contains(@class, 'js-search-btn')]")
companies_search_result_number_text = (By.XPATH, "//div[contains(@class, 'js-search-title')]/span")
companies_result_grid_element = (By.XPATH, "//div[@class='company-list']/div")


def open_companies_page_and_search_by_name(get_driver, text):  # testdata/options.py : click_on_grid_element_companies
    open_public_page(get_driver, "Companies")
    search_specific_public_page_request(get_driver, search_company_by_name_input, companies_result_grid_element, text)
    click_on_grid_element(get_driver, click_on_grid_element_companies, True)


def open_companies_page_and_search_by_location(get_driver, text):
    open_public_page(get_driver, "Companies")
    return search_specific_public_page_request(get_driver, search_company_by_location_input,
                                               companies_result_grid_element, text)
