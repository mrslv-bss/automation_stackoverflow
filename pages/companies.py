from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys, open_page_companies

search_company_by_name = (By.XPATH, "//div[contains(@class, 'js-keyword-search')]"
                                    "/div/input[contains(@class, 's-input__search')]")
search_company_by_location = (By.XPATH, "//div[contains(@class, 'js-location-search')]"
                                        "/div/input[contains(@class, 's-input__md')]")
search_button_companies = (By.XPATH, "//button[contains(@class, 'js-search-btn')]")
companies_search_result_number = (By.XPATH, "//div[contains(@class, 'js-search-title')]/span")


def open_companies_page_and_search_by_name(get_driver, text):
    open_page_companies(get_driver)
    initial_number = get_driver.find_element(*companies_search_result_number).text
    send_keys(get_driver, search_company_by_name, text)
    send_keys(get_driver, search_company_by_name, Keys.ENTER)
    final_number = get_driver.find_element(*companies_search_result_number).text
    while initial_number == final_number:
        final_number = get_driver.find_element(*companies_search_result_number).text
    return final_number  # returns number of found companies


def open_companies_page_and_search_by_location(get_driver, text):
    open_page_companies(get_driver)
    initial_number = get_driver.find_element(*companies_search_result_number).text
    send_keys(get_driver, search_company_by_location, text)
    send_keys(get_driver, search_company_by_location, Keys.ENTER)
    final_number = get_driver.find_element(*companies_search_result_number).text
    while initial_number == final_number:
        final_number = get_driver.find_element(*companies_search_result_number).text
    return final_number  # returns number of found companies
