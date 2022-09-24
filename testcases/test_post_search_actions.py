from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from libs.default import start, click, send_keys
from pages.default import search_request, click_on_grid_element
from testdata.options import click_on_element_group_by

main_vote_number_text = (By.XPATH, "//div[@id='question']//div//div[contains(@class, 'votecell')]"
                                   "//div//div[@itemprop='upvoteCount']")
bookmarks_number_text = (By.XPATH, "//div[@class='js-bookmark-count mt4']")
answers_number_text = (By.XPATH, "//span[@itemprop='answerCount']/..")
authorization_msg_popup = (By.CLASS_NAME, "message-text")
show_activity_button = (By.XPATH, "//*[@class='js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto']")
time_line_title_text = (By.XPATH, "//div[contains(@class, 'subheader')]//h1")
sort_by_dropdownlist = (By.ID, "answer-sort-dropdown-select-menu")


def test_vote_counter(get_driver):
    start(get_driver)
    search_request(get_driver, "python error")
    click_on_grid_element(get_driver, 1)
    in_element_vote_counter = get_driver.find_element(*main_vote_number_text).text
    assert in_element_vote_counter.isnumeric(), "Error in number"


def test_bookmarks_counter(get_driver):
    start(get_driver)
    search_request(get_driver, "python error")
    click_on_grid_element(get_driver, 13)
    in_element_bookmarks_counter = get_driver.find_element(*bookmarks_number_text).text
    bookmark_button = get_driver.find_element(*bookmarks_number_text)

    action = ActionChains(get_driver)
    action.move_to_element(bookmark_button).perform()
    assert in_element_bookmarks_counter.isnumeric(), "Error in number"


def test_answers_counter(get_driver):
    start(get_driver)
    search_request(get_driver, "python error")
    click_on_grid_element(get_driver, 1)
    in_element_answers_counter = get_driver.find_element(*answers_number_text).get_attribute("data-answercount")
    assert in_element_answers_counter.isnumeric(), "Error in number"


def test_group_by_elements(get_driver):  # testdata/options.py : click_on_element_group_by
    start(get_driver)
    search_request(get_driver, "python error")
    click_on_grid_element(get_driver, 13)
    wait = WebDriverWait(get_driver, 10)
    wait.until(EC.visibility_of_element_located((*sort_by_dropdownlist,)))

    sorted_by_ddl = get_driver.find_element(*sort_by_dropdownlist)
    for option in sorted_by_ddl.find_elements(By.TAG_NAME, 'option'):
        if option == sorted_by_ddl.find_elements(By.TAG_NAME, 'option')[int(click_on_element_group_by)]:
            option.click()
            break
