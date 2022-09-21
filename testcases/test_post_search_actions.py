from selenium.webdriver.common.by import By
from libs.default import start, click
from pages.default import search_request, click_on_grid_element

main_vote_number_text = (By.XPATH, "//div[@id='question']//div//div[contains(@class, 'votecell')]"
                                   "//div//div[@itemprop='upvoteCount']")
bookmarks_number_text = (By.XPATH, "//div[@class='js-bookmark-count mt4']")
answers_number_text = (By.XPATH, "//span[@itemprop='answerCount']/..")
authorization_message = (By.CLASS_NAME, "message-text")


def test_vote_counter(get_driver):
    start(get_driver)
    search_request(get_driver, "python error")
    click_on_grid_element(get_driver, 1)
    in_element_vote_counter = get_driver.find_element(*main_vote_number_text).text
    assert in_element_vote_counter.isnumeric(), "Error in number"


def test_bookmarks_counter(get_driver):
    start(get_driver)
    search_request(get_driver, "python error")
    click_on_grid_element(get_driver, 1)
    in_element_bookmarks_counter = get_driver.find_element(*bookmarks_number_text).text
    assert in_element_bookmarks_counter.isnumeric(), "Error in number"
    click(get_driver, bookmarks_number_text)
    authorization_validation_text = get_driver.find_element(*authorization_message).text
    assert authorization_validation_text == "Please log in or register to bookmark this question.", "Error auth"


def test_answers_counter(get_driver):
    start(get_driver)
    search_request(get_driver, "python error")
    click_on_grid_element(get_driver, 1)
    in_element_answers_counter = get_driver.find_element(*answers_number_text).get_attribute("data-answercount")
    assert in_element_answers_counter.isnumeric(), "Error in number"
