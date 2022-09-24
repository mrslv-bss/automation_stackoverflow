from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys, click
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

search_field = (By.XPATH, "//*[@class='s-topbar--searchbar--input-group']/child::input")
search_result_list_type_questions = (By.XPATH, "//div[@id='questions']/div")
title_inside_a_page = (By.XPATH, "//h1//a[@class='question-hyperlink']")
search_result_list_type_search = (By.XPATH, "//*[contains(@class, 'js-search-results')]/child::div/div")
search_result_item_name_type_search_hyperlink = (By.XPATH, "//a[@class='s-link'] | //a[@class='answer-hyperlink ']")
search_result_item_name_type_questions_hyperlink = (By.XPATH, "//a[@class='s-link']")
search_result_public_users = (By.XPATH, "//div[@class='grid--item user-info  user-hover']//div[@class='user-details']//a")
search_result_public_tags = (By.XPATH, "//div[contains(@class, 'grid--item')]//div//div[@class='flex--item']//a")
search_result_public_company = (By.XPATH, "//div[contains(@class, 'dismissable-company')]//div//div[@class='flex--item fl1 text mb0']//h2")
search_type_title_text = (By.XPATH, "//h1[contains(@class, 'fs-headline1')]")
page_number_button = (By.XPATH, "//*[@class='s-pagination--item is-selected'] | "
                                "//div[@class='py32 px16']//a[contains(text(),'Browse all companies')]")


def search_request(get_driver, text):
    send_keys(get_driver, search_field, text)
    send_keys(get_driver, search_field, Keys.ENTER)
    searchtype = get_driver.find_element(*search_type_title_text).text
    if "Questions tagged" in searchtype:
        return len(get_driver.find_elements(*search_result_list_type_questions))
    else:
        return len(get_driver.find_elements(*search_result_list_type_search))


def search_specific_public_page_request(get_driver, search_input_loc, grid_result_loc, text):
    send_keys(get_driver, search_input_loc, text)
    send_keys(get_driver, search_input_loc, Keys.ENTER)
    wait = WebDriverWait(get_driver, 10)
    wait.until(EC.presence_of_element_located((*page_number_button,)))
    return len(get_driver.find_elements(*grid_result_loc))


def click_on_grid_element(get_driver, elem_number, elem_type):
    # elem_type: True - grid elements in public pages (tags, users and companies)
    # elem_type: False - grid elements in basic search
    searchtype = get_driver.find_element(*search_type_title_text).text
    if elem_type:
        if "Tags" in searchtype:
            links_list = get_driver.find_elements(*search_result_public_tags)
        elif "Users" in searchtype:
            links_list = get_driver.find_elements(*search_result_public_users)
        elif "Companies" in searchtype:
            links_list = get_driver.find_elements(*search_result_public_company)
    else:
        if "Questions tagged" in searchtype:
            links_list = get_driver.find_elements(*search_result_item_name_type_questions_hyperlink)
        else:
            links_list = get_driver.find_elements(*search_result_item_name_type_search_hyperlink)
    action = ActionChains(get_driver)
    action.move_to_element(links_list[elem_number]).click().perform()
