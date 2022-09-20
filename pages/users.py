from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys, open_public_page
from pages.default import search_specific_public_page_request

search_user_by_name_input = (By.ID, "userfilter")
users_result_grid_element = (By.XPATH, "//div[@id='user-browser']/div/div")
user_result_users_name_text = (By.XPATH, "//div[@id='user-browser']/div/div/div[@class='user-details']/a")


def open_users_page_and_search(get_driver, text):
    open_public_page(get_driver, "Users")
    return search_specific_public_page_request(get_driver, user_result_users_name_text,
                                               search_user_by_name_input, users_result_grid_element, text)
