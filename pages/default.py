from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys

# often uses locators in search and after
search_field = (By.XPATH, "//*[@class='s-topbar--searchbar--input-group']/child::input")
search_result_array = (By.XPATH, "//*[@class='flush-left js-search-results']/child::div/div")
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


def search_course(get_driver, text):
    send_keys(get_driver, search_field, text)
    send_keys(get_driver, search_field, Keys.ENTER)
    output = get_driver.find_elements(*search_result_item_name)
    for item in output:
        print(item.text)
        print("--------------------------------------------")
