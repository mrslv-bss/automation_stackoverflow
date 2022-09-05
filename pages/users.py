from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys, open_page_users

search_user_by_name = (By.ID, "userfilter")
users_result_grid = (By.XPATH, "//div[@id='user-browser']/div/div")
user_result_users_name = (By.XPATH, "//div[@id='user-browser']/div/div/div[@class='user-details']/a")


def open_users_page_and_search(get_driver, text):
    open_page_users(get_driver)
    initial_number = get_driver.find_element(*user_result_users_name).text
    send_keys(get_driver, search_user_by_name, text)
    send_keys(get_driver, search_user_by_name, Keys.ENTER)
    final_number = get_driver.find_element(*user_result_users_name).text
    while initial_number == final_number:
        final_number = get_driver.find_element(*user_result_users_name).text
    return len(get_driver.find_elements(*users_result_grid))  # returns number of found users
