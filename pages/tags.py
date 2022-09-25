from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from libs.default import send_keys, open_public_page
from pages.default import search_specific_public_page_request, click_on_grid_element
from testdata.options import click_on_grid_element_tags

tags_result_questions_count_text = (By.XPATH, "//div[contains(@class, 'js-tag-cell')]/div[contains(@class, 'ai-center')]")
tags_result_grid_element = (By.XPATH, "//div[@id='tags-browser']/div")
tags_search_input = (By.ID, "tagfilter")


def open_tags_page_and_search(get_driver, text):  # testdata/options.py : click_on_grid_element_tags
    open_public_page(get_driver, "Tags")
    search_specific_public_page_request(get_driver, tags_search_input, tags_result_grid_element, text)
    click_on_grid_element(get_driver, click_on_grid_element_tags, True)
