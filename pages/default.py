from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys, click

# often uses locators in search and after
search_field = (By.XPATH, "//*[@class='s-topbar--searchbar--input-group']/child::input")
search_result_list_type_questions = (By.XPATH, "//div[@id='questions']/div")
title_inside_a_page = (By.XPATH, "//h1//a[@class='question-hyperlink']")
search_result_list_type_search = (By.XPATH, "//*[contains(@class, 'js-search-results')]/child::div/div")
search_result_item_name_type_search_hyperlink = (By.XPATH, "//a[@class='s-link'] | //a[@class='answer-hyperlink ']")
search_result_item_name_type_questions_hyperlink = (By.XPATH, "//a[@class='s-link']")
search_type_title_text = (By.XPATH, "//h1[contains(@class, 'fs-headline1')]")


def search_request(get_driver, text):
    send_keys(get_driver, search_field, text)
    send_keys(get_driver, search_field, Keys.ENTER)
    searchtype = get_driver.find_element(*search_type_title_text).text
    if "Questions tagged" in searchtype:
        return len(get_driver.find_elements(*search_result_list_type_questions))
    else:
        return len(get_driver.find_elements(*search_result_list_type_search))


def search_specific_public_page_request(get_driver, validate_new_result_loc, search_input_loc, grid_result_loc, text):
    initial_number = get_driver.find_element(*validate_new_result_loc).text
    send_keys(get_driver, search_input_loc, text)
    send_keys(get_driver, search_input_loc, Keys.ENTER)
    final_number = get_driver.find_element(*validate_new_result_loc).text
    while initial_number == final_number:
        final_number = get_driver.find_element(*validate_new_result_loc).text
    return len(get_driver.find_elements(*grid_result_loc))


def click_on_grid_element(get_driver, elem_number):
    searchtype = get_driver.find_element(*search_type_title_text).text
    if "Questions tagged" in searchtype:
        links_list = get_driver.find_elements(*search_result_item_name_type_questions_hyperlink)
    else:
        links_list = get_driver.find_elements(*search_result_item_name_type_search_hyperlink)
    links_list[elem_number].click()
    return get_driver.find_element(*title_inside_a_page).text


# def compare_result_grid_element_data_and_in_page_data():
