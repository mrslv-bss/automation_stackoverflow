from libs.default import start
from pages.default import search_request, click_on_grid_element
from pages.companies import open_companies_page_and_search_by_name, open_companies_page_and_search_by_location
from pages.users import open_users_page_and_search
from pages.tags import open_tags_page_and_search


def test_search_request(get_driver):
    start(get_driver)
    search_request(get_driver, "python error")


def test_users_page(get_driver):
    open_users_page_and_search(get_driver, "bass_")


def test_tags_page(get_driver):
    open_tags_page_and_search(get_driver, "go")


def test_companies_page_location(get_driver):
    open_companies_page_and_search_by_location(get_driver, "ukraine")


def test_companies_page_name(get_driver):
    open_companies_page_and_search_by_name(get_driver, "qa")
