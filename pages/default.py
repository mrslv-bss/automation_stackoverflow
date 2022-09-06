from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys

# often uses locators in search and after
search_field = (By.XPATH, "//*[@class='s-topbar--searchbar--input-group']/child::input")
search_result_array = (By.XPATH, "//*[contains(@class, 'js-search-results')]/child::div/div")
search_result_item_name = (By.XPATH, "//*[contains(@class, 'js-search-results')]/child::div/div/div"
                                     "[@class='s-post-summary--content']/child::h3/a")
search_result_item_desk = (By.XPATH, "//*[contains(@class, 'js-search-results')]/child::div/div/div"
                                     "[@class='s-post-summary--content']/child::div[@class='s-post-summary--content-excerpt']")
search_result_item_time = (By.XPATH, "//*[contains(@class, 'js-search-results')]/child::div/div/div"
                                     "[@class='s-post-summary--content']/child::div[@class='s-post-summary--meta']/div"
                                     "[contains(@class, 's-user-card s-user-card__minimal')]/time[@class='s-user-card--time']")
search_result_item_tags = (By.XPATH, "//*[contains(@class, 'js-search-results')]/child::div/div/div"
                                     "[@class='s-post-summary--content']/child::div[@class='s-post-summary--meta']/div"
                                     "[contains(@class, 's-post-summary--meta-tags')]")


def search_request(get_driver, text):
    send_keys(get_driver, search_field, text)
    send_keys(get_driver, search_field, Keys.ENTER)
    return len(get_driver.find_elements(*search_result_array))


def search_specific_public_page_request(get_driver, validate_new_result_loc, search_input_loc, grid_result_loc, text):
    initial_number = get_driver.find_element(*validate_new_result_loc).text
    send_keys(get_driver, search_input_loc, text)
    send_keys(get_driver, search_input_loc, Keys.ENTER)
    final_number = get_driver.find_element(*validate_new_result_loc).text
    while initial_number == final_number:
        final_number = get_driver.find_element(*validate_new_result_loc).text
    return len(get_driver.find_elements(*grid_result_loc))
