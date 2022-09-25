from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from libs.default import start, click, dual_tab_start, open_public_page
from pages.default import search_request, click_on_grid_element
from testdata.options import click_on_element_group_by, vote_counter_request, search_request_data
import pytest
import allure

main_vote_number_text = (By.XPATH, "//div[@id='question']//div//div[contains(@class, 'votecell')]"
                                   "//div//div[@itemprop='upvoteCount']")
bookmarks_number_text = (By.XPATH, "//div[@class='js-bookmark-count mt4']")
answers_number_text = (By.XPATH, "//span[@itemprop='answerCount']/..")
sort_by_dropdownlist = (By.ID, "answer-sort-dropdown-select-menu")


@pytest.mark.dualtab
@pytest.mark.question_page
@pytest.mark.parametrize("search_data", [1])
def test_vote_counter(get_driver, search_data):  # testdata/options.py : vote_counter_request, search_request_data
    with allure.step("[1] Testcase run with params: " + str(search_data)):
        start(get_driver)
    with allure.step("[2] Run dual tab mode"):
        win2 = dual_tab_start(get_driver)[1]  # [1] - we save second browser tab handler for further actions
    search_request(get_driver, search_request_data)
    click_on_grid_element(get_driver, search_data, False)
    in_element_vote_counter = get_driver.find_element(*main_vote_number_text).text
    assert in_element_vote_counter.isnumeric(), "Error in number"
    with allure.step("[3] in_element_vote_counter = " + in_element_vote_counter):
        pass
    with allure.step("[4] Switch tab"):
        get_driver.switch_to.window(win2)
    start(get_driver)
    with allure.step("[5] Open public page as " + vote_counter_request):
        open_public_page(get_driver, vote_counter_request)


@pytest.mark.question_page
@pytest.mark.parametrize("search_data", [13])
def test_bookmarks_counter(get_driver, search_data):  # testdata/options.py : search_request_data
    with allure.step("[1] Testcase run with params: "+ str(search_data)):
        start(get_driver)
    search_request(get_driver, search_request_data)
    click_on_grid_element(get_driver, search_data, False)
    in_element_bookmarks_counter = get_driver.find_element(*bookmarks_number_text).text
    with allure.step("[2] Bookmarks value is " + in_element_bookmarks_counter):
        bookmark_button = get_driver.find_element(*bookmarks_number_text)

    action = ActionChains(get_driver)
    with allure.step("[3] Move to bookmark_button"):
        action.move_to_element(bookmark_button).perform()
    with allure.step("[4] in_element_bookmarks_counter = " + in_element_bookmarks_counter):
        assert in_element_bookmarks_counter.isnumeric(), "Error in number"


@pytest.mark.question_page
@pytest.mark.parametrize("search_data", [1])
def test_answers_counter(get_driver, search_data):  # testdata/options.py : search_request_data
    with allure.step("[1] Testcase run with params: " + str(search_data)):
        start(get_driver)
    search_request(get_driver, search_request_data)
    click_on_grid_element(get_driver, search_data, False)
    in_element_answers_counter = get_driver.find_element(*answers_number_text).get_attribute("data-answercount")
    with allure.step("[2] in_element_answers_counter = " + in_element_answers_counter):
        assert in_element_answers_counter.isnumeric(), "Error in number"


@pytest.mark.question_page
@pytest.mark.parametrize("search_data", [13])
def test_group_by_elements(get_driver, search_data):
    # testdata/options.py : click_on_element_group_by, search_request_data
    with allure.step("[1] Testcase run with params: " + str(search_data)):
        start(get_driver)
    search_request(get_driver, search_request_data)
    click_on_grid_element(get_driver, search_data, False)
    wait = WebDriverWait(get_driver, 10)
    with allure.step("[2] EC wait for visibility_of_element_located:\n"+sort_by_dropdownlist[1]):
        wait.until(EC.visibility_of_element_located((*sort_by_dropdownlist,)))

    sorted_by_ddl = get_driver.find_element(*sort_by_dropdownlist)
    with allure.step("[3] DropDownList cycle in"):
        pass
    for option in sorted_by_ddl.find_elements(By.TAG_NAME, 'option'):
        with allure.step("[DDL] Iteration"):
            if option == sorted_by_ddl.find_elements(By.TAG_NAME, 'option')[int(click_on_element_group_by)]:
                with allure.step("[DDL] Click"):
                    option.click()
                break
    with allure.step("[4] DropDownList cycle out"):
        pass
