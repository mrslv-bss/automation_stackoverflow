from libs.default import start
from pages.default import search_request
from pages.companies import open_companies_page_and_search_by_name, open_companies_page_and_search_by_location
from pages.users import open_users_page_and_search
from pages.tags import open_tags_page_and_search
from testdata.options import search_request_data
import pytest
import allure


def test_search_request(get_driver):
    start(get_driver)
    search_request(get_driver, search_request_data)


@pytest.mark.public_page
@pytest.mark.parametrize("search_data", ['user_'])
def test_users_page(get_driver, search_data):
    with allure.step("[1] Testcase run with params: " + search_data):
        open_users_page_and_search(get_driver, search_data)


@pytest.mark.public_page
@pytest.mark.parametrize("search_data", ['go'])
def test_tags_page(get_driver, search_data):
    with allure.step("[1] Testcase run with params: " + search_data):
        open_tags_page_and_search(get_driver, search_data)


@pytest.mark.public_page
@pytest.mark.parametrize("search_data", ['ukraine'])
def test_companies_page_location(get_driver, search_data):
    with allure.step("[1] Testcase run with params: " + search_data):
        open_companies_page_and_search_by_location(get_driver, search_data)


@pytest.mark.public_page
@pytest.mark.parametrize("search_data", ['qa'])
def test_companies_page_name(get_driver, search_data):
    with allure.step("[1] Testcase run with params: " + search_data):
        open_companies_page_and_search_by_name(get_driver, search_data)
