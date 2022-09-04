from libs.default import start, open_page_companies, open_page_tags, open_page_users
from pages.default import search_request
from pages.companies import open_companies_page_and_search_by_name, open_companies_page_and_search_by_location


def test_main(get_driver):
    print(open_companies_page_and_search_by_location(get_driver, "ukraine"))


def test_tagspage(get_driver):
    start(get_driver)
    open_page_tags(get_driver)
