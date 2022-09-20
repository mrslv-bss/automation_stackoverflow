from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys, open_public_page
from pages.default import search_specific_public_page_request

tags_result_questions_count_text = (By.XPATH, "//div[contains(@class, 'js-tag-cell')]/div[contains(@class, 'ai-center')]")
tags_result_grid_element = (By.XPATH, "//div[@id='tags-browser']/div")
tags_search_input = (By.ID, "tagfilter")


def open_tags_page_and_search(get_driver, text):
    open_public_page(get_driver, "Tags")
    return search_specific_public_page_request(get_driver, tags_result_questions_count_text,
                                               tags_search_input, tags_result_grid_element, text)
